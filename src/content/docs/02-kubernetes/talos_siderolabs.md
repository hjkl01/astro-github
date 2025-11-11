---
title: Talos
---

# Talos

Talos Linux 是一个现代化的 Linux 发行版，专为运行 Kubernetes 而设计。它是安全、不可变且最小化的操作系统，由 Sidero Labs 支持，完全开源且生产就绪。

## 主要功能

- **安全性**：Talos 减少攻击面：它是最小化、硬化且不可变的。所有 API 访问都通过相互 TLS (mTLS) 认证进行保护。
- **可预测性**：Talos 消除配置漂移，通过采用不可变基础设施理念减少未知因素，并提供原子更新。
- **可演化性**：Talos 简化架构，提高敏捷性，并始终提供最新的稳定 Kubernetes 和 Linux 版本。

## 用法

Talos 的所有系统管理都通过 API 进行，没有 shell 或交互式控制台。部署和管理 Talos 的详细说明请参考 [官方文档](https://docs.siderolabs.com/talos)。

### 快速开始

1. 下载 Talos 镜像。
2. 使用 Talos CLI 工具配置和部署集群。
3. 通过 API 管理 Kubernetes 节点。

### 社区和支持

- 支持：问题、bug、功能请求请使用 [GitHub Discussions](https://github.com/siderolabs/talos/discussions)。
- Slack：加入 [Slack 频道](https://slack.dev.talos-systems.io)。
- 论坛：[社区论坛](https://groups.google.com/a/SideroLabs.com/forum/#!forum/community)。

## 许可证

Talos 使用 MPL-2.0 许可证。
