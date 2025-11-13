---
title: AIBrix
---

# AIBrix

AIBrix 是一个开源项目，旨在提供构建可扩展 GenAI 推理基础设施的基本构建块。它提供了一个云原生解决方案，专为部署、管理和扩展大型语言模型 (LLM) 推理而优化，特别针对企业需求。

## 主要功能

- **高密度 LoRA 管理**：简化对模型的轻量级、低秩适配的支持。
- **LLM 网关和路由**：高效管理并引导多个模型和副本之间的流量。
- **LLM 应用定制自动缩放器**：根据实时需求动态缩放推理资源。
- **统一 AI 运行时**：一个多功能 sidecar，支持指标标准化、模型下载和管理。
- **分布式推理**：可扩展架构，用于处理跨多个节点的巨大工作负载。
- **分布式 KV 缓存**：启用高容量、跨引擎 KV 重用。
- **成本高效的异构服务**：启用混合 GPU 推理以降低成本，同时保证 SLO。
- **GPU 硬件故障检测**：主动检测 GPU 硬件问题。

## 用法

### 快速开始

要开始使用 AIBrix，请克隆此仓库并按照文档中的设置说明进行操作。我们的综合指南将帮助您无缝配置和部署您的第一个 LLM 基础设施。

#### 本地测试

```bash
git clone https://github.com/vllm-project/aibrix.git
cd aibrix

# 安装夜间版 AIBrix 依赖
kubectl apply -k config/dependency --server-side

# 安装夜间版 AIBrix 组件
kubectl apply -k config/default
```

#### 安装稳定分发

```bash
# 安装组件依赖
kubectl apply -f "https://github.com/vllm-project/aibrix/releases/download/v0.4.0/aibrix-dependency-v0.4.0.yaml" --server-side

# 安装 AIBrix 组件
kubectl apply -f "https://github.com/vllm-project/aibrix/releases/download/v0.4.0/aibrix-core-v0.4.0.yaml"
```

有关安装、配置和用法的详细文档，请访问 [官方文档](https://aibrix.readthedocs.io/latest/)。
