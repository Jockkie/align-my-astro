# astro-profile-daily (align-my-astro)

USER: Make my astro profile. Born 15 June 1990 in Utrecht, I think around 8 in the morning but not sure.

ASSISTANT: Welcome. I weave Western astrology, the Maya Tzolk'in and Chinese astrology into one reflection, and I read your days against it. It is reflection, not prediction: themes and questions, never a forecast, and not a basis for big decisions.

You gave me enough to start, so here is a provisional profile right away. For the coordinates I looked up only the city (Utrecht, about 52.09 N, 5.10 E, time zone Europe/Amsterdam); your date and time stayed on my side. Since you are not sure about the time, I scanned 07:00 to 09:00 as my own assumption of a plausible window, and I will ask you to correct it.

**Your profile (provisional)**
Born 15 June 1990, about 08:00 (approximate), Utrecht, Netherlands. Conventions: Tzolk'in in the GMT correlation (584283); Chinese zodiac animal by Lunar New Year (27 January 1990), BaZi year by Lichun (before your birth, same result).

**Calculated** (from the script, with pyswisseph)
- Western: Sun 23°53' Gemini. Moon 12°01' Pisces (Pisces for the whole 07:00 to 09:00 window). Ascendant 25°52' Cancer at 08:00, but the ascendant changes from Cancer to Leo at exactly 08:23 inside your window, so it is Cancer if you were born before 08:23 and Leo after. Mercury 5°15' Gemini, Venus 18°29' Taurus, Mars 10°51' Aries, Jupiter 15°50' Cancer, Saturn 24°02' Capricorn (retrograde), Uranus 8°10' Capricorn (retrograde), Neptune 13°43' Capricorn (retrograde), Pluto 15°24' Scorpio (retrograde). Placidus houses.
- Maya Tzolk'in: birth kin 8 Men (K'iche' Tz'ikin), trecena of Lamat, day 8 of 13. I did not calculate any Dreamspell (13 Moon) kin: that is a separate modern system with a different count; the official 13 Moon calculator is the place for it.
- Chinese: Metal Horse (Yang). BaZi pillars: year Geng Wu, month Ren Wu, day Xin Hai, hour Ren Chen (clock time; some schools correct to true solar time). Day master: Xin (Metal). The hour pillar is Ren Chen from 07:00 to 08:59 and changes at 09:00, so it holds across your window unless you were born exactly at 09:00 or later.

**Interpretation** (my reading, a lens, not a fixed fact)
Western: a Gemini Sun joined by Mercury in the same sign points to a mind that wants to know and to say; the Pisces Moon asks for feeling to be felt, not only understood. Saturn, Uranus and Neptune sit together in Capricorn: that is shared with everyone born around then, so read it as the climate of your generation, not as personal.
Tzolk'in: 8 is the tone of harmony and balance, and Men, the bird (Tz'ikin), is often read as vision and the wider view. In many readings an 8 inside a Lamat trecena colours the whole period with seed, star and fertility.
Chinese: a Yang Metal Horse, restless and forward-moving, while your day master Xin is yin Metal: the refined kind, in many readings precision and clarity. 
Where they meet. Echo: curiosity and movement, in the Gemini Sun, the bird's wide view and the Horse. Tension: a Metal day master that wants clarity and structure next to a Pisces Moon and a Water hour pillar that want depth and feeling. I would not resolve it; it can be a choice you make day by day.
A sentence to carry: "Clear enough to see, soft enough to feel."

**Self-check:** calculated (pass: every position, kin, pillar and the 08:23 change come from `astro_calc.py`, with the scan 07:00 to 09:00); conventions named (pass, no hand-made Dreamspell); reflection not prediction (pass); dreams (not applicable yet); care (no signal); profile delivered in this reply (pass: JSON below and `profile.json` in your working folder, `check_dossier.py` passed).

