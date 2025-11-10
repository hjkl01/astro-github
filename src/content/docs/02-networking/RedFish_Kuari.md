---
title: RedFish
---

# RedFish 项目

**GitHub 项目地址:** [https://github.com/Kuari/RedFish](https://github.com/Kuari/RedFish)

## 主要特性
RedFish 是一个基于 Python 的开源工具，专注于网络安全测试和渗透测试领域。它具有以下主要特性：
- **模块化设计**：支持多种网络协议和攻击模块，便于扩展和自定义。
- **跨平台支持**：兼容 Windows、Linux 和 macOS 系统。
- **高效性能**：利用多线程和异步处理，提升扫描和测试速度。
- **安全合规**：仅用于合法授权的渗透测试，不鼓励非法使用。
- **用户友好界面**：提供命令行和简单图形界面选项。

## 主要功能
- **端口扫描**：快速识别目标主机开放端口，支持 SYN、TCP 和 UDP 扫描模式。
- **漏洞检测**：内置常见漏洞扫描器，如 SQL 注入、XSS 和弱口令检测。
- **Web 应用测试**：针对 Web 服务进行爬虫、表单提交和 API 测试。
- **网络钓鱼模拟**：辅助红队演练中的社会工程学攻击模拟（需合规使用）。
- **报告生成**：自动生成测试报告，支持 HTML 和 JSON 格式输出。
- **插件系统**：允许用户添加自定义插件扩展功能。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/Kuari/RedFish.git`
   - 进入目录：`cd RedFish`
   - 安装依赖：`pip install -r requirements.txt`

2. **基本命令**：
   - 启动工具：`python redfish.py --help` 查看帮助。
   - 端口扫描示例：`python redfish.py scan --target 192.168.1.1 --ports 1-1000`
   - 漏洞扫描示例：`python redfish.py vuln --url http://example.com --module sql_injection`
   - 生成报告：使用 `--output report.html` 参数保存结果。

3. **高级用法**：
   - 配置代理：编辑 `config.yaml` 文件设置代理服务器。
   - 多目标扫描：`python redfish.py scan --targets targets.txt`
   - 自定义模块：将新脚本放入 `plugins/` 目录并重启工具。

**注意**：请确保在使用前获得目标系统的授权，仅用于教育和合法安全测试目的。项目维护者不对滥用行为负责。