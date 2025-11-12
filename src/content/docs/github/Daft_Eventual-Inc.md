---
title: repository
---

# Daft: 分布式查询引擎

Daft 是一个用 Rust 实现的分布式查询引擎，专为大规模数据处理而设计，支持 Python 和 SQL 接口。

## 核心特性

### 🚀 熟悉的交互式 API

- **惰性 Python DataFrame**：支持快速交互式迭代
- **SQL 查询**：提供分析查询功能

### 🎯 强大的查询优化器

- 自动重写查询以获得最佳性能
- 智能缓存和查询优化加速实验和数据探索

### 📊 丰富的多模态类型系统

- 支持图像、URL、张量等复杂数据类型
- 高效处理嵌套多模态数据
- 基于 Apache Arrow 的内存表示

### ☁️ 云原生设计

- 与 AWS Glue、Unity Catalog 等数据目录集成
- 支持 Apache Iceberg 等表格式
- S3 云存储集成具有创纪录的 I/O 性能

### 🌐 分布式计算

- 原生集成 Ray 框架
- 支持在数千个 CPU/GPU 的大型机器集群上运行
- 轻松扩展到超出本地笔记本电脑资源限制的工作负载

## 安装使用

### 基础安装

```bash
pip install daft
```

### 快速开始示例

以下示例展示如何从 AWS S3 存储桶加载图像并调整大小：

```python
import daft

# 从 S3 存储桶的文件路径加载数据框
df = daft.from_glob_path("s3://daft-public-data/laion-sample-images/*")

# 1. 下载图像 URL 列作为字节列
# 2. 将字节列解码为图像列
df = df.with_column("image", df["path"].url.download().image.decode())

# 将每个图像调整为 32x32 大小
df = df.with_column("resized", df["image"].image.resize(32, 32))

df.show(3)
```

## 设计原则

### 1. 任意数据支持

除了传统的字符串/数字/日期外，Daft 列还可以高效地保存复杂或嵌套的多模态数据，如图像、嵌入和 Python 对象。

### 2. 交互式计算

Daft 专为通过笔记本或 REPL 进行交互式开发体验而构建，智能缓存和查询优化可加速您的实验和数据探索。

### 3. 分布式计算

当工作负载超出本地笔记本电脑的计算资源时，Daft 与 Ray 的原生集成允许在大型机器集群上运行数据框。

## 性能基准

Daft 在 AI 工作负载基准测试中表现优异，特别是在处理多模态数据和大规模数据集方面展现出卓越性能。

## 技术栈对比

| 特性       | Daft | Pandas     | Polars     | PySpark    |
| ---------- | ---- | ---------- | ---------- | ---------- |
| 查询优化器 | ✅   | ❌         | ✅         | ✅         |
| 多模态支持 | ✅   | Python对象 | Python对象 | ❌         |
| 分布式计算 | ✅   | 可选       | ✅         | ✅         |
| Arrow 支持 | ✅   | 部分       | ✅         | Pandas UDF |
| 向量化执行 | ✅   | ❌         | ✅         | ✅         |

## 更多资源

- [官方文档](https://docs.daft.ai)
- [快速入门指南](https://docs.daft.ai/en/stable/quickstart/)
- [API 参考](https://docs.daft.ai/en/stable/api/)
- [示例集合](https://docs.daft.ai/en/stable/examples/)
- [社区支持](https://github.com/Eventual-Inc/Daft/discussions)

## 许可证

Daft 采用 Apache 2.0 许可证。

## 贡献

欢迎开发者贡献代码！请阅读 [CONTRIBUTING.md](https://github.com/Eventual-Inc/Daft/blob/main/CONTRIBUTING.md) 了解开发生命周期和工具链。项目还提供了适合新贡献者的 [good first issues](https://github.com/Eventual-Inc/Daft/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) 列表。
