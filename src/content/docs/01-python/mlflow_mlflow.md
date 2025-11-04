
---
title: mlflow
---

# MLflow 项目概述

**项目地址**  
[https://github.com/mlflow/mlflow](https://github.com/mlflow/mlflow)

---

## 主要特性

| 特色 | 说明 |
|------|------|
| **实验追踪** | 记录参数、指标、模型文件及实验结果，支持可视化比较实验。 |
| **项目封装** | 使用MLflow Projects把代码、依赖和运行环境打包，保证可复现。 |
| **模型管理** | 支持多种框架（TensorFlow、PyTorch、scikit‑learn 等）的模型包；提供模型注册中心（Registry）。 |
| **模型部署** | 通过 MLflow Models 打包，可直接部署到 TorchServe、SageMaker、k8s、Java、Python 或 REST API。 |
| **与云平台结合** | 原生集成 AWS S3、Azure Blob、Google Cloud Storage，支持对应的实验后端存储。 |
| **可扩展性** | 支持自定义实验后端、存储后端以及插件机制。 |

---

## 核心组件

| 组件 | 作用 | 简短说明 |
|------|------|---------|
| **MLflow Tracking** | 日志实验 | `mlflow.start_run()`、`mlflow.log_param()`、`mlflow.log_metric()` 等 API。 |
| **MLflow Projects** | 打包与复现 | `mlflow run` 支持 `conda.yml`、`requirements.txt`、`setup.py` 等。 |
| **MLflow Models** | 模型封装 | `mlflow.pyfunc`、`sklearn`, `pytorch`, `keras`, `spark` 等签名。 |
| **MLflow Registry** | 模型版本管理 | 通过注册中心管理模型版本、阶段、元数据。 |

---

## 安装方法

```bash
# 使用 pip
pip install --upgrade mlflow

# 克隆源码并跑测试
git clone https://github.com/mlflow/mlflow.git
cd mlflow
pip install -e .
pytest
```

---

## 快速上手

### 1. 记录实验

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error

# 开始一个实验（可自定义实验名）
mlflow.set_experiment("rf_diabetes")

X, y = load_diabetes(return_X_y=True)

with mlflow.start_run():
    # 记录超参数
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 4)

    # 训练模型
    model = RandomForestRegressor(n_estimators=100, max_depth=4)
    model.fit(X, y)

    # 预测并评估
    preds = model.predict(X)
    rmse = mean_squared_error(y, preds, squared=False)

    # 记录指标
    mlflow.log_metric("rmse", rmse)

    # 保存模型
    mlflow.sklearn.log_model(model, "model")
```

### 2. 运行项目

假设有 `MLproject` 文件：

```yaml
name: my-mlflow-project

conda_env: conda.yaml

entry_points:
  main:
    parameters:
      max_depth: 4
      n_estimators: 100
    command: "python train.py --max_depth {max_depth} --n_estimators {n_estimators}"
```

```bash
mlflow run . -P max_depth=5 -P n_estimators=200
```

### 3. 发布和部署模型

```bash
# 先登录模型注册中心
mlflow models serve -m runs:/<RUN_ID>/model -p 5000

# 或者导出为 Docker 包
mlflow models build-docker -m runs:/<RUN_ID>/model -t myrf-image
docker run -p 5000:5000 myrf-image
```

---

## 常见命令行

| 命令 | 用途 |
|------|------|
| `mlflow ui` | 启动 Web UI，默认访问 5000 端口 |
| `mlflow run` | 运行 MLflow Projects |
| `mlflow models serve` | 快速启动模型 REST API |
| `mlflow models build-docker` | 构建模型 Docker 镜像 |
| `mlflow models list` | 查看已部署模型 |

---

### 参考链接

- 官方文档: <https://mlflow.org/docs/latest/index.html>
- GitHub: <https://github.com/mlflow/mlflow>

---