---
title: cnocr
---

# cnocr 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/breezedeus/cnocr)

## 主要特性
cnocr 是一个基于深度学习的开源中文 OCR（光学字符识别）工具包，专注于高精度识别简体中文和繁体中文文本。它采用先进的神经网络模型（如 CRNN + CTC），支持多种字体、背景和噪声场景下的文本识别。核心特性包括：
- **高准确率**：针对中文字符优化，识别率可达 95% 以上，尤其在印刷体文本中表现优秀。
- **轻量级部署**：模型体积小，支持 CPU 和 GPU 加速，易于集成到移动或 Web 应用。
- **多语言支持**：主要针对简体/繁体中文，也可扩展到英文等其他语言。
- **自定义训练**：提供预训练模型，并支持用户基于自定义数据集进行微调。
- **无依赖复杂环境**：基于 PyTorch 实现，安装简单，兼容 Windows、Linux 和 macOS。

## 主要功能
- **文本检测与识别**：从图像中自动检测并提取文本行，支持单行、多行和复杂布局的 OCR。
- **批量处理**：可处理单张图像或批量图像文件，支持常见格式如 JPG、PNG、PDF（需额外转换）。
- **模型选择**：内置多种预训练模型，如 `densenet_lite_136-gru`（轻量版）和 `resnet50_all`（高精度版），用户可根据需求切换。
- **后处理优化**：集成拼音纠正和语言模型，提升识别结果的准确性和流畅度。
- **可视化输出**：提供文本位置框和置信度分数，便于调试和应用集成。

## 用法
### 安装
```bash
pip install cnocr
```

### 基本用法
1. **简单识别**：
   ```python
   from cnocr import CnOcr

   ocr = CnOcr()  # 使用默认模型
   img_path = 'path/to/your/image.jpg'
   out = ocr.ocr(img_path)
   print(out)  # 输出: [{'text': '识别结果', 'box': [...], 'score': 0.95}]
   ```

2. **指定模型和参数**：
   ```python
   from cnocr import CnOcr

   ocr = CnOcr(rec_model_name='densenet_lite_136-gru', det_model_name='ch_PP-OCRv3_det')
   out = ocr.ocr('image.jpg', det=True, rec=True, img_mode='RGB')
   ```

3. **批量处理**：
   ```python
   out_list = ocr.ocr(['img1.jpg', 'img2.jpg'])
   ```

4. **自定义训练**（高级用法）：
   - 下载数据集并准备标注。
   - 使用提供的训练脚本：`python train.py --config configs/rec_densenet_lite_136.yaml`。
   - 更多细节参考项目文档中的训练指南。

详细用法请参考项目 README 和示例代码。项目活跃维护，支持社区贡献。