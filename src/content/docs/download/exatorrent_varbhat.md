---
title: exatorrent
---

# ExaTorrent 项目描述

## 项目地址
[https://github.com/varbhat/exatorrent](https://github.com/varbhat/exatorrent)

## 主要特性
ExaTorrent 是一个现代化的 BitTorrent 客户端，专注于高效、简洁的用户体验和资源管理。其核心特性包括：
- **流式下载支持**：允许边下载边播放媒体文件，无需等待完整下载。
- **Web 界面**：提供直观的浏览器-based 界面，支持远程管理和监控。
- **轻量级设计**：基于 Go 语言开发，资源占用低，适合服务器或低配置设备运行。
- **多协议支持**：兼容标准 BitTorrent 协议，包括 uTP（微传输协议）以优化网络性能。
- **种子管理和搜索**：内置种子管理器，支持 RSS 订阅和简单搜索集成。
- **跨平台兼容**：可在 Linux、Windows 和 macOS 上运行，支持 Docker 部署。

## 主要功能
- **下载管理**：添加 Torrent 文件或磁力链接，实时监控下载进度、速度和种子健康度。
- **文件选择**：下载前可选择特定文件，避免不必要的下载。
- **速度控制**：自定义上传/下载限速，防止网络拥塞。
- **API 接口**：提供 RESTful API，便于与其他工具集成，如自动化脚本或第三方应用。
- **安全特性**：支持 IP 过滤和加密连接，增强隐私保护。
- **通知系统**：下载完成后通过 Web 界面或 API 发送通知。

## 用法
1. **安装**：
   - 从 GitHub Releases 下载预编译二进制文件，或使用 Go 构建：`go install github.com/varbhat/exatorrent/cmd/exatorrent@latest`。
   - 对于 Docker：运行 `docker run -d -p 3000:3000 -v /path/to/downloads:/downloads varbhat/exatorrent`。

2. **启动**：
   - 运行 `./exatorrent`（或 Docker 容器），默认监听端口 3000。
   - 访问 `http://localhost:3000` 打开 Web 界面。

3. **使用步骤**：
   - 在 Web 界面点击“添加 Torrent”，上传 .torrent 文件或粘贴磁力链接。
   - 选择下载目录和文件，点击开始下载。
   - 通过仪表盘监控进度，支持暂停/恢复和删除任务。
   - 配置设置：进入“设置”页面调整限速、端口等参数。

更多详情请参考项目 README。