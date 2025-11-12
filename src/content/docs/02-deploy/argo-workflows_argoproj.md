---
title: repository
---

# Argo Workflows

Argo Workflows 是一个开源的容器原生工作流引擎，用于在 Kubernetes 上编排并行作业。它作为 Kubernetes CRD（自定义资源定义）实现。

## 项目概述

Argo Workflows 是 Cloud Native Computing Foundation (CNCF) 的毕业项目，是 Kubernetes 上最受欢迎的工作流执行引擎。

## 核心功能

### 工作流定义

- 将工作流的每个步骤定义为容器
- 将多步骤工作流建模为任务序列
- 使用有向无环图（DAG）捕获任务之间的依赖关系
- 轻松运行机器学习或数据处理的计算密集型作业

### 主要特性

- **可视化界面**：提供 UI 来可视化管理工作流
- **工件支持**：支持 S3、Artifactory、阿里云 OSS、Azure Blob 存储、HTTP、Git、GCS 等多种存储
- **工作流模板**：在集群中存储常用工作流模板
- **归档功能**：执行后归档工作流以供后续访问
- **定时调度**：使用 cron 安排定时工作流
- **REST API**：提供 HTTP 和 GRPC 服务器接口
- **多种声明方式**：支持 DAG 或 Steps 基础的工作流声明

### 高级功能

- 步骤级输入输出（工件/参数）
- 循环、参数化、条件语句
- 超时控制（步骤和工作流级别）
- 重试机制（步骤和工作流级别）
- 重新提交（记忆化）
- 暂停和恢复
- 取消功能
- K8s 资源编排
- 退出钩子（通知、清理）
- 垃圾回收
- 调度策略（亲和性/容忍度/节点选择器）
- 卷管理（临时/现有）
- 并行限制
- 守护进程步骤
- Docker-in-Docker 支持
- 脚本步骤
- 事件发射
- Prometheus 指标

## 使用场景

- **机器学习管道**：构建和编排 ML 训练、推理流程
- **数据和批处理**：大规模数据处理和 ETL 流程
- **基础设施自动化**：自动化部署和运维任务
- **CI/CD**：构建持续集成和持续部署流水线
- **其他场景**：各种需要工作流编排的场景

## 生态系统

Argo Workflows 拥有丰富的生态系统，包括：

- **Argo Events**：事件驱动的自动化
- **Couler**：用于工作流定义的 Python SDK
- **Hera**：Argo Workflows 的 Python SDK
- **Kubeflow Pipelines**：机器学习管道平台
- **Metaflow**：Netflix 的数据科学工作流框架

## 客户端库

提供多种语言的客户端库：

- Java 客户端
- Golang 客户端
- Python 客户端（包括 Hera Python SDK）

## 快速开始

1. **交互式培训材料**：https://killercoda.com/argoproj/course/argo-workflows/
2. **演示环境**：https://workflows.apps.argoproj.io/workflows/argo

## 社区和支持

- **文档**：https://argo-workflows.readthedocs.io/
- **Slack 社区**：https://argoproj.github.io/community/join-slack
- **月度社区会议**：定期举办社区会议讨论项目发展
- **GitHub**：https://github.com/argoproj/argo-workflows

## 技术特点

- **轻量级**：相比传统工作流引擎更加轻量
- **可扩展**：支持大规模工作流执行
- **易于使用**：提供直观的 YAML 定义和可视化界面
- **云原生**：专为容器环境设计，无传统 VM 和服务器环境的开销
- **云无关**：可在任何 Kubernetes 集群上运行

## 许可证

Apache-2.0 开源许可证

## 项目状态

- GitHub Stars：16.2k+
- Forks：3.4k+
- Contributors：900+
- CNCF 毕业项目
- 被 200+ 组织正式使用

Argo Workflows 是在 Kubernetes 环境中构建复杂工作流的理想选择，特别适合需要容器原生工作流编排的现代化应用场景。
