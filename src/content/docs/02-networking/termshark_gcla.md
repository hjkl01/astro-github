
---
title: termshark
---

# Termshark 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/gcla/termshark)

## 主要特性
Termshark 是一个基于终端的 Wireshark 界面工具，它将 Wireshark 的强大网络协议分析功能移植到命令行环境中。主要特性包括：
- **终端友好界面**：使用 TShark（Wireshark 的命令行版本）作为后端，提供 curses-based 的图形化界面，支持在终端中捕获和分析网络流量。
- **协议解码**：支持 Wireshark 相同的协议解析和过滤功能，能解码数百种网络协议，如 TCP、UDP、HTTP、DNS 等。
- **实时捕获**：可以从网络接口实时捕获数据包，或从 pcap 文件加载历史数据。
- **过滤与搜索**：内置强大的过滤表达式，支持 Wireshark 风格的显示过滤器（如 `http.request`），并提供搜索和导航功能。
- **跨平台支持**：兼容 Linux、macOS 和 Windows（需安装 Wireshark 和 TShark）。
- **无头模式**：适合服务器环境或脚本自动化，不依赖图形界面。

## 主要功能
- **数据包捕获**：通过指定网络接口（如 `eth0`）实时捕获流量，或从文件读取 pcap/ng 文件。
- **数据包分析**：显示数据包列表、详细信息和十六进制视图，支持树状协议层次展开。
- **过滤与统计**：应用过滤器查看特定流量，生成协议统计、端点统计和图表（文本形式）。
- **导出与保存**：将过滤后的数据包导出为 pcap 文件，或生成报告。
- **集成 Wireshark**：无缝与 Wireshark 协作，可从 Termshark 打开数据包到 Wireshark GUI 中进一步分析。

## 用法
### 安装
1. 确保已安装 Wireshark（包含 TShark）。例如，在 Ubuntu 上运行：
   ```
   sudo apt install wireshark tshark
   ```
2. 从 GitHub 下载并安装 Termshark：
   ```
   go install github.com/gcla/termshark@latest
   ```
   或使用预编译二进制文件。

### 基本命令
- **启动捕获模式**：`termshark -i <interface>`（例如 `termshark -i eth0`），开始从指定接口捕获数据包。
- **分析 pcap 文件**：`termshark -r <file.pcap>`（例如 `termshark -r capture.pcap`），加载并分析文件。
- **应用过滤器**：在界面中按 `/` 输入过滤表达式，如 `tcp.port == 80`，然后按 Enter 应用。
- **导航**：
  - 使用箭头键浏览数据包列表。
  - 按 Enter 查看数据包详情。
  - 按 `h` 显示帮助，按 `q` 退出。
- **实时模式选项**：`termshark -i eth0 -w output.pcap` 保存捕获到文件。
- **高级用法**：支持 `-f` 捕获过滤器（如 `-f "port 80"`）和 `-R` 只读模式。

更多细节请参考项目 README。