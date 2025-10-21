
---
title: speakr
---

# Speakr 项目

## 项目地址
[GitHub 项目地址](https://github.com/murtaza-nasir/speakr)

## 主要特性
Speakr 是一个基于 Python 的文本到语音 (TTS) 转换工具，主要特性包括：
- 支持多种语言的语音合成，使用 Google Text-to-Speech (gTTS) 引擎。
- 简单易用的命令行界面，适合快速转换文本为音频文件。
- 输出 MP3 格式音频，支持自定义文件名和保存路径。
- 轻量级设计，无需复杂配置，即开即用。
- 开源免费，基于 MIT 许可，便于扩展和修改。

## 功能
- **文本转语音**：将输入的文本转换为自然流畅的语音音频。
- **多语言支持**：默认支持英语，可通过参数指定其他语言（如中文、法语等）。
- **音频保存**：生成 MP3 文件，可用于播客、教育或辅助工具。
- **命令行集成**：通过终端运行，支持脚本自动化处理批量文本。

## 用法
1. **安装依赖**：
   - 克隆仓库：`git clone https://github.com/murtaza-nasir/speakr.git`
   - 进入目录：`cd speakr`
   - 安装 gTTS：`pip install gtts`

2. **运行命令**：
   - 基本用法：`python speakr.py "你的文本内容"`
     - 示例：`python speakr.py "Hello, this is a test."` 会生成 `output.mp3` 文件。
   - 指定语言：`python speakr.py "文本" --lang zh`（zh 为中文）。
   - 指定输出文件：`python speakr.py "文本" --output my_audio.mp3`。

3. **注意事项**：
   - 需要互联网连接以访问 gTTS 服务。
   - 支持的语言代码参考 gTTS 文档（如 en 为英语，zh 为中文）。
   - 如遇问题，检查 Python 版本（推荐 3.6+）和依赖安装。