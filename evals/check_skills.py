#!/usr/bin/env python3
"""Validate skill frontmatter. Bad frontmatter means a skill silently never loads.

Run: python3 evals/check_skills.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = sorted((ROOT / ".agents/skills").glob("*/SKILL.md"))
KNOWN = {"ux-companion", "ux-discover", "ux-user-context", "ux-research", "ux-design-spec"}


def parse_frontmatter(text):
    """Return the frontmatter block's key/value pairs, or None if absent/unterminated."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if line.startswith((" ", "\t")) or ":" not in line:
            continue  # continuation or non-field line
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def check(path):
    """Yield problems with one SKILL.md."""
    slug = path.parent.name
    fm = parse_frontmatter(path.read_text(encoding="utf-8"))
    if fm is None:
        yield "missing or unterminated --- frontmatter block"
        return
    if fm.get("name") != slug:
        yield f"name is {fm.get('name')!r}, expected {slug!r} to match the directory"
    desc = fm.get("description", "")
    if len(desc) < 40:
        yield "description missing or too short to route on"
    elif "Use when" not in desc:
        yield "description should say when to use the skill ('Use when ...')"
    for tool in re.split(r",\s*", fm.get("allowed-tools", "")):
        if tool and not re.fullmatch(r"[A-Z][A-Za-z]*", tool):
            yield f"allowed-tools entry {tool!r} is not a bare tool name"


def main():
    if not SKILLS:
        print("FAIL: no skills found under .agents/skills/")
        return 1
    found = {p.parent.name for p in SKILLS}
    failures = [f"missing skill: {s}" for s in sorted(KNOWN - found)]
    for path in SKILLS:
        for problem in check(path):
            failures.append(f"{path.parent.name}: {problem}")

    for failure in failures:
        print(f"FAIL  {failure}")
    if failures:
        return 1
    print(f"ok    {len(SKILLS)} skills, frontmatter valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
