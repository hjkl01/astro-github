
---
title: datafusion
---


# Apache DataFusion

**项目地址**：[https://github.com/apache/datafusion](https://github.com/apache/datafusion)

## 概述

Apache DataFusion 是一个用 Rust 编写的开源数据处理框架，旨在提供高性能、可扩展的列式内存查询引擎。它兼容 Apache Arrow 生态系统，支持 SQL、DataFrame API 以及可视化代码。

## 主要特性

- **列式内存数据模型**  
  使用 Arrow 记录和缓冲区，支持快速的向量化计算和 SIMD 优化。

- **自定义算子和扩展**  
  通过插件系统可以添加自定义 `PhysicalPlan`、`LogicalPlan` 以及 `Expression`。

- **多源数据访问**  
  原生支持 Hive、Parquet、CSV、JSON、Avro、S3、Kafka、SFTP 等多种数据源。

- **SQL 解析与执行**  
  - 解析 SQL → LogicalPlan → PhysicalPlan。  
  - 采用类似 Apache Spark Catalyst 的查询优化器（成本模型、谓词下推、列裁剪）。

- **并行执行与调度**  
  - 线程安全、共享内存多租户。  
  - 任务分解为 `PhysicalExec`，通过 `parquet-rs`、`arrow-flight` 等并行 I/O 库实现。

- **与 Apache Arrow Flight 集成**  
  支持 Arrow Flight 远程查询与结果返回，加速分布式查询。

- **可嵌入式部署**  
  通过 `datafusion` 库直接嵌入 Rust/Node.js/Python（借助 C FFI）项目中。  

- **面向开发者的 DataFrame API**  
  类似 Pandas，支持链式操作、窗口函数、聚合与连接。

## 核心功能

| 功能 | 说明 |
|------|------|
| **SQL** | 支持标准 ANSI SQL，能够通过 `sql` API 运行查询。 |
| **DataFrame** | 通过 `datafusion_sql` API 进行易读链式操作。 |
| **规划与优化** | 包含规则、成本模型、谓词下推、列裁剪、聚合推导等。 |
| **ICP** | `ParquetExec`, `CsvExec`, `FileScanExec` 等物理算子。 |
| **内存管理** | 采用 MPSC 通道与共享引用计数（Arc）实现。 |

## 开始使用

```rust
use datafusion::prelude::*;

// 创建执行环境
let ctx = SessionContext::new();

// 注册文件
ctx.register_csv("people", "data/people.csv", CsvReadOptions::new()).await?;

// 执行 SQL
let df = ctx.sql("SELECT age, count(*) FROM people GROUP BY age").await?;

// 展示结果
df.show().await?;
```

```bash
# 使用 cargo 直接运行
cargo run --example simple_sql
```

## 集成案例

| 场景 | 说明 |
|------|------|
| **大数据分析** | 读取大批量 Parquet/S3 数据，使用向量化查询加速。 |
| **ETL/ELT** | 结合 Arrow Flight 与 DataFusion 完成数据管道。 |
| **实时窗口聚合** | 通过 DataFrame API 与 Parquet/ParquetStreams 集成，实现低延迟聚合。 |
| **机器学习预处理** | 与 `arrow2`、`polars` 结合，作为预处理阶段。 |

---

> 详见官方文档：[https://datafusion.apache.org](https://datafusion.apache.org)  
> 示例与教程请查阅仓库 `docs/` 与 `examples/` 目录。  

