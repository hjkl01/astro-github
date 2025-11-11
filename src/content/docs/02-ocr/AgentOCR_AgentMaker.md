---
title: AgentOCR
---

# AgentOCR 项目

**项目地址：** [https://github.com/AgentMaker/AgentOCR](https://github.com/AgentMaker/AgentOCR)

## 主要特性

- **使用简单、调用方便**：基于 PaddleOCR 和 ONNXRuntime 项目开发的一个 OCR 项目。
- **多语言支持**：支持中文、英文、韩文、日文、法文、德文等多种语言。
- **高精度识别**：采用先进的深度学习模型，实现高效的文本检测和识别。
- **模块化设计**：包含 Python Package、OCR 标注软件和中国车牌检测识别系统等子项目。
- **易集成**：提供 Python API，支持命令行和服务器部署。
- **开源免费**：Apache-2.0 许可，社区活跃。

## 主要功能

- **文本检测与识别**：自动检测图像中的文本区域，并提取内容，支持多种语言和复杂布局。
- **多语言 OCR**：内置多种预训练模型，支持中英文混合识别。
- **服务器部署**：支持 HTTP 接口调用，便于集成到应用中。
- **批量处理**：支持单张和多张图像处理。
- **可视化输出**：提供检测框、文本和置信度信息。

## 用法

### 安装

```bash
pip install agentocr
# 或根据设备安装 ONNXRuntime
pip install onnxruntime  # CPU 版本
pip install onnxruntime-gpu  # GPU 版本
```

### 基本用法

```python
from agentocr import OCRSystem

# 初始化 OCR 模型
ocr = OCRSystem(config='ch')  # 中文配置

# 进行 OCR 识别
results = ocr.ocr('test.jpg')
print(results)
```

### 服务器部署

```bash
agentocr server
```

然后通过 HTTP 请求调用：

```python
import requests
import base64

# 图片 Base64 编码
with open('test.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode()

data = {'image': image_data}
response = requests.post('http://127.0.0.1:5000/ocr', json=data)
print(response.json())
```

更多细节请参考项目 README 文件。
