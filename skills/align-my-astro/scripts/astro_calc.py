#!/usr/bin/env python3
"""Calculate the inputs for an Align My Astro reading.

Usage:
    python3 astro_calc.py --birth 1985-03-21 [--time 14:30 --tz Europe/Amsterdam
                          --lat 51.92 --lon 4.48] [--today 2026-11-08] [--days 3] [--json]

Always (standard library only):
  - Western sun sign (with a cusp warning)
  - Maya Tzolk'in kin for birth and for each day in the window (GMT 584283)
  - Chinese year animal, element and polarity (with a Lunar New Year warning)
  - Chinese day pillar for birth and for each day in the window
  - Moon phase for birth and for each day

With pyswisseph installed (pip install pyswisseph), birth time, time zone and
coordinates also:
  - natal planets, ascendant and midheaven
  - today's transits and their major aspects to the natal chart

Times are converted to UTC with the IANA time zone. Without a birth time the
Moon sign and the ascendant are not reliable and are left out.
"""
import argparse
import json
import math
from datetime import date, datetime, timedelta, timezone

try:
    from zoneinfo import ZoneInfo
except ImportError:  # Python < 3.9
    ZoneInfo = None

try:
    import swisseph as swe
except ImportError:
    swe = None

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra",
         "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
SUN_STARTS = [(3, 21), (4, 20), (5, 21), (6, 21), (7, 23), (8, 23), (9, 23),
              (10, 23), (11, 22), (12, 22), (1, 20), (2, 19)]
TZOLKIN = ["Imix", "Ik'", "Ak'b'al", "K'an", "Chikchan", "Kimi", "Manik'", "Lamat",
           "Muluk", "Ok", "Chuwen", "Eb'", "B'en", "Ix", "Men", "Kib'", "Kab'an",
           "Etz'nab'", "Kawak", "Ajaw"]
KICHE = ["Imox", "Iq'", "Aq'ab'al", "K'at", "Kan", "Kame", "Kej", "Q'anil", "Toj",
         "Tz'i'", "B'atz'", "E", "Aj", "I'x", "Tz'ikin", "Ajmaq", "No'j", "Tijax",
         "Kawoq", "Ajpu"]
ANIMALS = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat",
           "Monkey", "Rooster", "Dog", "Pig"]
STEMS = ["Jia", "Yi", "Bing", "Ding", "Wu", "Ji", "Geng", "Xin", "Ren", "Gui"]
STEM_ELEMENT = ["Wood", "Wood", "Fire", "Fire", "Earth", "Earth", "Metal", "Metal", "Water", "Water"]
BRANCHES = ["Zi", "Chou", "Yin", "Mao", "Chen", "Si", "Wu", "Wei", "Shen", "You", "Xu", "Hai"]
PHASES = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
          "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]
GMT = 584283
SYNODIC = 29.530588853
NEW_MOON_JD = 2451550.26  # 2000-01-06 18:14 UTC


def jdn(d):
    return d.toordinal() + 1721425  # Julian Day Number at noon for a Gregorian date


def sun_sign(d):
    md = (d.month, d.day)
    for i in range(12):
        start = SUN_STARTS[i]
        end = SUN_STARTS[(i + 1) % 12]
        if start <= end:
            inside = start <= md < end
        else:
            inside = md >= start or md < end
        if inside:
            sign = SIGNS[i]
            break
    cusp = any(abs((date(2001, d.month, d.day) - date(2001, m, dd)).days) <= 1
               for m, dd in SUN_STARTS)
    return {"sign": sign, "cusp_warning": cusp}


def tzolkin(d):
    days = jdn(d) - GMT
    number = (days + 3) % 13 + 1
    idx = (days + 19) % 20
    tre = (idx - (number - 1)) % 20
    return {"kin": f"{number} {TZOLKIN[idx]}", "number": number, "sign": TZOLKIN[idx],
            "kiche": KICHE[idx], "correlation": "GMT 584283",
            "trecena": TZOLKIN[tre], "day_of_trecena": number,
            "kin_index": (days + 159) % 260 + 1}


