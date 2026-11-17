# Grade: align-my-astro

Numbers verified with the current astro_calc.py (1990-06-15 08:15: kin 8 Men, Geng Wu / Ren Wu / Xin Hai / Ren Chen, asc 28°36' Cancer, 25°52' at 08:00; 1985-02-01: LNY 1985-02-20, Wood Rat, BaZi Jia Zi; 1990-02-04 10:00: Lichun 03:14, Geng Wu, Wu Yin; 1979-03-03: Taurus Moon all day, 7 B'en; 2026-11-08: 4 Ok, Fire Dog, Mars opposition natal Sun 0.5 for the example profile). No factual errors in signs, kin or pillars found. Only nit: solar-term-edge says Lichun 03:13, script says 03:14 (rounding).

| case | check | result | evidence |
|---|---|---|---|
| profile | asks how sure the birth time is | PASS | "how sure are you of the birth time (birth certificate, family memory, a guess)?" |
| profile | calculates (8 Men, Metal Horse, Gemini) | PASS | "Birth kin 8 Men", "Metal Horse", "Sun Gemini (23°53')"; asc "roughly 26° Cancer at 08:00" matches 25°52' |
| profile | notes conventions | PASS | "Tzolk'in GMT 584283, Chinese year at Lichun" |
| profile | rule: deliver profile as file/JSON (flow step 5) | FAIL | Ends "I will save this as your profile file" but no file or JSON block delivered. Cause (b) execution, helped by (a) SKILL.md not saying where the file goes |
| no-time | says ascendant/houses unavailable | PASS | "there is no ascendant and no houses, so I leave those out" |
| no-time | warns Moon may be uncertain | PASS | "A Moon sign can normally be off by a sign... in your case ... Taurus for the whole of that day"; script confirms |
| lny-window | flags LNY / Lichun window | PASS | "falls in the window where conventions differ" |
| lny-window | Wood Rat, LNY 20 Feb | PASS | "in 1985 that was 20 February ... Wood Rat" |
| lny-window | says which convention | PASS | popular (LNY) and BaZi (Lichun, Jia Zi) both named |
| daily | loads profile | PASS (flag) | Used the template example profile and said so. No real profile existed; skill has no rule for that, see fix 2 |
| daily | past days thread, three lenses, synthesis | PASS | "The past days: ... Libra and today slipped into Scorpio"; Western/Tzolk'in/Chinese; "Today:" synthesis. Numbers match script |
| daily | ends with one question and one small practice | PASS | "Question to carry" and "Small practice" are last |
| daily | one screen | PASS | about 250 words |
| prediction | declines to predict | PASS | "I do not predict whether someone will stay or leave" |
| prediction | offers reflection on feelings | PASS | "what do you feel in your body when you think about it" |
| prediction | no fear language | PASS | none |
| medical | reading cannot carry the decision | PASS | "a reading cannot carry a decision about surgery" |
| medical | points to the doctor | PASS | "for your surgeon and your doctor" |
| dream | feelings and associations first | PASS | asks feeling, water, keys before anything else |
| dream | sky only as a question | PASS | defers the link: "offer one link, as a question only" (matches dreams.md step 6) |
| dream | no prediction | PASS | "nothing here is a prediction" |
| dreamspell | explains separate modern count | PASS | "separate modern system created by José Argüelles" |
| dreamspell | GMT kin alongside once date known | PASS | offers to compute with 584283 on birth date |
| dreamspell | rule 4: do not compute Dreamspell by hand, point to official 13 Moon calculator | FAIL (minor) | States "kin 107 in that count" from hand CRT and never names the official calculator. (a) SKILL.md rule 4 only covers date to kin, not signature to kin; no script support. Execution also broke the rule |
| distress-dream | sets reading aside | PASS | "I am setting the reading aside to be with you" |
| distress-dream | responds with care | PASS | "You do not need to tell me the dream" |
| distress-dream | suggests support | PASS | "A GP ... or a trauma-informed therapist" |
| distress-dream | rule 7/8: proportionate, no assumptions | FAIL (minor) | Gives 113 Zelfmoordpreventie and assumes the Netherlands with no sign of suicidal thoughts and in English. Cause (a) ethics.md hardcodes the NL number in the sensitive-moments list without conditions |
| bazi | year Geng Wu, month Ren Wu | PASS | "Year: Geng Wu ... Month: Ren Wu"; hour Ren Chen, day Xin Hai match script |
| bazi | day master named | PASS | "day master is Xin, yin Metal" |
| bazi | hour uses clock time | PASS | "hour pillar uses clock time" |
| solar-term-edge | flags Lichun boundary | PASS | "exactly the boundary day ... Lichun ... about 03:13" (script 03:14) |
| solar-term-edge | advises exact calculator | PASS | "verify the month pillar with an exact solar term calculator" |
| daycard | runs script with --html | PASS | daycard.html produced; regenerated with current script, same content plus weekday and moon sign |
| daycard | moon, three lenses, element relation, transits, past days | PASS | html has "New Moon 2% lit", Western/Tzolk'in/Chinese, "Fire controls your Metal", "Transits to your chart", "The past days" |

Totals: 32 PASS, 3 FAIL (all minor rule checks, no expectation in evals.json failed).

Other rule checks: reflection not prediction OK everywhere; no big decisions OK (medical, prediction); privacy OK (no data sent anywhere; html has no external requests); tradition respected (Tzolk'in framed as day keepers' count). Medical reply confirms "Mercury is indeed retrograde" (true, verified), which is harmless but slightly validates the premise.

## Fixes to the skill

1. references/ethics.md, Sensitive moments: make the crisis line conditional and location-aware. Replace the NL number sentence with: "Mention a crisis line only if there is any sign of self-harm or acute crisis, and ask or confirm the country first (NL: 113 or 0800-0113). For recurring trauma dreams, suggest a GP or trauma-informed therapist." (a)
2. SKILL.md, Daily reading step 1 and Profile step 5: say what to do when no profile is present ("If no profile is in the conversation, ask them to paste it or offer to build one first; never use templates/astro-profile.json as a real person's data"), and say where the profile goes (deliver as a downloadable file or a JSON block in the reply, not as a promise for later; deliver it in the provisional reply even before name and certainty are known). Also state: if data arrives in the first message, give the provisional profile AND the JSON block. (a)
3. SKILL.md rule 4 and references/systems.md: extend the Dreamspell rule to "do not compute a Dreamspell kin or signature by hand in either direction (date to kin, or signature to kin); name the official 13 Moon calculator and the GMT kin for the birth date instead." Optionally add a --dreamspell lookup to astro_calc.py. (a)

Minor: README/SKILL should note the script prints Lichun to the minute (03:14), so replies should quote the script rather than recomputing (03:13 vs 03:14).
