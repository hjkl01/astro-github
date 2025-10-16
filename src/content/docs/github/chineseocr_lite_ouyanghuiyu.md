
---
title: chineseocr_lite
---

# ChineseOCR Lite 项目

## 项目地址
[https://github.com/ouyanghuiyu/chineseocr_lite](https://github.com/ouyanghuiyu/chineseocr_lite)

## 主要特性
- **轻量级设计**：基于轻量级OCR引擎，优化了模型大小和推理速度，适合移动端和边缘设备部署。
- **中文识别优化**：专注于中文文本识别，支持简体和繁体中文，准确率高，尤其适用于印刷体和手写体场景。
- **模块化架构**：包含文本检测（DBNet）和文本识别（CRNN）模块，支持端到端OCR流程。
- **易于集成**：提供Python和ONNX格式模型，便于与各种框架（如PaddlePaddle、TensorFlow）集成。
- **高性能**：在标准数据集（如CCPD、ICDAR）上表现出色，推理速度快，资源消耗低。

## 主要功能
- **文本检测**：自动定位图像中的文本区域，支持多行、多角度文本。
- **文本识别**：对检测到的文本进行字符级识别，支持中文、英文和数字混合。
- **端到端OCR**：从图像输入到文本输出的完整流程，支持批量处理。
- **模型导出**：可导出为ONNX或TensorRT格式，用于生产环境部署。
- **自定义训练**：提供训练脚本，支持用户基于自定义数据集微调模型。

## 用法
1. **安装依赖**：
   - 克隆仓库：`git clone https://github.com/ouyanghuiyu/chineseocr_lite.git`
   - 安装Python环境：`pip install -r requirements.txt`（包括PaddlePaddle、OpenCV等）。

2. **快速推理**：
   - 使用预训练模型：下载模型文件到`models/`目录。
   - 运行示例：`python demo.py --image_path your_image.jpg`
   - 输出：检测框坐标和识别文本结果。

3. **训练模型**：
   - 准备数据集：组织图像和标签文件。
   - 运行训练：`python train.py --config configs/det.yml`（检测模型）或`--config configs/rec.yml`（识别模型）。
   - 评估：`python eval.py --model_path output/model.pdparams`。

4. **部署**：
   - 导出ONNX：`python tools/export_model.py --model_dir output/ --format onnx`
   - 集成到应用：使用ONNX Runtime加载模型进行推理。

更多细节请参考仓库README。