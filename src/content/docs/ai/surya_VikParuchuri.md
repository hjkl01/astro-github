---
title: surya
---

# Surya 项目

## 项目地址
[https://github.com/VikParuchuri/surya](https://github.com/VikParuchuri/surya)

## 主要特性
Surya 是一个开源的计算机视觉工具包，专注于对象检测、实例分割和语义分割任务。它基于 PyTorch 框架构建，支持多种预训练模型和高效的推理引擎。主要特性包括：
- **高性能对象检测**：支持 YOLO、Faster R-CNN 等算法，提供实时检测能力。
- **实例分割支持**：集成 Mask R-CNN 和其他分割模型，实现像素级对象分割。
- **语义分割功能**：使用 DeepLab 和 U-Net 等模型，对图像进行语义理解。
- **模型优化**：内置 TensorRT 和 ONNX 导出，支持 GPU/CPU 加速和移动端部署。
- **易扩展性**：模块化设计，便于自定义数据集训练和模型微调。
- **多语言支持**：提供 Python API，并兼容 Jupyter Notebook 环境。

## 主要功能
- **对象检测**：从图像或视频中识别和定位多个对象，支持自定义类别。
- **图像分割**：生成对象边界掩码，用于精确的区域提取。
- **基准测试**：内置 COCO 和 VOC 数据集评估工具，测量模型精度和速度。
- **训练管道**：端到端的训练支持，包括数据增强、损失函数优化和学习率调度。
- **可视化工具**：自动生成检测结果的可视化图像、热图和性能报告。
- **部署集成**：易于集成到 Web 应用、移动 App 或边缘设备中。

## 用法
### 安装
1. 克隆仓库：`git clone https://github.com/VikParuchuri/surya.git`
2. 进入目录：`cd surya`
3. 安装依赖：`pip install -r requirements.txt`
4. （可选）安装 PyTorch：`pip install torch torchvision`

### 基本用法示例
#### 对象检测
```python
from surya.detection import ObjectDetector
import cv2

# 初始化检测器（使用预训练 YOLO 模型）
detector = ObjectDetector(model_name="yolo_v5")

# 加载图像
image = cv2.imread("path/to/image.jpg")

# 运行检测
results = detector.detect(image)

# 可视化结果
detector.visualize(results, image, save_path="output.jpg")
```

#### 实例分割
```python
from surya.segmentation import InstanceSegmenter

# 初始化分割器
segmenter = InstanceSegmenter(model_name="mask_rcnn")

# 加载图像
image = cv2.imread("path/to/image.jpg")

# 运行分割
masks, boxes = segmenter.segment(image)

# 处理结果
for i, mask in enumerate(masks):
    cv2.imwrite(f"mask_{i}.png", mask * 255)
```

#### 训练自定义模型
1. 准备数据集：将标注文件置于 `data/` 目录下，支持 COCO 格式。
2. 运行训练脚本：`python train.py --model yolo --dataset custom --epochs 50`
3. 监控训练：使用 TensorBoard 查看日志 `tensorboard --logdir runs/`

### 注意事项
- 确保 CUDA 环境以获得最佳性能。
- 对于大型模型，推荐使用至少 8GB GPU 内存。
- 详细文档见仓库的 `docs/` 目录或 README.md 文件。