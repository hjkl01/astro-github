
---
title: ecapture
---

# eCapture 项目

**GitHub 项目地址:** [https://github.com/gojue/ecapture](https://github.com/gojue/ecapture)

## 主要特性
eCapture 是一个基于 eBPF（extended Berkeley Packet Filter）的开源工具，主要用于内核级网络数据捕获和安全分析。它具有以下核心特性：
- **内核级捕获**：利用 eBPF 技术在内核空间直接捕获网络流量，避免用户空间开销，提高效率和安全性。
- **低开销**：相比传统工具如 tcpdump，eCapture 的资源消耗更低，支持高吞吐量环境。
- **模块化设计**：支持多种捕获模块，包括 TLS/SSL 解密、HTTP/HTTPS 流量分析、MySQL 等数据库协议捕获，以及自定义协议支持。
- **跨平台兼容**：主要针对 Linux 系统，支持 x86_64 和 ARM 架构，适用于云原生环境如 Kubernetes。
- **安全审计**：可用于网络取证、入侵检测和合规审计，支持加密流量解密（需提供证书或密钥）。
- **开源免费**：基于 Apache 2.0 许可，社区活跃，提供详细文档和示例。

## 主要功能
eCapture 的功能聚焦于网络数据包捕获和分析，具体包括：
- **SSL/TLS 流量捕获**：解密 HTTPS 等加密流量，支持多种 TLS 版本（TLS 1.0-1.3），可捕获明文内容而不中断连接。
- **应用层协议支持**：内置模块捕获 HTTP/2、MySQL、Redis、PostgreSQL 等协议的数据，便于调试和监控。
- **过滤与导出**：支持 BPF 过滤器自定义捕获条件，可将数据导出为 PCAP 文件或实时输出到文件/stdout。
- **进程级捕获**：针对特定进程或 PID 捕获网络 I/O，实现精细化监控。
- **性能优化**：集成 ring buffer 和 perf event 机制，确保高性能捕获而不影响系统稳定性。
- **扩展性**：用户可编写自定义 eBPF 程序扩展功能，支持集成到 SIEM 系统或日志管道。

## 用法
eCapture 的使用简单，通过命令行工具操作。以下是基本步骤和示例（假设已安装 Go 环境和 eBPF 支持的 Linux 内核）：

### 安装
1. 克隆仓库：`git clone https://github.com/gojue/ecapture.git`
2. 构建：`cd ecapture && make build`
3. 安装：`sudo make install`（或直接运行 `./ecapture`）

### 基本用法
- **查看帮助**：`sudo ./ecapture -h`
- **捕获所有 SSL/TLS 流量**（保存为 PCAP 文件）：
  ```
  sudo ./ecapture -f ssl -i any -w output.pcap
  ```
  - `-f ssl`：指定 SSL 模块。
  - `-i any`：捕获所有接口。
  - `-w output.pcap`：输出到 PCAP 文件。
- **捕获特定进程的 HTTP 流量**：
  ```
  sudo ./ecapture -f http2 -p <PID> -w http_capture.pcap
  ```
  - `-p <PID>`：指定进程 ID。
- **MySQL 协议捕获**（带过滤）：
  ```
  sudo ./ecapture -f mysql -i eth0 -F "port 3306" -w mysql.pcap
  ```
  - `-F`：BPF 过滤表达式，如端口或 IP。
- **解密 TLS 流量**（需提供私钥）：
  ```
  sudo ./ecapture -f ssl -K /path/to/private.key -w decrypted.pcap
  ```
  - `-K`：指定私钥路径，用于解密。

### 注意事项
- 需要 root 权限运行。
- 确保内核版本 ≥ 4.14 并启用 eBPF 支持（`uname -r` 检查）。
- 对于生产环境，建议在测试环境中验证兼容性。
- 更多高级用法参考项目文档：https://github.com/gojue/ecapture/blob/master/README.md