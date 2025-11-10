---
title: cube
---

# Cube

Cube Core is an open-source semantic layer and LookML alternative for AI, BI, and embedded analytics. It enables data professionals to access data from modern data stores, organize it into consistent definitions, and deliver it to applications via multiple APIs.

## Key Features

- **Data Source Support**: Connects to SQL-enabled data sources including cloud data warehouses (Snowflake, Google BigQuery), query engines (Presto, Amazon Athena), and application databases (Postgres).
- **APIs**: Provides REST, GraphQL, and SQL APIs for embedded analytics and BI.
- **Performance**: Built-in relational caching engine for sub-second latency and high concurrency.
- **Multidimensional Analysis**: Enables OLAP-style analytics with consistent metric definitions.
- **Access Control**: Robust governance and security across data ecosystems.
- **Headless Architecture**: Flexible integration without vendor lock-in.

## Getting Started

### Cube Cloud (Recommended)

Cube Cloud offers managed infrastructure and free access for development projects.

1. Sign up at [Cube Cloud](https://cubecloud.dev/auth/signup).
2. Follow the [step-by-step guide](https://cube.dev/docs/getting-started/cloud/overview).

### Docker (Self-Hosted)

Run Cube locally using Docker:

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
