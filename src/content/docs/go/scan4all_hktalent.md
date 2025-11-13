---
title: scan4all
---

# scan4all 项目

## 项目地址
[GitHub 项目地址](https://github.com/hktalent/scan4all)

## 主要特性
scan4all 是一个开源的漏洞扫描工具，基于 Go 语言开发，专注于网络安全扫描。它集成了多种扫描引擎和规则，支持高性能的并行扫描，适用于大规模目标扫描。主要特性包括：
- **多协议支持**：支持 HTTP、HTTPS、FTP、SSH 等多种网络协议的漏洞检测。
- **规则引擎**：内置大量 POC（Proof of Concept）规则，可自定义扩展，支持从 Nuclei 等框架导入规则。
- **高性能**：利用 Go 的并发特性，实现快速扫描，适合扫描大型网络或多个目标。
- **轻量级设计**：无需复杂依赖，易于部署和使用，支持 Docker 容器化运行。
- **输出格式多样**：支持 JSON、HTML、TXT 等多种报告格式，便于后续分析。
- **集成友好**：可与其他安全工具如 Nuclei、fofa 等结合使用。

## 主要功能
- **漏洞扫描**：检测常见 Web 应用漏洞，如 SQL 注入、XSS、命令注入等，以及特定软件的已知漏洞（CVE）。
- **端口扫描**：集成端口发现功能，快速识别开放端口和服务。
- **指纹识别**：自动识别目标的 Web 框架、CMS、服务器类型等指纹信息。
- **批量扫描**：支持从文件导入目标列表，进行批量自动化扫描。
- **被动扫描**：通过流量分析或日志输入进行被动模式扫描，减少对目标的干扰。
- **自定义规则**：用户可编写 YAML 格式的规则文件，扩展扫描能力。

## 用法
### 安装
1. **从 GitHub 下载**：克隆仓库 `git clone https://github.com/hktalent/scan4all.git`，进入目录。
2. **构建**：运行 `go build` 编译生成可执行文件（需安装 Go 环境）。
3. **Docker 运行**：使用 `docker pull hktalent/scan4all` 拉取镜像，然后运行容器。
4. **预编译二进制**：从 Releases 页面下载适用于不同平台的二进制文件。

### 基本用法
- **命令行启动**：运行 `./scan4all -h` 查看帮助。
- **简单扫描**：`./scan4all -target example.com` 扫描单个目标。
- **批量扫描**：`./scan4all -list targets.txt` 从文件读取目标列表。
- **指定端口**：`./scan4all -target example.com -p 80,443` 扫描特定端口。
- **输出报告**：`./scan4all -target example.com -o result.json` 生成 JSON 报告。
- **自定义规则**：将规则文件置于 `rules/` 目录下，工具会自动加载。
- **高级选项**：使用 `-threads 100` 设置并发线程数，`-timeout 5` 设置超时时间等。

更多细节请参考项目 README 文件。