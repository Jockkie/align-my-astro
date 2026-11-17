# Self-check (visible to the user)

Run this before every gate summary and every delivery, and show the result to the user as a short block titled "Self-check". If an item fails, fix it first and say what you fixed. Never claim a check passed that you did not do.

## Checklist
1. **Calculated:** every sign, kin, pillar, moon phase and transit comes from `scripts/astro_calc.py` (or a named calculator), not from memory. Sign changes inside a time range come from `--scan`.
2. **Conventions named:** Tzolk'in correlation and Chinese year boundary are stated where they matter; no hand-made Dreamspell kin.
3. **Reflection, not prediction:** no outcome is predicted; no medical, legal, financial or relationship decision is based on the reading.
4. **Dreams:** the user's own associations came before any meaning you offered.
5. **Care:** a crisis line only with a crisis signal and a known country.
6. **Assumptions listed:** every choice you made that the user did not state (a birth-time window, a convention, a city's coordinates) is in the profile's `assumptions` list, so the check script shows it.
7. **Profile:** delivered in the same reply as a file or JSON block. If you can run code: `python3 scripts/check_dossier.py profile.json` must pass.

## Calculated and interpreted block (in every profile and reading)
Separate "Calculated" (the numbers and signs, with the convention) from "Interpretation" (your reading), so the user sees which part is fixed and which is a lens.
