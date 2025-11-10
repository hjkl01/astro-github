---
title: Trellis
---

# TRELLIS

## 项目简介

TRELLIS 是微软开发的一个大型 3D 资产生成模型。它能够根据文本或图像提示生成高质量的 3D 资产，支持多种输出格式，如辐射场 (Radiance Fields)、3D 高斯 (3D Gaussians) 和网格 (Meshes)。TRELLIS 的核心是统一的结构化潜在 (Structured LATent, SLAT) 表示，以及专为 SLAT 设计的校正流变换器 (Rectified Flow Transformers)。该模型在包含 50 万个多样化对象的 3D 资产数据集上进行了预训练，参数规模高达 20 亿。

## 主要功能

- **高质量生成**：生成多样化的 3D 资产，具有精细的形状和纹理细节。
- **多功能性**：支持文本或图像输入，可生成多种 3D 表示形式，满足不同下游需求。
- **灵活编辑**：允许对生成的 3D 资产进行编辑，如生成同一对象的变体或局部编辑。

## 安装和使用

### 安装

1. 克隆仓库：

   ```sh
   git clone --recurse-submodules https://github.com/microsoft/TRELLIS.git
   cd TRELLIS
   ```

2. 安装依赖：
   ```sh
   . ./setup.sh --new-env --basic --xformers --flash-attn --diffoctreerast --spconv --mipgaussian --kaolin --nvdiffrast
   ```

### 预训练模型

提供以下预训练模型：

- TRELLIS-image-large：图像到 3D 大型模型 (1.2B 参数)
- TRELLIS-text-base：文本到 3D 基础模型 (342M 参数)
- TRELLIS-text-large：文本到 3D 大型模型 (1.1B 参数)
- TRELLIS-text-xlarge：文本到 3D 超大型模型 (2.0B 参数)

### 基本用法

```python
import os
os.environ['SPCONV_ALGO'] = 'native'

from PIL import Image
from trellis.pipelines import TrellisImageTo3DPipeline

# 加载模型
pipeline = TrellisImageTo3DPipeline.from_pretrained("microsoft/TRELLIS-image-large")
pipeline.cuda()

# 加载图像
image = Image.open("path/to/image.png")

# 生成 3D 资产
outputs = pipeline.run(image, seed=1)

# 输出包括高斯、辐射场和网格
# 可以渲染视频或导出为 GLB/PLY 文件
```

### Web 演示

运行 Gradio 演示：

```sh
python app.py
```

## 许可证

TRELLIS 模型和大部分代码采用 MIT 许可证。某些子模块可能有不同许可证。
