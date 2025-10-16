
---
title: CosyVoice
---

# CosyVoice 项目

## 项目地址
[https://github.com/FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice)

## 主要特性
CosyVoice 是一个多语言语音生成模型，支持零样本和少样本语音克隆，能够生成高质量、自然的语音输出。主要特性包括：
- **多语言支持**：支持中文、英文、日文等多种语言的语音合成。
- **语音克隆**：通过少量参考音频（零样本或少样本）实现语音克隆，保留说话者的音色和风格。
- **情感控制**：支持控制语音的情感表达，如快乐、悲伤等，提升表达的自然度。
- **高效推理**：优化后的模型支持实时语音生成，适用于各种应用场景。
- **开源模型**：基于FunAudioLLM框架，提供预训练模型和训练工具，便于二次开发。

## 主要功能
- **文本到语音（TTS）**：将输入文本转换为自然流畅的语音。
- **语音风格迁移**：基于参考音频生成具有特定风格的语音输出。
- **多说话人支持**：可处理多个说话人的语音生成和克隆。
- **模型训练**：提供训练脚本，支持自定义数据集进行模型微调。
- **推理接口**：支持命令行和API调用，便于集成到其他应用中。

## 用法
### 安装
1. 克隆仓库：`git clone https://github.com/FunAudioLLM/CosyVoice.git`
2. 安装依赖：`pip install -r requirements.txt`
3. 下载预训练模型：从仓库的Releases或Hugging Face Hub下载模型权重。

### 基本推理
使用命令行生成语音：
```
python scripts/inference.py --text "你好，世界" --ref_audio "reference.wav" --output "output.wav"
```
- `--text`：输入文本。
- `--ref_audio`：参考音频路径（用于语音克隆）。
- `--output`：输出音频路径。

### API使用
启动服务：
```
python scripts/api_server.py
```
然后通过HTTP POST请求调用，例如：
```python
import requests
response = requests.post("http://localhost:8000/tts", json={
    "text": "你好，世界",
    "ref_audio": "reference.wav"
})
with open("output.wav", "wb") as f:
    f.write(response.content)
```

### 训练
1. 准备数据集：组织音频和文本对。
2. 运行训练脚本：`python train.py --config config.yaml`
详细用法请参考仓库的README.md和examples目录。