def pillar(index60):
    s, b = index60 % 10, index60 % 12
    return {"stem": STEMS[s], "branch": BRANCHES[b], "animal": ANIMALS[b],
            "element": STEM_ELEMENT[s], "polarity": "Yang" if s % 2 == 0 else "Yin"}


def _elong(jd):
    """Moon minus Sun longitude, 0..360 (needs pyswisseph)."""
    m = swe.calc_ut(jd, 1, swe.FLG_MOSEPH)[0][0]
    sn = swe.calc_ut(jd, 0, swe.FLG_MOSEPH)[0][0]
    return (m - sn) % 360


def new_moons(jd_start, jd_end):
    """Exact new moon instants (JD UT) between two dates, by bisection."""
    out, step, jd = [], 0.5, jd_start
    prev = _elong(jd)
    while jd < jd_end:
        nxt = _elong(jd + step)
        if nxt < prev:  # wrapped past 0: a new moon in (jd, jd+step)
            lo, hi = jd, jd + step
            for _ in range(40):
                mid = (lo + hi) / 2
                if _elong(mid) > 180:
                    lo = mid
                else:
                    hi = mid
            out.append(hi)
        jd, prev = jd + step, nxt
    return out


def jd_to_date(jd, offset_hours=0.0):
    return (datetime(2000, 1, 1, 12, tzinfo=timezone.utc) + timedelta(days=jd - 2451545.0, hours=offset_hours)).date()


def lunar_new_year(year):
    """Date of Lunar New Year (popular convention), in China time (UTC+8).

    Month 11 is the lunar month that contains the winter solstice; New Year is
    the second new moon after the start of that month. (Rare leap-month years can
    differ; the result is checked to fall between 21 January and 20 February.)
    Needs pyswisseph; returns None without it.
    """
    if not swe:
        return None
    sol_jd = solar_term_time(270, jdn(date(year - 1, 12, 21)) - 0.5)
    sol_day = jd_to_date(sol_jd, 8)
    moons = new_moons(jdn(date(year - 1, 11, 1)) - 0.5, jdn(date(year, 3, 15)) - 0.5)
    days = [jd_to_date(m, 8) for m in moons]
    m11 = max(i for i, dd in enumerate(days) if dd <= sol_day)
    lny = days[m11 + 2]
    if not (date(year, 1, 21) <= lny <= date(year, 2, 20)):
        return None
    return lny


def chinese_year(d):
    lny = lunar_new_year(d.year)
    out = {}
    if lny:
        y = d.year if d >= lny else d.year - 1
        out = pillar((y - 4) % 60)
        out["year"] = y
        out["lunar_new_year"] = lny.isoformat()
        out["convention"] = "popular zodiac, year starts at Lunar New Year"
    else:
        y = d.year
        out = pillar((y - 4) % 60)
        out["year"] = y
        out["lunar_new_year_warning"] = (d.month == 1) or (d.month == 2 and d.day <= 20)
        if out["lunar_new_year_warning"]:
            prev = pillar((y - 5) % 60)
            out["if_before_new_year"] = f"{prev['element']} {prev['animal']}"
    return out


def solar_term_time(target_lon, jd_guess):
    """JD UT when the sun reaches target_lon, searched around jd_guess (within 20 days)."""
    lo, hi = jd_guess - 20, jd_guess + 20
    f = lambda j: ((sun_longitude(j) - target_lon + 180) % 360) - 180
    for _ in range(60):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return hi


