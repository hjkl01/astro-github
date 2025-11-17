---
title: ebpf
---

# eBPF 项目介绍

## 项目概述

eBPF (extended Berkeley Packet Filter) 是一个开源项目，由 Cilium 组织维护。该项目提供了一个 Go 语言库，用于编写、加载和运行 eBPF 程序。eBPF 是一种在 Linux 内核中运行用户空间程序的技术，常用于网络过滤、安全监控、性能分析等领域。

## 主要功能

- **Go API 支持**：提供完整的 Go 语言 API，用于创建和管理 eBPF 程序
- **程序加载**：支持将 eBPF 字节码加载到内核中
- **映射管理**：提供对 eBPF 映射 (maps) 的操作接口
- **程序附加**：支持将 eBPF 程序附加到内核钩子点，如网络接口、系统调用等
- **类型安全**：通过 Go 的类型系统提供更好的开发体验

## 用法示例

1. **安装依赖**：

   ```bash
   go get github.com/cilium/ebpf
   ```

2. **基本使用**：

   ```go
   package main

   import (
       "github.com/cilium/ebpf"
       "github.com/cilium/ebpf/link"
   )

   func main() {
       // 加载 eBPF 程序
       spec, err := ebpf.LoadCollection("program.o")
       if err != nil {
           panic(err)
       }

       // 附加到网络接口
       link, err := link.AttachXDP(link.XDPOptions{
           Program:   spec.Programs["xdp_prog"],
           Interface: 1, // 接口索引
       })
       if err != nil {
           panic(err)
       }
       defer link.Close()
   }
   ```

3. **编译 eBPF 程序**：
   需要使用 clang 编译器将 C 代码编译为 eBPF 字节码。

## 注意事项

- 需要 Linux 内核版本 4.9 或更高
- 需要适当的权限运行（通常需要 root 权限）
- 建议在开发环境中使用，避免在生产环境直接部署未经测试的程序
