
---
title: ML-From-Scratch
---


# ML-From-Scratch (eriklindernoren)

## 项目地址
[https://github.com/eriklindernoren/ML-From-Scratch](https://github.com/eriklindernoren/ML-From-Scratch)

## 概述
该项目使用 `NumPy` 从零实现多种机器学习算法，深入演示了背后的数学原理和梯度下降、反向传播等核心步骤。全部代码均为书写教学用途，避免使用第三方机器学习库（如 `scikit-learn`、`tensorflow`、`pytorch` 等）。

## 主要功能
- **线性模型**：线性回归、逻辑回归（含 L1/L2 正则化）
- **支持向量机**：线性/高斯核 SVM，实现梯度下降求解
- **神经网络**：多层感知机（MLP）实现，支持 sigmoid、ReLU、tanh 激活函数，交叉熵、均方误差等损失
- **优化算法**：批量梯度下降、随机梯度下降（SGD）、动量（Momentum）等
- **梯度检查**：对自实现梯度进行数值梯度检查
- **可视化**：随实验自动绘制损失曲线、决策边界等图形
- **数据集**：使用公开数据集（Iris、MNIST、COCO 等）进行演示
- **工具**：学习率衰减、梯度裁剪、正则化、Early Stopping 等实用功能

## 目录结构
```
ML-From-Scratch/
├─ nn/        # 神经网络相关代码
├─ svm/       # SVM 实现
├─ lr/        # 线性、逻辑回归
├─ util/      # 工具和数据集加载
├─ notebooks/ # Jupyter Notebook 示例
├─ README.md
└─
```

## 安装与运行

```bash
# 克隆仓库
git clone https://github.com/eriklindernoren/ML-From-Scratch
cd ML-From-Scratch

# 创建虚拟环境（可选）
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 运行示例
python -m notebooks.linear_regression   # 线性回归
python -m notebooks.multi_layer_perceptron   # 多层感知机
```

> 你也可以直接在 `notebooks/` 目录打开 Jupyter Notebook 进行交互式学习。

## 用法示例

```python
import numpy as np
from lr.linear_regression import LinearRegression
from util.dataloader import load_data

X, y = load_data('iris')            # 数据集：Iris
model = LinearRegression(learning_rate=0.01, epochs=1000)
model.fit(X, y)
pred = model.predict(X)
print('Accuracy:', np.mean(pred == y))
```

## 贡献

若想在本仓库中贡献代码，遵循以下流程：

1. Fork 本仓库  
2. 新建功能分支 `git checkout -b feature/xxx`  
3. 提交代码并推送  
4. 创建 Pull Request，说明修改内容与预期

**请提前阅读** `CONTRIBUTING.md` **文件以了解贡献规范。**

--- 

此 Markdown 旨在快速了解项目主要特性、功能以及整体使用方式，供团队文档或个人学习参考。```

