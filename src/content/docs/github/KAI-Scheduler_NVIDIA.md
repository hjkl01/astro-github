---
title: KAI-Scheduler
---

# KAI-Scheduler

KAI-Scheduler 是 NVIDIA 开发的一个 Kubernetes 调度器插件，专为优化 AI 和机器学习工作负载而设计。它通过智能调度算法，提高 GPU 资源的利用率，并支持优先级调度、资源预留等功能。

## 主要功能

- **智能调度**：根据工作负载的 GPU 需求和集群资源状态，自动选择最佳节点。
- **优先级支持**：允许为不同工作负载设置优先级，确保关键任务优先执行。
- **资源预留**：支持为特定用户或团队预留 GPU 资源。
- **多租户支持**：在共享集群中提供公平的资源分配。

## 用法

1. **安装**：将 KAI-Scheduler 部署到 Kubernetes 集群中，作为调度器插件运行。
2. **配置**：在 Pod 规范中指定调度器为 `kai-scheduler`，并设置相关注解来定义调度策略。
3. **监控**：使用 Kubernetes 工具监控调度决策和资源使用情况。

更多详细信息请参考 [GitHub 仓库](https://github.com/NVIDIA/KAI-Scheduler)。
