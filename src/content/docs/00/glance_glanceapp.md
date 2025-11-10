---
title: glance
---

# Glance

## 项目简介

Glance 是一个轻量级、高度可定制的自托管仪表板，用于在一个美观、简洁的界面中显示您的所有 feed。

## 主要功能

### 多种小部件

- RSS feeds
- Subreddit posts
- Hacker News posts
- 天气预报
- YouTube 频道上传
- Twitch 频道
- 市场价格
- Docker 容器状态
- 服务器统计
- 自定义小部件
- 以及更多...

### 快速且轻量

- 低内存使用
- 少量依赖
- 最小化原生 JS
- 单个 <20MB 二进制文件，支持多种 OS 和架构，以及同样小的 Docker 容器
- 未缓存页面通常在 ~1s 内加载（取决于互联网速度和小部件数量）

### 高度可定制

- 不同布局
- 任意数量的页面/标签
- 每个小部件的众多配置选项
- 某些小部件的多种样式
- 自定义 CSS

### 移动设备优化

因为您会想在外出时使用它。

### 可主题化

通过调整几个数字轻松创建自己的主题，或从[已可用主题](/glanceapp/glance/blob/main/docs/themes.md)中选择。

## 使用方法

### 安装

选择以下方法之一：

#### Docker Compose 使用提供的目录结构（推荐）

创建一个名为 `glance` 的新目录，并在其中创建模板文件：

```bash
mkdir glance && cd glance && curl -sL https://github.com/glanceapp/docker-compose-template/archive/refs/heads/main.tar.gz | tar -xzf - --strip-components 2
```

然后，根据需要编辑以下文件：

- `docker-compose.yml`：配置端口、卷和其他容器相关内容
- `config/home.yml`：配置主页的小部件或布局
- `config/glance.yml`：如果要更改主题或添加更多页面

准备就绪后，运行：

```bash
docker compose up -d
```

#### Docker Compose 手动

创建一个 `docker-compose.yml` 文件，内容如下：

```yaml
services:
  glance:
    container_name: glance
    image: glanceapp/glance
    restart: unless-stopped
    volumes:
      - ./config:/app/config
    ports:
      - 8080:8080
```

然后，创建一个名为 `config` 的新目录，并下载示例起始 `glance.yml` 文件：

```bash
mkdir config && wget -O config/glance.yml https://raw.githubusercontent.com/glanceapp/glance/refs/heads/main/docs/glance.yml
```

随意编辑 `glance.yml` 文件，然后运行：

```bash
docker compose up -d
```

#### 手动二进制安装

预编译二进制文件适用于 Linux、Windows 和 macOS（x86、x86_64、ARM 和 ARM64 架构）。

对于 Linux，访问[最新发布页面](https://github.com/glanceapp/glance/releases/latest)获取可用二进制文件。您可以将二进制文件放在 `/opt/glance/` 中，并通过 [systemd 服务](https://linuxhandbook.com/create-systemd-services/)让它随服务器启动。默认情况下，运行二进制文件时，它会在放置目录中查找 `glance.yml` 文件。要指定不同的配置文件路径，使用 `--config` 选项：

```bash
/opt/glance/glance --config /etc/glance.yml
```

### 配置

配置通过 YAML 文件完成。要了解布局如何工作、如何添加更多页面以及如何配置小部件，请访问[配置文档](/glanceapp/glance/blob/main/docs/configuration.md#configuring-glance)。

## 常见问题

- **请求超时**：最常见原因是使用 Pi-Hole、AdGuard Home 或其他广告拦截 DNS 服务，默认速率限制较低。根据单个页面中的小部件数量，很容易超过此限制。要修复，请在 DNS 服务设置中增加速率限制。
- **市场、书签或其他小部件布局损坏**：这几乎总是由浏览器扩展 Dark Reader 引起。要修复，请为 Glance 托管的域禁用暗模式。

## 构建

从源代码构建：

#### 使用 Go 构建二进制文件

要求：[Go](https://go.dev/dl/) >= v1.23

要为当前 OS 和架构构建项目，运行：

```bash
go build -o build/glance .
```

要为特定 OS 和架构构建，运行：

```bash
GOOS=linux GOARCH=amd64 go build -o build/glance .
```

或者，如果您只想运行应用而不创建二进制文件，例如测试更改时，可以运行：

```bash
go run .
```

#### 使用 Docker 构建项目和 Docker 镜像

要求：[Docker](https://docs.docker.com/engine/install/)

仅使用 Docker 构建项目和镜像，运行：

（将 `owner` 替换为您的姓名或组织）

```bash
docker build -t owner/glance:latest .
```

如果希望将镜像推送到注册表（默认 Docker Hub），运行：

```bash
docker push owner/glance:latest
```
