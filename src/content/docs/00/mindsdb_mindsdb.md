
---
title: mindsdb
---


# MindsDB

## 项目地址
- https://github.com/mindsdb/mindsdb

## 主要特性
- **SQL 驱动的机器学习**：利用标准 SQL 语句（`PREDICT`、`TRAIN` 等）进行模型训练与预测，无需编写 Python 代码。
- **多数据源支持**：可连接 MySQL、PostgreSQL、SQL Server、BigQuery、Snowflake、Redshift、MongoDB、Excel、CSV、S3 等，数据来源极为灵活。
- **自动特征工程**：自动完成缺失值处理、标准化、聚合特征、时间序列衍生特征等。
- **模型管理与监控**：可视化仪表盘展示模型性能、持续评估与自动化漂移检测。
- **内嵌模型解释**：支持 SHAP、LIME 等解释方法，帮助理解模型决策。
- **插件生态**：支持自定义模型插件，能够使用 TensorFlow、PyTorch、CatBoost 等任意框架。

## 核心功能
| 功能 | 说明 |
|------|------|
| **数据连接** | 通过 `CONNECT TO` 或使用 `mindsdb` Python API 连接外部数据库。 |
| **模型训练** | `CREATE MODEL ... PREDICT` 语句实现一键训练。 |
| **预测** | `SELECT PREDICT(column) FROM table` 直接在 SQL 查询中获取预测结果。 |
| **模型评估与调优** | 自动生成训练集/验证集、训练曲线、性能指标；支持网格搜索。 |
| **持续学习** | `UPDATE MODEL ...` 自动将新数据纳入模型持续训练。 |
| **预测服务** | 通过 REST API 或自动生成的 SDK 接口在应用中调用。 |

## 快速上手

```bash
# 1. 安装 MindsDB
pip install mindsdb

# 2. 启动 MindsDB 服务器（支持 Docker）
docker run -p 47334:47334 -p 47335:47335 mindsdb/mindsdb

# 3. 连接外部数据库（以 MySQL 为例）
CREATE DATABASE IF NOT EXISTS mydb;
CONNECT TO `mysql://username:password@localhost:3306/target_db` WITHIN mydb;

# 4. 训练模型
CREATE MODEL my_model
  PREDICT target_column
  FROM my_table
  WHERE timestamp >= '2023-01-01';

# 5. 查看训练状态
SELECT * FROM my_model_status;

# 6. 做预测
SELECT *, PREDICT(target_column) FROM my_table
  WHERE timestamp BETWEEN '2023-01-01' AND '2023-01-07';

# 7. 导出模型
EXPORT MODEL my_model TO 's3://bucket/path/model.zip';

# 8. 在应用中使用 REST API
curl -X POST http://localhost:47334/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"model_name": "my_model", "payload": [{"col1": 10, "col2": 5}]}' 
```

## 文档与社区
- 官方文档: https://docs.mindsdb.com/
- 示例仓库: https://github.com/mindsdb/mindsdb/tree/master/example
- 社区支持: GitHub Issues、Discord、Slack

--- 

> **提示**：在生产环境建议使用 Docker 部署，并开启监控与日志收集，配合 MindsDB 的模型监控插件进行持续治理。