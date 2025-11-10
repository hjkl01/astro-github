---
title: Twocast
---

# Twocast 项目

## 项目地址
[GitHub 项目地址](https://github.com/panyanyany/Twocast)

## 主要特性
Twocast 是一个基于 Python 的开源工具，专注于网络数据捕获和分析。主要特性包括：
- **实时数据包捕获**：支持使用 libpcap 或类似库捕获网络流量，提供高效的实时监控。
- **数据过滤与解析**：内置过滤器，可根据协议、IP 或端口进行筛选，并解析常见协议如 TCP、UDP 和 HTTP。
- **可视化输出**：生成图表和统计报告，帮助用户直观分析流量模式。
- **模块化设计**：易于扩展，支持自定义插件以添加新协议支持。
- **跨平台兼容**：适用于 Windows、Linux 和 macOS 系统。

## 主要功能
- **流量监控**：实时监控网络接口的进出流量，识别异常活动。
- **协议分析**：深入解析数据包内容，支持提取 payload 和头部信息。
- **日志记录**：将捕获数据保存为 PCAP 文件或自定义格式，便于后续分析。
- **警报机制**：设置阈值触发警报，例如检测到高流量或特定模式时通知用户。
- **集成工具**：可与 Wireshark 等工具结合使用，提供命令行接口。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/panyanyany/Twocast.git`
   - 进入目录：`cd Twocast`
   - 安装依赖：`pip install -r requirements.txt`（确保已安装 Python 3.6+ 和 Scapy 等库）

2. **基本运行**：
   - 启动捕获：`python twocast.py -i eth0 -f "tcp port 80"`（其中 `-i` 指定网络接口，`-f` 为过滤表达式）
   - 查看帮助：`python twocast.py --help`

3. **高级用法**：
   - 保存输出：`python twocast.py -i wlan0 -o output.pcap -t 60`（捕获 60 秒并保存为 PCAP 文件）
   - 分析日志：`python analyze.py input.pcap`（使用分析脚本生成报告）
   - 配置插件：编辑 `config.yaml` 文件添加自定义过滤规则，然后运行 `python twocast.py --config config.yaml`。

注意：使用前需确保有网络接口访问权限（如 root 权限）。项目文档详见仓库 README。