---
title: Grounding DINO
---

# Grounding DINO

## 项目简介

Grounding DINO 是 IDEA-Research 团队开发的开源项目，实现论文 "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection" 中的模型。该模型结合了 DINO 和 Grounded Pre-Training，用于开放集对象检测，能够使用自然语言描述检测图像中的任意对象。

## 主要功能

- **开放集检测**：使用语言提示检测图像中的任何对象，无需预定义类别。
- **高性能**：在 COCO 数据集上实现 52.5 AP 的零样本性能，经过微调后可达 63.0 AP。
- **灵活集成**：可与 Stable Diffusion、GLIGEN 等模型结合，用于图像编辑和生成。
- **多模态**：结合文本和图像输入，实现语言引导的对象检测。

## 用法

### 安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/IDEA-Research/GroundingDINO.git
   cd GroundingDINO
   ```

2. 安装依赖：

   ```bash
   pip install -e .
   ```

3. 下载预训练权重：
   ```bash
   mkdir weights
   cd weights
   wget -q https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth
   cd ..
   ```

### 基本使用

#### 命令行推理

```bash
CUDA_VISIBLE_DEVICES=0 python demo/inference_on_a_image.py \
  -c groundingdino/config/GroundingDINO_SwinT_OGC.py \
  -p weights/groundingdino_swint_ogc.pth \
  -i image.jpg \
  -o output_dir \
  -t "chair . person . dog"
```

#### Python API

```python
from groundingdino.util.inference import load_model, load_image, predict, annotate
import cv2

model = load_model("groundingdino/config/GroundingDINO_SwinT_OGC.py", "weights/groundingdino_swint_ogc.pth")
image_source, image = load_image("image.jpg")
boxes, logits, phrases = predict(
    model=model,
    image=image,
    caption="chair . person . dog",
    box_threshold=0.35,
    text_threshold=0.25
)
annotated_frame = annotate(image_source=image_source, boxes=boxes, logits=logits, phrases=phrases)
cv2.imwrite("annotated_image.jpg", annotated_frame)
```

### 高级用法

- **零样本评估**：在 COCO 数据集上进行零样本检测评估。
- **图像编辑**：与 Stable Diffusion 或 GLIGEN 结合进行可控图像编辑。
- **Web UI**：使用 Gradio 构建交互式演示界面。

## 相关链接

- [论文](https://arxiv.org/abs/2303.05499)
- [Hugging Face Demo](https://huggingface.co/spaces/ShilongLiu/Grounding_DINO_demo)
- [Colab Demo](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/zero-shot-object-detection-with-grounding-dino.ipynb)
- [GitHub 仓库](https://github.com/IDEA-Research/GroundingDINO)
