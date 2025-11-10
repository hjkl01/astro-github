---
title: actions-runner-controller
---

# Actions Runner Controller (ARC)

## 功能

Actions Runner Controller (ARC) 是一个 Kubernetes operator，用于编排和扩展 GitHub Actions 的自托管运行器。

- 自动扩展基于仓库、组织或企业中的工作流数量的运行器规模集。
- 支持容器化的临时运行器，可以快速扩展和清理。
- 与 GitHub Actions 集成，提供自托管运行器的管理。

## 用法

1. 使用 Helm 在 Kubernetes 上安装 ARC。
2. 创建运行器规模集。
3. 在工作流中使用这些运行器。

参考 [Quickstart guide](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/quickstart-for-actions-runner-controller) 开始使用。
