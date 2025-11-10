---
title: Kata Containers
---

# Kata Containers

## 项目简介

Kata Containers 是一个开源项目和社区，致力于构建轻量级虚拟机（VMs）的标准实现，这些虚拟机感觉和表现像容器，但提供虚拟机的负载隔离和安全优势。

官方网站：[https://katacontainers.io/](https://katacontainers.io/)

## 功能特性

- **轻量级虚拟机**：提供容器般的性能和易用性，同时具备虚拟机的隔离和安全特性。
- **多架构支持**：
  - x86_64 / amd64：Intel VT-x, AMD SVM
  - aarch64 (arm64)：ARM Hyp
  - ppc64le：IBM Power
  - s390x：IBM Z & LinuxONE SIE
- **兼容性**：与 Docker、Kubernetes 等容器编排工具集成。
- **安全性**：通过虚拟机级别的隔离增强容器安全性。
- **性能**：针对容器工作负载优化的内置 VMM（如 Dragonball）。

## 主要组件

- **Runtime**：主要组件，由容器管理器运行，提供 containerd shimv2 运行时实现。
- **Runtime-rs**：Rust 版本的运行时。
- **Agent**：在虚拟机/POD 内运行的管理进程，设置容器环境。
- **Dragonball**：可选的内置 VMM，为 Kata Containers 提供开箱即用的体验，并针对容器工作负载进行优化。

## 安装和使用

### 系统要求

运行 `kata-runtime check` 命令检查主机系统是否支持 Kata Containers：

```bash
kata-runtime check
```

- 添加 `--no-network-checks` 选项可禁用网络检查。
- 使用 `--verbose` 标志显示所有检查详情。
- 以 root 用户运行时，会执行额外检查（包括检查是否有其他不兼容的虚拟机管理器运行）。

### 安装

参考官方安装文档：[Installation guides](https://github.com/kata-containers/kata-containers/blob/main/docs/install)

Kata Containers 现在在大多数发行版上原生可用。

### 配置

Kata Containers 使用单个配置文件，包含运行时、代理和虚拟机管理器的各个部分配置。

详细配置信息：[Configuration](https://github.com/kata-containers/kata-containers/blob/main/src/runtime/README.md#configuration)

### 虚拟机管理器

支持多种虚拟机管理器，包括 QEMU、Firecracker、ACRN 等。

详细文档：[Hypervisors](https://github.com/kata-containers/kata-containers/blob/main/docs/hypervisors.md)

## 社区和支持

- **社区**：访问 [Kata Containers 社区仓库](https://github.com/kata-containers/community) 了解项目、社区和治理。
- **获取帮助**：在 [GitHub Issues](https://github.com/kata-containers/kata-containers/issues) 中提出问题。
- **安全问题**：遵循 [漏洞报告流程](https://github.com/kata-containers/community#vulnerability-handling)。

## 开发者资源

- **开发者指南**：[Developer Guide](https://github.com/kata-containers/kata-containers/blob/main/docs/Developer-Guide.md)
- **设计文档**：[Design Documents](https://github.com/kata-containers/kata-containers/blob/main/docs/design)
- **测试**：[Tests Documentation](https://github.com/kata-containers/kata-containers/blob/main/tests/README.md)

## 许可证

代码基于 Apache 2.0 许可证开源。
