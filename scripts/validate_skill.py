#!/usr/bin/env python3
"""Validate the shipped skill files and before/after image pairs (without OCR)."""
from pathlib import Path
from PIL import Image
import json

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "SKILL.md", "WORKFLOW.md", "QUICK_START.md", "ASSETS.md", "llms.txt",
    "references/CHARACTER_DNA.md", "references/SUBTITLE_STYLE.md",
    "references/PROMPT_TEMPLATES.md", "references/QA_CHECKLIST.md",
    "scripts/add_subtitle.py", "data/examples.json",
    "assets/references/lulu_waving_closeup.jpg", "assets/references/lulu_arms_folded_fullbody.jpg",
]
errors = []
for path in required:
    if not (ROOT / path).is_file():
        errors.append(f"Missing: {path}")

manifest_path = ROOT / "data/examples.json"
if manifest_path.exists():
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        examples = data["examples"]
        if len(examples) != 6:
            errors.append(f"Expected six comparison pairs, found {len(examples)}")
        for example in examples:
            for field in ("original", "result"):
                f = ROOT / example[field]
                if not f.exists():
                    errors.append(f"Missing example image: {f}")
                else:
                    try:
                        with Image.open(f) as im:
                            im.verify()
                    except Exception as exc:
                        errors.append(f"Unreadable image: {f}: {exc}")
            for required_field in ("role_cn", "role_en", "new_cn", "new_en", "dialogue"):
                if not example.get(required_field):
                    errors.append(f"Missing {required_field} for {example.get('slug')}")
        by_slug = {item["slug"]: item for item in examples}
        if by_slug.get("gongsun_zan", {}).get("role_cn") != "公孙瓒":
            errors.append("Laughing general must be identified as 公孙瓒")
        if by_slug.get("sun_ce", {}).get("role_cn") != "孙策":
            errors.append("Jade seal character must be identified as 孙策")
    except Exception as exc:
        errors.append(f"Invalid manifest: {exc}")
if not (ROOT / "SKILL.md").read_text(encoding="utf-8").startswith("---\nname: lulu-meme-maker\n"):
    errors.append("Missing skill front matter")
if errors:
    raise SystemExit("\n".join(errors))
print("Validated: required skill files and all six original/result image pairs.")
