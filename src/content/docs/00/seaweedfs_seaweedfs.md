
---
title: seaweedfs
---

## SeaweedFS 入门

**项目地址**：<https://github.com/seaweedfs/seaweedfs>  

---

### 1.  项目概述  
SeaweedFS 是一款高性能、可水平扩展的对象存储与文件系统，专为分布式环境设计。  
- **水平可扩展**：可轻松新增 Volume 节点，实现数十 TB 甚至 级别容量。  
- **高吞吐**：支持并发读写、批量上传，秒级响应。  
- **多协议**：兼容 S3、Swift、HDFS、WebDAV、FUSE 和原生 RPC API。  
- **轻量**：核心组件只需数 MB，运行时内存占用低。  
- **零合并**：自带自动执行稀疏索引压缩、数据去重。  

---

### 2.  主要特性

| 特色 | 说明 |
|------|------|
| **分布式架构** | Master、Volume Server、Master Cache 三层互相协作，支持无单点故障 |
| **最小化网络** | 所有节点通过高效 RPC（gRPC/JSON-RPC）通信，降低延迟 |
| **对象与文件兼容** | S3 API、Swift API、WebDAV、FUSE、RESTful 兼容，让迁移无缝 |
| **数据分区** | 自动按文件大小、类型分配到不同 Volume，提升 IO 密集型性能 |
| **热容灾** | Volume Server 可以在任意节点上重建，自动复制/恢复，支持热迁移 |
| **Cacher** | 通过 Master Cache 节点把热点文件编入缓存，加速读取 |
| **自动压缩** | 对长时间不修改的文件进行压缩，节省存储空间 |
| **集成监控** | Prometheus 指标、Grafana 可视化，可以监控容量、延迟、率地磁盘、NAS、云对象存储（S3、AliYun OSS、GCS）等后端 |

---

### 3.  功能分类

| 功能 | 描述 |
|-----|-----|
| **文件上传 / 下载** | 通过 RESTful 或 S3 API 上传文件，可满足大文件（>10 GB）流式上传 |
| **文件分块** | 支持大文件分块写入，保证写入可靠性与性能 |
| **版本控制** | 通过 metadata/etag 控制文件版本，兼容 S3 的 `object versioning` |
| **ACL & IAM** | 通过 ACL token 或 IAM Role control 访问权限，数字签名 |
| **删除 / 标记** | 支持硬删除、软删除、过期策略 |
| **目录结构** | 虽为对象存储，但可在客户端使用 FUSE 构建层级视图 |
| **索引** | 内置全局索引，快速查询文件列表，支持多种查询过滤 |
| **文件共享** | 生成预签名 URL、公共桶、私有桶，提供短链接或永久链接 |
| **容灾恢复** | 内置 Volume 复制、热备援、镜像化恢复方案 |

---

### 4.  快速开始

> **前置要求**  
> - Go 1.18+ (编译或容器)  
> - Docker (可选)  
> - 任选一种云存储或本地磁盘作为后端（默认 /home/seaweed/var）  

#### 4.1 安装与运行

```bash
# 方式 1：使用 Docker
docker run -d \
  --name seaweedfs \
  --restart=unless-stopped \
  -p 8333:8333 -p 8443:8443 \
  -v /host/data:/data \
  -v /host/var:/var \
  sheepkiller/seaweedfs:latest \
  master -ip 0.0.0.0

# 方式 2：源码编译
go install github.com/seaweedfs/seaweedfs/cmd/weed@latest
weed master -dir /var -ip 0.0.0.0
# 启动 Volume 节点
weed volume -dir /data -master 127.0.0.1:8333
```

> **默认端口**  
> - Master: `8333`  
> - Volume: `8443` (可通过 `-p` 参数)  
> - S3 API: `8333`（REST/HTTP）  

#### 4.2 上传 & 下载

```bash
# 上传文件
curl -v -F file=@largefile.iso http://localhost:8333/put?filename=largefile.iso

# 下载文件
curl -O http://localhost:8333/largefile.iso
```

> **S3 兼容**  
> ```bash
> # 使用 AWS CLI 上传
> aws s3 cp largefile.iso s3://bucket/largefile.iso --endpoint-url http://localhost:8333
> ```

#### 4.3 使用 FUSE 挂载

```bash
# 需要先安装 seaweedfs-fuse
# 已包含在 docker 镜像
sudo mkdir /mnt/seaweed
sudo weed mount fs://localhost:8333 /mnt/seaweed
# 之后即可像普通文件系统那样读写
```

#### 4.4 监控

访问 `http://localhost:8333/metrics` 可获取 Prometheus 友好的指标，集成 Grafana Dashboard（可在官方 repo 下载）。

---

### 5.  常见命令 & 参数

| 命令 | 说明 | 关键参数 |
|-----|------|----------|
| `weed master` | 启动 Master 服务 | `-port`, `-ip`, `-dir` |
| `weed volume` | 启动 Volume 服务器 | `-dir`, `-master`, `-http.port` |
| `weed backup` | 对有效 Volume 做备份 | `-source`, `-dest` |
| `weed recover` | 恢复损坏 Volume | `-master`, `-target` |
| `weed mount` | 使用 FUSE 挂载 | `fs://MASTER_HOST`, `-mountpoint` |
| `weed -help` | 显示全部参数 | - |

---

### 6.  文档与社区

- 官方文档与快速启动：<https://github.com/seaweedfs/seaweedfs/wiki>
- 示例与脚本：<https://github.com/seaweedfs/seaweedfs/tree/master/examples>
- 讨论 & 归档：GitHub Issues、Slack 频道
- 开源协议：Apache‑2.0

---