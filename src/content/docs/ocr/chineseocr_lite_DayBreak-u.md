
---
title: chineseocr_lite
---

# ChineseOCR Lite 项目

## 项目地址
[https://github.com/DayBreak-u/chineseocr_lite](https://github.com/DayBreak-u/chineseocr_lite)

## 主要特性
- **轻量级设计**：基于ONNX Runtime优化，支持移动端和桌面端部署，模型大小小、推理速度快。
- **高精度中文OCR**：专注于中文文本识别，支持简体中文和繁体中文，识别准确率高。
- **端到端OCR**：集成文本检测和识别模块，无需额外配置复杂管道。
- **多平台支持**：兼容Windows、Linux、macOS，以及Android/iOS移动平台。
- **易集成**：提供Python API和示例，便于嵌入到其他应用中，如文档扫描、图像处理工具等。

## 主要功能
- **图像文本检测**：自动定位图像中的文本区域，支持多行、多角度文本。
- **中文文本识别**：对检测到的文本进行高精度识别，支持数字、标点和常见符号。
- **批量处理**：支持单张或多张图像输入，输出结构化文本结果。
- **自定义模型**：允许加载自定义训练的ONNX模型，实现个性化优化。
- **可视化输出**：可选生成带边界框的图像，便于调试和验证。

## 用法
### 安装
1. 克隆仓库：`git clone https://github.com/DayBreak-u/chineseocr_lite.git`
2. 安装依赖：`pip install -r requirements.txt`（包括onnxruntime、opencv-python等）。

### 基本用法（Python示例）
```python
from chineseocr_lite import ChineseOCR

# 初始化OCR引擎
ocr = ChineseOCR()

# 处理单张图像
img_path = 'path/to/image.jpg'
result = ocr.detect_and_ocr(img_path)

# 输出结果
for item in result:
    print(f"文本: {item['text']}, 置信度: {item['score']}")
```

### 高级用法
- **批量处理**：传入图像列表`ocr.detect_and_ocr(image_list)`。
- **仅检测**：使用`ocr.detect(img_path)`获取边界框。
- **仅识别**：使用`ocr.ocr(img_crop)`对裁剪图像进行识别。
- **移动端部署**：参考仓库中的Android/iOS示例，集成ONNX模型文件。

详细文档和更多示例请参考仓库的README.md文件。