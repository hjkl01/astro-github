---
title: runc
---

# runc

runc 是一个用于根据 OCI 规范生成和运行容器的 CLI 工具。它是 Open Container Initiative (OCI) 容器运行时规范的实现，主要用于 Linux 系统。

## 功能

- **容器运行时**：提供低级别的容器运行时功能，支持创建、启动、停止和管理容器。
- **OCI 兼容**：完全符合 OCI 运行时规范，确保容器的一致性和可移植性。
- **安全特性**：支持 seccomp、AppArmor、SELinux 等安全机制。
- **检查点和恢复**：支持容器的检查点和恢复功能（需要 CRIU 支持）。
- **无根容器**：支持以非 root 用户身份运行容器（rootless 模式）。

## 安装

runc 仅支持 Linux 系统。构建需要 Go 语言环境和一些系统依赖。

### 依赖项

在 Ubuntu/Debian 上安装依赖：

```bash
apt update && apt install -y make gcc linux-libc-dev libseccomp-dev pkg-config git
```

在 CentOS/Fedora 上：

```bash
yum install -y make gcc kernel-headers libseccomp-devel pkg-config git
```

### 构建

```bash
# 克隆仓库
git clone https://github.com/opencontainers/runc
cd runc

# 构建
make

# 安装
sudo make install
```

runc 将安装到 `/usr/local/sbin/runc`。

## 用法

runc 是一个低级工具，通常由更高层次的容器软件（如 Docker 或 Podman）使用。不推荐直接使用 runc，除非有特殊需求。

### 创建 OCI Bundle

要使用 runc，需要将容器格式化为 OCI bundle。首先创建根文件系统：

```bash
# 创建 bundle 目录
mkdir /mycontainer
cd /mycontainer

# 创建 rootfs 目录
mkdir rootfs

# 从 Docker 容器导出根文件系统
docker export $(docker create busybox) | tar -C rootfs -xvf -
```

然后生成配置文件：

```bash
runc spec
```

这将创建一个 `config.json` 文件，可以根据需要编辑。

### 运行容器

有两种方式运行容器：

#### 方式一：使用 run 命令

```bash
cd /mycontainer
runc run mycontainerid
```

这将创建、启动容器，并在退出后删除。

#### 方式二：使用生命周期操作

```bash
# 创建容器
runc create mycontainerid

# 查看容器状态
runc list

# 启动容器
runc start mycontainerid

# 删除容器
runc delete mycontainerid
```

### 无根容器

要运行无根容器，需要启用用户命名空间，并使用 `--rootless` 参数：

```bash
# 生成无根配置
runc spec --rootless

# 运行无根容器
runc --root /tmp/runc run mycontainerid
```

## 示例

以下是一个完整的示例：

```bash
# 创建目录
mkdir ~/mycontainer
cd ~/mycontainer
mkdir rootfs

# 导出 busybox 镜像
docker export $(docker create busybox) | tar -C rootfs -xvf -

# 生成配置
runc spec

# 运行容器
runc run mycontainerid
```

这将在容器内启动一个 shell 会话。

## 更多信息

- [官方文档](https://github.com/opencontainers/runc)
- [OCI 规范](https://github.com/opencontainers/runtime-spec)
- [安全审计报告](https://github.com/opencontainers/runc/blob/master/docs/Security-Audit.pdf)
