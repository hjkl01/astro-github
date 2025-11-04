
---
title: opendal
---


# Apache Opendal

> 项目地址: <https://github.com/apache/opendal>

## 简介
Apache Opendal 是一个 Rust 编写的跨平台、跨对象存储服务层（Object Storage Abstraction Layer）。它提供一致的 API，让开发者能够无缝切换不同的云存储服务（如 AWS S3、Azure Blob、Google Cloud Storage、Ceph、Alibaba OSS 等），同时支持本地文件系统等多种后端。

## 主要特性
- **多后端支持**：一次编写代码，适配 S3、Azure Blob、GCS、Ceph、Aliyun OSS、Alibaba OSS、Qiniu、MinIO、LocalFS 等 10+ 后端。
- **统一 API**：所有主流对象存储统一接口，操作一致，无需关心后端细节。
- **轻量高效**：纯 Rust，零依赖/可选依赖，可嵌入入任何 Rust 项目。
- **异步与同步**：同时提供 `async` 与同步版本，满足高并发或简单脚本需求。
- **插件化**：后端可用 Cargo features 控制开/闭，减小二进制体积。
- **兼容性**：支持 HDFS/Hive 等大数据环境的存储后端。
- **可扩展**：用户可自行实现 `Operator` 或 `Layer`，快速接入自定义存储。

## 核心功能
- **文件与目录操作**
  - 创建、删除、重命名文件/目录（`create`, `delete`, `rename`）
  - 读取文件内容，支持分块读取（`read`, `download`）
  - 写入文件，支持流式写（`write`, `upload`）
- **元数据管理**
  - 获取文件属性（大小、修改时间、自定义元数据）
  - 更新文件属性（`set_attr`）
- **目录遍历**
  - 列出目录内容（`list`, `walk`）
- **事务支持**
  - 事务撰写/偏移（`create`, `write`）
- **配置信息读取**
  - 各后端配置解析，统一 `Config` API

## 使用方法

### 依赖添加
```toml
[dependencies]
opendal = { version = "0.14", features = ["s3"] } # 只启用 S3 后端
```

### 初始化 Operator
```rust
use opendal::Operator;

let op = Operator::with_path("s3://my-bucket/") // 也可使用 `opendal::path::Config` 替代
    .with("access_key_id", "YOUR_ACCESS_KEY")
    .with("secret_access_key", "YOUR_SECRET_KEY")
    .build()
    .await?;
```

### 读取文件
```rust
let content = op.read("hello.txt").await?;
println!("文件内容: {:?}", String::from_utf8_lossy(&content));
```

### 写入文件
```rust
op.write("data.bin", data.into()).await?;
```

### 列出目录
```rust
let list = op.list("").await?;
for entry in list {
    println!("{:?}", entry);
}
```

### 异步与同步
- 异步使用 `tokio` 或 `async-std`
- 同步版本使用 `opendal::Operator::sync(...)` 创建同步实例（不支持异步后端）

```rust
use opendal::Operator;

let op = Operator::with_path("local://tmp/").build()?;
let data = op.read_sync("file.txt")?; // 同步读
```

## 参考文档
- 官方 Wiki: <https://github.com/apache/opendal/wiki>
- API 文档: <https://docs.rs/opendal/>

祝你使用愉快！