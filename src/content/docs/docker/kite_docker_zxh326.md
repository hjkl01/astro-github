---
title: kite docker
---

# Kite Docker 部署

Kite 是一个现代化的 Kubernetes 仪表板，提供直观的界面来管理和监控 Kubernetes 集群。本页面介绍如何使用 Docker 运行 Kite。

## 功能

Kite 提供了以下主要功能：

- **现代用户体验**：支持多主题、国际化、响应式设计
- **多集群管理**：无缝集群切换、Kubeconfig 集成
- **全面资源管理**：支持 Pods、Deployments、Services 等资源的管理
- **监控与可观测性**：实时指标、日志查看、终端访问
- **安全性**：OAuth 集成、基于角色的访问控制

## 用法

### Docker 运行

使用预构建的 Docker 镜像快速启动 Kite：

```bash
docker run --rm -p 8080:8080 ghcr.io/zxh326/kite:latest
```

启动后，在浏览器中访问 `http://localhost:8080` 即可使用 Kite 仪表板。

### 高级配置

如果需要持久化配置或自定义设置，可以使用 Docker Compose 或挂载配置目录：

```yaml
version: '3.8'
services:
  kite:
    image: ghcr.io/zxh326/kite:latest
    ports:
      - '8080:8080'
    volumes:
      - ./config:/app/config
    environment:
      - KITE_CONFIG_PATH=/app/config
```

更多详细用法和配置选项，请参考 [Kite 官方文档](https://kite.zzde.me)。