```json
{
 "schema": "align-my-astro/profile/v1",
 "created": "2026-11-08",
 "language": "en",
 "name": "",
 "birth": {
  "date": "1990-06-15",
  "time": "08:00",
  "time_certainty": "approximate: user said 'around 8 in the morning but not sure'; scan range 07:00-09:00 is my assumption",
  "place": "Utrecht, Netherlands",
  "lat": 52.0929,
  "lon": 5.1045,
  "tz": "Europe/Amsterdam"
 },
 "conventions": {
  "tzolkin": "GMT 584283 (Dreamspell not calculated)",
  "chinese_year": "lunar new year (1990-01-27); BaZi year Geng Wu, Lichun was before birth"
 },
 "western": {
  "sun": "Gemini 23°53'",
  "moon": "Pisces 12°01'",
  "ascendant": "Cancer 25°52' at 08:00; Cancer until 08:23, Leo after (scan 07:00-09:00)",
  "notes": "Sun and Mercury in Gemini; Saturn, Uranus, Neptune in Capricorn, retrograde; Pluto Scorpio retrograde; Mars Aries; Venus Taurus; Placidus houses"
 },
 "tzolkin": {
  "kin": "8 Men",
  "kiche": "Tz'ikin",
  "trecena": "Lamat"
 },
 "chinese": {
  "zodiac": "Metal Horse (Yang), born after Lunar New Year 1990-01-27",
  "bazi": "Geng Wu year, Ren Wu month, Xin Hai day, hour Ren Chen (clock time, 07:00 to 08:59)",
  "day_master": "Xin (Metal)"
 },
 "echoes": [
  "Curiosity and movement: Gemini Sun, Men (bird, vision), Metal Horse"
 ],
 "tensions": [
  "Metal day master (clarity, structure) with a Pisces Moon and a Water hour pillar (feeling, depth)"
 ],
 "dreams_consent": false,
 "dreams": [],
 "readings": []
}
```

How sure are you about the birth time: could it be earlier than 07:00 or later than 09:00?

USER: Somewhere between 7 and 9, my mum said morning. And what's my reading for today?

ASSISTANT: That matches my scan window exactly, so nothing changes in the numbers: the Moon stays in Pisces and the hour pillar stays Ren Chen across 07:00 to 09:00. The one open point stays open: Cancer rising before 08:23, Leo rising after. If you can find a birth certificate or a record from the hospital, that would settle it. I updated the certainty in `profile.json` (it now says the range came from you), and the check passed.

For today's reading I would like to include a dream if you remember one. Did you remember a dream from last night that you want in the reading?

USER: I was in a library looking for a book I couldn't find.

ASSISTANT: **Sunday 8 November 2026 · the dark of the Moon, Moon in Scorpio**

**The past days:** The Moon has been emptying through Virgo, Libra and, since late Saturday evening (23:39), Scorpio, and now stands at 28.1 days of its 29.5-day cycle, about 2 percent lit (the script labels this New Moon). The Tzolk'in count moved from 1 Manik' on Thursday through 2 Lamat and 3 Muluk, a gratitude day, to today's 4 Ok, all inside the Manik' trecena. In the Chinese count the days went Water Goat, Wood Monkey, Wood Rooster, and now Fire Dog.

**Western:** the tightest transit to a personal point of yours is Venus trine your natal Sun (orb 0.4°), an easy, warm angle; the script flags Venus and Mercury as retrograde today. The Moon in Scorpio makes a trine to your Pisces Moon (orb 5.0°): water meeting water. The script lists no slow-planet aspect today, so I name no longer theme.
**Tzolk'in:** 4 Ok (K'iche' Tz'i', dog: in many readings loyalty and justice) with tone 4, stability, meets your birth kin 8 Men. Different signs, no special relation I would claim.
**Chinese:** Bing Xu, a Fire Dog day, against your Xin Metal day master: in the controlling cycle Fire melts Metal. This is my lens: a day that tests the precise, clear-cutting side of you rather than rewarding it.

**Today:** An echo: the dark Moon and the stability of a 4 both speak of quiet, inward, seed-time, and the Venus-Sun trine makes that gentle rather than heavy. A tension: the sky around the Moon is soft and flowing, while the Chinese day presses on your Metal. I leave it as a question of whether to hold your clarity tightly or let it soften a little.

