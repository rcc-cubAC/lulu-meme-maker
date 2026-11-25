# 噜噜影视名场面 Skill — 快速使用

## 一句话使用

上传一张影视截图并输入：“**按 lulu-meme-maker 工作流，把图里[人物]替换为噜噜，名字改成[新名字]，保留[动作和眼神方向]，字幕改为‘[准确台词]’，单独出一张完整图，去掉水印、弹幕、日文假名和平台UI，字幕统一白粗体黑描边。**”

## 三个经过讨论的例子

- 马噜：白马与银甲，头微微向左、眼神斜视右前方，短圆手向前指；台词 `曹贼`。
- 袁公噜：肩甲贴合胖身，酒红围巾、火光古堡背景，微微不甘的眼神；台词 `那就容我袁公噜告老还乡了`。
- 邢道噜：顶戴铆钉盔、短手小胖肚、张嘴喊话，背后刘字旗；台词 `我乃是零陵上将军邢道噜`。

## 使用完整包

本包是一个遵循 Agent Skills 约定的文件夹，包含 `SKILL.md`、参考图、成品示例、工作流与字幕辅助脚本。

**在支持本地 Skills 的 Codex 或 ChatGPT 桌面工作环境中**：将 `lulu-meme-maker` 整个文件夹放入支持的 Skills 目录（Codex 常用 `$HOME/.agents/skills/`；仓库可以放 `.agents/skills/`），再按所在应用的技能入口调用。技能会指导图片生成工具的使用，但需要该环境实际具备图片创作能力。

**在普通 ChatGPT 对话中**：可上传本包或单独的 `SKILL.md`、两张参考图，然后明确说“请按这套规则改这张图片”。上传文件只是提供上下文，并不等同于系统安装或自动启用 Skill。

**在本地添加精确字幕**：在 Skill 根目录安装 Pillow 并确保系统能找到中文粗体字体，运行如下命令。

```bash
python -m pip install Pillow
python scripts/add_subtitle.py --input clean_render.png --output finished.png --text '那就容我袁公噜告老还乡了'
```

Windows/macOS/Linux 的中文字体路径存在差异，脚本会优先找 Noto Sans CJK Bold；如果无法自动找到，可以用 `--font-path /路径/到/已安装字体文件` 指定。**字体文件本身不随包分发。**

## 参考文档

- 官方 Skills 编写说明：https://learn.chatgpt.com/docs/build-skills
- 角色造型与禁忌：`references/CHARACTER_DNA.md`
- 统一字体与精确台词：`references/SUBTITLE_STYLE.md`
- 完整生产流程：`WORKFLOW.md`
