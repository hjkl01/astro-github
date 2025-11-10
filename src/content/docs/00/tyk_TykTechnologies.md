---
title: tyk
---

# Tyk API Gateway

## 功能介绍

Tyk Gateway 是云原生、开源、企业级的 API 网关，支持 REST、GraphQL、TCP 和 gRPC 协议。自 2014 年以来，它被认为是地球上最快的 API 网关。

Tyk Gateway 提供"电池包含"的功能，没有功能锁定。使您的组织能够轻松地进行速率限制、认证、收集分析、应用微服务模式等。

Tyk 原生运行在 Kubernetes 上，如果您喜欢，可以使用 Tyk Kubernetes Operator。

### 主要功能

- **支持多种协议**：REST、SOAP、GraphQL、gRPC 和 TCP。
- **行业标准认证**：OIDC、JWT、Bearer Tokens、Basic Auth、Client Certificates 等。
- **Open API 标准**：导入 Swagger 和 OpenAPI 文档（OAS 2.X 和 OAS 3.0.1）来搭建 API。
- **超高性能**：低延迟，使用单个 CPU 即可处理数千 RPS，水平和垂直可扩展。
- **内容调解**：转换请求或响应头，从 SOAP 转换为 GraphQL 等。
- **可扩展插件架构**：通过用您选择的语言编写插件来自定义 Tyk 的中间件链 - 从 Python 到 JavaScript 到 Go，或任何支持 gRPC 的语言。
- **速率限制和配额**：保护上游免受过载，并为每个消费者应用限制。
- **API 版本控制**：轻松设置和停用 API 版本。
- **细粒度访问控制**：基于版本和操作授予对一个或多个 API 的访问。
- **黑名单/白名单/忽略端点访问**：对您的访问点强制执行严格的安全模型。
- **分析日志**：记录谁在使用您的 API 的详细使用数据（仅原始数据）。
- **CORS**：为某些 API 启用 CORS，以便用户进行基于浏览器的请求。
- **Webhooks**：针对配额违规和认证失败等事件触发 webhooks。
- **IP 白名单**：阻止非受信任 IP 地址的访问以进行更安全的交互。
- **无击重载**：动态更改 Tyk 配置并重新启动服务，而不影响任何活动请求。
- **Kubernetes 原生**：使用开源 Tyk Operator 进行声明式 API。

## 用法

### 快速开始

我们推荐使用 Tyk Gateway Docker 作为现在开始的最快方式。后来，您可以移动到我们其他支持的分发方式之一。

#### 步骤 1 - 克隆 docker-compose 仓库

```bash
git clone https://github.com/TykTechnologies/tyk-gateway-docker
```

#### 步骤 2 - 更改到新目录

```bash
cd tyk-gateway-docker
```

#### 步骤 3 - 部署 Tyk Gateway 和 Redis

```bash
docker-compose up
```

您可以使用 `-d` 标志在分离模式下运行：`docker-compose up -d`

**恭喜，您完成了！**

您的 Tyk Gateway 现在已配置并准备使用。通过检查"hello"端点来确认：

```bash
curl localhost:8080/hello
```

输出：

```json
{ "status": "pass", "version": "v3.2.1", "description": "Tyk GW" }
```

接下来，访问[添加您的第一个 API](https://tyk.io/docs/getting-started/create-api/)到 Tyk 并遵循开源说明。

### 其他安装方式

1. [Docker](https://tyk.io/docs/tyk-oss/ce-docker/)
2. [Kubernetes-Native](https://github.com/TykTechnologies/tyk-oss-k8s-deployment)
3. [Kubernetes-Helm](https://github.com/TykTechnologies/tyk-helm-chart#install-tyk-community-edition)
4. [Ansible](https://tyk.io/docs/tyk-oss/ce-ansible/)
5. [Red Hat](https://tyk.io/docs/tyk-oss/ce-redhat/)
6. [Ubuntu](https://tyk.io/docs/tyk-oss/ce-ubuntu/)
7. [CentOS](https://tyk.io/docs/tyk-oss/ce-centos/)
8. [从源码编译 Tyk Gateway](#compiling-tyk-gateway)

### 从源码编译

```bash
git clone https://github.com/TykTechnologies/tyk
go build
```

需要 Go 版本 1.22 来构建 `master`，当前开发版本。Tyk 正式支持 `Linux/amd64`、`Linux/i386` 和 `Linux/arm64`。

要在本地运行测试，请使用以下命令：

```bash
go test ./...
```

注意，测试需要在同一台机器上运行 Redis（默认端口）。

要编写自己的测试，请使用此指南：https://github.com/TykTechnologies/tyk/blob/master/TESTING.md
