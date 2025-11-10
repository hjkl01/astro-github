---
title: monarch
---


# Monarch（Meta-PyTorch）项目介绍

## 项目地址
<https://github.com/meta-pytorch/monarch>

## 主要特性
- **统一数据加载与预处理**  
  支持 `CSV`、`JSON Lines`、`TFRecord`、HDF5 等多种数据格式，提供灵活的数据管道（`DataLoader`、`Dataset`）以及内置的数据增强工具。

- **分布式训练与弹性扩容**  
  基于 PyTorch 分布式数据并行（DDP）实现，支持多机多卡、单机多卡以及梯度累积。可无缝切换 GPU ↔ 混合精度训练。

- **自动混合精度（AMP）**  
  集成 `torch.cuda.amp`，默认使用 `fp16`/`bf16` 训练，显著降低显存占用与提升吞吐量。

- **Checkpoint & 训练恢复**  
  提供便捷的 `CheckpointManager`，支持周期保存、最优模型保留、恢复训练以及从中间断点继续。

- **日志与可视化**  
  内置 TensorBoard、Weights & Biases、MLflow 对接，支持指标、梯度、模型结构等全方位可视化。

- **模型注册与部署**  
  通过 `ModelRegistry` 统一管理实验模型，可直接导出为 ONNX、TorchScript、TensorRT 等多种格式。

- **命令行工具**  
  `monarch` CLI 可完成数据准备、训练启动、评估与推理等一站式操作。支持自定义脚本组合与参数覆盖。

- **高可扩展性与易用性**  
  模块化设计，项目内所有核心类/函数均按功能拆分（数据、模型、训练、日志、配置），极易集成到现有项目。

## 功能说明 & 用法示例

### 1. 安装
```bash
# pip 安装（仅 PyPI 版）
pip install monarch-pytorch

# 源码安装（请先克隆仓库）
git clone https://github.com/meta-pytorch/monarch.git
cd monarch
pip install -e .
```

### 2. 目录结构示例
```text
monarch/
├── monarch/
│   ├── data/
│   ├── models/
│   ├── trainer/
│   ├── utils/
├── scripts/
│   ├── train.py
│   ├── eval.py
│   ├── build_dataset.py
├── config/
│   ├── base.yaml
│   ├── train.yaml
│   ├── eval.yaml
└── README.md
```

### 3. 快速训练
1. **准备数据**  
   ```bash
   python scripts/build_dataset.py --config config/data.yaml
   ```

2. **启动训练**  
   ```bash
   python scripts/train.py --config config/train.yaml
   ```

3. **可视化**  
   在训练过程中，在浏览器打开 `tensorboard --logdir=logs` 或 `wandb` 监控。

### 4. 自定义模型示例 (`monarch/models/my_model.py`)

```python
from monarch.models.base import BaseModel
import torch.nn as nn

class MyModel(BaseModel):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.encoder = nn.TransformerEncoderLayer(d_model=cfg.model.d_model,
                                                   nhead=cfg.model.nhead)
        self.fc = nn.Linear(cfg.model.d_model, cfg.model.num_classes)

    def forward(self, x):
        x = self.encoder(x)
        x = torch.mean(x, dim=1)
        return self.fc(x)
```

### 5. 通过 CLI 运行完整 pipeline
```bash
# 训练 + 评估 + 推理
monarch run --config config/full.yaml
```

## 贡献 & 开发

- **开发流程**  
  1. Fork → Clone → `git checkout -b feature/xxx`  
  2. 编码 + 单元测试 (`pytest`)  
  3. 提交 PR 并附上详细说明

- **编码规范**  
  - Python 3.10+  
  - 代码风格：Black + Flake8  
  - 每个模块加入 docstring & type hints

- **Issue 跟踪**  
  请使用官方 issue 模板，以便快速定位与复现。

## 许可
MIT License

> 关注我们:
> - 官方文档：<https://monarch.meta-pytorch.org>
> - 示例与教程：<https://github.com/meta-pytorch/monarch/tree/main/docs>
> - Slack / Discord：Meta AI 社区
