---
title: ingestr
---

# Ingestr 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/bruin-data/ingestr)

## 主要特性
Ingestr 是一个开源的数据摄取工具，由 Bruin Data 开发，主要用于简化数据管道中的数据摄取过程。它支持多种数据源的集成，具有以下核心特性：
- **多源支持**：兼容多种数据源，如数据库（PostgreSQL、MySQL）、文件系统（CSV、JSON、Parquet）和云存储（S3、GCS）。
- **配置驱动**：通过 YAML 或 JSON 配置文件定义摄取任务，易于管理和扩展。
- **增量摄取**：支持基于时间戳或主键的增量数据加载，避免全量重复处理，提高效率。
- **错误处理与重试**：内置鲁棒的错误恢复机制，包括自动重试和日志记录。
- **可扩展性**：模块化设计，便于自定义插件和集成到现有 ETL 管道中。
- **轻量级**：无外部依赖，适合在容器化环境中部署，如 Docker 或 Kubernetes。

## 主要功能
- **数据提取**：从各种来源提取结构化和非结构化数据。
- **数据转换**：提供基本的转换功能，如过滤、映射和简单聚合，支持与 Apache Spark 或 Pandas 等工具集成。
- **数据加载**：将处理后的数据加载到目标存储中，如数据仓库（Snowflake、BigQuery）或数据库。
- **调度与监控**：集成 cron-like 调度，支持任务监控和警报通知。
- **安全性**：支持加密凭证管理和访问控制，确保数据传输安全。

## 用法
1. **安装**：
   - 通过 pip 安装：`pip install ingestr`
   - 或从源代码克隆：`git clone https://github.com/bruin-data/ingestr.git` 并运行 `pip install -e .`

2. **配置**：
   - 创建配置文件 `ingestr.yaml`，示例：
     ```yaml
     sources:
       - name: my_db
         type: postgresql
         connection: "host=localhost dbname=test user=admin password=secret"
         query: "SELECT * FROM users WHERE updated_at > {{ last_run }}"
     
     targets:
       - name: warehouse
         type: bigquery
         project: my-project
         dataset: staging
     
     jobs:
       - name: ingest_users
         source: my_db
         target: warehouse
         schedule: "0 2 * * *"
     ```

3. **运行**：
   - 命令行执行：`ingestr run --config ingestr.yaml --job ingest_users`
   - 调度模式：`ingestr schedule --config ingestr.yaml`
   - 测试配置：`ingestr validate --config ingestr.yaml`

4. **高级用法**：
   - 自定义转换：在配置文件中添加 `transform` 部分，使用 Python 脚本。
   - 监控：集成 Prometheus 或 ELK 栈，通过日志文件查看任务状态。
   - 更多细节请参考项目文档：https://github.com/bruin-data/ingestr/tree/main/docs