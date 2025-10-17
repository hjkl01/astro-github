
---
title: pytesseract
---

# pytesseract 项目

**GitHub 项目地址:** [https://github.com/madmaze/pytesseract](https://github.com/madmaze/pytesseract)

## 主要特性
pytesseract 是一个 Python 包装器，用于 Tesseract OCR（光学字符识别）引擎。它提供了简单易用的接口，将图像转换为文本，支持多种语言识别和自定义配置。主要特性包括：
- **跨平台支持**：兼容 Windows、Linux 和 macOS。
- **多语言识别**：内置支持超过 100 种语言的 OCR 处理。
- **图像预处理集成**：可与 Pillow 等图像库结合，进行 OCR 前处理。
- **自定义选项**：支持 Tesseract 的各种参数配置，如页面分割模式（PSM）和字符白名单。
- **轻量级**：作为 Tesseract 的 Python 绑定，依赖 Tesseract 二进制文件，易于集成到 Python 项目中。

## 主要功能
- **文本提取**：从图像、PDF 或扫描文档中提取文本内容。
- **语言支持**：指定语言代码进行识别，例如英文（eng）、中文（chi_sim）。
- **配置参数**：调整 OCR 精度，如设置 DPI、输出格式（纯文本、hOCR 等）。
- **批量处理**：支持处理多页图像或文件序列。
- **错误处理**：提供异常捕获机制，确保鲁棒性。

## 用法
### 安装
首先安装 Tesseract OCR 引擎（从 [官方仓库](https://github.com/tesseract-ocr/tesseract) 下载），然后使用 pip 安装 pytesseract：
```
pip install pytesseract pillow
```

### 基本用法示例
1. **简单文本提取**：
   ```python
   import pytesseract
   from PIL import Image

   # 指定 Tesseract 路径（如果未在系统 PATH 中）
   # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Linux 示例

   # 打开图像
   image = Image.open('example.png')

   # 提取文本
   text = pytesseract.image_to_string(image, lang='eng')  # 指定语言
   print(text)
   ```

2. **带配置的提取**：
   ```python
   import pytesseract
   from PIL import Image

   image = Image.open('example.png')

   # 使用自定义配置
   custom_config = r'--oem 3 --psm 6'  # OEM: 引擎模式，PSM: 页面分割模式
   text = pytesseract.image_to_string(image, config=custom_config, lang='chi_sim')
   print(text)
   ```

3. **从 PDF 提取**（需结合 pdf2image 等库）：
   ```python
   from pdf2image import convert_from_path
   import pytesseract

   pages = convert_from_path('example.pdf', 300)  # DPI=300
   for page in pages:
       text = pytesseract.image_to_string(page, lang='eng')
       print(text)
   ```

更多高级用法请参考项目文档，包括数据输出格式（如 `image_to_boxes`、`image_to_data`）和性能优化。