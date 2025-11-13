---
title: csghub-server
---

# csghub-server

## 功能

csghub-server 是 CSGHub 的后端服务器，专注于通过 REST API 管理模型、数据集和其他 LLM 资产。

### 主要功能

- **用户和组织管理**：创建和管理用户及组织。
- **自动标签**：自动标记模型和数据集标签。
- **搜索功能**：搜索用户、组织、模型和数据。
- **在线预览**：在线预览数据集文件，如 `.parquet` 文件。
- **内容审核**：对文本和图像进行内容审核。
- **文件下载**：下载单个文件，包括 LFS 文件。
- **活动跟踪**：跟踪模型和数据集的活动数据，如下载量和点赞量。

## 用法

### 快速开始

系统资源要求：4c CPU / 8GB 内存。

请自行安装 Docker。本项目已在 Ubuntu 22 环境中测试。

通过 docker-compose 快速部署本地化的 CSGHub Server 服务：

```bash
# API token 应至少 128 个字符长，HTTP 请求到 csghub-server 需要将 API token 作为 Bearer token 发送以进行认证
export STARHUB_SERVER_API_TOKEN=<API token>
mkdir -m 777 gitea minio_data
curl -L https://raw.githubusercontent.com/OpenCSGs/csghub-server/main/docker-compose.yml -o docker-compose.yml
docker-compose -f docker-compose.yml up -d
```

### 本地启动 CSGHub Server 服务

CSGHub 支持 TOML 格式的配置文件。在命令行启动任何服务时，可以使用 `--config` 选项指定配置文件：

```bash
go run cmd/csghub-server/main.go start server --config local.toml
go run cmd/csghub-server/main.go deploy runner --config local.toml
```

提供了一个[示例配置文件](https://github.com/OpenCSGs/csghub-server/blob/main/common/config/config.toml.example)，你可以重命名并根据需要修改。所有可用配置都在[此 Go 文件](https://github.com/OpenCSGs/csghub-server/blob/main/common/config/config.go)中定义。TOML 配置使用 snake_case 命名约定，名称自动映射到相应的结构体字段名。

### 技术架构

CSGHub Server 支持不同的 Git 服务器，如 Gitea、GitLab 等。支持灵活配置 LFS 存储系统，可以选择本地或任何兼容 S3 协议的第三方云存储服务。可以按需启用内容审核，并选择任何第三方内容审核服务。

更多信息请访问 [CSGHub 仓库](https://github.com/OpenCSGs/csghub-server)。
