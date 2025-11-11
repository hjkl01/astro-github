---
title: Bootc
---

# bootc

## 功能

bootc 是一个用于通过 OCI/Docker 容器镜像进行事务性、原地操作系统更新的工具。它使用标准容器镜像作为操作系统更新的传输和交付格式，包括 Linux 内核用于引导。运行时，基础用户空间不是在容器中运行，而是像通常一样使用 systemd 等作为 pid1。

## 用法

要使用 bootc，首先需要一个基于 bootc 的操作系统镜像。安装后，可以使用 bootc CLI 来升级系统到新版本的容器镜像。例如：

- 安装：从 [ADOPTERS.md](https://github.com/bootc-dev/bootc/blob/main/ADOPTERS.md) 中选择一个基础镜像。
- 升级：运行 `bootc upgrade` 来应用新镜像。

详细用法请参考 [官方文档](https://bootc-dev.github.io/bootc/)。

社区讨论在 [GitHub Discussions](https://github.com/containers/bootc/discussions) 和 CNCF Slack 的 #bootc-dev 频道。
