
---
title: Spark-TTS
---

# Spark-TTS 项目

**项目地址：** [https://github.com/SparkAudio/Spark-TTS](https://github.com/SparkAudio/Spark-TTS?tab=readme-ov-file)

## 主要特性
Spark-TTS 是一个开源的文本到语音（Text-to-Speech, TTS）合成项目，由 SparkAudio 团队开发。它基于先进的深度学习模型，提供高质量的语音合成，支持多种语言和声音风格。主要特性包括：
- **高保真语音合成**：生成自然、流畅的语音输出，接近人类发音水平。
- **多语言支持**：兼容中文、英文等多种语言，适用于全球用户。
- **自定义声音**：支持多种声音模型和情感表达，如中性、快乐、悲伤等语气调整。
- **实时处理**：优化了推理速度，适合实时应用场景，如聊天机器人或语音助手。
- **开源与易集成**：基于 PyTorch 框架，代码开源，便于开发者二次开发和集成到其他项目中。
- **轻量级部署**：支持 CPU 和 GPU 加速，适用于从桌面到移动端的各种设备。

## 主要功能
- **文本转语音**：输入任意文本，快速生成对应的音频文件，支持 SSML（Speech Synthesis Markup Language）标签以控制发音和节奏。
- **声音克隆**：使用少量音频样本训练自定义声音模型，实现个性化语音合成。
- **批量处理**：支持批量转换文本列表，高效处理大量内容。
- **API 接口**：提供 RESTful API，便于 Web 应用集成。
- **音频格式支持**：输出 WAV、MP3 等常见格式，并支持采样率调整。
- **模型训练**：内置工具允许用户训练新模型，扩展语言或声音库。

## 用法
### 安装
1. 克隆仓库：
   ```
   git clone https://github.com/SparkAudio/Spark-TTS.git
   cd Spark-TTS
   ```
2. 安装依赖（推荐 Python 3.8+）：
   ```
   pip install -r requirements.txt
   ```
3. 下载预训练模型（从 README 中的链接获取）并放置到 `models/` 目录。

### 基本使用
- **命令行合成**：
  ```
  python tts.py --text "你好，这是 Spark-TTS 的测试。" --output output.wav --voice zh-female
  ```
  这将生成名为 `output.wav` 的音频文件。

- **Python API 示例**：
  ```python
  from spark_tts import TTS

  tts = TTS(model_path='models/spark_model.pth')
  audio = tts.synthesize("这是一个示例文本。", voice='zh-male', emotion='neutral')
  audio.save('result.wav')
  ```

- **训练自定义模型**：
  准备数据集后运行：
  ```
  python train.py --data_path your_dataset/ --epochs 100
  ```

详细用法请参考项目 README 文件中的示例和文档。项目支持 Docker 部署，便于环境隔离。