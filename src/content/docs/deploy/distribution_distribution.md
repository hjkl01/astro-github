---
title: distribution
---

# Distribution

## 项目简介

Distribution 是 Docker Distribution 的开源实现，是一个用于存储和分发容器镜像及其他内容的工具集。它实现了 [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec)，提供了简单、安全、可扩展的基础，用于构建大规模 registry 解决方案或运行私有 registry。

该项目是许多知名 registry 的核心库，包括 Docker Hub、GitHub Container Registry、GitLab Container Registry、DigitalOcean Container Registry，以及 CNCF Harbor Project 和 VMware Harbor Registry。

## 主要功能

- **Registry 实现**：提供完整的 OCI Distribution Specification 实现，支持存储和分发容器镜像。
- **安全性**：内置安全机制，确保内容分发的可靠性。
- **可扩展性**：设计为可扩展的基础，允许用户构建自定义的 registry 解决方案。
- **库支持**：提供丰富的 Go 库，用于与 distribution 组件交互（注意：库接口不稳定）。
- **集成**：与 Docker、containerd 等 OCI 客户端兼容，通过 HTTP 通信。

## 用法

### 安装和运行

1. **从源码构建**：

   ```bash
   git clone https://github.com/distribution/distribution.git
   cd distribution
   make build
   ```

2. **使用 Docker 运行**：

   ```bash
   docker run -d -p 5000:5000 --name registry registry:2
   ```

3. **配置**：
   - 编辑配置文件 `config.yml` 来定制 registry 设置，如存储后端、认证等。
   - 支持多种存储后端：本地文件系统、云存储等。

### 基本操作

- **推送镜像**：

  ```bash
  docker tag my-image localhost:5000/my-image
  docker push localhost:5000/my-image
  ```

- **拉取镜像**：
  ```bash
  docker pull localhost:5000/my-image
  ```

### 高级用法

- **认证**：配置 TLS 和认证机制以保护 registry。
- **存储配置**：使用不同的存储驱动，如 S3、Azure Blob Storage 等。
- **扩展**：通过插件和中间件扩展功能。

更多详细信息请参考官方文档：[https://distribution.github.io/distribution](https://distribution.github.io/distribution)。

## 许可证

该项目采用 Apache 2.0 许可证。
