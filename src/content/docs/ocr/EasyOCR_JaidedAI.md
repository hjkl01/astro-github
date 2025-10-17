
---
title: EasyOCR
---

# EasyOCR 项目介绍

## 项目地址
[GitHub 项目地址](https://github.com/JaidedAI/EasyOCR)

## 主要特性
EasyOCR 是一个开源的 OCR（光学字符识别）工具，支持超过 80 种语言的文本检测和识别。它基于深度学习模型，易于集成到各种应用中。主要特性包括：
- **多语言支持**：内置 80+ 种语言模型，包括中文、英文、日文等，支持自定义语言训练。
- **高准确率**：使用先进的 CNN 和 RNN 模型，实现高效的文本检测和识别，适用于复杂背景和各种字体。
- **轻量级部署**：无需复杂配置，支持 CPU 和 GPU 加速，适合移动端和服务器环境。
- **易用性**：简单 API 接口，快速上手，支持图像、视频和实时捕获的输入。
- **开源免费**：MIT 许可，社区活跃，提供预训练模型和文档。

## 主要功能
- **文本检测**：自动定位图像中的文本区域，支持倾斜和曲面文本。
- **文本识别**：提取并识别文本，支持数字、字母和符号。
- **批量处理**：处理多张图像或视频帧，实现高效批量 OCR。
- **自定义训练**：允许用户基于自定义数据集训练模型，提高特定场景的准确率。
- **输出格式**：返回识别结果的文本、置信度和边界框信息，便于后续处理。

## 用法
### 安装
使用 pip 安装：
```bash
pip install easyocr
```

### 基本用法
1. **导入库**：
   ```python
   import easyocr
   ```

2. **初始化 Reader**（指定语言，例如 'ch_sim' 为简体中文）：
   ```python
   reader = easyocr.Reader(['ch_sim', 'en'])  # 支持中英文
   ```

3. **读取图像**：
   ```python
   results = reader.readtext('path/to/image.jpg')
   ```

4. **输出结果**：
   - `results` 是一个列表，每个元素包含 [边界框, 文本, 置信度]。
   - 示例输出：
     ```python
     for (bbox, text, confidence) in results:
         print(f"文本: {text}, 置信度: {confidence}")
     ```

### 高级用法
- **GPU 加速**：初始化时设置 `reader = easyocr.Reader(['ch_sim'], gpu=True)`。
- **自定义参数**：如 `reader.readtext('image.jpg', detail=0)` 只返回文本（无边界框）。
- **实时视频**：结合 OpenCV 处理视频流，实现实时 OCR。
- 更多示例和文档请参考项目 README。