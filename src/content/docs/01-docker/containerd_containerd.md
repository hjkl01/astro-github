---
title: containerd
---

# containerd

## 项目简介

containerd 是一个行业标准的容器运行时，强调简单性、健壮性和可移植性。它作为 Linux 和 Windows 的守护进程运行，能够管理主机系统的完整容器生命周期：镜像传输和存储、容器执行和监督、低级存储和网络附件等。

containerd 是 CNCF 的毕业项目，旨在嵌入到更大的系统中，而不是直接由开发人员或最终用户使用。

## 主要功能

- **容器生命周期管理**：处理容器的创建、启动、停止和删除。
- **镜像管理**：支持 OCI 兼容镜像的拉取、推送和存储。
- **存储和网络**：提供低级存储和网络附件功能。
- **插件架构**：支持各种插件，如 CRI（Container Runtime Interface）插件，用于与 Kubernetes 集成。
- **跨平台支持**：支持 Linux 和 Windows。
- **安全性**：提供容器隔离和安全功能。

## 用法

### 安装

从 [releases 页面](https://github.com/containerd/containerd/releases) 下载最新版本的二进制文件。

### 基本命令

使用 `ctr` 命令行工具与 containerd 交互：

- 拉取镜像：`ctr images pull docker.io/library/alpine:latest`
- 运行容器：`ctr run --rm docker.io/library/alpine:latest hello sh -c "echo hello world"`
- 列出镜像：`ctr images list`

### 配置

containerd 的配置文件通常位于 `/etc/containerd/config.toml`。可以通过编辑此文件来配置各种选项，如存储驱动、网络插件等。

### 与 Kubernetes 集成

containerd 可以作为 Kubernetes 的容器运行时使用，通过 CRI 插件实现。配置 Kubernetes 使用 containerd 作为运行时，请参考 [官方文档](https://containerd.io/docs/getting-started/)。

### 更多信息

- 官方网站：[containerd.io](https://containerd.io)
- 文档：[containerd 文档](https://containerd.io/docs/)
- GitHub：[containerd/containerd](https://github.com/containerd/containerd)
