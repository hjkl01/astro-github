
---
title: easy-dataset
---


# easy-dataset

**项目地址**: <https://github.com/ConardLi/easy-dataset>

## 项目简介
`easy-dataset` 是一个轻量级的 Python 库，用于简化数据集的构建、读取和处理流程。它提供了一套统一的接口，支持多种数据格式（如 CSV、JSON、Parquet、图片/视频文件等），并且可以与流行的数据处理框架（如 Pandas、NumPy、PyTorch、TensorFlow）无缝集成。

## 主要特性
- **统一 API**：一次性导入即可使用 `Dataset` 对象操作不同格式的数据。
- **自动化预处理**：支持自定义或内置的预处理管道（如归一化、标准化、图像增强等）。
- **并行加载**：利用多线程/多进程实现高效数据读取。
- **灵活的分区**：支持训练/验证/测试集的自动划分与存储。
- **可扩展**：通过插件机制轻松集成第三方数据源或自定义数据类型。

## 核心功能
| 功能 | 说明 |
|------|------|
| `Dataset.load()` | 按路径加载数据，自动识别文件类型 |
| `Dataset.split()` | 按比例或固定样本数划分子集 |
| `Dataset.apply()` | 对数据应用预处理函数或管道 |
| `Dataset.to_torch()` | 将数据转换为 PyTorch 的 `DataLoader` |
| `Dataset.to_tf()` | 将数据转换为 TensorFlow 的 `tf.data.Dataset` |
| `Dataset.save()` | 将处理后的数据以指定格式保存到磁盘 |

## 用法示例
```python
from easy_dataset import Dataset

# 1. 加载数据
ds = Dataset.load("data/train.csv")

# 2. 划分子集
train_ds, val_ds = ds.split(train_ratio=0.8)

# 3. 应用预处理（示例：归一化）
train_ds.apply(lambda x: (x - x.mean()) / x.std())
val_ds.apply(lambda x: (x - x.mean()) / x.std())

# 4. 转换为 PyTorch DataLoader
train_loader = train_ds.to_torch(batch_size=64, shuffle=True)
val_loader = val_ds.to_torch(batch_size=64, shuffle=False)

# 5. 训练循环（示例）
for epoch in range(num_epochs):
    for batch in train_loader:
        # 训练代码
        pass
```

> **提示**：更多高级用法请参阅官方文档与代码示例。

---

*本文件由项目作者提供，旨在快速了解 easy-dataset 的核心特性及使用方式。*
```