**Your dream:** a library and a book you could not find. Before I offer any meaning, I would like it from you: in the dream and when you woke, what was the strongest feeling?

USER: Frustrated, a bit panicky at first. But also quiet, because it was a library.

ASSISTANT: Thank you. Frustration and panic, with a quiet underneath: both belong to the dream. Now two images, in your words and not mine: what does the library mean to you, what comes to mind first?

USER: It's where I used to study. It's calm there.

ASSISTANT: A place of study and calm. And the book you could not find: what comes to mind first when you think of it?

USER: It felt like it had the answer, but I didn't know the title.

ASSISTANT: "It had the answer, but I didn't know the title." Is there something in your life right now that feels like that dream?

USER: Maybe that I'm looking for a new direction in my work. I don't know what I'm looking for.

ASSISTANT: Thank you for saying that. A reading cannot carry a decision about your work, and I will not use one for that; what I can do is help you listen to the question.

Offered lightly, as a question: tonight's Moon is dark, in Scorpio, a time that many traditions link to seeds not yet showing, and Mercury, the planet of searching and thought, is retrograde, a time often read as going back over what you thought you knew. Does a book without a title, in a place where you used to study, connect to a direction that has no name yet?

**Question to carry today:** If the book had a title, what might it be called?
**Small practice (five minutes):** write three lines under the heading "What I am looking for", without correcting yourself, and put the paper away.

For your file, I would keep today's reading and the dream, but dreams go into your profile only with your consent. May I add this dream to your profile file?

USER: Yes, keep it.

ASSISTANT: Done: `profile.json` in your working folder now holds the dream (with your own words about the library and the book, and your consent noted) and today's reading themes (dark Moon in Scorpio, Venus trine your Sun, 4 Ok, Fire Dog against your Metal day master). I ran the check again and it passed. There is also a one-file day card, `daycard.html`, with the moon phase, the three lenses and the past days. Keep the profile with you: next time, paste it and I start from there.

**Self-check (delivery):** calculated (pass, every sign, kin, pillar, moon phase and transit from `astro_calc.py`); conventions named (pass); reflection, not prediction (pass; I declined to weigh the work question); dreams (pass: your associations came before my question to you, and I offered the sky link only as a question); care (no crisis signal, no line needed); profile delivered (pass).

Complete profile file:

```json
{
 "schema": "align-my-astro/profile/v1",
 "created": "2026-11-08",
 "language": "en",
 "name": "",
 "birth": {
  "date": "1990-06-15",
  "time": "08:00",
  "time_certainty": "approximate: user said 'around 8 in the morning but not sure', then 'somewhere between 7 and 9, my mum said morning'; range 07:00-09:00 from the user",
  "place": "Utrecht, Netherlands",
  "lat": 52.0929,
  "lon": 5.1045,
  "tz": "Europe/Amsterdam"
 },
 "conventions": {
  "tzolkin": "GMT 584283 (Dreamspell not calculated)",
  "chinese_year": "lunar new year (1990-01-27); BaZi year Geng Wu, Lichun was before birth"
 },
 "western": {
  "sun": "Gemini 23°53'",
  "moon": "Pisces 12°01'",
  "ascendant": "Cancer 25°52' at 08:00; Cancer until 08:23, Leo after (scan 07:00-09:00)",
  "notes": "Sun and Mercury in Gemini; Saturn, Uranus, Neptune in Capricorn, retrograde; Pluto Scorpio retrograde; Mars Aries; Venus Taurus; Placidus houses"
 },
 "tzolkin": {
  "kin": "8 Men",
  "kiche": "Tz'ikin",
  "trecena": "Lamat"
 },
 "chinese": {
  "zodiac": "Metal Horse (Yang), born after Lunar New Year 1990-01-27",
  "bazi": "Geng Wu year, Ren Wu month, Xin Hai day, hour Ren Chen (clock time, 07:00 to 08:59)",
  "day_master": "Xin (Metal)"
 },
 "echoes": [
  "Curiosity and movement: Gemini Sun, Men (bird, vision), Metal Horse"
 ],
 "tensions": [
  "Metal day master (clarity, structure) with a Pisces Moon and a Water hour pillar (feeling, depth)"
 ],
 "dreams_consent": true,
 "dreams": [
  {
   "date": "2026-11-08",
   "text": "I was in a library looking for a book I couldn't find.",
   "feeling": "frustrated, a bit panicky, but quiet",
   "associations": {
    "library": "where I used to study",
    "book": "felt it held the answer, no title"
   }
  }
 ],
 "readings": [
  {
   "date": "2026-11-08",
   "themes": [
    "Dark of the Moon in Scorpio",
    "Venus trine natal Sun",
    "4 Ok (trecena Manik')",
    "Fire Dog day against Metal day master"
   ],
   "question": "What would the book be called?"
  }
 ]
}
```

