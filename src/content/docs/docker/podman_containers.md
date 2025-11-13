---
title: podman_containers
---

# Podman

Podman 是一个用于管理 OCI 容器和 pods 的工具，由 containers 组织开发。它基于 libpod 库，提供完整的容器生命周期管理功能，无需守护进程即可运行。

## 主要功能

- **容器管理**：支持创建、运行、停止、删除容器，支持多种容器镜像格式（OCI 和 Docker）。
- **镜像管理**：拉取、构建、推送镜像，支持从各种来源获取镜像。
- **Pods 支持**：管理容器组，这些容器共享资源并作为一个单元管理。
- **无根运行**：支持以普通用户身份运行容器，无需 root 权限，提供更好的安全性。
- **网络管理**：使用 Netavark 处理容器网络。
- **兼容性**：提供 Docker 兼容的 CLI 接口，支持在 Linux、Windows 和 Mac 上运行（在非 Linux 系统上通过虚拟机）。
- **REST API**：提供 REST API，支持 Docker 兼容接口和高级 Podman 功能。
- **检查点和恢复**：通过 CRIU 支持容器的检查点和恢复。

## 用法示例

### 运行容器

```bash
podman run quay.io/podman/hello
```

### 构建镜像

```bash
podman build -t myimage .
```

### 管理 pods

```bash
podman pod create mypod
podman run --pod mypod nginx
```

Podman 的命令与 Docker 类似，但设计上更注重安全性，无守护进程运行，适合在生产环境中使用。更多详细信息请参考 [官方文档](https://podman.io)。
