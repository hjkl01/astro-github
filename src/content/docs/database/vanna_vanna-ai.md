---
title: vanna
---

# Vanna

**项目地址:** [https://github.com/vanna-ai/vanna](https://github.com/vanna-ai/vanna)

## 简介
Vanna 是一个基于 OpenAI GPT-4 的数据库查询助手，能够将自然语言转换为 SQL，并自动执行查询返回结果。它支持多种数据库（PostgreSQL、MySQL、SQLite 等）以及多种数据源（本地文件、REST API、LLM 等），通过一个统一的插件架构实现可扩展性。

## 核心特性
- **自然语言 SQL 生成**：使用 GPT-4 将用户问题自动转化为高质量 SQL 查询。
- **多数据库支持**：内置对 PostgreSQL、MySQL、SQLite、BigQuery 等数据库的连接与执行。
- **插件化架构**：支持自定义插件，轻松扩展到新的数据源或功能（如文件读取、REST 调用、LLM 回答等）。
- **运行时安全**：使用安全模式过滤不安全或有害查询，避免 SQL 注入。
- **交互式界面**：提供命令行和 Jupyter Notebook 两种交互接口。
- **可插拔 Prompt**：开发者可以自定义 Prompt 以调整模型行为。

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/vanna-ai/vanna
cd vanna

# 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -e .

# 设置 OpenAI API Key
export OPENAI_API_KEY="sk-..."

# 运行示例
python -m vanna.cli --db-type postgres --db-host localhost --db-username user --db-password pass --db-name test_db
```

在弹出的交互式提示中输入自然语言问题，例如：

```
> What are the top 5 most recent sales?
```

Vanna 会生成对应的 SQL 并返回结果。

## 使用插件（可选）

```python
from vanna.backends import PostgreSQLBackend
from vanna.querier import Vanna

db_config = {
    "type": "postgres",
    "host": "localhost",
    "username": "user",
    "password": "pass",
    "database": "test_db",
}
querier = Vanna(db_config=db_config, llm_model="gpt-4")
response = querier.ask("What is the average order amount?")
print(response)
```

## 进一步资源

- 官方文档: https://vanna.ai/docs/
- 贡献指南: https://github.com/vanna-ai/vanna/blob/main/CONTRIBUTING.md
- 示例和教程: https://github.com/vanna-ai/vanna/blob/main/examples/README.md

---