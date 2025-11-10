---
title: Server
---

# Triton Inference Server

## 项目简介

Triton Inference Server 是一个开源推理服务软件，用于简化 AI 推理。它允许团队从多个深度学习和机器学习框架部署任何 AI 模型，包括 TensorRT、PyTorch、ONNX、OpenVINO、Python、RAPIDS FIL 等。Triton Inference Server 支持在云、数据中心、边缘和嵌入式设备上进行推理，适用于 NVIDIA GPUs、x86 和 ARM CPU，或 AWS Inferentia。它为多种查询类型提供优化性能，包括实时、批处理、集成和音频/视频流。

## 主要功能

- **多框架支持**：支持多种深度学习和机器学习框架的后端。
- **并发模型执行**：允许多个模型同时执行。
- **动态批处理**：自动将多个请求批处理以提高效率。
- **序列批处理和隐式状态管理**：适用于有状态模型。
- **后端 API**：允许添加自定义后端和预/后处理操作。
- **Python 后端**：支持用 Python 编写自定义后端。
- **模型管道**：使用集成或业务逻辑脚本 (BLS) 创建模型管道。
- **推理协议**：支持 HTTP/REST 和 GRPC 协议，基于 KServe 协议。
- **API 绑定**：提供 C API 和 Java API，用于边缘和其他进程内用例。
- **指标**：提供 GPU 利用率、服务器吞吐量、服务器延迟等指标。

## 用法

### 快速开始：3 步服务模型

1. **创建示例模型仓库**：

   ```bash
   git clone -b r25.10 https://github.com/triton-inference-server/server.git
   cd server/docs/examples
   ./fetch_models.sh
   ```

2. **从 NGC Triton 容器启动 Triton**：

   ```bash
   docker run --gpus=1 --rm --net=host -v ${PWD}/model_repository:/models nvcr.io/nvidia/tritonserver:25.10-py3 tritonserver --model-repository=/models --model-control-mode explicit --load-model densenet_onnx
   ```

3. **发送推理请求**：
   在另一个控制台中，从 NGC Triton SDK 容器启动 image_client 示例：
   ```bash
   docker run -it --rm --net=host nvcr.io/nvidia/tritonserver:25.10-py3-sdk /workspace/install/bin/image_client -m densenet_onnx -c 3 -s INCEPTION /workspace/images/mug.jpg
   ```
   推理应返回类似结果：
   ```
   Image '/workspace/images/mug.jpg':
       15.346230 (504) = COFFEE MUG
       13.224326 (968) = CUP
       10.422965 (505) = COFFEEPOT
   ```

### 准备模型

- 将模型放入[模型仓库](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_repository.md)。
- 根据模型类型和所需功能，可能需要创建[模型配置](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_configuration.md)。
- 添加自定义操作、启用模型管道、优化调度和批处理参数、使用 Model Analyzer 工具进行配置优化。

### 配置和使用 Triton

- 阅读[快速开始指南](https://github.com/triton-inference-server/server/blob/main/docs/getting_started/quickstart.md)，在 GPU 和 CPU 上运行 Triton。
- 支持多种执行引擎（后端），如 TensorRT、PyTorch、ONNX 等。
- 使用 Performance Analyzer 和 Model Analyzer 优化性能。
- 管理模型加载和卸载。
- 使用 HTTP/REST 或 gRPC 协议直接发送请求。

### 客户端支持

- 使用 [Python 和 C++ 客户端库](https://github.com/triton-inference-server/client) 发送推理请求。
- 查看客户端示例：[C++](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/examples)、[Python](https://github.com/triton-inference-server/client/blob/main/src/python/examples)、[Java](https://github.com/triton-inference-server/client/blob/main/src/java/src/main/java/triton/client/examples)。
- 配置 HTTP 和 gRPC 客户端选项。

### 扩展 Triton

- 自定义 Triton 容器。
- 创建自定义后端（C/C++ 或 Python）。
- 创建解耦后端和模型。
- 使用仓库代理添加功能，如认证、解密或转换。
- 在 Jetson 和 JetPack 上部署 Triton。
- 在 AWS Inferentia 上使用 Triton。

## 更多信息

- [文档](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)
- [教程](https://github.com/triton-inference-server/tutorials)
- [NVIDIA Developer Zone](https://developer.nvidia.com/nvidia-triton-inference-server)
