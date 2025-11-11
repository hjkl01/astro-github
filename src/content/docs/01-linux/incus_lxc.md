---
title: Incus
---

# Incus

Incus 是一个现代、安全且强大的系统容器和虚拟机管理器。它提供了一个统一的体验，用于在容器或虚拟机中运行和管理完整的 Linux 系统。Incus 支持大量 Linux 发行版的镜像（包括官方 Ubuntu 镜像和社区提供的镜像），并围绕一个强大而简单的 REST API 构建。Incus 可以从单机上的一个实例扩展到数据中心机架中的集群，使其适合开发和生产环境中的工作负载。

Incus 允许您轻松设置一个感觉像小型私有云的系统。您可以在保持资源优化的同时高效运行任何类型的工作负载。

如果您想要容器化不同的环境、运行虚拟机，或以成本效益的方式运行和管理基础设施，您应该考虑使用 Incus。

## 功能特性

- **系统容器管理**：运行完整的 Linux 系统作为容器，提供隔离和安全性。
- **虚拟机支持**：除了容器，还支持虚拟机管理。
- **镜像支持**：支持多种 Linux 发行版的官方和社区镜像。
- **REST API**：强大的 API 用于自动化和管理。
- **集群支持**：从单节点扩展到多节点集群。
- **安全性**：内置安全功能，包括网络隔离和访问控制。
- **迁移工具**：从 LXD 迁移到 Incus 的工具。

## 用法

### 安装和开始使用

请参考 [Incus 文档](https://linuxcontainers.org/incus/docs/main/tutorial/first_steps/) 获取安装说明和第一步。

- 发布公告：[https://discuss.linuxcontainers.org/c/news/](https://discuss.linuxcontainers.org/c/news/)
- 发布 tarball：[https://github.com/lxc/incus/releases/](https://github.com/lxc/incus/releases/)
- 完整文档：[https://linuxcontainers.org/incus/docs/main/](https://linuxcontainers.org/incus/docs/main/)

### 从 LXD 迁移

LXD 用户可以通过迁移工具 [`lxd-to-incus`](https://linuxcontainers.org/incus/docs/main/howto/server_migrate_lxd/) 轻松迁移到 Incus。

### 安全注意事项

- 保持操作系统更新并安装所有可用的安全补丁。
- 仅使用受支持的 Incus 版本。
- 限制对 Incus 守护进程和远程 API 的访问。
- 除非必要，否则不要使用特权容器。如果使用，请采取适当的安全措施。
- 配置网络接口以确保安全。

有关详细信息，请参阅 [安全文档](https://github.com/lxc/incus/blob/main/doc/explanation/security.md)。

**重要提示：** 通过 Unix 套接字对 Incus 的本地访问始终授予对 Incus 的完全访问权限，包括附加文件系统路径或设备到任何实例的能力。因此，只应授予您信任的用户以 root 访问权限。

### 支持和社区

- **Bug 报告**：[https://github.com/lxc/incus/issues/new](https://github.com/lxc/incus/issues/new)
- **社区支持**：[https://discuss.linuxcontainers.org](https://discuss.linuxcontainers.org)
- **商业支持**：由 [Zabbly](https://zabbly.com) 为其 Debian 或 Ubuntu 包的用户提供。

### 贡献

修复和新功能非常受欢迎。请先阅读我们的 [贡献指南](https://github.com/lxc/incus/blob/main/CONTRIBUTING.md)！

## 项目历史

Incus 以 Cumulonimbus incus（砧状积雨云）命名，是 Canonical 的 LXD 的社区分支，在 Canonical 接管 LXD 项目后启动。该项目随后被 Linux Containers 社区采用，填补了 LXD 离开留下的空白。

Incus 是一个真正的开源社区项目，没有 CLA，并根据 Apache 2.0 许可证发布。由最初创建 LXD 的同一开发团队维护。
