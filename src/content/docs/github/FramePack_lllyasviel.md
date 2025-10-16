
---
title: FramePack
---

# FramePack 项目

## 项目地址
[GitHub 项目地址](https://github.com/lllyasviel/FramePack)

## 主要特性
FramePack 是一个基于 PyTorch 的高效视频帧插值框架，专注于提升视频处理的速度和质量。主要特性包括：
- **高效的帧插值算法**：利用先进的神经网络模型，实现高帧率视频生成，支持从低帧率视频到高帧率的平滑转换。
- **实时处理能力**：优化了计算效率，适用于实时视频增强场景，如游戏录像或直播优化。
- **模块化设计**：易于扩展，支持自定义模型和插件，兼容多种视频格式（MP4、AVI 等）。
- **轻量级部署**：依赖少量资源，可在 CPU/GPU 上运行，适合个人开发者使用。
- **开源与社区支持**：完全开源，提供预训练模型和详细文档，便于二次开发。

## 主要功能
- **视频帧插值**：输入低帧率视频，输出高帧率版本，例如将 30FPS 视频转换为 60FPS 或更高。
- **运动补偿**：自动检测和补偿视频中的运动模糊，提高输出视频的流畅度和清晰度。
- **批量处理**：支持处理多个视频文件，一键优化。
- **可视化工具**：内置预览功能，允许用户实时查看插值效果并调整参数。
- **模型训练支持**：提供训练脚本，用户可使用自定义数据集训练模型。

## 用法
1. **环境准备**：
   - 克隆仓库：`git clone https://github.com/lllyasviel/FramePack.git`
   - 安装依赖：`pip install -r requirements.txt`（需要 Python 3.8+ 和 PyTorch）。

2. **基本使用**：
   - 运行主脚本：`python main.py --input video.mp4 --output output.mp4 --fps 60`
     - `--input`：输入视频路径。
     - `--output`：输出视频路径。
     - `--fps`：目标帧率（默认 60）。

3. **高级用法**：
   - 自定义模型：加载预训练模型 `python train.py --dataset path/to/data`。
   - 实时模式：`python realtime.py --device cuda`（使用 GPU 加速）。
   - 参数调整：通过配置文件 `config.yaml` 修改插值强度、质量设置等。

详细用法请参考仓库中的 README.md 文件。