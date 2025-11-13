---
title: RustScan
---

# RustScan

## 项目简介

RustScan 是一个现代化的端口扫描器，使用 Rust 编写，旨在快速、智能化地发现开放端口。它是 Nmap 的替代品，专注于速度和可扩展性。

## 主要功能

- **高速扫描**：能够在 3 秒内扫描所有 65,535 个端口。
- **脚本引擎**：支持 Python、Lua 和 Shell 脚本，可以自动将结果管道到 Nmap 或自定义脚本进行进一步分析。
- **自适应学习**：根据使用环境和习惯自动优化扫描参数。
- **广泛支持**：支持 IPv6、CIDR 范围、文件输入等。
- **自动集成**：可以无缝地将开放端口管道到 Nmap 进行详细扫描。

## 安装方法

### 使用包管理器

RustScan 在多个包管理器中可用：

- **macOS**：`brew install rustscan`
- **Arch Linux**：`yay rustscan`
- 其他系统请查看 [Repology](https://repology.org/project/rustscan/versions) 以获取更多安装选项。

### 从源码编译

如果您的系统没有预编译包，可以使用 Cargo 安装：

```bash
cargo install rustscan
```

### 下载二进制文件

从 [GitHub Releases](https://github.com/RustScan/RustScan/releases) 下载最新版本的二进制文件。

## 基本用法

### 简单扫描

扫描单个主机：

```bash
rustscan 192.168.1.1
```

### 扫描端口范围

```bash
rustscan 192.168.1.1 --ports 1-1000
```

### 扫描 CIDR 范围

```bash
rustscan 192.168.1.0/24
```

### 与 Nmap 集成

RustScan 可以自动将发现的开放端口传递给 Nmap 进行详细扫描：

```bash
rustscan 192.168.1.1 -- -A -sV
```

### 使用脚本

运行自定义脚本处理结果：

```bash
rustscan 192.168.1.1 --scripts python my_script.py
```

## 配置

RustScan 支持配置文件，可以在 `~/.rustscan.toml` 或项目根目录的 `config.toml` 中自定义设置。更多配置选项请参考 [官方文档](https://github.com/RustScan/RustScan/wiki/Config-File)。

## 注意事项

- RustScan 专注于快速端口发现，不进行详细的服务指纹识别。
- 对于需要详细扫描的情况，建议结合 Nmap 使用。
- 该工具主要用于渗透测试和安全审计，请确保在授权范围内使用。

## 链接

- [GitHub 仓库](https://github.com/bee-san/RustScan)
- [官方文档](https://github.com/bee-san/RustScan/wiki)
- [Discord 社区](http://discord.skerritt.blog)
