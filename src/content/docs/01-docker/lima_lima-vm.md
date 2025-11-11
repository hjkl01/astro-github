---
title: Lima
---

# Lima

## 功能

Lima 是一个用于启动 Linux 虚拟机的工具，专注于运行容器。它提供自动文件共享和端口转发（类似于 WSL2）。Lima 的最初目标是向 Mac 用户推广 containerd 和 nerdctl（contaiNERD ctl），但它也可以用于非容器应用程序。

Lima 支持其他容器引擎（如 Docker、Podman、Kubernetes 等），并且可以在非 macOS 主机（如 Linux、NetBSD 等）上运行。

## 用法

### 安装

使用 Homebrew 安装：

```bash
brew install lima
```

### 启动虚拟机

启动默认虚拟机：

```bash
limactl start
```

### 运行 Linux 命令

在 Lima 虚拟机中运行命令：

```bash
lima uname -a
```

### 使用 containerd 运行容器

```bash
lima nerdctl run --rm hello-world
```

### 使用 Docker 运行容器

启动 Docker 模板：

```bash
limactl start template://docker
```

设置环境变量：

```bash
export DOCKER_HOST=$(limactl list docker --format 'unix://{{.Dir}}/sock/docker.sock')
```

运行容器：

```bash
docker run --rm hello-world
```

### 使用 Kubernetes 运行容器

启动 Kubernetes 模板：

```bash
limactl start template://k8s
```

设置环境变量：

```bash
export KUBECONFIG=$(limactl list k8s --format 'unix://{{.Dir}}/copied-from-guest/kubeconfig.yaml')
```

应用配置：

```bash
kubectl apply -f ...
```

更多详细信息，请参考 [官方文档](https://lima-vm.io/docs/)。
