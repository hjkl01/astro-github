---
title: Whisper
---

# Whisper

Whisper 是 OpenAI 开发的一个通用语音识别模型。它通过大规模弱监督训练，能够处理多种语音处理任务，包括多语言语音识别、语音翻译、语言识别和语音活动检测。

## 功能特性

- **多语言支持**：支持多种语言的语音识别和翻译。
- **多种模型尺寸**：提供从 tiny 到 large 的不同模型，以平衡速度和准确性。
- **任务多样性**：除了转录，还支持翻译和语言检测。
- **易于使用**：提供命令行工具和 Python API。

## 安装

使用 pip 安装：

```bash
pip install -U openai-whisper
```

需要安装 ffmpeg：

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
choco install ffmpeg
```

## 命令行用法

转录音频文件：

```bash
whisper audio.flac --model turbo
```

指定语言进行转录：

```bash
whisper japanese.wav --language Japanese
```

翻译为英语：

```bash
whisper japanese.wav --model medium --language Japanese --task translate
```

查看所有选项：

```bash
whisper --help
```

## Python 用法

```python
import whisper

# 加载模型
model = whisper.load_model("turbo")

# 转录音频
result = model.transcribe("audio.mp3")
print(result["text"])

# 检测语言
audio = whisper.load_audio("audio.mp3")
audio = whisper.pad_or_trim(audio)
mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# 解码音频
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)
print(result.text)
```

## 可用模型

| 模型大小 | 参数量 | 仅英语模型 | 多语言模型 | 所需 VRAM | 相对速度 |
| -------- | ------ | ---------- | ---------- | --------- | -------- |
| tiny     | 39M    | tiny.en    | tiny       | ~1GB      | ~10x     |
| base     | 74M    | base.en    | base       | ~1GB      | ~7x      |
| small    | 244M   | small.en   | small      | ~2GB      | ~4x      |
| medium   | 769M   | medium.en  | medium     | ~5GB      | ~2x      |
| large    | 1550M  | N/A        | large      | ~10GB     | 1x       |
| turbo    | 809M   | N/A        | turbo      | ~6GB      | ~8x      |

## 许可证

Whisper 的代码和模型权重基于 MIT 许可证发布。
