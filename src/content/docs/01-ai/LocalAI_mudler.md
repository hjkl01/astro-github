
---
title: LocalAI
---


# LocalAI（mudler/LocalAI）

- **项目地址**: https://github.com/mudler/LocalAI

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **离线推理** | 通过本地模型直接推理，无需调用外部 API，保证数据隐私与低延迟。 |
| **多模型支持** | 兼容多种开源 LLM（如 `llama.cpp`、`gpt4all`、`phi` 等）以及多种后端（VLLM、ONNX、TensorRT、OpenVINO、OpenBLAS 等）。 |
| **OpenAI API 兼容** | 提供标准的 OpenAI REST/WS 接口，直接替换第三方服务，代码最小改动即可迁移。 |
| **插件化架构** | 通过插件系统可轻松扩展功能（例如自定义 tokenizer、embedding 模型、提示工程等）。 |
| **轻量级部署** | 支持 Docker、二进制包、Kubernetes Helm Chart 等多种部署方式，资源占用低。 |
| **多语言支持** | 支持多种编程语言调用（Python、Go、Node.js 等），统一的 API 接口。 |
| **性能优化** | 支持 GPU 加速、FP16/INT8 推理、内存映射等技术，最大化利用硬件。 |
| **安全与可控** | 支持本地模型裁剪、prompt 限制、请求速率限制等安全机制。 |

---

## 功能概览

- **文本生成**  
  `POST /v1/chat/completions`、`POST /v1/completions`  
- **文本嵌入**  
  `POST /v1/embeddings`  
- **流式生成**  
  WebSocket 或 Server-Sent Events（SSE）支持  
- **模型管理**  
  动态加载/卸载模型，支持多模型并发运行  
- **监控与日志**  
  Prometheus 指标、HTTP 日志、可视化面板（Grafana）  
- **插件 API**  
  通过插件扩展自定义 tokenizer、后端或前置过滤器  

---

## 安装与部署

### 1. Docker

```bash
docker pull ghcr.io/mudler/localai:latest
docker run -d --name localai \
  -p 8080:8080 \
  -v /path/to/models:/models \
  ghcr.io/mudler/localai:latest
```

> **注意**：将 `/path/to/models` 替换为本地模型目录，模型文件需放在 `models` 子目录中。

### 2. 二进制包

```bash
# 下载安装脚本
curl -L https://github.com/mudler/LocalAI/releases/latest/download/localai-linux-amd64 -o localai
chmod +x localai
# 运行
./localai --models /path/to/models
```

### 3. Helm Chart（Kubernetes）

```bash
helm repo add mudler https://mudler.github.io/helm-charts
helm repo update
helm install localai mudler/localai \
  --set persistence.enabled=true \
  --set persistence.storageClass=local-storage \
  --set persistence.size=10Gi
```

---

## 配置

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `PORT` | HTTP 端口 | `8080` |
| `MODEL_DIR` | 模型存放目录 | `./models` |
| `BACKEND` | 后端引擎（vllm, llama, onnx, trt, openvino） | `llama` |
| `MAX_TOKENS` | 单次生成最大 token 数 | `2048` |
| `DEVICE` | 设备（cpu, cuda, auto） | `auto` |
| `LOG_LEVEL` | 日志级别（debug, info, warn, error） | `info` |

> 通过环境变量或 `config.yaml` 文件进行配置。

---

## 用法示例

### 1. 文本生成（REST）

```bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3",
    "messages": [{"role":"user","content":"写一段关于 AI 的短文"}],
    "max_tokens": 100
  }'
```

### 2. 文本生成（流式）

```bash
curl -N -X POST http://localhost:8080/v1/chat/completions \
  -H "Accept: text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3",
    "messages": [{"role":"user","content":"帮我写一段关于 AI 的短文"}],
    "stream": true
  }'
```

### 3. 嵌入向量

```bash
curl -X POST http://localhost:8080/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sentence-embeddings",
    "input": ["机器学习", "深度学习"]
  }'
```

### 4. 使用 Python SDK

```python
import requests

api_url = "http://localhost:8080/v1/chat/completions"
payload = {
    "model": "llama3",
    "messages": [{"role":"user","content":"写一段关于 AI 的短文"}],
    "max_tokens": 100
}
resp = requests.post(api_url, json=payload)
print(resp.json()["choices"][0]["message"]["content"])
```

---

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| 模型加载失败 | 确认模型文件完整，路径与 `MODEL_DIR` 一致。 |
| GPU 未被识别 | 确认 `DEVICE=cuda`，并安装对应的 CUDA 驱动与 `nvidia-container-runtime`。 |
| 超时 | 调整 `MAX_TOKENS` 或开启多模型并行，减少单模型的推理负载。 |
| 日志混乱 | 设置 `LOG_LEVEL=debug` 查看详细错误信息。 |

---

## 贡献

- Fork 本仓库
- 创建 Feature/Issue
- 提交 PR
- 参考 `CONTRIBUTING.md`

---

## 许可证

MIT © 2024 mudler

---