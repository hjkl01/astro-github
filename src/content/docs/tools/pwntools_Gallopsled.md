---
title: pwntools
---

# Pwntools 项目

**项目地址:** [https://github.com/Gallopsled/pwntools](https://github.com/Gallopsled/pwntools)

## 主要特性
Pwntools 是一个专为 CTF（Capture The Flag）竞赛和二进制漏洞利用开发设计的 Python 库。它提供了丰富的工具集，帮助开发者快速构建和测试漏洞利用程序。主要特性包括：
- **跨平台支持**：兼容 Linux、Windows 和 macOS，支持 32 位和 64 位架构。
- **高层次抽象**：简化了二进制分析、ROP（Return-Oriented Programming）链构建和 shellcode 生成等复杂任务。
- **模块化设计**：包含进程管理、符号解析、网络通信和加密工具等模块，便于扩展和集成。
- **社区驱动**：开源项目，活跃维护，广泛用于安全研究和教育。

## 主要功能
Pwntools 的核心功能聚焦于二进制 exploitation 和逆向工程：
- **进程交互**：启动本地或远程进程，发送/接收数据，支持动态符号解析（如 ELF 文件的函数地址）。
- **ROP 工具**：自动生成 ROP 链，利用现有代码片段绕过 DEP（Data Execution Prevention）。
- **网络工具**：处理 TCP/UDP 连接、SSL/TLS 加密，支持自定义协议实现。
- **符号与格式化**：解析二进制文件（ELF/PE），处理格式字符串漏洞，提供 shellcode 编码/解码。
- **实用工具**：内存视图、日志记录、上下文管理（Context 对象用于架构特定操作）。

## 用法示例
安装 Pwntools：`pip install pwntools`。

### 基本用法：本地进程利用
```python
from pwn import *

# 启动本地进程
p = process('./binary')

# 发送 payload
payload = b'A' * 40 + p64(0xdeadbeef)  # 示例 payload
p.sendline(payload)

# 接收输出
p.interactive()  # 进入交互模式
```

### 远程利用
```python
from pwn import *

# 连接远程服务
p = remote('example.com', 1234)

# 发送数据并交互
p.sendline(b'payload')
p.interactive()
```

### ROP 链构建
```python
from pwn import *

elf = context.binary = ELF('./binary')
rop = ROP(elf)

# 添加 ROP gadgets
rop.system(elf.search('/bin/sh').__next__())

# 生成 payload
payload = flat({0x40: rop})
p.sendline(payload)
```

更多细节请参考官方文档：https://docs.pwntools.com/。