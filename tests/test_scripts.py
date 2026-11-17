"""Tests for the scripts that ship with this skill. Run: python -m unittest discover -s tests -v"""
import csv
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = "align-my-astro"


def path(*parts):
    return os.path.join(ROOT, "skills", SKILL, *parts)


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, file)
    mod = importlib.util.module_from_spec(spec)
    sys.argv = [file]
    spec.loader.exec_module(mod)
    return mod


def run(*args, stdin=None):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True, input=stdin)


class Astro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = load("astro_calc", path("scripts", "astro_calc.py"))

    def test_tzolkin(self):
        self.assertEqual(self.m.tzolkin(date(1990, 6, 15))["kin"], "8 Men")

    def test_day_pillar(self):
        p = self.m.chinese_day(date(2000, 1, 1))
        self.assertEqual((p["stem"], p["branch"]), ("Wu", "Wu"))

    def test_bazi_1990(self):
        b = self.m.bazi(date(1990, 6, 15), "08:15", "Europe/Amsterdam")
        self.assertEqual((b["year"]["stem"], b["year"]["branch"]), ("Geng", "Wu"))
        self.assertEqual((b["month"]["stem"], b["month"]["branch"]), ("Ren", "Wu"))

    @unittest.skipUnless(importlib.util.find_spec("swisseph"), "pyswisseph not installed")
    def test_lunar_new_year(self):
        known = {1966: date(1966, 1, 21), 1979: date(1979, 1, 28), 1985: date(1985, 2, 20),
                 1990: date(1990, 1, 27), 2004: date(2004, 1, 22), 2012: date(2012, 1, 23),
                 2023: date(2023, 1, 22), 2026: date(2026, 2, 17), 2033: date(2033, 1, 31)}
        for y, d in known.items():
            self.assertEqual(self.m.lunar_new_year(y), d, y)

class CheckDossier(unittest.TestCase):
    script = path("scripts", "check_dossier.py")

    def test_template_passes(self):
        r = run(self.script, path("templates", "astro-profile.json"), "--gate", "deliver")
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_seen_without_quote_fails(self):
        d = {"schema": "consult-anything/dossier/v1", "goal": {"metric": "x", "label": "seen"}, "steps": [{"name": "A"}]}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(d, f)
        r = run(self.script, f.name)
        self.assertEqual(r.returncode, 1)
        self.assertIn("no quote", r.stdout)

class Assumptions(unittest.TestCase):
    def test_approximate_birth_time_listed(self):
        d = {"schema": "align-my-astro/profile/v1", "birth": {"date": "1990-06-15", "time": "08:00", "time_certainty": "around 8, not sure"}, "conventions": {"tzolkin": "GMT"}}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(d, f)
        r = run(path("scripts", "check_dossier.py"), f.name, "--assumptions")
        self.assertIn("approximate", r.stdout)

class Hook(unittest.TestCase):
    hook = os.path.join(ROOT, "hooks", "check_reply.py")

    def reply(self, text, tool=None, skill=SKILL, active=False):
        entries = [{"type": "user", "message": {"content": "please use " + SKILL}}]
        if tool:
            entries.append({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": tool, "input": {}}]}})
        entries.append({"type": "assistant", "message": {"content": [{"type": "text", "text": text}]}})
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            f.write("\n".join(json.dumps(e) for e in entries))
        r = run(self.hook, skill, stdin=json.dumps({"transcript_path": f.name, "stop_hook_active": active}))
        return r.stdout.strip()

    def test_one_question_passes(self):
        self.assertEqual(self.reply("What type of practice is it?"), "")

    def test_two_questions_block(self):
        self.assertIn("block", self.reply("How many per week? And who makes them?"))

    def test_compound_question_blocks(self):
        self.assertIn("block", self.reply("How many per week, and who makes them?"))

    def test_gap_list_counts_as_one(self):
        self.assertEqual(self.reply("Three quick gaps:\n1. Which channel?\n2. Which date?\n3. Price?"), "")

    def test_quoted_question_ignored(self):
        self.assertEqual(self.reply('She asked "is this right?". What does your week look like?'), "")

    def test_to_whom_compound_blocks(self):
        self.assertIn("block", self.reply("What do you sell, and to whom?"))

    def test_translation_line_ignored(self):
        self.assertEqual(self.reply("Wil je erbij zijn?\nIn English: Want to join?"), "")

    def test_note_to_self_blocks(self):
        self.assertIn("block", self.reply("Note to self: run the script. How many?"))

    def test_false_save_claim_blocks(self):
        self.assertIn("block", self.reply("I added this to business-context.md."))
        self.assertEqual(self.reply("I added this to business-context.md.", tool="Write"), "")

    def test_inactive_skill_and_loop_guard(self):
        self.assertEqual(self.reply("A? B?", skill="some-other-skill"), "")
        self.assertEqual(self.reply("A? B?", active=True), "")


if __name__ == "__main__":
    unittest.main()
