---
title: cli
---


# Docker CLI 项目介绍

**GitHub 地址**: https://github.com/docker/cli

## 1. 项目概述
Docker CLI 是 Docker 官方提供的命令行工具，负责与 Docker Engine 进行交互。通过统一的 `docker` 命令行，用户可以管理容器、镜像、网络、卷等 Docker 资源，并执行高层次应用部署与管理任务。

## 2. 主要特性
- **统一命令体系**：所有 Docker 操作均通过 `docker <command>` 形式调用，支持子命令层级组织。
- **跨平台支持**：在 Linux、macOS、Windows 等主流操作系统上运行。
- **插件化扩展**：可以通过 Docker 插件机制添加自定义命令与功能。
- **本地与远程访问**：支持本地 Docker Engine 以及通过 Docker API 的远程服务器。

## 3. 核心功能
| 领域 | 具体子命令 | 主要用途 |
|------|------------|----------|
| 容器管理 | `run`, `ps`, `stop`, `rm`, `exec`, `logs` | 创建、列举、停止、删除、执行命令、查看日志 |
| 镜像管理 | `build`, `pull`, `push`, `images`, `rmi` | 构建、拉取、推送、列表、删除镜像 |
| 网络管理 | `network`, `network ls`, `network create`, `network rm` | 创建、列表、删除网络 |
| 卷管理 | `volume`, `volume ls`, `volume create`, `volume rm` | 创建、列举、删除数据卷 |
| 配置管理 | `config`, `config ls`, `config create`, `config rm` | 存储与管理配置对象 |
| 插件管理 | `plugin`, `plugin ls`, `plugin enable`, `plugin disable` | 管理 Docker 插件 |
| 调试与日志 | `info`, `version`, `debug`, `events` | 获取系统信息、版本、调试日志、事件流 |

## 4. 基本用法
```bash
# 查看帮助
docker --help

# 运行容器
docker run -d --name my_nginx nginx:latest

# 查看正在运行的容器
docker ps

# 查看所有容器（包含已停止）
docker ps -a

# 拉取镜像
docker pull redis:6

# 构建镜像
docker build -t myapp:1.0 .

# 进入容器交互式终端
docker exec -it my_nginx bash

# 查看容器日志
docker logs my_nginx

# 停止容器
docker stop my_nginx

# 删除容器
docker rm my_nginx

# 删除镜像
docker rmi myapp:1.0
```

> **小技巧**  
> - 使用 `docker compose` 可以通过 `docker compose up -d` 快速部署多容器应用（位于同一工作区的 `docker-compose.yml`）。  
> - 所有命令均支持 `--help` 查看详细参数，例如 `docker run --help`。

## 5. 进一步阅读
- Docker CLI 官方文档: https://docs.docker.com/engine/reference/commandline/docker/
- GitHub 仓库: https://github.com/docker/cli

**文件路径**：`src/content/docs/00/cli_docker.md`
