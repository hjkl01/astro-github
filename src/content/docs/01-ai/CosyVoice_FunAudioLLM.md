
---
title: CosyVoice
---


# CosyVoice - FunAudioLLM

> GitHub 项目地址: [https://github.com/FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice)

## 项目简介
CosyVoice 是一款基于 FunAudioLLM 的端到端、多语种文本转语音（TTS）系统，专注于高质量、低延迟的语音合成。项目实现了多语种支持、流式推理、个性化声音调教等功能，适合对 TTS 性能有较高要求的场景。

## 主要特性
- **多语种支持**：覆盖中文、英文、日语、法语、德语等多种语言。
- **高清语音合成**：采用最新的声码器与预训练模型，实现自然流畅的音质。
- **流式推理**：支持按需实时生成音频，适用于聊天机器人、语音助手等场景。
- **个性化声音**：提供 Voice-Conversion（VC）接口，可根据目标声音进行调音。
- **轻量部署**：支持 Docker、ONNX、OpenVINO 部署，易于本地或云端部署。
- **可扩展性**：代码结构模块化，便于接入新的声学## 功能列表
| 功能 | 描述 |
|------|------|
| 文本前处理 | 文字标点分割、去除无用符号、语言检测 |
| 语音合成 | 利用 Tacotron2+MelGAN/Hermes 进行声纹合成 |
| 语音转换 | 将目标声纹迁移到原始音频 |
| API 接口 | RESTful + gRPC 接口，支持批量请求 |
| 可视化 | 在线 Demo 与本地 Web UI，实时预览 |
| 评估 | 自动化指标评估（MOS、Perceptual音频） |

## 快速上手

### 1. 克隆仓库
```bash
git clone https://github.com/FunAudioLLM/CosyVoice.git
cd CosyVoice
```

### 2. 环境准备
```bash
# 建议使用 conda 虚拟环境
conda create -n cosyvoice python=3.10
conda activate cosyvoice
pip install -r requirements.txt
```

### 3. 预训练模型下载
```bash
# 预训练模型已放在 releases，下载后放到 models/ 目录
wget https://github.com/FunAudioLLM/CosyVoice/releases/download/vx.y/models.zip
unzip models.zip -d models/
```

### 4. 启动服务
```bash
# RESTful API 示例
python serve_api.py --config configs/api.yaml
# Web Demo
python demo_web.py --config configs/web.yaml
```

### 5. 通过 API 合成语音
```bash
curl -X POST http://localhost:8000/tts \
  -H "Content-Type: application/json" \
  -d '{"text":"你好，世界！","lang":"zh"}' \
  --output output.wav
```

### 6. 流式推理
```bash
python demo_stream.py --text "这是流式语音合成示例。"
```

### 7. 进行语音转换（VC）
```bash
python vc_demo.py \
  --source wav/src.wav \
  --target wav/target.wav \
  --output wav/converted.wav
```

## 开发与贡献
- 代码遵循 PEP8 规范，注释中文。
- 新功能请提交 PR 并详细描述。
- 发表 issue 前请仔细阅读官方文档。

## 文档与帮助
- 官方 Wiki: https://github.com/FunAudioLLM/CosyVoice/wiki
- 示例脚本: `scripts/`
- 配置文件示例: `configs/`

---

> 以上内容为 CosyVoice 项目概要与快速使用指南，更多细节请参阅官方仓库与 Wiki。
