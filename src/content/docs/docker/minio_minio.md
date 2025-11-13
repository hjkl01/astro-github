---
title: minio
---

# MinIO 项目

**GitHub 项目地址:** [https://github.com/minio/minio](https://github.com/minio/minio)

## 主要特性

MinIO 是一个开源的对象存储服务器，兼容 Amazon S3 API，专为云原生工作负载设计。其核心特性包括：

- **高性能**：支持大规模分布式部署，提供亚毫秒级延迟的对象存储。
- **S3 兼容性**：完全兼容 Amazon S3 API，包括多部分上传、版本控制和生命周期管理。
- **分布式架构**：支持 erasure coding（纠删码）以实现数据冗余和高可用性，即使在多节点故障时也能保持数据完整。
- **安全性**：内置加密（服务器端和客户端）、访问控制（IAM 策略）和审计日志。
- **多租户支持**：通过桶（bucket）和策略实现隔离，支持多用户、多应用场景。
- **跨平台**：支持 Linux、Windows 和 macOS，易于在 Kubernetes、Docker 等环境中部署。
- **开源与免费**：采用 AGPLv3 许可，社区活跃，提供企业级功能。

## 主要功能

MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

## 用法

请参考项目文档获取详细用法。
