---
title: MONAI
---


# MONAI（Medical Open Network for AI）

项目地址: [https://github.com/Project-MONAI/MONAI](https://github.com/Project-MONAI/MONAI)

## 主要特性
- **基于 PyTorch**：利用 PyTorch 的高性能张量运算，方便构建、训练和部署医学影像模型。
- **模块化架构**：提供丰富的可复用组件（如数据读取、预处理、网络层、损失函数、评估指标等），支持快速搭建端到端工作流。
- **专注医学影像**：内置针对 CT、MRI、超声等多模态医学影像的专用工具和标准格式支持（NIfTI、DICOM 等）。
- **跨平台部署**：支持 CPU、GPU，兼容 ONNX、TorchScript、ONNX Runtime 等推理框架，方便嵌入式和云端部署。
- **完善的模型仓库**：预训练模型库（如 UNet、ResNet、DenseNet 等）已针对医学影像进行微调，可直接下载使用。
- **社区活跃**：持续更新，拥有大量示例、教程和论文实现，活跃的 GitHub 讨论区和贡献指南。

## 主要功能
| 功能 | 说明 |
|------|------|
| **数据处理** | 支持多模态读取、标准化、增强、分割标注读取等。 |
| **网络模块** | 提供 2D/3D UNet、ResNet、DenseNet、Attention、Transformer 等骨干网络。 |
| **损失函数** | Dice、Cross-Entropy、Tversky、Focal 等医学常用损失。 |
| **评估指标** | Dice、IoU、Hausdorff Distance、Sensitivity、Specificity 等。 |
| **训练器** | `Engine` 与 `Trainer`，可自定义回调、学习率调度、日志记录。 |
| **推理** | 简单 API 支持单张/批量推理，输出后处理（阈值、连通域筛选）。 |
| **部署** | 通过 `torchscript`, `onnx`, `onnxruntime` 等实现离线推理。 |

## 用法示例
```python
import monai
from monai.transforms import (
    Compose, LoadImaged, AddChanneld, ScaleIntensityRanged, ToTensord
)
from monai.networks.nets import UNet
from monai.inferers import SlidingWindowInferer
from monai.metrics import DiceMetric
from monai.data import Dataset, DataLoader

# 1. 数据集
data = [
    {"image": "path/to/img1.nii.gz", "label": "path/to/label1.nii.gz"},
    {"image": "path/to/img2.nii.gz", "label": "path/to/label2.nii.gz"},
]
train_ds = Dataset(data=data, transform=Compose([
    LoadImaged(keys=["image", "label"]),
    AddChanneld(keys=["image", "label"]),
    ScaleIntensityRanged(keys=["image"], a_min=-1000, a_max=400, b_min=0.0, b_max=1.0, clip=True),
    ToTensord(keys=["image", "label"]),
]))
train_loader = DataLoader(train_ds, batch_size=2, shuffle=True)

# 2. 网络
model = UNet(
    dimensions=3,
    in_channels=1,
    out_channels=1,
    channels=(16, 32, 64, 128),
    strides=(2, 2, 2),
)

# 3. 损失 + 优化器
loss_function = monai.losses.DiceLoss(sigmoid=True)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)

# 4. 训练循环（简化示例）
for epoch in range(10):
    for batch_data in train_loader:
        inputs, labels = batch_data["image"], batch_data["label"]
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()

# 5. 推理
inferer = SlidingWindowInferer(
    roi_size=(128, 128, 128),
    sw_batch_size=4,
    overlap=0.25,
    mode="gaussian",
)
with torch.no_grad():
    predictions = inferer(inputs, model)

# 6. 评估
dice_metric = DiceMetric(include_background=False, reduction="mean")
dice_metric(y_pred=predictions, y=labels)
print("Dice:", dice_metric.aggregate().item())
```

> 上述代码仅为示例，实际项目中可根据数据、任务需求灵活调整传输、网络结构与训练策略。

---
**文档**: 详细使用说明请参阅官方文档：<https://docs.monai.io/en/latest/>  
**贡献**: 如需贡献代码，请阅读 `CONTRIBUTING.md`。