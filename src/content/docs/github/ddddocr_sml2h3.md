
---
title: ddddocr
---

# ddddocr 项目

## 项目地址
https://github.com/sml2h3/ddddocr

## 主要特性
ddddocr 是一个开源的 OCR（光学字符识别）工具，专注于识别各种验证码图像，如滑动验证码、旋转验证码、点选验证码等。它采用纯 Python 实现，轻量级且无需依赖外部服务，支持高精度识别。核心优势包括：
- **高兼容性**：支持多种验证码类型，包括常见的 12306 铁路验证码、腾讯滑动验证码等。
- **无深度学习依赖**：基于传统图像处理算法，运行速度快，资源消耗低。
- **易集成**：可作为 Python 库导入，支持命令行和 API 调用。
- **开源免费**：MIT 许可，社区活跃，可自定义扩展。

## 主要功能
- **验证码识别**：自动解析图像中的文字、数字、汉字或图形验证码。
- **滑动验证码破解**：检测滑块缺口位置，支持自动计算偏移量。
- **点选验证码处理**：识别图像中的特定点位或路径。
- **批量处理**：支持处理多张图像，提高效率。
- **自定义模型**：允许用户训练或加载自定义识别模型以适应特定场景。

## 用法
### 安装
```bash
pip install ddddocr
```

### 基本用法（Python 脚本示例）
1. **简单 OCR 识别**：
   ```python
   import ddddocr

   ocr = ddddocr.DdddOcr()
   with open('captcha.png', 'rb') as f:
       image = f.read()
   result = ocr.classificationResult(image)
   print(result)  # 输出识别结果，如 "1234"
   ```

2. **滑动验证码识别**：
   ```python
   import ddddocr

   det = ddddocr.DdddOcrDet()
   with open('slide.png', 'rb') as f:
       image = f.read()
   res = det.detection(image)
   print(res)  # 输出滑块位置信息
   ```

3. **命令行用法**：
   ```bash
   ddddocr -i captcha.png  # 识别单张图像
   ```

更多高级用法请参考 GitHub 仓库的 README 文档，包括 API 参数和示例代码。