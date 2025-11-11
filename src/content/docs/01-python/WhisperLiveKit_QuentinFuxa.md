---
title: WhisperLiveKit
---

## 功能介绍

WhisperLiveKit 是一个实时的、全本地化的语音转文字模型，支持说话人识别。它基于领先的研究技术，如 Simul-Whisper、NLLW 翻译、WhisperStreaming 等，提供超低延迟的转录。

主要功能：

- 实时语音转文字，直接在浏览器中显示
- 支持多种语言和翻译（200 种语言）
- 说话人识别（diarization）
- 语音活动检测（VAD）
- 支持 GPU 和 CPU 部署
- 提供后端服务器和前端界面

## 用法

### 安装

```bash
pip install whisperlivekit
```

### 快速开始

1. 启动转录服务器：

   ```bash
   whisperlivekit-server --model base --language en
   ```

2. 打开浏览器，访问 `http://localhost:8000`，开始说话即可实时看到转录结果。

### 高级用法

- 使用大模型并翻译：

  ```bash
  whisperlivekit-server --model large-v3 --language fr --target-language da
  ```

- 启用说话人识别：
  ```bash
  whisperlivekit-server --diarization --language fr
  ```

### Python API 示例

```python
from whisperlivekit import TranscriptionEngine, AudioProcessor
from fastapi import FastAPI, WebSocket

transcription_engine = TranscriptionEngine(model="medium", diarization=True, lan="en")
audio_processor = AudioProcessor(transcription_engine=transcription_engine)
```

### Docker 部署

- GPU 支持：

  ```bash
  docker build -t wlk .
  docker run --gpus all -p 8000:8000 --name wlk wlk
  ```

- CPU 支持：
  ```bash
  docker build -f Dockerfile.cpu -t wlk .
  docker run -p 8000:8000 --name wlk wlk
  ```

更多配置选项请参考项目文档。
