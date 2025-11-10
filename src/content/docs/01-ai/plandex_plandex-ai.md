---
title: plandex
---


# Plandex AI

**项目地址**: <https://github.com/plandex-ai/plandex>

## 项目概述

Plandex 是一个专为 AI 与机器学习项目设计的全栈框架，帮助开发者快速构建、调试、部署与监控 AI 工作流。它采用模块化设计，支持模型训练、数据处理、推理推送、实验跟踪和可视化等功能，兼容主流深度学习框架（PyTorch、TensorFlow、JAX 等）。

## 核心特性

| 特性 | 说明 |
|------|------|
| **工作流定义** | 通过直观的 YAML/JSON 或 Python DSL 定义数据流、模型训练与推理流程。 |
| **任务调度** | 内置多线程/多进程调度器，可在单机或分布式环境下高效执行任务。 |
| **模型管理** | 自动版本化、容器化与部署，支持 TorchScript、ONNX、TensorFlow Serving 等多种推理后端。 |
| **实验跟踪** | 集成实验日志、超参数记录、指标可视化，支持与 MLflow、Weights & Biases 等平台互通。 |
| **数据管道** | 支持批处理与流式数据源，内置数据预处理、增强与缓存机制。 |
| **可视化与监控** | 提供 Web UI，实时监控任务状态、指标曲线与异常报警。 |
| **插件生态** | 通过插件系统可扩展自定义算子、数据源、模型后端等。 |
| **安全与权限** | 细粒度访问控制、审计日志，支持多租户部署。 |

## 快速开始

### 1. 安装

```bash
pip install plandex
```

> **Tip**：如果需要 GPU 支持，请在安装时指定对应的深度学习框架，例如 `pip install plandex[torch]`.

### 2. 创建一个简单的工作流

```python
from plandex import Pipeline, Task

# 定义任务
def load_data():
    # 读取数据
    return ...

def preprocess(data):
    # 数据预处理
    return ...

def train_model(preprocessed):
    # 训练模型
    return ...

def evaluate(model, test_data):
    # 评估
    return ...

# 构建流水线
pipeline = Pipeline(
    Task(name="load_data", func=load_data),
    Task(name="preprocess", func=preprocess, inputs=["load_data"]),
    Task(name="train_model", func=train_model, inputs=["preprocess"]),
    Task(name="evaluate", func=evaluate, inputs=["train_model"])
)

# 运行
pipeline.run()
```

### 3. 配置与调度

- **YAML 配置**（`pipeline.yaml`）

```yaml
tasks:
  - name: load_data
    func: plandex_demo.load_data
  - name: preprocess
    func: plandex_demo.preprocess
    inputs: [load_data]
  - name: train_model
    func: plandex_demo.train_model
    inputs: [preprocess]
  - name: evaluate
    func: plandex_demo.evaluate
    inputs: [train_model]
```

- **执行**

```bash
plandex run pipeline.yaml
```

### 4. 监控与可视化

启动 Web UI：

```bash
plandex ui
```

访问 `http://localhost:8000`，即可查看任务进度、指标曲线以及日志。

## 文档与社区

- **官方文档**：<https://plandex.ai/docs>
- **GitHub Issues**：<https://github.com/plandex-ai/plandex/issues>
- **Discord 社区**：<https://discord.gg/plandex>

## 贡献

欢迎提交 PR、Issue 与插件！请先阅读 `CONTRIBUTING.md`。

---
> 以上内容基于最新项目版本（2025‑10），如有更新请以官方仓库为准。