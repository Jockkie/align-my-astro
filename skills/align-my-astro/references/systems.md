# The three traditions

## Western astrology

**Calculate:** Sun, Moon and planets in signs (and houses with birth time and place), ascendant and midheaven, retrograde planets. For daily readings: today's transits and their major aspects to the natal chart (conjunction, sextile, square, trine, opposition), and the Moon's sign and phase.

**Core meanings to work with:**
- Sun: core self and vitality · Moon: emotions, needs, rhythm · Ascendant: how you meet the world
- Mercury: thinking and speaking · Venus: love, values, beauty · Mars: drive and action
- Jupiter: growth and trust · Saturn: structure, limits, maturity
- Uranus: change and freedom · Neptune: dreams and dissolving · Pluto: depth and transformation
- Elements: fire (action), earth (form), air (thought), water (feeling). Modes: cardinal (start), fixed (hold), mutable (adapt).
- Aspects: conjunction (merging), trine and sextile (flow), square (friction that builds), opposition (balance between two poles).

**Without birth time:** no ascendant or houses; the Moon can be in either of two signs on that day. Say so.

## Maya Tzolk'in

A 260-day sacred count of 13 numbers (tones) and 20 day signs, still kept by Maya day keepers (ajq'ij) in Guatemala. The script uses the GMT correlation (584283), the one used by Mayanists and by K'iche' day keepers. The Dreamspell or 13 Moon system (José Argüelles) uses a different count and gives a different kin; never calculate it by hand; point to the official 13 Moon calculator and label it as a different system.

**Calculate:** birth kin (tone and sign), today's kin, and the trecena: the 13-day period named after the day sign of its first day. The script gives both. A trecena colours the whole period; the day sign colours the single day.

**Day signs (Yucatec · K'iche' · core theme):**
1 Imix · Imox · origin, the unconscious, water · 2 Ik' · Iq' · wind, breath, communication · 3 Ak'b'al · Aq'ab'al · dawn, darkness before light, renewal · 4 K'an · K'at · seed, net, abundance and entanglement · 5 Chikchan · Kan · serpent, life force, instinct · 6 Kimi · Kame · death and transformation, ancestors · 7 Manik' · Kej · deer, stability, nature, leadership · 8 Lamat · Q'anil · seed and star, fertility, harmony · 9 Muluk · Toj · offering, gratitude, paying debts · 10 Ok · Tz'i' · dog, loyalty, justice · 11 Chuwen · B'atz' · weaving, time, art, beginnings · 12 Eb' · E · path, journey, destiny · 13 B'en · Aj · reed, home, growth, authority · 14 Ix · I'x · jaguar, earth, inner strength · 15 Men · Tz'ikin · bird, vision, prosperity · 16 Kib' · Ajmaq · forgiveness, ancestors, wisdom from mistakes · 17 Kab'an · No'j · thought, knowledge, ideas · 18 Etz'nab' · Tijax · flint, cutting, healing, truth · 19 Kawak · Kawoq · storm, community, family · 20 Ajaw · Ajpu · sun, light, hero, completion

**Tones (1 to 13):** 1 beginning · 2 duality · 3 movement · 4 stability · 5 centre · 6 flow · 7 reflection · 8 harmony · 9 patience · 10 manifestation · 11 release · 12 understanding · 13 completion. Lower tones are gentler in traditional reading, higher tones stronger.

Keep meanings modest; traditions and day keepers differ. Say "in many readings" rather than "it means".

## Chinese astrology

**Calculate:** the four pillars (BaZi) of birth with `scripts/astro_calc.py`: year (changes at Lichun, sun at 315 degrees), month (changes at the 12 sectional solar terms, stem by the Five Tigers rule), day (60-day cycle) and hour (two-hour periods, stem by the Five Rats rule). The day stem is the day master, the core of the person in BaZi. For each day in the window: the day pillar.

The script warns when a birth falls within about a day of a solar term (check the month pillar with an exact calculator), when a birth is at 23:00 or later (schools differ on whether the day already changes), and that the hour uses clock time (some schools correct to true solar time). Mention these honestly when they apply.

**Year boundary:** popular zodiac changes at Lunar New Year (between 21 January and 20 February); BaZi changes at Lichun (around 4 February). The script calculates the exact Lunar New Year date (with pyswisseph) and the exact Lichun time when a birth falls near it, and says on which side the birth falls. Without pyswisseph it only flags the window; then check a reliable calendar. Say which convention you mean.

**Animals:** Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig.
**Elements:** Wood (growth), Fire (expression), Earth (grounding), Metal (clarity, structure), Water (depth, flow). Generating cycle: Wood feeds Fire, Fire makes Earth, Earth bears Metal, Metal carries Water, Water feeds Wood. Controlling cycle: Wood parts Earth, Earth dams Water, Water quenches Fire, Fire melts Metal, Metal cuts Wood.

**Daily use:** compare today's day pillar element with the birth day pillar (the "day master" in BaZi): is today feeding, draining, controlled by or controlling their element?

## Weaving them together

1. Find **echoes:** the same theme appearing in two or three traditions (for example a Mars transit, a Tz'i' day and a Fire day all speaking of action and justice).
2. Find **tensions:** where one tradition invites rest and another action. Do not resolve them artificially; name them as a choice.
3. Add the **moon phase** as the rhythm underneath: new (seed), waxing (build), full (see, harvest), waning (release).
4. Turn the synthesis into one question and one small practice.

Never claim the traditions agree when they do not. A reading is stronger for being honest about mixed signals.
