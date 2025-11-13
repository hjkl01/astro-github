---
title: pytorch-image-models
---

# PyTorch Image Models (timm)

## 功能

PyTorch Image Models (timm) 是 PyTorch 图像模型、层、实用工具、优化器、调度器、数据加载器/增强和参考训练/验证脚本的集合。它旨在收集各种 SOTA 模型，并能够重现 ImageNet 训练结果。

主要功能包括：

- **模型**：支持多种图像编码器/骨干网络，如 ResNet, ResNeXT, EfficientNet, NFNet, Vision Transformer (ViT), MobileNetV4, MobileNet-V3 & V2, RegNet, DPN, CSPNet, Swin Transformer, MaxViT, CoAtNet, ConvNeXt 等。

- **优化器**：提供多种优化器，如 AdaBelief, AdaFactor, AdaHessian, AdamP, Adan, Lamb, Lion, Lookahead, MADGRAD, NovoGrad, RAdam 等。

- **增强**：支持随机擦除、Mixup、CutMix、AutoAugment、RandAugment、AugMix 等数据增强技术。

- **正则化**：包括 DropPath、DropBlock、Blur Pooling 等。

- **其他特性**：统一的模型配置接口、多尺度特征提取、预训练权重加载、参考训练脚本等。

## 用法

### 安装

```bash
pip install timm
```

### 使用模型

```python
import timm

# 创建模型
model = timm.create_model('resnet50', pretrained=True)

# 推理
import torch
x = torch.randn(1, 3, 224, 224)
output = model(x)
print(output.shape)  # torch.Size([1, 1000])
```

### 训练和验证

参考仓库中的 train.py 和 validate.py 脚本。

更多详细信息，请参阅官方文档：[https://huggingface.co/docs/timm](https://huggingface.co/docs/timm)