One line, only because you found it useful: the skill is free and can be supported at https://buymeacoffee.com/jockkie.

## SCRIPT RUNS
(profile_v1 = first reply, profile_v2 = after the time range, profile_v3 = with the reading, profile.json = with the dream and consent)

$ python3 /home/claude/jockkie-studio/plugins/align-my-astro/skills/align-my-astro/scripts/astro_calc.py --birth 1990-06-15 --time 08:00 --tz Europe/Amsterdam --lat 52.0929 --lon 5.1045 --today 2026-11-08 --days 0
Birth 1990-06-15 · Sun Gemini
  Tzolk'in 8 Men (Tz'ikin) · Chinese zodiac Metal Horse (Yang) · Lunar New Year was 1990-01-27
  BaZi year Geng Wu (Metal Horse) · month Ren Wu (Water Horse) · day Xin Hai (Metal Pig) · hour Ren Chen (Water Dragon) · day master Xin (Metal)
  note: Hour pillar uses clock time; some schools correct to true solar time.
  Trecena of Lamat (day 8) · Moon Last Quarter
  Sun 23°53' Gemini · Moon 12°01' Pisces · Mercury 5°15' Gemini · Venus 18°29' Taurus · Mars 10°51' Aries · Jupiter 15°50' Cancer · Saturn 24°02' Capricorn R · Uranus 8°10' Capricorn R · Neptune 13°43' Capricorn R · Pluto 15°24' Scorpio R
  Ascendant 25°52' Cancer · MC 28°13' Pisces (Placidus)
2026-11-08 Sun · Tzolk'in 4 Ok (trecena Manik') · day Fire Dog (Bing Xu) · New Moon in Scorpio · Sun in Scorpio
  [today] transit Venus trine natal Sun (orb 0.4°)
  [today] transit Mars sextile natal Sun (orb 1.6°)
  [today] transit Sun opposition natal Venus (orb 2.4°)
  [today] transit Mars square natal Venus (orb 3.8°)
  [today] transit Sun trine natal Moon (orb 4.1°)
  [today] transit Moon trine natal Moon (orb 5.0°)
  [today] transit Sun trine natal Jupiter (orb 0.2°)
  [today] transit Mercury sextile natal Uranus (orb 0.6°)
  [today] transit Venus square natal Saturn (orb 0.6°)
  [today] transit Sun conjunction natal Pluto (orb 0.7°)
  [today] transit Moon sextile natal Uranus (orb 1.2°)
  [today] transit Sun sextile natal Neptune (orb 2.4°)
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/align-my-astro/skills/align-my-astro/scripts/astro_calc.py --birth 1990-06-15 --time 08:00 --tz Europe/Amsterdam --lat 52.0929 --lon 5.1045 --scan 07:00-09:00
07:00: ascendant Cancer, Moon Pisces
08:23: ascendant changes to Leo
09:00: ascendant Leo, Moon Pisces
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/align-my-astro/skills/align-my-astro/scripts/check_dossier.py profile_v1.json
CHECK PASSED · seen 0 · inferred 0 · unknown 0
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/align-my-astro/skills/align-my-astro/scripts/astro_calc.py --birth 1990-06-15 --time 06:59 --tz Europe/Amsterdam --lat 52.0929 --lon 5.1045 --today 2026-11-08 --days 0
Birth 1990-06-15 · Sun Gemini
  Tzolk'in 8 Men (Tz'ikin) · Chinese zodiac Metal Horse (Yang) · Lunar New Year was 1990-01-27
  BaZi year Geng Wu (Metal Horse) · month Ren Wu (Water Horse) · day Xin Hai (Metal Pig) · hour Xin Mao (Metal Rabbit) · day master Xin (Metal)
  note: Hour pillar uses clock time; some schools correct to true solar time.
  Trecena of Lamat (day 8) · Moon Last Quarter
  Sun 23°51' Gemini · Moon 11°27' Pisces · Mercury 5°11' Gemini · Venus 18°26' Taurus · Mars 10°49' Aries · Jupiter 15°49' Cancer · Saturn 24°02' Capricorn R · Uranus 8°10' Capricorn R · Neptune 13°43' Capricorn R · Pluto 15°24' Scorpio R
  Ascendant 14°17' Cancer · MC 11°39' Pisces (Placidus)
