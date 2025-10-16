
---
title: moby
---

# Moby 项目（Docker）

## 项目地址
[GitHub 项目地址](https://github.com/moby/moby)

## 主要特性
Moby 项目是一个开源的容器化平台，主要用于构建、运行和管理容器化应用程序。它是 Docker 的核心引擎，提供容器技术的核心功能，包括：
- **容器化支持**：允许将应用程序及其依赖打包成轻量级、可移植的容器，实现“一次构建，到处运行”。
- **镜像管理**：支持创建、拉取、推送和管理 Docker 镜像，使用分层文件系统来优化存储和传输。
- **网络和存储**：内置网络驱动（如 bridge、overlay）和卷管理，支持多容器通信和持久化数据存储。
- **插件系统**：可扩展的架构，支持添加自定义网络、存储和授权插件。
- **安全性**：集成用户命名空间、内容信任和秘密管理，提升容器运行的安全性。
- **跨平台**：支持 Linux、Windows 和 macOS 等多种操作系统。

## 主要功能
- **容器生命周期管理**：创建、启动、停止、重启和删除容器，支持资源限制（如 CPU、内存）。
- **镜像构建**：使用 Dockerfile 定义镜像，支持多阶段构建和缓存机制。
- **编排集成**：作为 Docker Engine 的基础，与 Docker Compose、Swarm 和 Kubernetes 等工具无缝集成。
- **日志和监控**：提供容器日志收集和健康检查功能，便于调试和运维。
- **CLI 接口**：通过 Docker CLI 命令行工具交互，支持脚本化和自动化操作。

## 用法
1. **安装**：从 GitHub 仓库克隆代码，构建 Docker Engine。官方推荐使用 Docker Desktop 或直接安装预构建二进制文件。
   - 示例：`git clone https://github.com/moby/moby.git`
   - 构建：`make binary`

2. **基本命令**：
   - 拉取镜像：`docker pull nginx`
   - 运行容器：`docker run -d -p 80:80 nginx`（后台运行 Nginx 容器，映射端口 80）
   - 构建镜像：使用 Dockerfile 执行 `docker build -t myapp .`
   - 查看容器：`docker ps` 或 `docker images`

3. **高级用法**：
   - 配置 Docker Daemon：编辑 `/etc/docker/daemon.json` 以自定义网络、存储等。
   - 开发贡献：仓库使用 Go 语言编写，支持通过 `make` 命令进行测试和构建。
   - 文档参考：项目 README 和官方 Docker 文档提供详细指南。

更多细节请查看项目仓库的文档和示例。