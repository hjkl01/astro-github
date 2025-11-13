---
title: pytorch
---

# PyTorch

## 项目简介

PyTorch 是一个开源的机器学习框架，由 Facebook 的 AI 研究团队开发。它提供了两个主要的高级功能：

- **Tensor 计算**：类似于 NumPy 的张量库，具有强大的 GPU 加速支持
- **动态神经网络**：基于 tape-based autograd 系统的深度神经网络构建工具

## 主要特性

### GPU 就绪的张量库

PyTorch 提供可以在 CPU 或 GPU 上运行的张量，并通过大量加速实现高速计算。支持切片、索引、数学运算、线性代数、归约等操作。

### 动态神经网络：Tape-Based Autograd

PyTorch 使用反向模式自动微分技术，允许任意改变网络行为而无延迟开销。与静态框架不同，PyTorch 提供了最大的灵活性和速度。

### Python 优先

PyTorch 深度集成到 Python 中，可以自然地使用 NumPy、SciPy 等库。可以在 Python 中编写新的神经网络层，使用 Cython 和 Numba 等工具。

### 命令式体验

PyTorch 设计直观、线性思维、易于使用。代码执行是同步的，调试和错误追踪简单直接。

### 快速且精简

PyTorch 具有最小的框架开销，集成了 Intel MKL、NVIDIA cuDNN、NCCL 等加速库。内存使用高效，支持训练更大的深度学习模型。

### 无痛扩展

编写新的神经网络模块或与 PyTorch 张量 API 接口非常简单。可以使用 torch API 或 NumPy-based 库编写层，也可以使用 C/C++ 扩展 API。

## 安装方法

### 二进制安装

通过 Conda 或 pip wheel 从官方网站安装：

```bash
# 访问 https://pytorch.org/get-started/locally/ 获取最新安装命令
```

### 从源码安装

```bash
git clone https://github.com/pytorch/pytorch
cd pytorch
git submodule sync
git submodule update --init --recursive

# 安装依赖
pip install --group dev

# 安装 PyTorch
python -m pip install --no-build-isolation -v -e .
```

### Docker 镜像

```bash
docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest
```

## 基本用法

### 张量操作

```python
import torch

# 创建张量
x = torch.tensor([1, 2, 3])
y = torch.randn(3, 3)

# 张量运算
z = x + y
result = torch.matmul(x, y)
```

### 自动微分

```python
# 启用梯度计算
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# 执行运算
y = x ** 2
z = y.sum()

# 计算梯度
z.backward()
print(x.grad)  # 输出梯度
```

### 神经网络

```python
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

model = SimpleNet()
```

## 学习资源

- [官方教程](https://pytorch.org/tutorials/)
- [示例代码](https://github.com/pytorch/examples)
- [API 文档](https://pytorch.org/docs/)
- [PyTorch 论坛](https://discuss.pytorch.org)

## 许可证

PyTorch 使用 BSD 风格许可证。
