
---
title: AI-Video-Transcriber
---

下面是 **AI-Video-Transcriber**（wendy7756 版）的主要特性、功能与使用方法，已按要求以 Markdown 格式编写，可直接保存为 `src/content/docs/00/AI-Video-Transcriber_wendy7756.md`。

```markdown
# AI-Video-Transcriber (wendy7756)

> **项目地址**：<https://github.com/wendy7756/AI-Video-Transcriber>

## 目录

- [简介](#简介)
- [主要特性](#主要特性)
- [功能概览](#功能概览)
- [安装与依赖](#安装与依赖)
- [使用方法](#使用方法)
  - [命令行工具](#命令行工具)
  - [Python API](#python-api)
- [常见问题](#常见问题)
- [贡献与反馈](#贡献与反馈)

---

## 简介

AI-Video-Transcriber 是一款基于 OpenAI Whisper 的视频转写工具。它可以从任意视频文件中提取音频、识别语音并生成时间戳式文本。支持多语言识别、自动语言检测、字幕文件生成（SRT/ASS/TTML）以及可选的中文翻译。适用于视频内容创作者、字幕制作、音频归档等场景。

---

## 主要特性

| 功能 | 说明 |
|------|------|
| **多格式视频支持** | 支持 MP4、MKV、AVI、MOV、FLV 等常见视频格式 |
| **高精度转写** | 采用 Whisper `large` 模型，兼顾速度与准确性 |
| **自动语言检测** | 无需手动指定语言，系统自动识别并转写 |
| **时间戳输出** | 生成带时间轴的文本，兼容 SRT、ASS、TTML 等字幕格式 |
| **可选翻译** | 支持将原始转写文本翻译为中文（或其他目标语言） |
| **分段处理** | 对长视频进行拆分，避免单次处理过大导致内存占用过高 |
| **轻量化安装** | 仅需 `pip install .`，自动拉取 `torch`、`ffmpeg` 等依赖 |

---

## 功能概览

- **视频转文本**：`transcribe_video.py` 读取视频文件，提取音频后调用 Whisper 完成转写，返回 JSON/文本结果。
- **字幕生成**：`subtitle_generator.py` 将转写结果转换为 SRT/ASS/TTML 格式，可直接导入视频编辑软件。
- **翻译功能**：`translator.py` 通过 OpenAI GPT 或本地模型将英文转写翻译为中文（可选）。
- **CLI 工具**：在 `cli.py` 中封装了完整的命令行接口，支持批量处理、日志输出、进度条等。
- **Python API**：提供 `Transcriber` 类，供其他 Python 项目直接调用。

---

## 安装与依赖

```bash
# 克隆仓库
git clone https://github.com/wendy7756/AI-Video-Transcriber.git
cd AI-Video-Transcriber

# 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
# 或者直接安装项目
pip install .
```

> **依赖说明**  
> - `torch`（CPU 版已足够）  
> - `ffmpeg`（系统层面安装，或使用 `ffmpeg-python` 包）  
> - `whisper`（OpenAI Whisper）  
> - `openai`（如果使用 GPT 翻译）  

> **可选**  
> - `tqdm`：进度条  
> - `pydub`：音频处理（已包含在 requirements）  

---

## 使用方法

### 命令行工具

```bash
# 基本转写
python -m ai_video_transcriber.cli \
  --input path/to/video.mp4 \
  --output transcript.txt

# 指定输出格式（srt、ass、ttml）
python -m ai_video_transcriber.cli \
  --input video.mp4 \
  --output subtitles.srt \
  --format srt

# 自动语言检测 + 翻译为中文
python -m ai_video_transcriber.cli \
  --input video.mp4 \
  --output transcript.txt \
  --translate zh

# 批量处理
python -m ai_video_transcriber.cli \
  --input-dir ./videos \
  --output-dir ./transcripts \
  --format srt
```

> **参数说明**  
> - `--input` / `--input-dir`：单个视频文件或文件夹  
> - `--output` / `--output-dir`：转写文件或字幕文件路径/文件夹  
> - `--format`：字幕格式（`srt`、`ass`、`ttml`）  
> - `--translate`：目标语言代码（如 `zh`、`en`、`es` 等）  
> - `--model`：Whisper 模型（`tiny`、`base`、`small`、`medium`、`large`）  
> - `--verbose`：打印详细日志  

### Python API

```python
from ai_video_transcriber import Transcriber

# 初始化
transcriber = Transcriber(
    model="large",
    device="cpu",            # 或 "cuda"
    translate_to="zh"        # 目标语言，None 表示不翻译
)

# 单文件转写
result = transcriber.transcribe("video.mp4")
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

# 生成字幕
srt = transcriber.to_srt(result)
with open("subtitles.srt", "w", encoding="utf-8") as f:
    f.write(srt)

# 批量处理
for video_path in ["a.mp4", "b.mkv"]:
    res = transcriber.transcribe(video_path)
    # ...
```

> **返回结构**  
> ```python
> {
>     "text": "完整转写文本",
>     "segments": [
>         {"start": 0.0, "end": 3.2, "text": "..."},
>         {"start": 3.2, "end": 6.5, "text": "..."},
>         ...
>     ],
>     "language": "en",
>     "translation": "中文翻译文本"  # 若开启 translate
> }
> ```

---

## 常见问题

| # | 说明 | 解决方案 |
|---|------|----------|
| 1 | **ffmpeg 未找到** | 在系统 PATH 中添加 ffmpeg，或安装 `ffmpeg-python` 并确保可执行文件可用 |
| 2 | **GPU 版本报错** | 确认已安装对应 CUDA 版本的 `torch`，可使用 `pip install torch==...+cu118` |
| 3 | **内存不足** | 对长视频使用 `--segment-length 600`（单位秒）或手动拆分视频 |
| 4 | **翻译失败** | 检查 `OPENAI_API_KEY` 环境变量是否已设置，或使用本地翻译模型 |

---

## 贡献与反馈

- **提交 Issue**：如果发现 bug 或有功能建议，请在 GitHub 仓库中提交 Issue。  
- **Pull Request**：欢迎任何形式的贡献，尤其是对模型微调、翻译改进、字幕格式扩展等方面。  
- **讨论**：在 Discussions 区域讨论使用体验、最佳实践。

---

**祝你使用愉快！** 🚀

```

将上述内容保存为 `src/content/docs/00/AI-Video-Transcriber_wendy7756.md` 即可。