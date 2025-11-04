
---
title: eShop
---


# eShop (dotnet)

**GitHub 地址**: https://github.com/dotnet/eShop

## 概述  
eShop 是微软官方开源示例项目，演示了在 ASP.NET Core + Docker + 微服务架构下构建云原生电子商务应用的完整实践。项目以一套完整的业务场景为核心，展示了微服务拆分、通信、治理、CI/CD、监控等关键技术。

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

| 模块 | 主要职责 |
|------|----------|
| **Identity** | 用户认证与授权 |
| **Catalog** | 商品目录、库存 |
| **Basket** | 购物车功能 |
| **Ordering** | 订单创建、支付、发票 |
| **Payment** | 支付处理（模拟） |
| **Messages** | 同步与异步消息共享 |
| **API Gateway** | 用于统一入口（Ocelot） |
| **Web Client** | ASP.NET Core MVC 前端 |

## 使用方法

1. **克隆项目**  
   ```bash
   git clone https://github.com/dotnet/eShop.git
   cd eShop/src
   ```

2. **Docker Compose（本地开发）**  
   ```bash
   docker-compose up -d
   ```
   - 启动后访问 **https://localhost:5000**（Web）或 **https://localhost:5100**（API Gateway）。

3. **Kubernetes（生产环境）**  
   ```bash
   kubectl apply -f k8s/namespace.yaml
   kubectl apply -f k8s/service.yaml
   ```
   - 具体 YAML 文件已提供，配合 Helm Chart 部署更方便。

4. **本地调试**  
   - 通过 Visual Studio / VS Code 开启对应服务打断点即可。

5. **构建与发布**  
   ```bash
   dotnet build
   dotnet test
   ```

6. **CI/CD**  
   - GitHub Actions 自动构建镜像并推送到 Docker Registry。  
   - 可自定义 `docker-registry` 与 `helm repo`。

## 关键文件与目录

- `src/Services/Identity` – 身份服务
- `src/Services/Catalog` – 商品目录
- `src/Services/Ordering` – 订单服务
- `src/Web` – 前端页面
- `docker-compose.yaml` – 本地 Docker 方案
- `k8s/` – Kubernetes YAML
- `ci/` – CI 脚本与 GitHub Actions

> 仅供学习参考，真实项目建议按业务需求自行拆分与扩展。