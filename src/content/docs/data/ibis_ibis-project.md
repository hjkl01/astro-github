---
title: ibis
---

# Ibis 项目

## 项目地址
[GitHub 项目地址](https://github.com/ibis-project/ibis)

## 主要特性
Ibis 是一个开源的 Python 数据分析框架，旨在提供统一的 API 来处理多种数据后端（如 SQL 数据库、Pandas、Polars 等）。其主要特性包括：
- **后端无关的查询接口**：使用 Python 代码编写查询，支持多种数据源（如 PostgreSQL、MySQL、BigQuery、DuckDB 等），无需为每个后端编写不同的 SQL。
- **延迟执行**：查询是惰性求值的，只有在调用 `.execute()` 或类似方法时才实际执行，提高效率。
- **类型安全**：内置类型检查和推断，确保查询的正确性。
- **可扩展性**：易于集成第三方后端，支持自定义表达式和操作。
- **性能优化**：生成优化的 SQL 或其他后端代码，利用底层引擎的性能优势。
- **跨平台兼容**：支持本地数据（如 Pandas DataFrame）和云服务（如 Snowflake、Databricks）。

Ibis 特别适合数据科学家和工程师，用于构建可移植的数据管道，避免 SQL 方言的差异。

## 主要功能
- **数据加载和连接**：连接各种数据源，支持文件格式（如 CSV、Parquet）和数据库。
- **查询构建**：提供类似 Pandas 的 API，用于过滤、聚合、分组、连接、窗口函数等操作。
- **表达式系统**：使用 Ibis 表达式树构建复杂查询，支持 UDF（用户定义函数）。
- **可视化和导出**：集成 Matplotlib 等工具进行数据可视化，或导出结果到 DataFrame。
- **子查询和 CTE 支持**：处理嵌套查询和公共表表达式。
- **机器学习集成**：与 scikit-learn 等库结合，用于特征工程。

## 用法
### 安装
使用 pip 安装核心包：
```
pip install ibis-framework
```
针对特定后端安装扩展，例如：
```
pip install 'ibis-framework[postgres]'  # PostgreSQL 支持
pip install 'ibis-framework[duckdb]'   # DuckDB 支持
```

### 基本用法示例
1. **连接数据源**：
   ```python
   import ibis

   # 连接 DuckDB（内存数据库）
   con = ibis.duckdb.connect()

   # 或连接 PostgreSQL
   con = ibis.postgres.connect(host='localhost', user='user', password='pass', database='mydb')
   ```

2. **加载数据并查询**：
   ```python
   # 从 CSV 加载表
   t = con.read_csv('data.csv')

   # 简单查询：过滤和聚合
   result = t.filter(t['age'] > 30).group_by('city').aggregate(total=ibis.sum('salary')).execute()
   print(result)
   ```

3. **复杂操作**：
   ```python
   # 连接两个表
   joined = t1.join(t2, t1['id'] == t2['id'])

   # 窗口函数
   windowed = t.window(ibis.order_by(t['date'])).mutate(running_total=ibis.cumsum('value'))
   ```

4. **执行查询**：
   - 调用 `.execute()` 获取 Pandas DataFrame 结果。
   - 对于 SQL 输出，使用 `.compile()` 查看生成的 SQL 代码。

更多细节请参考官方文档：https://ibis-project.org/