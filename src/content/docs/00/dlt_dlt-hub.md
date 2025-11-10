---
title: dlt
---

# dlt (data load tool)

## 项目简介

dlt 是一个开源的 Python 库，用于简化数据加载任务。它可以从各种数据源（如 REST API、SQL 数据库、云存储等）提取数据，并将其加载到结构化的数据集中。dlt 设计简单、灵活且可扩展，支持增量加载、模式演化和多种目的地。

## 主要功能

- **数据提取**：支持从 REST API、SQL 数据库、文件系统、Python 数据结构等多种来源提取数据。
- **数据规范化**：自动推断模式和数据类型，处理嵌套数据结构。
- **多种目的地**：支持流行的数据仓库和数据库，如 DuckDB、BigQuery、Snowflake 等，并允许自定义目的地。
- **增量加载**：自动化维护管道，支持增量数据加载。
- **模式演化**：处理数据模式的变化。
- **数据访问**：支持 Python 和 SQL 数据访问、转换和管道检查。
- **部署灵活**：可在任何运行 Python 的环境中部署，如 Airflow、服务器less 函数等。

## 安装

dlt 支持 Python 3.9 到 3.14（3.14 支持为实验性）。

```bash
pip install dlt
```

## 快速开始

以下是一个简单的示例，从 Chess.com API 加载玩家数据到 DuckDB：

```python
import dlt
from dlt.sources.helpers import requests

# 创建 dlt 管道，将数据加载到 DuckDB
pipeline = dlt.pipeline(
    pipeline_name='chess_pipeline',
    destination='duckdb',
    dataset_name='player_data'
)

# 从 Chess.com API 获取玩家数据
data = []
for player in ['magnuscarlsen', 'rpragchess']:
    response = requests.get(f'https://api.chess.com/pub/player/{player}')
    response.raise_for_status()
    data.append(response.json())

# 提取、规范化并加载数据
pipeline.run(data, table_name='player')
```

你可以在 [Colab Demo](https://colab.research.google.com/drive/1NfSB1DpwbbHX9_t5vlalBTf13utwpMGx?usp=sharing) 或 [playground](https://dlthub.com/docs/tutorial/playground) 中试用。

## 文档和示例

- 详细文档：[dlthub.com/docs](https://dlthub.com/docs)
- 示例代码：[examples](https://dlthub.com/docs/examples)

## 社区和贡献

- 加入社区：[Slack](https://dlthub.com/community)
- 报告问题：[GitHub Issues](https://github.com/dlt-hub/dlt/issues)
- 贡献代码：请阅读 [CONTRIBUTING.md](https://github.com/dlt-hub/dlt/blob/devel/CONTRIBUTING.md)

## 许可证

Apache 2.0 License