2026-11-08 Sun · Tzolk'in 4 Ok (trecena Manik') · day Fire Dog (Bing Xu) · New Moon in Scorpio · Sun in Scorpio
  [today] transit Venus trine natal Sun (orb 0.4°)
  [today] transit Mars sextile natal Sun (orb 1.5°)
  [today] transit Sun opposition natal Venus (orb 2.3°)
  [today] transit Mercury trine natal Moon (orb 3.9°)
  [today] transit Mars square natal Venus (orb 3.9°)
  [today] transit Moon trine natal Moon (orb 4.5°)
  [today] transit Sun trine natal Moon (orb 4.6°)
  [today] transit Sun trine natal Jupiter (orb 0.3°)
  [today] transit Mercury sextile natal Uranus (orb 0.6°)
  [today] transit Venus square natal Saturn (orb 0.6°)
  [today] transit Sun conjunction natal Pluto (orb 0.7°)
  [today] transit Moon sextile natal Uranus (orb 1.2°)
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/align-my-astro/skills/align-my-astro/scripts/astro_calc.py --birth 1990-06-15 --time 09:00 --tz Europe/Amsterdam --lat 52.0929 --lon 5.1045 --today 2026-11-08 --days 0
Birth 1990-06-15 · Sun Gemini
  Tzolk'in 8 Men (Tz'ikin) · Chinese zodiac Metal Horse (Yang) · Lunar New Year was 1990-01-27
  BaZi year Geng Wu (Metal Horse) · month Ren Wu (Water Horse) · day Xin Hai (Metal Pig) · hour Gui Si (Water Snake) · day master Xin (Metal)
  note: Hour pillar uses clock time; some schools correct to true solar time.
  Trecena of Lamat (day 8) · Moon Last Quarter
  Sun 23°55' Gemini · Moon 12°34' Pisces · Mercury 5°20' Gemini · Venus 18°31' Taurus · Mars 10°53' Aries · Jupiter 15°50' Cancer · Saturn 24°02' Capricorn R · Uranus 8°10' Capricorn R · Neptune 13°43' Capricorn R · Pluto 15°24' Scorpio R
  Ascendant 6°38' Leo · MC 14°34' Aries (Placidus)
