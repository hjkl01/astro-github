
---
title: onnx
---

# ONNX

- **项目地址**：<https://github.com/onnx/onnx>

## 项目简介

ONNX（Open Neural Network Exchange）是一个开源的深度学习模型交换格式，旨在实现不同框架（如 PyTorch、TensorFlow、Caffe2 等）之间的模型互通。通过统一的 IR（Intermediate Representation）和一套标准算子集，ONNX 使模型能够在多种硬件和软件平台上无缝迁移与部署。

## 主要特性

| 序号 | 特性 | 说明 |
|------|------|------|
| 1 | **跨框架互通** | 支持将模型从多种主流框架导出为 ONNX 格式，或将 ONNX 模型导入回框架。 |
| 2 | **标准化算子集** | 定义了统一的算子（operator）集合，保证不同实现的一致性。 |
| 3 | **版本控制** | 采用语义化版本管理，保持向后兼容性；可通过 `opset_version` 指定算子集版本。 |
| 4 | **可扩展性** | 允许自定义算子，满足特殊需求。 |
| 5 | **生态丰富** | 伴随 ONNX Runtime、ONNX.js、ONNX-MLIR 等多种运行时与工具，覆盖从训练到推理的完整流程。 |
| 6 | **高效推理** | ONNX Runtime 支持多平台（CPU、GPU、NPU 等）加速，提供 API 与 CLI 交互。 |

## 主要功能

- **模型导出**：`torch.onnx.export`, `tf2onnx.convert`, `keras2onnx.convert_keras` 等工具将框架模型转换为 ONNX。
- **模型验证**：`onnx.checker.check_model` 用于校验模型完整性与算子合法性。
- **模型优化**：`onnxoptimizer`, `onnx-simplifier` 等工具对图做结构优化，减少冗余算子。
- **运行时推理**：ONNX Runtime 支持 C++, Python, C#, Java, Go 等多语言 API；可在多种硬件上部署。
- **编辑与分析**：`onnxruntime-tools`, `Netron` 等可视化工具帮助检查模型结构与参数。

## 快速使用示例

```bash
# 1. 安装 ONNX
pip install onnx

# 2. 从 PyTorch 导出为 ONNX
import torch
import torch.onnx
model = MyModel()
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, "model.onnx",
                  opset_version=17, input_names=["input"],
                  output_names=["output"])

# 3. 验证模型
import onnx
onnx_model = onnx.load("model.onnx")
onnx.checker.check_model(onnx_model)

# 4. 使用 ONNX Runtime 推理
import onnxruntime as ort
sess = ort.InferenceSession("model.onnx")
inputs = {"input": dummy_input.numpy()}
outputs = sess.run(None, inputs)
print(outputs[0])
```

## 进一步阅读

- 官方文档: <https://onnx.ai/>
- ONNX Runtime: <https://github.com/microsoft/onnxruntime>
- ONNX 生态: <https://onnx.ai/onnx/onnx-ecosystem.html>