---
title: asterinas
---

# Asterinas

Asterinas 是一个安全、快速且通用的操作系统内核，使用 Rust 编写并与 Linux 兼容。它提供了 Linux ABI，可以作为 Linux 的无缝替换，同时通过内存安全和开发者友好性增强安全性。

## 主要特性

- **内存安全**：使用 Rust 作为唯一编程语言，将 unsafe Rust 限制在明确定义的最小可信计算基 (TCB) 中。
- **框架内核架构**：通过模块化设计实现安全和性能。
- **Linux 兼容**：提供 Linux ABI，支持现有 Linux 应用程序。
- **开发者友好**：使用 Rust 编程语言，提供 OSDK 工具链简化工作流。
- **高性能**：针对 x86-64、RISC-V 和 LoongArch 架构优化。

## 主要功能

- **内核开发**：使用 Rust 构建安全操作系统内核。
- **模块化**：支持开源和专有内核模块。
- **测试和基准**：提供全面的测试套件和性能基准。
- **文档**：详细的书籍和指南。

## 用法

### 快速开始

1. 下载最新源代码：

   ```
   git clone https://github.com/asterinas/asterinas
   ```

2. 运行 Docker 容器作为开发环境：

   ```
   docker run -it --privileged --network=host --device=/dev/kvm -v $(pwd)/asterinas:/root/asterinas asterinas/asterinas:0.16.1-20250922
   ```

3. 在容器中构建和运行 Asterinas：
   ```
   make build
   make run
   ```

### 更多信息

请参考 [Asterinas Book](https://asterinas.github.io/book/) 获取详细文档。

项目地址: [Asterinas GitHub](https://github.com/asterinas/asterinas)
