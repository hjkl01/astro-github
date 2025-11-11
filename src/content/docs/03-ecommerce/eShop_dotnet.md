---
title: eShop
---

# eShop (dotnet)

**GitHub 地址**: https://github.com/dotnet/eShop

## 概述

eShop 是微软官方开源示例项目，使用 .NET Aspire 实现基于微服务架构的电子商务网站。项目以一套完整的业务场景为核心，展示了微服务拆分、通信、治理、CI/CD、监控等关键技术。

## 主要特性

- **微服务架构**
  - 业务拆分为独立服务（Catalog, Basket, Ordering, Payment, Identity 等），每个服务可独立部署、扩容。
  - 采用 **gRPC**、**REST**、**Event Sourcing** 等通信方式。

- **容器化与编排**
  - 支持 **Docker Compose**（开发）与 **Kubernetes**（生产）部署。
  - Dockerfile 对所有服务进行容器化，Compose 定义本地网络与数据库。

- **分布式事务与可靠性**
  - 使用 **Saga** 模式实现跨服务事务；采用 **Outbox**、**Bus** 保障消息可靠传递。
  - 通过 RabbitMQ / Azure Service Bus 等消息中间件实现事件驱动。

- **容错与监控**
  - 集成 **Resilience.NET**（重试、熔断）与 **Health Checks**。
  - 打开 Prometheus + Grafana、OpenTelemetry 追踪，用于可观测性。

- **安全与身份认证**
  - **IdentityServer** 提供 OAuth 2.0 / OpenID Connect。
  - Role‑Based Access Control (RBAC) 与 Claims 体系。

- **CI/CD**
  - GitHub Actions 自动构建、测试、发布 Docker 镜像。
  - 随项目自带 Helm chart、Azure DevOps Pipelines 示例。

- **代码质量与开发支持**
  - 采用 **CQRS** 与 **Event Sourcing** 的分层架构。
  - 通过 Cross‑Cutting Concerns（日志、缓存、验证）提升可维护性。

## 功能模块

| 模块            | 主要职责               |
| --------------- | ---------------------- |
| **Identity**    | 用户认证与授权         |
| **Catalog**     | 商品目录、库存         |
| **Basket**      | 购物车功能             |
| **Ordering**    | 订单创建、支付、发票   |
| **Payment**     | 支付处理（模拟）       |
| **Messages**    | 同步与异步消息共享     |
| **API Gateway** | 用于统一入口（Ocelot） |
| **Web Client**  | ASP.NET Core MVC 前端  |

## 使用方法

1. **前提条件**
   - 克隆项目：`git clone https://github.com/dotnet/eShop.git`
   - 安装 .NET 9 SDK 和 Docker Desktop。

2. **运行解决方案**
   - 使用 Visual Studio：打开 `eShop.Web.slnf`，设置 `eShop.AppHost.csproj` 为启动项目，按 Ctrl-F5 启动 Aspire。
   - 或命令行：`dotnet run --project src/eShop.AppHost/eShop.AppHost.csproj`
   - 查看控制台输出中的 Aspire 仪表板 URL（如 http://localhost:19888），登录后访问应用。

3. **Azure OpenAI（可选）**
   - 在 `eShop.AppHost/appsettings.json` 中添加 OpenAI 连接字符串。
   - 在 `Program.cs` 中设置 `useOpenAI = true`。

4. **Azure Developer CLI**
   - 安装 azd：`azd init`，选择 .NET (Aspire)，然后 `azd up` 部署到 Azure。

5. **本地调试与构建**
   - 通过 Visual Studio / VS Code 调试服务。
   - 构建：`dotnet build`，测试：`dotnet test`。

6. **CI/CD**
   - GitHub Actions 自动构建和发布。

## 关键文件与目录

- `src/Services/Identity` – 身份服务
- `src/Services/Catalog` – 商品目录
- `src/Services/Ordering` – 订单服务
- `src/Web` – 前端页面
- `docker-compose.yaml` – 本地 Docker 方案
- `k8s/` – Kubernetes YAML
- `ci/` – CI 脚本与 GitHub Actions

> 仅供学习参考，真实项目建议按业务需求自行拆分与扩展。
