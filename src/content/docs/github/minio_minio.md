
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
MinIO 提供以下关键功能：
- **对象存储**：存储非结构化数据，如图像、视频、备份和日志文件，支持无限扩展。
- **数据管理**：支持桶创建、删除、ACL 设置，以及对象元数据管理。
- **集成与扩展**：与 Hadoop、Spark、Presto 等大数据工具无缝集成；支持 Web 管理界面（MinIO Console）进行可视化操作。
- **备份与恢复**：通过纠删码实现数据保护，自动处理节点失败和恢复。
- **API 支持**：RESTful API、SDK（Go、Java、Python 等语言）和 CLI 工具，便于开发集成。

## 用法
### 安装
1. **二进制安装**（Linux/macOS 示例）：
   ```
   wget https://dl.min.io/server/minio/release/linux-amd64/minio
   chmod +x minio
   mkdir /data  # 数据目录
   ./minio server /data --console-address ":9001"
   ```
   默认访问：API (http://localhost:9000)，Console (http://localhost:9001)。默认凭证：minioadmin/minioadmin。

2. **Docker 部署**：
   ```
   docker run -p 9000:9000 -p 9001:9001 \
     -e "MINIO_ROOT_USER=admin" \
     -e "MINIO_ROOT_PASSWORD=password" \
     quay.io/minio/minio server /data --console-address ":9001"
   ```

3. **Kubernetes 部署**：使用官方 Helm Chart 或 Operator 进行分布式部署，支持多节点集群。

### 基本用法
- **CLI 操作**（使用 mc 工具）：
  1. 安装 mc：`wget https://dl.min.io/client/mc/release/linux-amd64/mc` 并配置。
  2. 配置别名：`mc alias set myminio http://localhost:9000 minioadmin minioadmin`。
  3. 创建桶：`mc mb myminio/mybucket`。
  4. 上传对象：`mc cp localfile.txt myminio/mybucket/`。
  5. 下载对象：`mc cp myminio/mybucket/file.txt .`。

- **编程集成**（Python 示例，使用 boto3）：
  ```python
  import boto3
  s3 = boto3.client('s3',
      endpoint_url='http://localhost:9000',
      aws_access_key_id='minioadmin',
      aws_secret_access_key='minioadmin')
  s3.create_bucket(Bucket='mybucket')
  s3.upload_file('localfile.txt', 'mybucket', 'file.txt')
  ```

- **Web Console**：通过浏览器访问 Console 界面，进行桶管理、用户配置和监控。

更多详情请参考官方文档：https://docs.min.io。