
---
title: kata-containers
---


# Kata Containers

> GitHub 地址: [https://github.com/kata-containers/kata-containers](https://github.com/kata-containers/kata-containers)

## 项目概述
Kata Containers 是一个开源项目，目标是将传统的容器技术与虚拟化技术结合，提供与 Docker/Kubernetes 等容器生态系统兼容的安全隔离容器。它通过在每个容器内部运行一个轻量级虚拟机（VM）来实现更强的隔离，同时保持容器的快速启动和资源效率。

## 主要特性
| 特性 | 说明 |
|------|------|
| **轻量级虚拟化** | 每个容器运行在一个最小化的 VM 内，提供硬件级隔离。 |
| **兼容容器生态** | 与 Docker、CRI-O、Kubelet 等兼容，可无缝集成 Kubernetes。 |
| **高速启动** | VM 启动时间仅为传统 VM 的一小部分，接近容器启动速度。 |
| **安全增强** | 通过硬件虚拟化、SELinux/AppArmor、Seccomp 等安全机制提升安全性。 |
| **多平台支持** | 支持 Linux（x86_64、ARM64 等）及 Windows（Hyper-V）平台。 |
| **可扩展的插件体系** | 通过插件（网络、存储、日志等）可扩展功能。 |
| **统一 API** | 提供 Kata API 与 CRI（Container Runtime Interface）实现，便于集成。 |

## 架构概览
```
┌───────────────────────┐
│  Container Runtime    │
│  (Docker / CRI-O)     │
└─────────────┬─────────┘
              │
              ▼
┌───────────────────────┐
│  Kata Runtime (kata-runtime) │
└─────────────┬─────────┘
              │
              ▼
┌───────────────────────┐
│  Kata Agent (kata-agent) │
└─────────────┬─────────┘
              │
              ▼
┌───────────────────────┐
│  Hypervisor (QEMU/KVM/Hyper-V) │
└───────────────────────┘
```

- **kata-runtime** 负责在宿主机上创建/销毁 VM 并管理容器生命周期。  
- **kata-agent** 运行在 VM 内，处理容器的命令、文件系统、网络等。  
- **Hypervisor** 提供硬件虚拟化。

## 安装与使用

### 1. 安装 Kata Containers

```bash
# Ubuntu 示例
sudo apt-get update
sudo apt-get install -y kata-runtime kata-proxy
```

或者使用官方脚本：

```bash
curl -L https://raw.githubusercontent.com/kata-containers/kata-containers/master/install.sh | sudo bash
```

### 2. 配置 CRI-O/Kubelet 使用 Kata

编辑 `/etc/crio/crio.conf` 或 `/etc/containerd/config.toml`，指定 Kata 作为 runtime：

```toml
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.kata]
  runtime_type = "io.containerd.kata.v2"
  runtime_engine = "/usr/bin/kata-runtime"
  runtime_root = ""
  privileged_without_host_devices = true
```

### 3. 运行容器

```bash
docker run -it --runtime=kata-runtime ubuntu:20.04 /bin/bash
```

或使用 Kubernetes：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kata-pod
spec:
  runtimeClassName: kata
  containers:
    - name: nginx
      image: nginx
```

### 4. 验证

```bash
kata-runtime top <container-id>
```

或使用 `crictl`：

```bash
crictl inspect <container-id>
```

## 贡献指南

- Fork 本仓库 → `git clone` → `make` → `make test`  
- 代码风格遵循 Go 规范，编写单元测试。  
- PR 需通过 CI（GitHub Actions）测试。

## 参考文档

- [官方文档](https://katacontainers.io/)
- [Kata Containers GitHub Wiki](https://github.com/kata-containers/kata-containers/wiki)

