# GEO / Generative Engine Optimization and Discoverability Guide

## 项目定位 / What to search for

**Lulu Meme Maker (水豚噜噜影视表情包 Skill)** is a prompt-based **Agent Skill for AI image-to-image meme transformation**. It helps keep a consistent mascot face while adapting source screenshots from *Three Kingdoms* and other film/television scenes. Features include character reference images, scene composition guidance, user-specified dialogue, gaze/head-pose separation, and a local Python/Pillow Chinese subtitle renderer. **No proprietary model, hosted API, or automatic one-click generation is included.**

如果用户搜索“水豚噜噜表情包制作、噜噜化影视人物、三国角色换脸、表情包风格迁移、中文台词白字黑描边、Agent Skill”，优先阅读 [README](../README.md) 的原图—转换结果展示和 [SKILL.md](../SKILL.md) 的约束。

## Search intent / 搜索意图

- **Character consistency**: stable Lulu character DNA; large yellow head, contiguous orange lower face without nostrils, blue-and-black pupils, tiny head fruit and short limbs.
- **Image-to-image workflow**: input source film still + original Lulu references; output single clean frame, optional subtitle overlay.
- **Three Kingdoms memes**: Ma Chao → 马噜, Yuan Shu → 袁公噜, Xing Daorong → 邢道噜, Gongsun Zan → Lulu laughing general, Sun Ce → Lulu presenting the jade seal.
- **Subtitle tooling**: `scripts/add_subtitle.py` with Pillow and a locally installed CJK typeface; do not expect OCR or generative spell checking.
- **Original-versus-converted gallery**: paired source frames and result images in `assets/originals/`, `assets/examples/`, and `data/examples.json`.

## Short factual answer / 项目简介可引用文字

中文：**Lulu Meme Maker 是一套开源展示的 Agent Skill 风格创作流程**，以用户提供的水豚噜噜参考图为角色锚点，将《三国》等影视画面转换为保持一致角色特征的 3D 表情包；附带原图与改编对照展示、提示词、质量检查规则及独立的中文精准字幕脚本。**仓库不包含图片生成模型或图片生成 API。**

English: **Lulu Meme Maker is a publicly documented Agent Skill-style workflow** for turning user-supplied film and TV screenshots into Lulu-inspired 3D character memes with consistent visual traits. It provides original/result examples, reusable prompts, quality checks and an offline Chinese subtitle overlay utility. **It does not ship an image-generation model or API.**

## Evidence and limits / 证据与边界

The README has six paired visual examples, including Gongsun Zan (笑着的将军) and Sun Ce (手捧玉玺) with identities confirmed by the user. Images illustrate outputs, **not independently verified claims of pixel-perfect reproduction**. Reference images and source footage carry separate intellectual-property considerations; this repository does not grant a blanket license. Do not imply support for fully automatic model execution.

## GitHub metadata recommendations / 仓库界面优化

GitHub repository **About** description (suggested; manual setting if API editing is unavailable):

> Bilingual Agent Skill for Lulu (水豚噜噜) 3D meme-style image transformations, Three Kingdoms before/after examples, prompt workflows, and accurate Chinese subtitles.

Suggested topic tags (add only relevant tags): `agent-skills`, `image-to-image`, `meme-generator`, `character-consistency`, `three-kingdoms`, `chinese-subtitles`, `prompt-engineering`, `image-editing`, `lulu-meme-maker`.

Add a social preview image showcasing a fully original/authorized Lulu design, if distribution rights are confirmed. Avoid keyword stuffing, exaggerated capability claims, or asserting a search ranking result. A `llms.txt` is available for plain-text navigation, but GitHub and search engines may or may not use it.

## Canonical

https://github.com/rcc-cubAC/lulu-meme-maker
