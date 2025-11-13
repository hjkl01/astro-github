---
title: polars
---

# polars - Rust 数据帧与列式计算库

**仓库地址**

[https://github.com/pola-rs/polars](https://github.com/pola-rs/polars)

## 主要特性

- **列式内存布局**  
  高效的“列优先”存储，结合 Arrow 兼容性提高向量化累加与 SIMD 计算性能。

- **DataFrame 与 Series API**  
  兼具类似 Pandas/SQL 的 DataFrame 语义，Series 提供向量化数值/字符串操作。

- **惰性执行（Lazy API）**  
  建立查询计划后统一优化与批量执行，显著提升批处理数据分析速度。

- **多线程与 SIMD 并行**  
  通过 Rayon 并行计算与 Intel AVX/AVX512 加速，支持多核与 SIMD 处理。

- **SQL‑style 变换**  
  `groupby`, `agg`, `filter`, `sort`, `join`, `merge`, `pivot` 等操作，类 SQL 数据操作。

- **窗口函数与滚动统计**  
  `rolling_window`, `expanding_window` 等窗口聚合功能。

- **多种格式读写**  
  `csv`, `parquet`, `orc`, `ipc`（Arrow）`, `json`, `excel` 等，支持压缩 & 冗余。

- **时序分析**  
  支持频率转换、时间窗聚合及行号/前向/后向索引计算。

- **Rust & Python 接口**  
  通过 `pyo3` 提供 Python 包 (`polars`)，兼容 Python 数据科学生态。

- **动态列操作**  
  `lazy_mutate`, `with_column`, `replace_at_idx` 等，支持按需添加/更新列。

## 使用方法

### Rust

```toml
# Cargo.toml
[dependencies]
polars = { version = "0.31", features = ["lazy", "parquet"] }
```

```rust
use polars::prelude::*;

fn main() -> Result<()> {
    // CSV 读取
    let df = CsvReader::from_path("data.csv")?
        .infer_schema(None)
        .has_header(true)
        .finish()?;

    // 基础变换
    let rows = df.filter(&df.column("age")?.gt_eq(18).into_series())?;
    println!("{}", rows);

    // 惰性执行
    let lazy = df.lazy()
        .groupby([col("country")])
        .agg([
            col("salary").mean().alias("avg_salary"),
            col("age").max().alias("max_age")
        ])
        .sort("avg_salary", Default::default())
        .collect()?;

    println!("{}", lazy);

    Ok(())
}
```

### Python

```bash
pip install polars
```

```python
import polars as pl

df = pl.read_csv("data.csv")
df_filtered = df.filter(pl.col("age") >= 18)

# 惰性查询
lazy_df = df.lazy().groupby("country").agg(
    pl.col("salary").mean().alias("avg_salary"),
    pl.col("age").max().alias("max_age")
).sort("avg_salary")

print(lazy_df.collect())
```

## 安装与编译

- **Rust**  
  `cargo build --release`（或直接 `cargo install polars`）

- **Python**  
  `pip install polars`（基于 wheels）或 `pip install git+https://github.com/pola-rs/polars`（从源构建）

- **IDE 集成**  
  在 PyCharm、VS Code 等 IDE 中使用 `polars` 语法高亮与类型提示。

## 进一步阅读

- [官方文档](https://pola-rs.github.io/polars/)
- [API 参考](https://pola-rs.github.io/polars/polars/)
- [贡献指南](https://github.com/pola-rs/polars/blob/master/CONTRIBUTING.md)

---