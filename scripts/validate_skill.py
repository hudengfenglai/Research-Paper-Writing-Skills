from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "research-paper-writing"
errors = []

skill = ROOT / "SKILL.md"
if not skill.exists():
    errors.append("missing research-paper-writing/SKILL.md")
else:
    text = skill.read_text(encoding="utf-8")
    for required in ("name:", "description:", "Evidence before prose", "claim-evidence-matrix.md", "citation-integrity.md"):
        if required not in text:
            errors.append(f"SKILL.md missing required marker: {required}")

for path in sorted((ROOT / "references").glob("*.md")):
    if not path.read_text(encoding="utf-8").strip():
        errors.append(f"empty reference: {path.relative_to(ROOT)}")

for source in [skill, *sorted((ROOT / "references").glob("*.md"))]:
    if not source.exists():
        continue
    text = source.read_text(encoding="utf-8")
    for raw in re.findall(r"`(references/[A-Za-z0-9_./-]+\.md)`", text):
        target = ROOT / raw
        if not target.exists():
            errors.append(f"{source.relative_to(ROOT)} points to missing {raw}")

if errors:
    print("FAIL")
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)

print(f"PASS: {len(list((ROOT / 'references').glob('*.md')))} reference files checked")


