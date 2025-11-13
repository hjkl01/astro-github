---
title: traefik
---

## 功能介绍

Traefik（发音为traffic）是一个现代的HTTP反向代理和负载均衡器，旨在简化微服务的部署。它能够与现有的基础设施组件（如Docker、Swarm模式、Kubernetes、Consul、Etcd、Rancher v2、Amazon ECS等）无缝集成，并自动动态配置路由。通过指向你的编排器API，Traefik可以即时生成路由，将微服务连接到外部世界，无需手动干预。

### 主要特性

- **动态配置更新**：无需重启即可持续更新配置。
- **负载均衡**：支持多种负载均衡算法。
- **HTTPS支持**：通过Let's Encrypt自动获取证书，包括通配符证书。
- **可靠性**：内置断路器和重试机制。
- **监控界面**：提供简洁的Web UI用于查看配置和状态。
- **协议支持**：支持WebSocket、HTTP/2和gRPC。
- **指标和日志**：提供多种指标输出（如Prometheus、Datadog、Statsd、InfluxDB 2.X）和访问日志（JSON、CLF格式）。
- **性能**：快速且高效。
- **API**：暴露REST API用于管理。
- **部署简单**：打包为单个二进制文件，并提供官方Docker镜像。

### 支持的后端

- Docker / Swarm模式
- Kubernetes
- Amazon ECS
- 文件配置

## 用法

### 快速开始

要开始使用Traefik，可以参考官方文档的[5分钟快速开始指南](https://doc.traefik.io/traefik/getting-started/quick-start/)，需要Docker环境。

### 下载和安装

- **二进制文件**：从[GitHub Releases](https://github.com/traefik/traefik/releases)下载最新版本，并使用示例配置文件运行：
  ```
  ./traefik --configFile=traefik.toml
  ```
- **Docker镜像**：使用官方Docker镜像运行：
  ```
  docker run -d -p 8080:8080 -p 80:80 -v $PWD/traefik.toml:/etc/traefik/traefik.toml traefik
  ```
- **源码安装**：克隆仓库并构建：
  ```
  git clone https://github.com/traefik/traefik
  ```

### Web UI

Traefik提供了一个简单的HTML Web UI，可以通过浏览器访问，用于查看路由、后端和服务状态。

### 文档

完整文档请访问：[https://doc.traefik.io/traefik/](https://doc.traefik.io/traefik/)

### 支持

- 社区支持：加入[Traefik社区论坛](https://community.traefik.io/)
- 商业支持：联系[support@traefik.io](mailto:support@traefik.io)
