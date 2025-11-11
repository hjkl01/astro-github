---
title: hashcat
---

# Hashcat 项目

## 项目地址

[https://github.com/hashcat/hashcat](https://github.com/hashcat/hashcat)

## 主要特性

Hashcat 是世界上最快的密码恢复工具，支持超过 300 种哈希算法，包括 MD5、SHA1、SHA256、NTLM、bcrypt 等。它利用 CPU 和 GPU（支持 NVIDIA CUDA 和 AMD OpenCL）进行高效并行计算，能够处理大规模密码破解任务。主要特性包括：

- **高性能**：优化了 GPU 加速，支持多设备并行处理，实现极高的哈希破解速度（可达数万亿哈希/秒）。
- **多种攻击模式**：支持直行攻击、组合攻击、基于规则的攻击、掩码攻击、字典攻击和混合攻击。
- **跨平台支持**：兼容 Windows、Linux 和 macOS，支持多种硬件架构。
- **模块化设计**：易于扩展，支持自定义哈希模块和规则。
- **开源免费**：基于 MIT 许可证，社区活跃，提供详细文档和基准测试。

## 主要功能

- **密码破解**：针对各种加密哈希值进行暴力破解或智能猜测，用于安全审计、取证分析和密码恢复。
- **哈希类型支持**：内置多种预设哈希模式，如 WPA/WPA2 Wi-Fi 密码、PDF/Office 文档加密、数据库哈希等。
- **规则引擎**：使用自定义规则文件修改字典词条，实现高级变体生成（如大小写变换、数字后缀）。
- **基准测试**：内置 benchmark 功能，测试硬件性能并比较不同设备。
- **恢复会话**：支持保存和恢复破解进度，避免长时间任务中断。

## 用法

### 安装

- 下载 [最新发布](https://hashcat.net/hashcat/) 并解压。
- 平台包：Arch Linux、Debian、Fedora 等提供包。
- 从源构建：参考 [BUILD.md](https://github.com/hashcat/hashcat/blob/master/BUILD.md)。

### 基本用法

- 基准测试：`hashcat -b`
- 字典攻击：`hashcat -m 0 -a 0 hash.txt wordlist.txt`
- 暴力破解：`hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a`
- 规则攻击：`hashcat -m 0 -a 0 hash.txt wordlist.txt -r rules/best64.rule`
- GPU 指定：`-d 1` 使用第二个 GPU。

### 高级用法

- 输出结果：`--outfile=cracked.txt`
- 恢复会话：`hashcat --restore`
- 帮助：`hashcat --help` 或 [Wiki](https://hashcat.net/wiki/)

注意：仅用于合法安全研究。
