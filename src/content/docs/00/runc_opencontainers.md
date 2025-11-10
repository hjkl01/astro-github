---
title: Runc
---

# runc

## 功能介绍

runc 是一个 CLI 工具，用于根据 OCI 规范在 Linux 上生成和运行容器。它是 Open Container Initiative (OCI) 的参考实现，提供低级别的容器运行时功能。

主要功能包括：

- 创建和运行 OCI 兼容的容器
- 支持容器生命周期管理（创建、启动、停止、删除）
- 提供 checkpoint 和 restore 功能
- 支持 rootless 容器运行
- 集成 seccomp、AppArmor 和 SELinux 等安全特性

## 用法

### 安装

从源码构建：

```bash
git clone https://github.com/opencontainers/runc
cd runc
make
sudo make install
```

### 创建 OCI Bundle

1. 创建 bundle 目录和 rootfs：

```bash
mkdir /mycontainer
cd /mycontainer
mkdir rootfs
docker export $(docker create busybox) | tar -C rootfs -xvf -
```

2. 生成配置文件：

```bash
runc spec
```

### 运行容器

使用 `run` 命令（便捷方式）：

```bash
runc run mycontainerid
```

或使用生命周期操作：

```bash
runc create mycontainerid
runc start mycontainerid
runc delete mycontainerid
```

### Rootless 容器

生成 rootless 配置：

```bash
runc spec --rootless
runc --root /tmp/runc run mycontainerid
```

更多详细信息请参考 [官方文档](https://github.com/opencontainers/runc)。
