---
title: Spark-TTS
---

# Spark-TTS (SparkAudio)

项目地址: https://github.com/SparkAudio/Spark-TTS

## 主要特性

- **高质量语音合成**：采用VITS端到端模型，生成自然、流畅的语音。
- **低延迟实时推理**：支持 GPU/CPU 实时推理，适合应用于交互式语音系统。
- **多声纹支持**：预训练多个声纹，可通过 `--speaker_id` 轻松切换。
- **易用的接口**：提供命令行脚本和 Python API，使用极其简便。
- **Docker 化部署**：可直接构建 Docker 镜像，快速部署到服务器或容器化环境。

## 功能概览

| 功能 | 说明 |
|------|------|
| 文本 → 语音 | 直接将输入文本转为 wav/mp3 音频 |
| 参数调节 | 文字转语音时可调节速度、音高、音色等 |
| 批量合成 | 支持一次性合成多条文本，输出多文件 |
| Docker 镜像 | 提供 `Dockerfile`，可一键构建镜像进行推理 |
| 兼容多平台 | 可在 Linux/MacOS/Windows 上运行，CPU 与 GPU均可 |
| 开源可复现 | 所有模型、代码、依赖均公开，方便复现与研究 |

## 快速使用

```bash
# 1. 克隆仓库
git clone https://github.com/SparkAudio/Spark-TTS
cd Spark-TTS

# 2. 安装依赖
pip install -r requirements.txt

# 3. 调用 Python API 合成语音
python inference.py --text "你好，世界！" --speaker_id 0 --out_path out.wav

# 4. 或使用一键脚本
./run.sh text="你好，世界！" speaker_id=0 out_path=hello.wav
```

**参数说明**

- `--text`：待合成的文本字符串。  
- `--speaker_id`：选择预训练的声纹 ID（默认 0）。  
- `--out_path`：输出音频文件路径。  

可以根据需要调整速度、音高等，可在命令行或 Python 调用时添加相应参数。

## Docker 部署

```bash
# 构建镜像
docker build -t spark-tts .

# 启动并推理
docker run --gpus all \
  -v $(pwd)/output:/output \
  spark-tts:latest \
  python inference.py --text "你好" --speaker_id 0 --out_path /output/hello.wav
```

> 该 Docker 镜像已包含所有依赖，容器中可以直接运行推理脚本。

## 贡献与许可

- **贡献方式**：提交 Issue 或 Pull Request。  
- **许可证**：Apache‑2.0。

**一句话总结**：Spark‑TTS 是 SparkAudio 提供的高质量、低延迟、易用的端到端文本转语音系统，支持多声纹、Docker 化部署，可快速集成到任何语音相关项目中。