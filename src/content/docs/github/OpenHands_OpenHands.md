---
title: OpenHands
---

# OpenHands

OpenHands（前身为OpenDevin）是一个由AI驱动的软件开发代理平台。它允许AI代理执行人类开发者所能做的任何任务，包括修改代码、运行命令、浏览网页、调用API，甚至从StackOverflow复制代码片段。

## 功能特性

- **代码修改**：AI代理可以直接编辑和修改代码文件
- **命令执行**：在沙盒环境中运行终端命令
- **网页浏览**：访问互联网获取信息和资源
- **API调用**：与外部服务进行交互
- **多语言支持**：支持多种编程语言和框架
- **沙盒环境**：安全的隔离执行环境

## 使用方法

### 在线使用（推荐）

访问 [OpenHands Cloud](https://app.all-hands.dev) 开始使用，新用户可获得10美元免费积分。

### 本地运行

#### 选项1：CLI Launcher（推荐）

使用 uv 安装和运行：

```bash
# 安装 uv（如果尚未安装）
# 参考：https://docs.astral.sh/uv/getting-started/installation/

# 启动GUI服务器
uvx --python 3.12 openhands serve

# 或启动CLI
uvx --python 3.12 openhands
```

访问 http://localhost:3000 开始使用。

#### 选项2：Docker

```bash
docker pull docker.openhands.dev/openhands/runtime:0.61-nikolaik

docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.openhands.dev/openhands/runtime:0.61-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands:/.openhands \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.openhands.dev/openhands/openhands:0.61
```

### 配置LLM

首次使用时需要配置LLM提供商和API密钥。推荐使用 Anthropic 的 Claude Sonnet 4.5。

更多配置选项请参考[官方文档](https://docs.all-hands.dev)。

## 许可证

采用 MIT 许可证（enterprise/ 文件夹除外）。
