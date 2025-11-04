
---
title: HAMi
---


# Project-HAMi

- **GitHub 地址**: https://github.com/Project-HAMi/HAMi

## 项目简介

HAMi（Hybrid AI Model Interface）是一套开源工具库，旨在统一不同深度学习框架（如 PyTorch、TensorFlow、ONNX 等）的模型加载、推理与部署流程。通过提供统一的 API，用户可以在不更改业务代码的前提下，轻松切换模型后端、硬件平台以及推理引擎，实现一次编写、处处运行的目标。

## 主要特性

| 特性 | 说明 |
|------|------|
| **多框架兼容** | 直接支持 PyTorch、TensorFlow、ONNX Runtime 等主流框架，统一模型接口。 |
| **跨平台推理** | 支持 CPU、GPU（NVIDIA CUDA）、NPU 等多种硬件，自动选配最优后端。 |
| **插件式扩展** | 通过插件机制可自由接入自定义后端、优化器、量化器等。 |
| **轻量级部署** | 仅需 `pip install hami` 或 `pip install git+https://github.com/Project-HAMi/HAMi.git`，无需额外编译。 |
| **高性能推理** | 内置多线程、批量推理与动态图优化，显著提升吞吐量。 |
| **易用 API** | 简洁的 `HamiModel` 类封装，支持 `load_model()`, `predict()`, `export()` 等常用操作。 |
| **完整文档与示例** | 详细的 README、API 说明以及多种示例脚本，快速上手。 |

## 主要功能

- **模型加载**  
  ```python
  from hami import HamiModel
  model = HamiModel.load_model(path='model.onnx')
  ```
- **推理**  
  ```python
  input_tensor = torch.randn(1, 3, 224, 224)
  output = model.predict(input_tensor)
  ```
- **模型导出**  
  ```python
  model.export(path='optimized_model.onnx')
  ```
- **后端切换**  
  ```python
  model.set_backend('cuda')   # 或 'cpu', 'npu'
  ```
- **量化与剪枝**  
  通过插件可对模型进行量化、剪枝，进一步提升速度与压缩模型体积。

## 安装与使用

```bash
# 直接安装
pip install hami

# 或者从源码安装
pip install git+https://github.com/Project-HAMi/HAMi.git
```

使用示例：

```python
from hami import HamiModel

# 1. 加载模型
model = HamiModel.load_model('path/to/model.onnx')

# 2. 选择后端
model.set_backend('cuda')          # 如有 CUDA 可用

# 3. 进行推理
import torch
input_data = torch.randn(1, 3, 224, 224)
result = model.predict(input_data)

print(result.shape)
```

## 参考文档

- 官方 README: https://github.com/Project-HAMi/HAMi/blob/main/README.md
- API 文档: https://github.com/Project-HAMi/HAMi/blob/main/docs/api.md
- 示例代码: https://github.com/Project-HAMi/HAMi/tree/main/examples

---

> **提示**：在实际项目中，建议先阅读 `docs/` 目录下的详细说明，了解各后端的配置要求与性能调优方法。
