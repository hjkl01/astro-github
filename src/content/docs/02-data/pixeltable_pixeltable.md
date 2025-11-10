---
title: pixeltable
---

# Pixeltable

**项目地址**: <https://github.com/pixeltable/pixeltable>

## 主要特性

| 特性 | 说明 |
|------|------|
| **高性能** | 基于 C++ 内核，利用向量化和并行执行，速度可与 C++/Rust 库媲美。 |
| **Pandas‑style API** | 兼容 `pandas.DataFrame` 语法，使用 `pixeltable.DataFrame` 进行数据操作。 |
| **延迟执行** | 所有变换（filter、select、join 等）默认延迟计算，直到 `execute()`、`collect()` 或 `to_pandas()` 被调用。 |
| **列式存储** | 内存中使用列式布局，提升缓存命中率并减少内存占用。 |
| **SQL 与 DataFrame 混合** | 支持 `.sql()` 执行 SQL 语句，也可使用链式 DataFrame 方法。 |
| **分布式计算** | 与 Dask 兼容，可通过 `pixeltable.DaskEngine` 在多核/多节点上并行处理。 |
| **高效 IO** | 原生支持 Parquet、CSV、Arrow 等文件格式读写。 |
| **可扩展插件** | 通过插件系统可添加自定义聚合函数、UDF、连接器等。 |

## 核心功能

- **数据导入/导出**  
  ```python
  df = pt.read_parquet("data.parquet")          # 读取
  df.to_parquet("out.parquet")                 # 写入
  df.to_csv("out.csv")                         # 写 csv
  ```

- **查询与过滤**  
  ```python
  result = df.filter(pt.col("age") > 30).select("name", "age")
  ```

- **聚合**  
  ```python
  agg = df.group_by("country").agg(
          total_sales=pt.sum("sales"),
          avg_age=pt.mean("age")
      )
  ```

- **连接**  
  ```python
  joined = df_left.join(df_right, how="inner", on="id")
  ```

- **窗口函数**  
  ```python
  win = pt.window.partition_by("category").order_by("date")
  df = df.with_column("rank", win.rank())
  ```

- **SQL 语法**  
  ```python
  sql_df = pt.sql("""
      SELECT name, SUM(sales) AS total
      FROM sales
      GROUP BY name
      HAVING total > 1000
  """)
  ```

- **延迟执行**  
  ```python
  lazy = df.filter(...).select(...)
  # 仍未执行
  result = lazy.collect()           # 触发执行
  ```

- **分布式 Dask**  
  ```python
  import dask
  engine = pt.DaskEngine(dask_client)
  df = pt.read_parquet(..., engine=engine)
  ```

## 使用示例

```python
import pixeltable as pt

# 读取数据
df = pt.read_parquet("sales.parquet")

# 简单查询
summary = (
    df
    .filter(pt.col("region") == "North")
    .group_by("product")
    .agg(total_sales=pt.sum("amount"))
    .sort_by("total_sales", ascending=False)
    .collect()
)

# 输出结果
print(summary)
```

> **提示**：所有变换操作返回新的 `DataFrame`，原始对象保持不变。

---
以上内容可直接复制到 `src/content/docs/00/pixeltable_pixeltable.md`，即可完成所需说明。