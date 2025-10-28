
---
title: pottery
---

# Pottery 项目

## 项目地址
[GitHub 项目地址](https://github.com/brainix/pottery)

## 主要特性
Pottery 是一个开源的命令行工具，专注于简化本地开发环境的管理。它采用 Docker 容器化技术，提供轻量级、隔离的开发环境，支持多种编程语言和框架。主要特性包括：
- **容器化开发环境**：使用 Docker 快速启动预配置的开发容器，避免本地环境依赖冲突。
- **多语言支持**：内置支持 Python、Node.js、Java 等常见语言的模板，便于快速搭建项目。
- **热重载与调试**：集成实时文件同步和调试工具，提升开发效率。
- **资源管理**：自动管理容器资源占用，支持自定义配置以优化性能。
- **跨平台兼容**：适用于 Linux、macOS 和 Windows 系统，无需复杂安装。

## 主要功能
- **环境初始化**：通过简单命令创建和管理开发环境，例如启动 Web 服务器或数据库实例。
- **项目模板**：提供现成模板，如 Flask/Django for Python、Express for Node.js，帮助用户快速启动项目。
- **端口管理和代理**：自动处理端口映射和反向代理，便于本地测试和部署预览。
- **日志与监控**：实时查看容器日志，支持性能监控和错误调试。
- **扩展性**：支持插件系统，用户可自定义 Dockerfile 或脚本扩展功能。

## 用法
1. **安装**：
   - 确保已安装 Docker 和 Git。
   - 克隆仓库：`git clone https://github.com/brainix/pottery.git`
   - 进入目录并安装依赖：`cd pottery && pip install -r requirements.txt`（或根据 README 指示）。

2. **基本命令**：
   - 初始化项目：`pottery init --template python-flask`（选择模板启动环境）。
   - 启动容器：`pottery up`（运行开发服务器，通常在 localhost:8000）。
   - 停止环境：`pottery down`（清理容器和资源）。
   - 查看日志：`pottery logs`（监控输出）。

3. **自定义配置**：
   - 编辑 `pottery.yml` 文件，修改端口、卷挂载或环境变量。
   - 示例：为 Node.js 项目添加自定义脚本，通过 `pottery run npm install` 执行命令。

详细用法请参考项目 README 文件。