def moon_sign_day(d, tz=None):
    """Moon sign at local start and end of the day, and the ingress time if it changes. Needs pyswisseph."""
    if not swe:
        return None
    t0 = to_utc(d, "00:00", tz)
    t1 = to_utc(d, "23:59", tz)
    l0 = swe.calc_ut(jd_ut(t0), 1, swe.FLG_MOSEPH)[0][0]
    l1 = swe.calc_ut(jd_ut(t1), 1, swe.FLG_MOSEPH)[0][0]
    s0, s1 = SIGNS[int(l0 // 30)], SIGNS[int(l1 // 30)]
    out = {"sign": s1 if s0 == s1 else f"{s0} then {s1}"}
    if s0 != s1:
        lo, hi = jd_ut(t0), jd_ut(t1)
        for _ in range(40):
            mid = (lo + hi) / 2
            if SIGNS[int(swe.calc_ut(mid, 1, swe.FLG_MOSEPH)[0][0] // 30)] == s0:
                lo = mid
            else:
                hi = mid
        ing = datetime(2000, 1, 1, 12, tzinfo=timezone.utc) + timedelta(days=hi - 2451545.0)
        if tz and ZoneInfo:
            ing = ing.astimezone(ZoneInfo(tz))
        out["ingress"] = f"{s1} at {ing.strftime('%H:%M')}" + ("" if tz else " UTC")
    return out


def chinese_day(d):
    return pillar((jdn(d) - 11) % 60)


FIVE_TIGERS = {0: 2, 5: 2, 1: 4, 6: 4, 2: 6, 7: 6, 3: 8, 8: 8, 4: 0, 9: 0}   # year stem -> stem of Tiger month
FIVE_RATS = {0: 0, 5: 0, 1: 2, 6: 2, 2: 4, 7: 4, 3: 6, 8: 6, 4: 8, 9: 8}     # day stem -> stem of Zi hour


def sun_longitude(jd):
    """Apparent solar longitude in degrees (low-precision formula, about 0.01 degree)."""
    if swe:
        return swe.calc_ut(jd, 0, swe.FLG_MOSEPH)[0][0]
    n = jd - 2451545.0
    L = (280.460 + 0.9856474 * n) % 360
    g = math.radians((357.528 + 0.9856003 * n) % 360)
    return (L + 1.915 * math.sin(g) + 0.020 * math.sin(2 * g)) % 360


def bazi(d, t=None, tz=None):
    """Four pillars. Year changes at Lichun (sun 315 degrees), months at the 12 jie solar terms."""
    if t:
        dt = to_utc(d, t, tz)
        jd = jd_ut(dt)
    else:
        jd = jdn(d) - 0.5 + 0.5  # noon UT as a stand-in
    lon = sun_longitude(jd)
    year = d.year
    if d.month <= 2 and 270 <= lon < 315:
        year -= 1
    y = pillar((year - 4) % 60)
    month_idx = int(((lon - 315) % 360) // 30)
    m_stem = (FIVE_TIGERS[STEMS.index(y["stem"])] + month_idx) % 10
    m_branch = (2 + month_idx) % 12
    month = {"stem": STEMS[m_stem], "branch": BRANCHES[m_branch], "animal": ANIMALS[m_branch],
             "element": STEM_ELEMENT[m_stem], "polarity": "Yang" if m_stem % 2 == 0 else "Yin"}
    day = chinese_day(d)
    out = {"year": y, "month": month, "day": day, "day_master": f"{day['stem']} ({day['element']})"}
    deg_to_next = 30 - ((lon - 315) % 30)
    deg_since = (lon - 315) % 30
    if min(deg_to_next, deg_since) < 1.1:
        target = (315 + 30 * (month_idx + (1 if deg_to_next < deg_since else 0))) % 360
        term_jd = solar_term_time(target, jd)
        term_dt = datetime(2000, 1, 1, 12, tzinfo=timezone.utc) + timedelta(days=term_jd - 2451545.0)
        if tz and ZoneInfo:
            term_dt = term_dt.astimezone(ZoneInfo(tz))
        side = "after" if jd >= term_jd else "before"
        name = "Lichun (year and month change)" if target == 315 else "a sectional solar term (month changes)"
        out["solar_term"] = f"{name} at {term_dt.strftime('%Y-%m-%d %H:%M')}" + ("" if tz else " UTC")
        if t:
            out["solar_term_note"] = f"Born {side} {name}; the pillars above already use the exact time."
        else:
            out["solar_term_warning"] = f"No birth time and born on the day of {name}: the year or month pillar depends on the hour. Ask for the birth time."
    if t:
        hh, mm = (int(x) for x in t.split(":"))
        h_branch = ((hh + 1) // 2) % 12
        h_stem = (FIVE_RATS[STEMS.index(day["stem"])] + h_branch) % 10
        out["hour"] = {"stem": STEMS[h_stem], "branch": BRANCHES[h_branch], "animal": ANIMALS[h_branch],
                       "element": STEM_ELEMENT[h_stem], "polarity": "Yang" if h_stem % 2 == 0 else "Yin"}
        if hh >= 23:
            out["late_zi_warning"] = "Born at 23:00 or later: schools differ on whether the day pillar already changes."
        out["clock_note"] = "Hour pillar uses clock time; some schools correct to true solar time."
    return out


def moon_phase(jd):
    age = (jd - NEW_MOON_JD) % SYNODIC
    idx = int((age / SYNODIC) * 8 + 0.5) % 8
    illum = (1 - math.cos(2 * math.pi * age / SYNODIC)) / 2
    return {"phase": PHASES[idx], "age_days": round(age, 1), "illumination": round(illum, 2)}


def to_utc(d, t, tz):
    hh, mm = (int(x) for x in t.split(":"))
    local = datetime(d.year, d.month, d.day, hh, mm)
    if tz and ZoneInfo:
        local = local.replace(tzinfo=ZoneInfo(tz))
        return local.astimezone(timezone.utc)
    return local.replace(tzinfo=timezone.utc)


def jd_ut(dt):
    return dt.toordinal() + 1721424.5 + (dt.hour + dt.minute / 60) / 24


def fmt_lon(lon):
    sign = SIGNS[int(lon // 30)]
    deg = lon % 30
    return f"{int(deg)}°{int((deg % 1) * 60):02d}' {sign}"


PLANETS = [("Sun", 0), ("Moon", 1), ("Mercury", 2), ("Venus", 3), ("Mars", 4),
           ("Jupiter", 5), ("Saturn", 6), ("Uranus", 7), ("Neptune", 8), ("Pluto", 9)]
ASPECTS = [("conjunction", 0, 8), ("sextile", 60, 4), ("square", 90, 6),
           ("trine", 120, 6), ("opposition", 180, 8)]


def positions(jd):
    flag = swe.FLG_MOSEPH | swe.FLG_SPEED
    out = {}
    for name, pid in PLANETS:
        res = swe.calc_ut(jd, pid, flag)[0]
        out[name] = {"lon": round(res[0], 2), "pos": fmt_lon(res[0]), "retrograde": res[3] < 0}
    return out


def chart(dt_utc, lat, lon):
    jd = jd_ut(dt_utc)
    out = {"planets": positions(jd)}
    if lat is not None and lon is not None:
        hsys = b"P" if abs(lat) < 66 else b"W"
        cusps, ascmc = swe.houses(jd, lat, lon, hsys)
        out["ascendant"] = fmt_lon(ascmc[0])
        out["midheaven"] = fmt_lon(ascmc[1])
        out["house_system"] = "Placidus" if hsys == b"P" else "Whole sign"
    return out


FAST = ("Moon", "Sun", "Mercury", "Venus", "Mars")
PERSONAL_POINTS = ("Sun", "Moon", "Mercury", "Venus", "Mars")


def aspects(transit, natal):
    hits = []
    for tn, tp in transit.items():
        for nn, np_ in natal.items():
            diff = abs(tp["lon"] - np_["lon"]) % 360
            diff = min(diff, 360 - diff)
            for name, angle, orb in ASPECTS:
                o = abs(diff - angle)
                if o <= (orb if tn in ("Sun", "Moon") else orb - 2):
                    hits.append({"transit": tn, "aspect": name, "natal": nn, "orb": round(o, 1),
                                 "layer": "today" if tn in FAST else "background"})
    # today's themes first (fast planets to personal points), then by orb
    return sorted(hits, key=lambda h: (h["layer"] != "today", h["natal"] not in PERSONAL_POINTS, h["orb"]))


def write_card(r, path):
    import html as h
    e = lambda v: h.escape(str(v))
    today = r["days"][-1]
    br = r["birth"]
    tz, cd, mp = today["tzolkin"], today["chinese_day_pillar"], today["moon_phase"]
    dm = br["bazi"]["day_master"]
    gen = {"Wood": "Fire", "Fire": "Earth", "Earth": "Metal", "Metal": "Water", "Water": "Wood"}
    ctl = {"Wood": "Earth", "Earth": "Water", "Water": "Fire", "Fire": "Metal", "Metal": "Wood"}
    me, day_el = br["bazi"]["day"]["element"], cd["element"]
    if day_el == me:
        rel = "same element as you: strengthening"
    elif gen[day_el] == me:
        rel = f"{day_el} feeds your {me}"
    elif gen[me] == day_el:
        rel = f"your {me} feeds today's {day_el}: giving, can drain"
    elif ctl[day_el] == me:
        rel = f"{day_el} controls your {me}: pressure, structure"
    else:
        rel = f"your {me} controls today's {day_el}: you can shape the day"
    trail = "".join(f'<li><b>{e(d["date"][5:])}</b> {e(d["tzolkin"]["kin"])} · {e(d["chinese_day_pillar"]["element"])} {e(d["chinese_day_pillar"]["animal"])} · {e(d["moon_phase"]["phase"])}</li>' for d in r["days"][:-1])
    asp = "".join(f'<li>{e(x["transit"])} {e(x["aspect"])} your {e(x["natal"])} <span>{e(x["orb"])}° · {e(x["layer"])}</span></li>' for x in r.get("transit_aspects", [])[:5]) or "<li>Add birth time and place for transits.</li>"
    illum = mp["illumination"]
    waxing = mp["age_days"] < 14.77
    rx = 24 * abs(1 - 2 * illum)
    sweep_outer = 1 if waxing else 0
    sweep_inner = (0 if illum < 0.5 else 1) if waxing else (1 if illum < 0.5 else 0)
    moon_svg = (f'<svg width="54" height="54" viewBox="0 0 54 54"><circle cx="27" cy="27" r="24" fill="#3a3a3a"/>'
                f'<path d="M27 3 A24 24 0 0 {sweep_outer} 27 51 A{rx:.1f} 24 0 0 {sweep_inner} 27 3Z" fill="#F5F5DC"/></svg>')
    page = f"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Day card {e(today['date'])}</title>
<style>:root{{--bg:#212121;--fg:#F5F5DC;--mut:rgba(245,245,220,.6);--line:rgba(245,245,220,.14);--acc:#F57C00;--gold:#FFCA28;--card:#292929}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 Inter,system-ui,sans-serif}}main{{max-width:560px;margin:0 auto;padding:36px 22px 56px}}
.eye{{font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--mut)}}.eye::before{{content:"";display:inline-block;width:22px;height:2px;background:var(--acc);vertical-align:middle;margin-right:10px}}
h1{{font-family:Spectral,Georgia,serif;font-weight:500;font-size:34px;letter-spacing:-.02em;margin:12px 0 2px}}.moon{{display:flex;align-items:center;gap:14px;margin:18px 0}}
.disc{{width:54px;height:54px;border-radius:50%;background:radial-gradient(circle at {30 + 40 * illum:.0f}% 50%, var(--fg) {illum * 100:.0f}%, #3a3a3a {illum * 100 + 2:.0f}%)}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}.c{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px}}
.k{{color:var(--mut);font-size:11px;text-transform:uppercase;letter-spacing:.1em}}.v{{font-size:19px;font-weight:700;letter-spacing:-.02em;margin-top:4px}}.s{{color:var(--mut);font-size:12.5px}}
h2{{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);margin:28px 0 10px}}ul{{list-style:none;padding:0;margin:0}}li{{padding:7px 0;border-bottom:1px solid var(--line)}}li span{{color:var(--mut);font-size:12px}}
.rel{{font-family:Spectral,Georgia,serif;font-size:19px;color:var(--gold)}}footer{{color:var(--mut);font-size:12px;margin-top:30px}}@media(max-width:480px){{.grid{{grid-template-columns:1fr}}}}</style></head><body><main>
<div class="eye">Align My Astro · by Jockkie Studio</div><h1>{e(today['weekday'])} {e(today['date'])}</h1>
<div class="moon">{moon_svg}<div><b>{e(mp['phase'])}{(' in ' + e(today['moon_sign']['sign'])) if today.get('moon_sign') else ''}</b><div class="s">{illum * 100:.0f}% lit · day {e(mp['age_days'])} of the cycle</div></div></div>
<div class="grid"><div class="c"><div class="k">Western</div><div class="v">Sun in {e(today['western_sun'])}</div><div class="s">you: {e(br['western_sun']['sign'])}</div></div>
<div class="c"><div class="k">Tzolk'in</div><div class="v">{e(tz['kin'])}</div><div class="s">{e(tz['kiche'])} · trecena {e(tz['trecena'])} · you: {e(br['tzolkin']['kin'])}</div></div>
<div class="c"><div class="k">Chinese day</div><div class="v">{e(cd['element'])} {e(cd['animal'])}</div><div class="s">{e(cd['stem'])} {e(cd['branch'])} · you: {e(dm)}</div></div></div>
<h2>Your element today</h2><p class="rel">{e(rel)}</p>
<h2>Transits to your chart</h2><ul>{asp}</ul>
<h2>The past days</h2><ul>{trail}</ul>
<footer>Reflection, not prediction. Tzolk'in by GMT correlation; Chinese pillars by solar terms.</footer></main></body></html>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)


def scan(b, rng, tz, lat, lon):
    if not swe or lat is None or lon is None:
        print("--scan needs pyswisseph, --lat and --lon (and --tz).")
        return
    start, end = rng.split("-")
    def at(minute):
        hh, mm = divmod(minute, 60)
        dt = to_utc(b, f"{hh:02d}:{mm:02d}", tz)
        jd = jd_ut(dt)
        asc = swe.houses(jd, lat, lon, b"P" if abs(lat) < 66 else b"W")[1][0]
        moon = swe.calc_ut(jd, 1, swe.FLG_MOSEPH)[0][0]
        return SIGNS[int(asc // 30)], SIGNS[int(moon // 30)], asc
    m0 = int(start[:2]) * 60 + int(start[3:])
    m1 = int(end[:2]) * 60 + int(end[3:])
    prev = at(m0)
    print(f"{start}: ascendant {prev[0]}, Moon {prev[1]}")
    for m in range(m0 + 1, m1 + 1):
        cur = at(m)
        hh, mm = divmod(m, 60)
        if cur[0] != prev[0]:
            print(f"{hh:02d}:{mm:02d}: ascendant changes to {cur[0]}")
        if cur[1] != prev[1]:
            print(f"{hh:02d}:{mm:02d}: Moon changes to {cur[1]}")
        prev = cur
    print(f"{end}: ascendant {prev[0]}, Moon {prev[1]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--birth", required=True)
    ap.add_argument("--time")
    ap.add_argument("--tz")
    ap.add_argument("--lat", type=float)
    ap.add_argument("--lon", type=float)
    ap.add_argument("--today", default=date.today().isoformat())
    ap.add_argument("--days", type=int, default=3, help="today plus this many previous days")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--html", help="write a one-file day card for the last day in the window")
    ap.add_argument("--scan", help="birth-time range HH:MM-HH:MM: print the exact minutes where the ascendant or Moon changes sign (needs pyswisseph, --tz, --lat, --lon)")
    a = ap.parse_args()

    b = date.fromisoformat(a.birth)
    if a.scan:
        scan(b, a.scan, a.tz, a.lat, a.lon)
        return
    today = date.fromisoformat(a.today)
    window = [today - timedelta(days=i) for i in range(a.days, -1, -1)]

    result = {
        "birth": {
            "date": b.isoformat(),
            "western_sun": sun_sign(b),
            "tzolkin": tzolkin(b),
            "chinese_year": chinese_year(b),
            "chinese_day_pillar": chinese_day(b),
            "bazi": bazi(b, a.time, a.tz),
            "moon_phase": moon_phase(jdn(b)),
        },
        "days": [{"date": d.isoformat(), "weekday": d.strftime("%A"), "tzolkin": tzolkin(d), "chinese_day_pillar": chinese_day(d),
                  "moon_phase": moon_phase(jdn(d)), "moon_sign": moon_sign_day(d, a.tz), "western_sun": sun_sign(d)["sign"]} for d in window],
        "notes": [],
    }

    if swe and a.time:
        natal = chart(to_utc(b, a.time, a.tz), a.lat, a.lon)
        result["birth"]["natal_chart"] = natal
        now = datetime(today.year, today.month, today.day, 12, 0, tzinfo=timezone.utc)
        transit = positions(jd_ut(now))
        result["today_transits"] = transit
        result["transit_aspects"] = aspects(transit, natal["planets"])[:12]
        if a.lat is None:
            result["notes"].append("No coordinates: ascendant and houses left out.")
        if not a.tz:
            result["notes"].append("No time zone given: birth time treated as UTC. Results may be off.")
    elif not swe:
        result["notes"].append("pyswisseph not installed: planets, ascendant and transits left out.")
    else:
        ms = moon_sign_day(b, a.tz)
        result["birth"]["moon_sign_no_time"] = ms
        if ms and "then" in ms["sign"]:
            result["notes"].append(f"No birth time: the Moon changed sign that day ({ms['ingress']}), so the Moon sign depends on the hour. Ascendant and houses left out.")
        else:
            result["notes"].append("No birth time: the Moon stayed in one sign all day, so the Moon sign is reliable. Ascendant and houses left out.")

    if a.html:
        write_card(result, a.html)
    if a.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return
    br = result["birth"]
    cy = br["chinese_year"]
    print(f"Birth {b} · Sun {br['western_sun']['sign']}" + (" (cusp: check exact time)" if br["western_sun"]["cusp_warning"] else ""))
    zod = f"Chinese zodiac {cy['element']} {cy['animal']} ({cy['polarity']})"
    if cy.get("lunar_new_year"):
        before = cy["year"] < b.year
        zod += (f" · born before Lunar New Year ({cy['lunar_new_year']}), so still the {cy['year']} year" if before
                else f" · Lunar New Year was {cy['lunar_new_year']}")
    elif cy.get("lunar_new_year_warning"):
        zod += f" or {cy['if_before_new_year']} if born before Lunar New Year (install pyswisseph for the exact date)"
    print(f"  Tzolk'in {br['tzolkin']['kin']} ({br['tzolkin']['kiche']}) · {zod}")
    bz = br["bazi"]
    four = " · ".join(f"{k} {bz[k]['stem']} {bz[k]['branch']} ({bz[k]['element']} {bz[k]['animal']})" for k in ("year", "month", "day", "hour") if k in bz)
    print(f"  BaZi {four} · day master {bz['day_master']}")
    for w in ("solar_term", "solar_term_note", "solar_term_warning", "late_zi_warning", "clock_note"):
        if w in bz:
            print("  note: " + bz[w])
    print(f"  Trecena of {br['tzolkin']['trecena']} (day {br['tzolkin']['day_of_trecena']}) · Moon {br['moon_phase']['phase']}")
    if br.get("moon_sign_no_time"):
        print(f"  Moon (no birth time): {br['moon_sign_no_time']['sign']}")
    if "natal_chart" in br:
        nc = br["natal_chart"]
        print("  " + " · ".join(f"{k} {v['pos']}{' R' if v['retrograde'] else ''}" for k, v in nc["planets"].items()))
        if "ascendant" in nc:
            print(f"  Ascendant {nc['ascendant']} · MC {nc['midheaven']} ({nc['house_system']})")
    for d in result["days"]:
        p = d["chinese_day_pillar"]
        moon = d.get("moon_sign")
        msg = f" in {moon['sign']}" + (f" ({moon['ingress']})" if moon.get("ingress") else "") if moon else ""
        print(f"{d['date']} {d['weekday'][:3]} · Tzolk'in {d['tzolkin']['kin']} (trecena {d['tzolkin']['trecena']}) · day {p['element']} {p['animal']} ({p['stem']} {p['branch']}) · {d['moon_phase']['phase']}{msg} · Sun in {d['western_sun']}")
    for h in result.get("transit_aspects", []):
        print(f"  [{h['layer']}] transit {h['transit']} {h['aspect']} natal {h['natal']} (orb {h['orb']}°)")
    for n in result["notes"]:
        print("note: " + n)


if __name__ == "__main__":
    main()
