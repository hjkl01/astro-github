
---
title: Umi-OCR
---

# Umi-OCR 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/hiroi-sora/Umi-OCR)

## 主要特性
Umi-OCR 是一个开源的 OCR（光学字符识别）工具，专注于高效、准确的文本识别和图像处理。它基于 PaddleOCR 和其他开源引擎，支持多种语言识别，特别是中文、日文等亚洲语言。核心特性包括：
- **高精度识别**：集成 PaddleOCR 引擎，支持简体/繁体中文、英文、日文等多种语言，识别准确率高。
- **实时处理**：支持截图、文件上传和实时捕获图像，实现快速 OCR 操作。
- **多平台支持**：兼容 Windows、macOS 和 Linux 系统，提供 GUI 界面和命令行模式。
- **自定义配置**：允许用户调整识别模型、阈值和输出格式，支持批量处理。
- **开源免费**：采用 MIT 许可，用户可自由修改和扩展。

## 主要功能
- **图像文本提取**：从图片、PDF 或截图中提取文本，支持旋转校正和布局分析。
- **截屏 OCR**：一键截取屏幕区域并进行识别，适用于游戏、文档或网页内容提取。
- **批量处理**：处理文件夹中的多张图片，一次性输出所有识别结果。
- **语言模型切换**：内置多种预训练模型，可切换以优化特定语言或场景的识别效果。
- **结果导出**：支持文本、JSON 或 Markdown 格式导出，便于后续编辑和使用。
- **插件扩展**：可集成其他工具，如翻译接口或自动化脚本。

## 用法指南
### 安装
1. 从 GitHub 仓库克隆或下载项目：`git clone https://github.com/hiroi-sora/Umi-OCR.git`。
2. 安装依赖：确保 Python 3.7+ 环境，运行 `pip install -r requirements.txt`（包括 PaddlePaddle 和 PaddleOCR）。
3. 对于 GUI 版本，安装 PyQt5 或类似框架。

### 基本用法
1. **启动程序**：
   - GUI 模式：运行 `python main.py` 或双击可执行文件。
   - 命令行模式：`python ocr.py --image path/to/image.jpg`。

2. **进行 OCR**：
   - 在 GUI 中，选择“截屏”按钮捕获区域，或上传图像文件。
   - 设置语言（默认中文）和模型参数。
   - 点击“识别”按钮，查看提取的文本结果。
   - 示例命令行：`python ocr.py --image input.jpg --lang ch --output result.txt`（提取 input.jpg 的中文文本到 result.txt）。

3. **高级用法**：
   - 批量处理：`python batch_ocr.py --folder images/ --output results/`。
   - 自定义模型：编辑 `config.py` 文件加载自定义 PaddleOCR 模型。
   - 集成 API：项目支持 HTTP 接口，可作为后端服务调用。

更多细节请参考仓库的 README.md 文件。