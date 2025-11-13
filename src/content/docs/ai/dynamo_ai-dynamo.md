---
title: Dynamo
---

# Dynamo (ai-dynamo)

## 项目简介

NVIDIA Dynamo 是一个高吞吐量、低延迟的推理框架，专为在多节点分布式环境中服务生成式AI和推理模型而设计。它支持多GPU、多节点架构，能够协调多个GPU和服务器，实现高效的推理服务。

## 主要功能

- **推理引擎无关**：支持 TRT-LLM、vLLM、SGLang 等多种推理引擎
- **Disaggregated Prefill & Decode Inference**：分离预填充和解码阶段，最大化GPU吞吐量，支持吞吐量和延迟的权衡
- **动态GPU调度**：根据需求波动优化性能
- **LLM-aware请求路由**：避免不必要的KV缓存重新计算
- **加速数据传输**：使用NIXL减少推理响应时间
- **KV缓存卸载**：利用多个内存层次提高系统吞吐量

## 支持矩阵

| 功能                       | vLLM | SGLang | TensorRT-LLM |
| -------------------------- | ---- | ------ | ------------ |
| Disaggregated Serving      | ✅   | ✅     | ✅           |
| Conditional Disaggregation | 🚧   | 🚧     | 🚧           |
| KV-Aware Routing           | ✅   | ✅     | ✅           |
| Load Based Planner         | 🚧   | 🚧     | 🚧           |
| SLA-Based Planner          | ✅   | ✅     | ✅           |
| KVBM                       | ✅   | 🚧     | ✅           |

## 安装和使用

### 1. 初始设置

推荐使用 Ubuntu 24.04 和 x86_64 CPU。

安装 uv Python 包管理器：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

安装 Python 开发头文件：

```bash
sudo apt install python3-dev
```

安装 etcd 和 NATS：

```bash
# 使用 Docker Compose 快速设置
docker compose -f deploy/docker-compose.yml up -d
```

### 2. 选择引擎

创建虚拟环境并安装对应引擎：

```bash
uv venv venv
source venv/bin/activate
uv pip install pip

# 选择一个引擎
uv pip install "ai-dynamo[sglang]"  # 或 [vllm], [trtllm]
```

### 3. 运行 Dynamo

启动 OpenAI 兼容的 HTTP 服务器：

```bash
python -m dynamo.frontend --http-port 8000
```

启动推理引擎（以 SGLang 为例）：

```bash
python -m dynamo.sglang --model deepseek-ai/DeepSeek-R1-Distill-Llama-8B
```

### 发送请求

```bash
curl localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
    "messages": [{"role": "user", "content": "Hello, how are you?"}],
    "stream": false,
    "max_tokens": 300
  }'
```

## 引擎支持

### vLLM

```bash
uv pip install ai-dynamo[vllm]
python -m dynamo.vllm --help
```

### SGLang

```bash
apt install -y libnuma-dev
uv pip install ai-dynamo[sglang]
python -m dynamo.sglang --help
```

### TensorRT-LLM

推荐使用 NGC PyTorch Container，安装依赖后：

```bash
uv pip install ai-dynamo[trtllm]
python -m dynamo.trtllm --help
```

## 部署和基准测试

- Kubernetes 部署：参考 Quickstart Guide
- 基准测试：使用 AIPerf 比较不同部署拓扑的性能
- SLA 驱动部署：优化部署以满足 SLA 要求

更多详细信息请参考官方文档：https://docs.nvidia.com/dynamo/latest/
