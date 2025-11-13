---
title: repository
---

# MLX-Audio

MLX-Audio 是一个基于 Apple MLX 框架构建的文本到语音 (TTS)、语音到文本 (STT) 和语音到语音 (STS) 库，在 Apple Silicon 上提供高效的语音分析。

## 功能特性

- **高效推理**：在 Apple Silicon (M 系列芯片) 上快速推理
- **多语言支持**：支持多种语言
- **语音定制**：提供语音定制选项
- **速度控制**：可调节语音速度 (0.5x 到 2.0x)
- **交互式 Web 界面**：带有 3D 音频可视化
- **REST API**：用于 TTS 生成
- **量化支持**：优化性能
- **文件集成**：通过 Finder/Explorer 直接访问输出文件

## 安装

```bash
# 安装包
pip install mlx-audio

# 对于 Web 界面和 API 依赖
pip install -r requirements.txt
```

## 快速开始

### 命令行使用

```bash
# 基本使用
mlx_audio.tts.generate --text "Hello, world"

# 指定输出文件前缀
mlx_audio.tts.generate --text "Hello, world" --file_prefix hello

# 调整说话速度 (0.5-2.0)
mlx_audio.tts.generate --text "Hello, world" --speed 1.4
```

### Python 调用

```python
from mlx_audio.tts.generate import generate_audio

# 示例：生成有声读物章节为 mp3 音频
generate_audio(
    text=("In the beginning, the universe was created...\n"
        "...or the simulation was booted up."),
    model_path="prince-canuma/Kokoro-82M",
    voice="af_heart",
    speed=1.2,
    lang_code="a",  # Kokoro: (a)f_heart，或注释掉为自动
    file_prefix="audiobook_chapter1",
    audio_format="wav",
    sample_rate=24000,
    join_audio=True,
    verbose=True  # 设置为 False 禁用打印消息
)

print("有声读物章节成功生成！")
```

## Web 界面和 FastAPI 服务器

MLX-Audio 提供现代 Web 界面，具有实时音频可视化功能。界面提供：

1. 具有可定制语音和参数的文本到语音生成
2. 支持多种语言的语音到文本转录
3. 音频文件上传和播放功能
4. 交互式 3D 音频可视化
5. outputs 目录中的自动音频文件管理
6. 从界面直接访问输出文件夹 (仅本地部署)

### 启动服务器

**UI:**

```bash
# 配置 API 基础 URL 和端口
export NEXT_PUBLIC_API_BASE_URL=http://localhost
export NEXT_PUBLIC_API_PORT=8000

# 启动 UI 服务器
cd mlx_audio/ui
npm run dev
```

**服务器:**

```bash
# 使用命令行界面
mlx_audio.server

# 使用自定义主机和端口
mlx_audio.server --host 0.0.0.0 --port 9000

# 带详细日志
mlx_audio.server --verbose
```

然后在浏览器中打开：

```
http://127.0.0.1:8000
```

### API 端点

服务器提供以下 REST API 端点：

- `POST /v1/audio/speech`：从文本生成语音，遵循 OpenAI TTS 规范。
- `POST /v1/audio/transcriptions`：使用 STT 模型转录音频文件，与 OpenAI API 兼容。
- `GET /v1/models`：列出已加载的模型。
- `POST /v1/models`：按名称加载模型。
- `DELETE /v1/models`：卸载模型。

## 支持的模型

### Kokoro

Kokoro 是一个多语言 TTS 模型，支持各种语言和语音风格。

### CSM (Conversational Speech Model)

CSM 是来自 Sesame 的模型，允许文本到语音并使用参考音频样本定制语音。

## 高级功能

### 量化

您可以量化模型以提高性能：

```python
from mlx_audio.tts.utils import quantize_model, load_model
import json
import mlx.core as mx

model = load_model(repo_id='prince-canuma/Kokoro-82M')
config = model.config

# 量化到 8-bit
group_size = 64
bits = 8
weights, config = quantize_model(model, config, group_size, bits)

# 保存量化模型
with open('./8bit/config.json', 'w') as f:
    json.dump(config, f)

mx.save_safetensors("./8bit/kokoro-v1_0.safetensors", weights, metadata={"format": "mlx"})
```

## 要求

- MLX
- Python 3.8+
- Apple Silicon Mac (最佳性能)
- 对于 Web 界面和 API：
  - FastAPI
  - Uvicorn

## Swift 集成

此仓库还提供 Swift 包，用于在 macOS 和 iOS 上使用 Apple MLX 框架进行设备端 TTS。

### 支持平台

- **macOS**: 14.0+
- **iOS**: 16.0+

### 使用

```swift
import MLXAudio

// 使用内置语音创建会话 (首次使用时自动下载模型)
let session = try await MarvisSession(voice: .conversationalA) // 默认启用播放

// 一次性生成 (如果启用播放则自动播放)
let result = try await session.generate(for: "Your text here")
print("Generated \(result.sampleCount) samples @ \(result.sampleRate) Hz")
```
