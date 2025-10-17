
---
title: KubePi
---

# KubePi 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/KubeOperator/KubePi)

## 主要特性
KubePi 是一个基于 Kubernetes 的轻量级 API 网关和控制平面解决方案，主要用于简化 Kubernetes 集群的管理和访问控制。其核心特性包括：
- **API 网关功能**：提供统一的入口点，支持 API 路由、负载均衡和安全认证，方便外部系统访问 Kubernetes 资源。
- **权限管理**：集成 RBAC（Role-Based Access Control），允许细粒度控制用户对 Kubernetes 资源的访问权限，支持多租户隔离。
- **轻量级设计**：无需复杂的部署，支持单二进制运行，资源占用低，适合小型到中型 Kubernetes 集群。
- **插件化扩展**：支持自定义插件和扩展机制，便于集成第三方服务如监控、日志等。
- **高可用性**：支持集群模式部署，确保服务的高可用和故障恢复。

## 主要功能
KubePi 的功能聚焦于 Kubernetes 的管理简化，具体包括：
- **集群管理**：通过 Web UI 或 API 管理多个 Kubernetes 集群，支持集群注册、监控和健康检查。
- **用户认证与授权**：集成 OAuth2、LDAP 等认证方式，实现用户登录和权限分配。
- **资源代理**：代理 Kubernetes API 请求，支持 WebSocket 和 HTTP 协议，确保安全代理访问 Pod、Service 等资源。
- **审计日志**：记录 API 调用日志，便于安全审计和问题排查。
- **Dashboard 支持**：内置简易 Dashboard，提供可视化界面查看集群状态和资源使用情况。

## 用法
### 安装部署
1. **前提条件**：确保有 Kubernetes 集群（版本 1.16+），并安装 Go 1.16+ 用于构建。
2. **从源代码构建**：
   - 克隆仓库：`git clone https://github.com/KubeOperator/KubePi.git`
   - 进入目录：`cd KubePi`
   - 构建：`make build`
3. **Docker 部署**：
   - 拉取镜像：`docker pull kubeoperator/kubepi:latest`
   - 运行容器：`docker run -d -p 8080:8080 kubeoperator/kubepi`
4. **Kubernetes 部署**：
   - 使用 Helm：添加 Helm 仓库 `helm repo add kubepi https://charts.kubeoperator.io`，然后 `helm install kubepi kubepi/kubepi`。
   - 或直接应用 YAML 文件：`kubectl apply -f deploy/kubernetes/manifests/`。

### 配置与使用
1. **基本配置**：编辑 `config.yaml` 文件，设置 Kubernetes API 服务器地址、认证方式和端口（默认 8080）。
2. **启动服务**：运行 `./kubepi server --config config.yaml`。
3. **访问 Dashboard**：浏览器打开 `http://localhost:8080`，使用配置的凭证登录。
4. **API 使用**：通过代理 API 调用 Kubernetes 资源，例如 `curl -H "Authorization: Bearer <token>" http://localhost:8080/api/v1/namespaces`。
5. **权限设置**：在 Dashboard 中创建用户和角色，分配 RBAC 策略。
6. **扩展**：开发插件时，实现接口并注册到 KubePi 中，重启服务生效。

更多细节请参考项目文档中的 [README](https://github.com/KubeOperator/KubePi/blob/main/README.md) 和 [API 文档](https://github.com/KubeOperator/KubePi/tree/main/docs)。