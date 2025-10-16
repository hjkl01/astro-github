
---
title: seaweedfs
---

# SeaweedFS 项目

## 项目地址
[https://github.com/chrislusf/seaweedfs](https://github.com/chrislusf/seaweedfs)

## 主要特性
SeaweedFS 是一个分布式存储系统，专为高性能、可扩展性和简单性设计。主要特性包括：
- **高性能**：支持亿级文件存储，文件查找时间在微秒级，使用 Filer 作为命名空间层。
- **分布式架构**：由 Master、Volume Server 和 Filer 等组件组成，支持水平扩展。
- **多存储后端**：兼容 S3、HDFS 等接口，便于集成现有生态。
- **数据可靠性**：支持复制、纠删码（Erasure Coding）和快照功能，确保数据安全。
- **轻量级**：单个二进制文件部署，资源占用低，适合云原生环境如 Kubernetes。
- **开源免费**：采用 Apache 2.0 许可，支持社区贡献。

## 主要功能
- **文件存储**：高效存储海量小文件和大文件，支持块级存储（Volume Server 处理实际数据）。
- **命名空间管理**：Filer 提供 POSIX-like 文件系统接口，支持目录结构、权限控制和元数据搜索。
- **API 支持**：内置 WebDAV、S3 兼容 API，以及自定义 gRPC 接口，便于应用程序集成。
- **数据管理**：支持文件复制、迁移、垃圾回收和自动平衡，优化存储利用率。
- **监控与运维**：集成 Prometheus 指标、Web UI 和命令行工具，便于监控集群状态。
- **扩展性**：可与 CDN、数据库等结合，实现混合存储场景。

## 用法
### 安装
1. 下载二进制文件：从 GitHub Releases 下载适合平台的 sea-weedfs 可执行文件。
2. 解压并赋予执行权限：`chmod +x weed`。

### 启动集群
- **启动 Master**：`weed master -port=9333`（管理元数据）。
- **启动 Volume Server**：`weed volume -mserver=localhost:9333 -dir=/path/to/storage -port=8080`（存储实际数据）。
- **启动 Filer**：`weed filer -master=localhost:9333 -port=8888`（文件系统接口）。

### 基本操作
- **上传文件**：使用 S3 API，例如通过 `aws s3` 工具：`aws s3 cp file.txt s3://bucket/path/`（需配置 endpoint 为 Filer 地址）。
- **下载文件**：`aws s3 cp s3://bucket/path/file.txt .`。
- **命令行工具**：使用 `weed` 命令，如 `weed shell` 进入交互模式，或 `weed filer.copy` 复制文件。
- **集成示例**：在应用中通过 Go/Python SDK 调用 API 进行文件操作。

详细文档请参考项目 Wiki 或运行 `weed --help` 获取更多命令选项。