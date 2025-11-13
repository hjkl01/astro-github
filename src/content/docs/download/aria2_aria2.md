---
title: aria2
---

# aria2 项目

**GitHub 项目地址:** [https://github.com/aria2/aria2](https://github.com/aria2/aria2)

## 主要特性
aria2 是一个轻量级、多协议的命令行下载工具，支持 HTTP/HTTPS、FTP、BitTorrent (BT) 和 Metalink 等多种协议。它具有高效的下载性能、多源并发下载和断点续传功能，适用于各种下载场景。核心特性包括：
- **多协议支持**：兼容 HTTP、HTTPS、FTP、SFTP、BitTorrent 和 Metalink。
- **并发下载**：支持多连接和多文件同时下载，提高下载速度。
- **断点续传**：即使下载中断，也能从断点处继续。
- **跨平台**：支持 Linux、Windows、macOS 等操作系统。
- **轻量高效**：无图形界面，资源占用低，适合服务器和脚本自动化使用。
- **插件扩展**：可通过 RPC 接口集成到其他工具，如下载管理器或 Web UI。

## 主要功能
- **单文件下载**：快速下载单个文件，支持限速和代理设置。
- **批量下载**：处理多个 URL 或种子文件，实现并行下载。
- **种子下载**：支持 BT 种子和磁力链接，自动选择 tracker 和 peer。
- **Metalink 支持**：使用 Metalink 文件优化多源下载，选择最佳镜像。
- **RPC 接口**：提供 JSON-RPC 服务，便于远程控制和集成（如与 aria-ng 等前端结合）。
- **自定义配置**：通过配置文件或命令行参数调整下载行为，包括文件过滤、目录结构等。

## 用法
aria2 的基本用法通过命令行执行。首先，确保已安装 aria2（可通过包管理器如 apt、brew 或从 GitHub 编译安装）。

### 基本命令示例
1. **简单下载单个文件**：
   ```
   aria2c https://example.com/file.zip
   ```
   这将下载文件到当前目录。

2. **多 URL 并发下载**：
   ```
   aria2c -x 16 -s 16 https://example.com/file1.zip https://example.com/file2.zip
   ```
   `-x 16` 表示每个 URL 最多 16 个连接，`-s 16` 表示每个文件分割成 16 部分并发下载。

3. **下载 BitTorrent 种子**：
   ```
   aria2c --seed-time=0 torrent_file.torrent
   ```
   `--seed-time=0` 表示下载完成后不做种。

4. **使用配置文件**：
   创建 `aria2.conf` 文件，内容示例：
   ```
   dir=/downloads
   max-concurrent-downloads=5
   split=16
   max-connection-per-server=16
   enable-rpc=true
   rpc-listen-all=true
   ```
   然后运行：
   ```
   aria2c --conf-path=aria2.conf
   ```

5. **启用 RPC 模式**（用于 Web 界面控制）：
   ```
   aria2c --enable-rpc --rpc-listen-all=true
   ```
   然后可通过工具如 aria-ng 连接 localhost:6800/jsonrpc 进行管理。

更多高级用法请参考官方文档：https://aria2.github.io/manual/en/html/。建议在实际使用前查看完整参数列表以优化配置。