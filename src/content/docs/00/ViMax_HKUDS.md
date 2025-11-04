
---
title: ViMax
---

# ViMax (HKUDS)
**项目地址**: <https://github.com/HKUDS/ViMax>

## 项目简介
ViMax 是一种基于 Vision Transformer 的轻量化视觉模型，旨在在保持高性能的同时显著降低参数量和计算成本。它将卷积操作与自注意力机制相结合，适用于多任务视觉推理（分类、检测、分割等）。

## 主要特性
- **轻量高效**：通过局部卷积与全局自注意力的耦合，参数量大幅减少，推理速度提升。  
- **可扩展性**：支持分布式训练与模型扩展，适用于不同规模的数据集。  
- **多任务支持**：模型结构可直接用于分类、目标检测、语义分割等任务。  
- **预训练模型**：提供多种基准数据集（ImageNet、COCO 等）的预训练权重。  
- **易用性**：完整的 PyTorch 实现，包含训练脚本、推理脚本、评估工具等。

## 功能概览
| 功能 | 概述 |
|-----|-----|
| **训练** | `train.py` 支持多卡分布式训练，支持多种数据加载策略。 |
| **推理** | `inference.py` 可对单张或批量图像进行快速推理。 |
| **评估** | `evaluate.py` 包含分类、检测、分割等常用评估指标。 |
| **模型转换** | `export.py` 可将 PyTorch 模型导出为 ONNX、TensorRT 等格式。 |
| **数据预处理** | `datasets/` 目录下提供多种常用数据集的读取与增强方法。 |

## 用法示例

```bash
# 1. 克隆仓库
git clone https://github.com/HKUDS/ViMax.git
cd ViMax

# 2. 创建并激活虚拟环境
conda create -n vimax python=3.9
conda activate vimax
pip install -r requirements.txt

# 3. 下载预训练权重
wget https://github.com/HKUDS/ViMax/releases/download/v1.0/vimax_base.pth
# 或者自行在 checkpoints/ 目录放置权重

# 4. 训练（单卡）
python train.py --config configs/vimax_base.yaml

# 5. 多卡分布式训练
python -m torch.distributed.run --nproc_per_node=4 train.py --config configs/vimax_base.yaml

# 6. 推理
python inference.py --model_path checkpoints/vimax_base.pth --image_path data/test.jpg
```

> **提示**  
> - 配置文件 `configs/*.yaml` 可自行修改模型结构、学习率、batch size 等参数。  
> - `datasets/` 目录支持多种常用数据集，可自定数据加载方式。  
> - 如需推理多个图像，可在 `inference.py` 中配合 `--batch_size` 参数。

---

> 以上内容仅包含项目的核心信息与使用方法，供参考。