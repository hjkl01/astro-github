
---
title: wandb
---


# WandB（Weights & Biases）

- **项目地址**: <https://github.com/wandb/wandb>

## 主要特性

- **实验记录**  
  自动记录训练日志、模型权重、超参数和评估指标，支持多种框架（PyTorch, TensorFlow, JAX, Keras 等）。

- **可视化仪表盘**  
  实时可视化训练过程（损失曲线、准确率、学习率等），可在浏览器中交互式查看。

- **版本控制**  
  对实验结果、模型文件和配置进行版本化，支持回滚和比较不同实验。

- **协作工具**  
  多人团队可共享实验结果、对比实验，支持权限管理与评论。

- **自定义合成**  
  支持自定义图表、日志格式和多任务实验管理。

- **大规模部署**  
  与云服务（AWS, GCP, Azure）集成，支持分布式训练与自动化实验追踪。

## 核心功能

| 功能 | 说明 |
|------|------|
| `wandb.init` | 启动实验，记录超参数、代码版本等 |
| `wandb.log` | 记录单步训练信息（损失、指标等） |
| `wandb.watch` | 自动记录模型梯度与结构 |
| `wandb.save` | 保存模型文件、检查点 |
| `wandb.sweep` | 自动化超参数搜索 |
| `wandb.agent` | 运行 sweep 任务 |
| `wandb.run` | 访问当前实验对象，进行高级操作 |

## 用法示例

```python
import wandb
from wandb.keras import WandbCallback
import tensorflow as tf

# 初始化实验
wandb.init(project="my-ml-project", config={"epochs": 10, "batch_size": 32})

# 训练模型
model = tf.keras.models.Sequential([...])
model.compile(optimizer='adam', loss='categorical_crossentropy')
model.fit(train_ds, epochs=wandb.config.epochs, callbacks=[WandbCallback()])

# 手动记录指标
wandb.log({"val_accuracy": val_acc})
```

> **提示**  
> - 若使用 PyTorch，可直接调用 `wandb.log` 或 `wandb.watch`。  
> - 通过 `wandb.sweep` 可设置网格搜索或贝叶斯优化。  
> - 在实验结束后，模型与日志会自动上传到 WandB 服务器，随后可在 Web 仪表盘中查看。

---

> **更多信息**  
> 详细文档请参阅官方仓库中的 `README.md` 与 `docs` 目录。  
> ```bash
> git clone https://github.com/wandb/wandb
> cd wandb
> pip install -e .
> 