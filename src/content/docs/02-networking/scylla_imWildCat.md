---
title: scylla
---

# Scylla 项目

**GitHub 项目地址:** [https://github.com/imWildCat/scylla](https://github.com/imWildCat/scylla)

## 主要特性
Scylla 是一个基于 Python 的高性能网络扫描工具，灵感来源于神话中的海拉怪物，旨在模拟高效的多线程扫描能力。其主要特性包括：
- **高并发扫描**：支持多线程和异步 I/O，实现快速端口扫描和漏洞探测，适用于大规模网络环境。
- **模块化设计**：内置多种扫描模块，如 TCP/UDP 端口扫描、Web 漏洞扫描和服务指纹识别，便于扩展自定义模块。
- **隐蔽性强**：集成代理支持和随机化扫描顺序，减少被检测风险。
- **数据可视化**：提供扫描结果的实时输出和导出功能，支持 JSON、CSV 等格式，便于后续分析。
- **跨平台兼容**：支持 Windows、Linux 和 macOS 系统，依赖 Python 3.x 环境。

## 功能
- **端口扫描**：检测目标主机开放端口，支持常见服务如 HTTP、SSH、FTP 等。
- **漏洞扫描**：集成常见漏洞库（如 CVE），自动识别潜在安全弱点。
- **主机发现**：通过 ICMP 或 ARP 协议发现活跃主机。
- **服务枚举**：对开放端口进行服务版本探测和操作系统指纹识别。
- **报告生成**：自动生成详细扫描报告，包括风险评估和修复建议。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/imWildCat/scylla.git`
   - 进入目录：`cd scylla`
   - 安装依赖：`pip install -r requirements.txt`

2. **基本命令**：
   - 扫描单个主机端口：`python scylla.py -t 192.168.1.1 -p 1-1000`
   - 扫描 IP 范围：`python scylla.py -t 192.168.1.0/24 --threads 50`
   - 启用漏洞扫描：`python scylla.py -t example.com --vuln-scan`
   - 使用代理：`python scylla.py -t target.com --proxy socks5://127.0.0.1:1080`
   - 查看帮助：`python scylla.py --help`

3. **高级用法**：
   - 自定义模块：编辑 `modules/` 目录下的 Python 文件，添加新扫描逻辑。
   - 输出报告：`python scylla.py -t target -o report.json`
   
注意：使用前确保遵守当地法律法规，仅用于合法授权的安全测试。