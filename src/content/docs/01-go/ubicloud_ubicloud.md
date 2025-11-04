
---
title: ubicloud
---


# ubicloud

> **项目地址**  
> https://github.com/ubicloud/ubicloud

## 主要特性

- **多租户云存储** – 为每位用户提供隔离的存储空间，支持对象存储、文件同步等方式。  
- **安全认证** – 内置 OAuth2、LDAP 等多种身份验证机制，支持自定义权限策略。  
- **RESTful API** – 提供统一的 API 接口，方便外部应用集成与自动化操作。  
- **Web UI** – 友好的 Web 控制台，用户可通过浏览器完成文件上传、下载、分享等操作。  
- **多后端支持** – 内置 S3、MinIO、FileSystem、Glacier 等后端，按需切换。  
- **备份与恢复** – 支持按时间点、标签等方式的快速备份与恢复。  
- **自动扩容** – 与 Kubernetes 集成，可根据负载自动水平扩容。  
- **日志审计** – 所有操作都有详细的审计日志，满足合规要求。  

## 核心模块

| 模块 | 作用 |
|------|------|
| `api` | 提供 REST API 与 Swagger 文档 |
| `cli` | 命令行工具，支持批量文件管理与配置 |
| `web` | 前端 UI，基于 React + Ant Design |
| `storage` | 后端接口层，支持多种存储实现 |
| `auth` | 统一身份认证、授权模块 |
| `watcher` | 监听文件变化并同步至后端 |

## 快速使用

### 1. 环境准备

```bash
# 必须安装 Docker 与 docker‑compose
# 可选：安装 Go 1.22+，用于构建 CLI
```

### 2. 本地启动

```bash
git clone https://github.com/ubicloud/ubicloud.git
cd ubicloud

# 启动所有服务
docker compose up -d
```

访问 `http://localhost:8080` 即可看到 Web UI，默认管理员账号为 `admin@ubicloud.com`，密码 `admin`.

### 3. CLI 操作

```bash
# 安装
go install ./cmd/ubicloud

# 登录
ubicloud login http://localhost:8080/api/v1/auth/login -u admin@ubicloud.com -p admin

# 上传文件
ubicloud upload ~/test.txt

# 下载文件
ubicloud download 12345 -o ./downloaded.txt

# 删除文件
ubicloud delete 12345
```

### 4. 自定义后端

编辑 `config.yaml`，选择不同的后端：

```yaml
storage:
  type: s3
  endpoint: "https://s3.amazonaws.com"
  bucket:  "my-ubicloud"
  access_key:  <AK>
  secret_key:  <SK>
```

随后重启服务即可生效。

### 5. 部署到 Kubernetes

```yaml
# ubicloud-values.yaml
app Count: 3
image:
  repository: ubicloud/ubicloud
  tag: latest
```

```bash
helm repo add ubicloud https://charts.ubicloud.com
helm upgrade --install ubicloud ubicloud/ubicloud -f ubicloud-values.yaml
```

## 文档

- API 文档：访问 `/api/v1/openapi.json` 或 UI 的 Swagger 页面  
- CLI 使用手册：`ubicloud --help`  
- 详细部署说明：请查看 `docs/` 目录

> 如需进一步帮助，请参考官方文档或提交 issue 至 GitHub。  
