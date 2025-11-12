---
title: cube
---

# Cube

Cube Core 是一个开源的语义层和 LookML 的替代方案，用于 AI、BI 和嵌入式分析。它使数据专业人员能够从现代数据存储中访问数据，将其组织成一致的定义，并通过多个 API 交付给应用程序。

## 主要特性

- **数据源支持**：连接到启用 SQL 的数据源，包括云数据仓库（Snowflake、Google BigQuery）、查询引擎（Presto、Amazon Athena）和应用程序数据库（Postgres）。
- **API**：为嵌入式分析和 BI 提供 REST、GraphQL 和 SQL API。
- **性能**：内置关系缓存引擎，实现亚秒级延迟和高并发。
- **多维分析**：使用一致的指标定义启用 OLAP 风格的分析。
- **访问控制**：跨数据生态系统的强大治理和安全。
- **无头架构**：灵活集成，无供应商锁定。

## 入门指南

### Cube Cloud（推荐）

Cube Cloud 提供托管基础设施，并为开发项目提供免费访问。

1. 在 [Cube Cloud](https://cubecloud.dev/auth/signup) 注册。
2. 按照 [逐步指南](https://cube.dev/docs/getting-started/cloud/overview) 操作。

### Docker（自托管）

使用 Docker 在本地运行 Cube：

```bash
docker run -p 4000:4000 \
  -p 15432:15432 \
  -v ${PWD}:/cube/conf \
  -e CUBEJS_DEV_MODE=true \
  cubejs/cube
```

Open [http://localhost:4000](http://localhost:4000) to continue setup. See [Docker docs](https://cube.dev/docs/getting-started-docker) for details.

## Basic Usage

1. **Define Data Models**: Create cube definitions in YAML or JavaScript to model your data.
2. **Connect Data Sources**: Configure connections to your databases.
3. **Query Data**: Use REST API, GraphQL, or SQL to query metrics and dimensions.
4. **Integrate**: Embed analytics into applications or connect to BI tools.

For examples and tutorials, visit [Cube Docs](https://cube.dev/docs/examples).
