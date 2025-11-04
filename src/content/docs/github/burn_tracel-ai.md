
---
title: burn
---


# Burn（Tracel‑AI）

项目地址: https://github.com/tracel-ai/burn

## 主要特性
- **简洁的训练接口**：提供统一的 `Trainer` 与 `Engine`，让模型训练、验证、测试流程一行代码即可完成。
- **多卡与分布式支持**：原生兼容 PyTorch 的 `DataParallel` 与 `DistributedDataParallel`，可在多 GPU 或多节点环境下无缝运行。
- **自动模型与日志管理**：支持自动保存最佳模型、周期性 checkpoint，集成 TensorBoard、Weights & Biases 等日志后端。
- **可插拔的组件化设计**：训练、评估、学习率调度器、优化器等均可通过插件方式自定义或替换。
- **轻量级依赖**：核心仅依赖 PyTorch、NumPy，避免不必要的第三方库，易于部署与维护。

## 核心模块
| 模块 | 作用 |
|------|------|
| `burn.trainer` | 定义 `Trainer` 类，包装训练循环、验证、测试等流程 |
| `burn.engine` | 提供 `Engine` 对象，管理数据加载、模型前向、反向传播、梯度更新 |
| `burn.callbacks` | 一组可复用的回调，例如 `EarlyStopping`、`LearningRateScheduler`、`ModelCheckpoint` |
| `burn.utils` | 工具函数，支持随机种子设置、设备切换、参数统计等 |
| `burn.cli` | 命令行工具，快速启动训练任务或查看日志 |

## 快速使用

```bash
# 安装
pip install git+https://github.com/tracel-ai/burn.git

# 示例训练脚本
python train.py \
  --model resnet50 \
  --dataset cifar10 \
  --epochs 50 \
  --batch-size 128 \
  --lr 0.01 \
  --device cuda:0
```

```python
# train.py
import torch
from burn.trainer import Trainer
from burn.utils import get_device

device = get_device()
model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet50', pretrained=False).to(device)
train_loader, val_loader = ...  # 数据加载
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
criterion = torch.nn.CrossEntropyLoss()

trainer = Trainer(
    model=model,
    optimizer=optimizer,
    criterion=criterion,
    train_loader=train_loader,
    val_loader=val_loader,
    callbacks=[
        burn.callbacks.ModelCheckpoint(save_best=True, filepath='best.pth'),
        burn.callbacks.EarlyStopping(patience=5)
    ]
)

trainer.fit(epochs=50)
```

## 文档与示例
- 完整 API 参考见 [docs](https://github.com/tracel-ai/burn/tree/main/docs)
- 示例代码在 `examples/` 目录，涵盖图像分类、语言模型、强化学习等多种任务。

## 贡献
欢迎 Issue 与 PR，详细贡献指南请查看 `CONTRIBUTING.md`。
