---
title: Transformers
---

## 功能介绍

🤗 Transformers 是 Hugging Face 开发的开源库，提供最先进的预训练模型，用于文本、视觉、音频、视频和多模态任务的推理和训练。它作为模型定义框架，在生态系统中统一模型定义，确保兼容性。

- 支持超过 100 万个预训练模型检查点
- 涵盖自然语言处理、计算机视觉、音频处理等多个领域
- 易于使用，降低入门门槛
- 支持 PyTorch、JAX、TensorFlow 等框架
- 提供高性能推理和训练 API

## 用法

### 安装

需要 Python 3.9+ 和 PyTorch 2.1+。

```bash
pip install "transformers[torch]"
```

### 快速开始

使用 Pipeline API 进行推理，支持文本生成、语音识别、图像分类等任务。

#### 文本生成示例

```python
from transformers import pipeline

pipeline = pipeline(task="text-generation", model="Qwen/Qwen2.5-1.5B")
result = pipeline("the secret to baking a really good cake is ")
print(result)
```

#### 语音识别示例

```python
from transformers import pipeline

pipeline = pipeline(task="automatic-speech-recognition", model="openai/whisper-large-v3")
result = pipeline("https://example.com/audio.flac")
print(result)
```

#### 图像分类示例

```python
from transformers import pipeline

pipeline = pipeline(task="image-classification", model="facebook/dinov2-small-imagenet1k-1-layer")
result = pipeline("https://example.com/image.png")
print(result)
```

更多示例和文档请参考 [官方文档](https://huggingface.co/docs/transformers/index)。
