
---
title: oxker
---

# Oxker 项目

**GitHub 项目地址:** [https://github.com/mrjackwills/oxker](https://github.com/mrjackwills/oxker)

## 主要特性
Oxker 是一个开源的命令行工具，专注于简化 Docker 和 Kubernetes 的工作流程。它基于 Go 语言开发，提供轻量级、高效的接口，支持自动化容器管理和编排。主要特性包括：
- **跨平台兼容**：支持 Linux、macOS 和 Windows 系统。
- **集成 Docker 和 Kubernetes**：无缝连接 Docker 容器运行时和 Kubernetes 集群管理。
- **命令简洁**：提供直观的 CLI 命令，减少复杂配置。
- **插件扩展**：支持自定义插件，允许用户扩展功能。
- **资源监控**：内置监控工具，可实时查看容器资源使用情况。

## 主要功能
- **容器管理**：启动、停止、重启 Docker 容器，支持镜像拉取和构建。
- **Kubernetes 部署**：简化 YAML 文件编辑、应用部署和回滚操作。
- **日志查看**：实时尾随容器日志，支持过滤和搜索。
- **网络配置**：管理容器网络、端口映射和服务发现。
- **备份与恢复**：自动化容器数据备份和迁移功能。

## 用法
1. **安装**：
   - 通过 Go 安装：`go install github.com/mrjackwills/oxker@latest`
   - 或从 GitHub Releases 下载预编译二进制文件。

2. **基本命令**：
   - 初始化项目：`oxker init`
   - 启动容器：`oxker run <image-name> [options]`
   - 部署到 Kubernetes：`oxker deploy <yaml-file>`
   - 查看日志：`oxker logs <container-id>`
   - 帮助：`oxker --help`

详细用法请参考项目 README 文件。项目采用 MIT 许可，欢迎贡献代码。