---
title: compose
---

# Docker Compose

Docker Compose 是一个用于在 Docker 上运行多容器应用程序的工具，使用 [Compose 文件格式](https://compose-spec.io) 定义。一个 Compose 文件用于定义组成应用程序的一个或多个容器的配置。一旦有了 Compose 文件，就可以使用单个命令创建和启动应用程序：`docker compose up`。

## 功能

- 定义和运行多容器应用程序
- 使用 YAML 文件配置服务、网络和卷
- 支持构建、启动、停止和扩展容器
- 与 Docker Swarm 兼容（但有一些限制）

## 用法

### 安装

#### Windows 和 macOS

Docker Compose 包含在 [Docker Desktop](https://www.docker.com/products/docker-desktop/) 中。

#### Linux

从 [发布页面](https://github.com/docker/compose/releases) 下载 Docker Compose 二进制文件。

将相关二进制文件重命名为 `docker-compose` 并复制到 `$HOME/.docker/cli-plugins`，或者复制到以下文件夹之一进行系统范围安装：

- `/usr/local/lib/docker/cli-plugins` 或 `/usr/local/libexec/docker/cli-plugins`
- `/usr/lib/docker/cli-plugins` 或 `/usr/libexec/docker/cli-plugins`

（可能需要使用 `chmod +x` 使下载的文件可执行）

### 快速开始

使用 Docker Compose 是一个三步过程：

1. 使用 `Dockerfile` 定义应用程序的环境，以便可以在任何地方重现。
2. 在 `compose.yaml` 中定义组成应用程序的服务，以便它们可以在隔离环境中一起运行。
3. 最后，运行 `docker compose up`，Compose 将启动并运行整个应用程序。

一个 Compose 文件看起来像这样：

```yaml
services:
  web:
    build: .
    ports:
      - '5000:5000'
    volumes:
      - .:/code
  redis:
    image: redis
```

运行 `docker compose up` 来启动应用程序。
