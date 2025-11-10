---
title: Coze Loop
---

# Coze Loop

## 项目介绍

Coze Loop 是一个面向开发者的、平台级解决方案，专注于 AI Agent 的开发和运营。它解决了 AI Agent 开发过程中面临的各种挑战，提供从开发、调试、评估到监控的全生命周期管理能力。

基于商业版本，Coze Loop 推出开源版本，为开发者免费提供核心基础功能模块。通过开源模式分享核心技术框架，开发者可以根据业务需求进行定制和扩展，促进社区共建、分享和交流，帮助开发者零门槛参与 AI Agent 探索和实践。

## 主要功能

Coze Loop 通过提供全生命周期管理能力，帮助开发者更高效地开发和运营 AI Agent。无论是 Prompt 工程、AI Agent 评估，还是部署后的监控和优化，Coze Loop 都提供强大的工具和智能支持，大大简化 AI Agent 的开发流程，提升其运营性能和稳定性。

- **Prompt 开发**：Coze Loop 的 Prompt 开发模块为开发者提供编写、调试、优化、版本管理的端到端支持。通过可视化 Playground，支持实时交互测试 Prompt，让开发者直观比较不同 LLM 的输出。
- **评估**：Coze Loop 的评估模块为开发者提供系统性评估能力，支持自动化多维度测试 Prompt 和 Coze Agent 的输出，如准确性、简洁性、合规性等。
- **可观测性**：Coze Loop 为开发者提供整个执行过程的可观测性，完整记录从用户输入到 AI 输出的每个阶段，包括 Prompt 解析、模型调用、工具执行等关键阶段，并自动捕获中间结果和异常。

## 功能列表

| 功能        | 功能点                                   |
| ----------- | ---------------------------------------- |
| Prompt 调试 | Playground 调试和比较<br>Prompt 版本管理 |
| 评估        | 管理评估集<br>管理评估器<br>管理实验     |
| 观测        | SDK Trace 上报<br>Trace 数据观测         |
| 模型        | 支持集成 OpenAI、火山引擎 Ark 等模型     |

## 用法

### 部署方式 1：Docker 部署 (Docker Compose)

1. 克隆源码：

   ```bash
   git clone https://github.com/coze-dev/coze-loop.git
   cd coze-loop
   ```

2. 配置模型：编辑 `release/deployment/docker-compose/conf/model_config.yaml`，修改 api_key 和 model 字段（以火山引擎 Ark 为例）。

3. 启动服务：

   ```bash
   make compose-up
   ```

4. 通过浏览器访问 `http://localhost:8082`。

### 部署方式 2：Kubernetes 部署 (Helm Chart)

1. 获取 Helm Chart 包：

   ```bash
   helm pull oci://docker.io/cozedev/coze-loop --version 1.0.0-helm
   tar -zxvf coze-loop-1.0.0-helm.tgz && cd coze-loop
   ```

2. 配置模型：编辑 `release/deployment/helm-chart/umbrella/conf/model_config.yaml`。

3. 配置 Ingress 规则：根据集群情况修改 `templates/ingress.yaml`。

4. 部署启动服务：

   ```bash
   make helm-up
   make helm-pod
   make helm-logf-app
   make helm-logf-nginx
   ```

5. 通过浏览器访问（根据集群域名和 URL）。

更多详情请参考 [Quick Start](https://github.com/coze-dev/coze-loop/wiki/2.-Quickstart)。
