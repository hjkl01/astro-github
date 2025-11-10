---
title: tortoise-tts
---

# Tortoise TTS 项目

**项目地址:** [https://github.com/neonbjb/tortoise-tts](https://github.com/neonbjb/tortoise-tts)

## 主要特性
Tortoise TTS 是一个先进的文本到语音（Text-to-Speech, TTS）合成系统，基于深度学习技术，具有以下主要特性：
- **高保真语音合成**：生成自然、富有表现力的语音，支持多说话者声音克隆，能产生接近人类水平的音频质量。
- **声音克隆功能**：只需提供几秒钟的参考音频样本，即可克隆特定说话者的声音，实现个性化语音生成。
- **多语言支持**：主要针对英语，但可扩展到其他语言，通过训练模型实现。
- **开源与可扩展**：使用PyTorch构建，允许用户自定义模型、训练新数据或集成到其他应用中。
- **实时与离线模式**：支持快速推理，适用于从命令行到Web应用的各种场景。

## 主要功能
- **文本到语音转换**：将输入文本转换为音频，支持情感和语调控制。
- **说话者适应**：通过参考音频自动适应声音特征，包括音调、语速和口音。
- **批量处理**：可处理多个文本输入，同时生成音频文件。
- **模型训练**：提供工具用于微调模型，以适应特定数据集或声音。
- **音频后处理**：内置噪声抑制和音频增强功能，提升输出质量。

## 用法
### 安装
1. 克隆仓库：
   ```
   git clone https://github.com/neonbjb/tortoise-tts.git
   cd tortoise-tts
   ```
2. 安装依赖（推荐使用Python 3.9+和虚拟环境）：
   ```
   pip install -r requirements.txt
   pip install -e .
   ```
3. 下载预训练模型（通过脚本或手动从仓库releases获取）。

### 基本用法
- **命令行生成语音**：
  ```
  python tortoise/do_tts.py --text "你好，这是一个测试。" --voice "random" --preset "fast" --output_path output.wav
  ```
  - `--text`：输入文本。
  - `--voice`：指定声音（预设或参考音频路径）。
  - `--preset`：质量预设（ultra_fast, fast, standard, high_quality）。
  - `--output_path`：输出音频文件路径。

- **声音克隆**：
  提供参考音频文件夹：
  ```
  python tortoise/do_tts.py --text "克隆的声音测试。" --voice "path/to/reference_audio" --output_path cloned.wav
  ```

- **高级用法**：
  - 使用API集成：导入`tortoise.api`模块，在Python脚本中调用`tts()`函数生成音频。
  - 训练自定义模型：运行`python tortoise/train.py`并提供数据集。
  - 示例脚本：仓库中包含`recipes/`文件夹，提供完整示例，如长文本合成或多说话者生成。

更多细节请参考仓库的README和文档。建议在GPU环境中运行以获得最佳性能。