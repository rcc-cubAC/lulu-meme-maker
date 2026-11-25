#!/usr/bin/env python3
"""Add exact Chinese dialogue to a clean, text-free Lulu image.

Usage:
    python scripts/add_subtitle.py --input base.png --output final.png \
        --text '那就容我袁公噜告老还乡了'

Requires: Pillow; an installed Chinese CJK font (Noto Sans CJK Bold preferred).
Does not delete or inpaint existing subtitles.
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


FONT_CANDIDATES = [
    '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',
    '/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    'C:/Windows/Fonts/msyhbd.ttc',
    'C:/Windows/Fonts/simhei.ttf',
]


def resolve_font(explicit: str | None) -> str:
    if explicit:
        path = Path(explicit).expanduser()
        if not path.is_file():
            raise FileNotFoundError(f'字体文件不存在：{path}')
        return str(path)
    for path in FONT_CANDIDATES:
        if Path(path).is_file():
            return path
    try:
        result = subprocess.run(['fc-match', '-f', '%{file}', 'Noto Sans CJK SC:style=Bold'],
                                text=True, capture_output=True, check=True)
        path = result.stdout.strip()
        if path and Path(path).is_file():
            return path
    except (OSError, subprocess.CalledProcessError):
        pass
    raise FileNotFoundError('找不到能显示中文的字体，请安装 Noto Sans CJK Bold 或使用 --font-path 指定。')


def line_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> float:
    return draw.textlength(text, font=font)


def wrap_line(text: str, max_width: float, font: ImageFont.FreeTypeFont,
              draw: ImageDraw.ImageDraw) -> list[str]:
    # Preserve explicit line breaks. Chinese subtitles are wrapped by Unicode character,
    # never truncated or rewritten.
    out: list[str] = []
    for paragraph in text.split('\n'):
        if not paragraph:
            out.append('')
            continue
        current = ''
        for ch in paragraph:
            if current and line_width(draw, current + ch, font) > max_width:
                out.append(current)
                current = ch
            else:
                current += ch
        out.append(current)
    return out


def render(input_file: Path, output_file: Path, text: str, font_path: str,
           max_lines: int = 2, width_fraction: float = 0.92,
           bottom_fraction: float = 0.065, override_size: int | None = None) -> None:
    if not text.strip():
        raise ValueError('字幕不能为空。')
    if max_lines < 1:
        raise ValueError('--max-lines 必须为正整数。')
    with Image.open(input_file) as im:
        canvas = im.convert('RGBA')
    width, height = canvas.size
    draw = ImageDraw.Draw(canvas)
    max_width = width * width_fraction
    max_size = override_size if override_size else max(20, round(min(height * 0.082, width * 0.074)))
    min_size = max(12, round(min(height * 0.028, width * 0.024)))
    chosen_font = None
    chosen_lines = None
    chosen_size = None

    for font_size in range(max_size, min_size - 1, -1):
        font = ImageFont.truetype(font_path, font_size)
        lines = wrap_line(text.strip(), max_width, font, draw)
        if len(lines) <= max_lines:
            chosen_font, chosen_lines, chosen_size = font, lines, font_size
            break

    if chosen_font is None or chosen_lines is None or chosen_size is None:
        raise ValueError('台词过长，无法在指定行数内显示。请手动换行或放宽 --max-lines。')

    stroke = max(2, round(chosen_size * 0.095))
    ascent, descent = chosen_font.getmetrics()
    line_height = round((ascent + descent) * 1.03)
    block_height = len(chosen_lines) * line_height
    bottom_margin = round(height * bottom_fraction)
    start_y = height - bottom_margin - block_height
    if start_y < 0:
        raise ValueError('图像过小，无法放置字幕。')

    for index, line in enumerate(chosen_lines):
        cx = round(width / 2)
        cy = round(start_y + (index + 0.5) * line_height)
        # Black outline and a soft black offset create the familiar meme caption look.
        draw.text((cx + 1, cy + 2), line, font=chosen_font, anchor='mm',
                  fill=(0, 0, 0, 96), stroke_width=stroke + 1,
                  stroke_fill=(0, 0, 0, 120))
        draw.text((cx, cy), line, font=chosen_font, anchor='mm',
                  fill=(255, 255, 255, 255), stroke_width=stroke,
                  stroke_fill=(8, 8, 8, 255))

    output_file.parent.mkdir(parents=True, exist_ok=True)
    if output_file.suffix.lower() in {'.jpg', '.jpeg'}:
        canvas.convert('RGB').save(output_file, quality=95, subsampling=0)
    else:
        canvas.save(output_file)
    print(f'已保存：{output_file} | {width}×{height} | {chosen_size}px | {len(chosen_lines)}行')


def main() -> None:
    parser = argparse.ArgumentParser(description='为无字噜噜图片添加精确、统一的中文字幕。')
    parser.add_argument('--input', required=True, type=Path, help='无字幕底图')
    parser.add_argument('--output', required=True, type=Path, help='输出 PNG/JPG 路径')
    parser.add_argument('--text', required=True, help='准确字幕（原样输出；可包含换行符）')
    parser.add_argument('--font-path', default=None, help='可选字体路径，默认自动寻找 Noto Sans CJK Bold')
    parser.add_argument('--font-size', type=int, default=None, help='可选最大字号，不保证最终字号相同')
    parser.add_argument('--max-lines', type=int, default=2)
    parser.add_argument('--width-fraction', type=float, default=0.92)
    parser.add_argument('--bottom-fraction', type=float, default=0.065)
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f'找不到输入图片：{args.input}')
    font = resolve_font(args.font_path)
    render(args.input, args.output, args.text, font, args.max_lines,
           args.width_fraction, args.bottom_fraction, args.font_size)


if __name__ == '__main__':
    main()