2026-11-08 Sun · Tzolk'in 4 Ok (trecena Manik') · day Fire Dog (Bing Xu) · New Moon in Scorpio · Sun in Scorpio
  [today] transit Venus trine natal Sun (orb 0.5°)
  [today] transit Mars sextile natal Sun (orb 1.6°)
  [today] transit Sun opposition natal Venus (orb 2.4°)
  [today] transit Sun trine natal Moon (orb 3.5°)
  [today] transit Mars square natal Venus (orb 3.8°)
  [today] transit Moon trine natal Moon (orb 5.6°)
  [today] transit Sun trine natal Jupiter (orb 0.2°)
  [today] transit Mercury sextile natal Uranus (orb 0.6°)
  [today] transit Venus square natal Saturn (orb 0.6°)
  [today] transit Sun conjunction natal Pluto (orb 0.7°)
  [today] transit Moon sextile natal Uranus (orb 1.2°)
  [today] transit Sun sextile natal Neptune (orb 2.4°)
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/align-my-astro/skills/align-my-astro/scripts/check_dossier.py profile_v2.json
CHECK PASSED · seen 0 · inferred 0 · unknown 0
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/align-my-astro/skills/align-my-astro/scripts/astro_calc.py --birth 1990-06-15 --time 08:00 --tz Europe/Amsterdam --lat 52.0929 --lon 5.1045 --today 2026-11-08 --days 3 --html daycard.html
Birth 1990-06-15 · Sun Gemini
  Tzolk'in 8 Men (Tz'ikin) · Chinese zodiac Metal Horse (Yang) · Lunar New Year was 1990-01-27
  BaZi year Geng Wu (Metal Horse) · month Ren Wu (Water Horse) · day Xin Hai (Metal Pig) · hour Ren Chen (Water Dragon) · day master Xin (Metal)
  note: Hour pillar uses clock time; some schools correct to true solar time.
  Trecena of Lamat (day 8) · Moon Last Quarter
  Sun 23°53' Gemini · Moon 12°01' Pisces · Mercury 5°15' Gemini · Venus 18°29' Taurus · Mars 10°51' Aries · Jupiter 15°50' Cancer · Saturn 24°02' Capricorn R · Uranus 8°10' Capricorn R · Neptune 13°43' Capricorn R · Pluto 15°24' Scorpio R
  Ascendant 25°52' Cancer · MC 28°13' Pisces (Placidus)
2026-11-05 Thu · Tzolk'in 1 Manik' (trecena Manik') · day Water Goat (Gui Wei) · Waning Crescent in Virgo then Libra (Libra at 15:38) · Sun in Scorpio
2026-11-06 Fri · Tzolk'in 2 Lamat (trecena Manik') · day Wood Monkey (Jia Shen) · Waning Crescent in Libra · Sun in Scorpio
2026-11-07 Sat · Tzolk'in 3 Muluk (trecena Manik') · day Wood Rooster (Yi You) · Waning Crescent in Libra then Scorpio (Scorpio at 23:39) · Sun in Scorpio
2026-11-08 Sun · Tzolk'in 4 Ok (trecena Manik') · day Fire Dog (Bing Xu) · New Moon in Scorpio · Sun in Scorpio
  [today] transit Venus trine natal Sun (orb 0.4°)
  [today] transit Mars sextile natal Sun (orb 1.6°)
  [today] transit Sun opposition natal Venus (orb 2.4°)
  [today] transit Mars square natal Venus (orb 3.8°)
  [today] transit Sun trine natal Moon (orb 4.1°)
  [today] transit Moon trine natal Moon (orb 5.0°)
  [today] transit Sun trine natal Jupiter (orb 0.2°)
  [today] transit Mercury sextile natal Uranus (orb 0.6°)
  [today] transit Venus square natal Saturn (orb 0.6°)
  [today] transit Sun conjunction natal Pluto (orb 0.7°)
  [today] transit Moon sextile natal Uranus (orb 1.2°)
  [today] transit Sun sextile natal Neptune (orb 2.4°)
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/align-my-astro/skills/align-my-astro/scripts/check_dossier.py profile_v3.json
CHECK PASSED · seen 0 · inferred 0 · unknown 0
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/align-my-astro/skills/align-my-astro/scripts/check_dossier.py profile.json --assumptions
### What you told me and what I assumed

**You told me:**
- none

**I estimated (please check):**
- none

**Still unknown:**
- none

CHECK PASSED · seen 0 · inferred 0 · unknown 0
[exit 0]
