---
title: stable-diffusion-webui
---

# Stable Diffusion Web UI

Stable Diffusion Web UI 是一个基于 Gradio 库实现的 Stable Diffusion Web 界面，提供了一个用户友好的方式来生成和编辑图像。

## 功能

- **文本到图像 (txt2img)**: 从文本提示生成图像。
- **图像到图像 (img2img)**: 使用现有图像作为起点生成新图像。
- **修复 (Inpainting)**: 修复图像的特定部分。
- **外扩 (Outpainting)**: 扩展图像边界。
- **颜色草图 (Color Sketch)**: 基于草图生成彩色图像。
- **提示矩阵 (Prompt Matrix)**: 探索不同提示组合的效果。
- **上采样 (Stable Diffusion Upscale)**: 提高图像分辨率。
- **注意力控制**: 使用语法如 `((tuxedo))` 或 `(tuxedo:1.21)` 来强调提示中的特定部分。
- **循环处理 (Loopback)**: 多次运行 img2img 以迭代改进图像。
- **X/Y/Z 图**: 生成参数变化的三维图像图。
- **文本反转 (Textual Inversion)**: 使用自定义嵌入来训练模型。
- **额外功能 (Extras tab)**:
  - GFPGAN: 修复面部。
  - CodeFormer: 面部修复替代方案。
  - RealESRGAN/ESRGAN: 神经网络上采样器。
  - SwinIR/Swin2SR: 高级上采样器。
  - LDSR: 潜在扩散超分辨率。
- **高级采样**: 多种采样方法，支持调整 eta 值。
- **批处理**: 处理多个文件。
- **高分辨率修复 (Highres Fix)**: 一键生成高分辨率图像。
- **检查点合并**: 合并多个模型检查点。
- **自定义脚本**: 支持社区扩展。
- **可组合扩散**: 使用 `AND` 组合多个提示。
- **无令牌限制**: 支持长提示。
- **DeepDanbooru**: 为动漫提示生成标签。
- **xformers**: 加速推理。
- **训练**: 支持超网络、嵌入和 LoRA。
- **API**: 提供编程接口。
- **其他**: 样式、变体、种子调整、CLIP 询问等。

## 用法

### 安装

确保满足依赖项（Python 3.10.6, Git 等）。

#### Windows (自动安装)

1. 安装 Python 3.10.6 和 Git。
2. 克隆仓库：`git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`。
3. 运行 `webui-user.bat`。

#### Linux (自动安装)

1. 安装依赖：
   ```bash
   sudo apt install wget git python3 python3-venv libgl1 libglib2.0-0
   ```
2. 克隆仓库或下载脚本：
   ```bash
   git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
   ```
3. 运行 `webui.sh`。

#### 其他平台

参考 Wiki 中的安装指南，支持 AMD GPU、Intel CPU/GPU、Apple Silicon 等。

### 运行

运行启动脚本后，Web UI 将在浏览器中打开。输入提示，选择参数，然后生成图像。

- **提示**: 描述要生成的图像。
- **负面提示**: 指定要避免的内容。
- **参数**: 调整步骤、CFG 比例、种子等。
- **模型**: 加载不同的 Stable Diffusion 模型。

更多详细信息请参考项目的 [Wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki)。
