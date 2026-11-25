#!/usr/bin/env python3
"""Offline, non-OCR package integrity checks for this Skill."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
required = [
    'SKILL.md',
    'WORKFLOW.md',
    'QUICK_START.md',
    'references/CHARACTER_DNA.md',
    'references/SUBTITLE_STYLE.md',
    'references/PROMPT_TEMPLATES.md',
    'references/QA_CHECKLIST.md',
    'scripts/add_subtitle.py',
    'assets/references/lulu_waving_closeup.jpg',
    'assets/references/lulu_arms_folded_fullbody.jpg',
    'assets/examples/ma_lu.jpg',
    'assets/examples/yuan_gong_lu.jpg',
    'assets/examples/xing_dao_lu.jpg',
]
errors = []
for item in required:
    file = ROOT / item
    if not file.is_file():
        errors.append(f'缺失：{item}')
        continue
    if file.suffix.lower() in {'.png', '.jpg', '.jpeg'}:
        try:
            with Image.open(file) as im:
                im.verify()
        except Exception as exc:
            errors.append(f'图像错误：{item}: {exc}')
if not (ROOT / 'SKILL.md').read_text(encoding='utf-8').startswith('---\nname: lulu-meme-maker\n'):
    errors.append('SKILL.md 的 YAML 元数据缺失或不正确')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'校验通过：{len(required)} 个核心文件，参考图与示例图均可读取。')
