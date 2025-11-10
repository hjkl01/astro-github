---
title: Nvidia Container Toolkit
---

# nvidia-container-toolkit

## 功能介绍

NVIDIA Container Toolkit 允许用户构建和运行利用 NVIDIA GPU 的容器。该工具包包括一个容器运行时库和实用程序，用于自动配置容器以利用 NVIDIA GPU。

该工具包支持在容器中无缝访问 NVIDIA GPU，从而使 GPU 加速的应用程序能够在容器化环境中运行，而无需手动配置 GPU 设备和驱动。

## 用法

### 安装前提

在使用 NVIDIA Container Toolkit 之前，请确保您的 Linux 发行版已安装 NVIDIA 驱动程序。请注意，您不需要在主机系统上安装 CUDA Toolkit，但必须安装 NVIDIA 驱动程序。

### 安装步骤

1. 参考 [安装指南](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installation-guide) 获取详细的安装说明。

2. 安装完成后，您可以使用 Docker 或其他容器运行时来运行 GPU 加速的容器。

### 基本用法

运行 GPU 加速的容器示例：

```bash
docker run --gpus all nvidia/cuda:11.0-base nvidia-smi
```

这将运行一个 CUDA 容器，并显示 GPU 信息。

### 配置选项

[user guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/user-guide.html) 提供了运行 GPU 容器时可用的配置和命令行选项的详细信息。

### 更多信息

- 产品文档：[https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html)
- GitHub 仓库：[https://github.com/NVIDIA/nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
