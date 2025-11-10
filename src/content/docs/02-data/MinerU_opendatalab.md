---
title: MinerU
---

# MinerU (OpenDataLab)

> **项目地址**  
> https://github.com/opendatalab/MinerU

## 简介  
MinerU 是一个面向开源数据分析的 Python 工具集，旨在帮助研究人员和工程师快速完成用户数据的抽取、清洗、特征工程与建模。项目提供了统一的接口和高效的实现，支持多种常见的数据源（CSV、JSON、SQL、NoSQL 等）以及多种分析方法（聚类、关联规则、图挖掘、文本挖掘等）。

## 主要特性  

| 特性 | 说明 |
|------|------|
| **多源数据抽取** | 通过统一的 `DataLoader` 接口支持 CSV、JSON、MySQL、MongoDB 等多种来源。 |
| **自动化清洗** | 内置缺失值填充、异常值检测与修复、数据类型转换等工具。 |
| **特征工程** | 提供数值型、分类型、文本型特征的标准化、独热编码、TF‑IDF、词嵌入等转换器。 |
| **用户画像** | 通过聚类与关联规则生成用户画像，支持可视化展示。 |
| **图挖掘** | 通过 NetworkX 与 PyTorch Geometric 进行用户关系图构建、节点嵌入与社区检测。 |
| **模型训练** | 内置轻量级机器学习管道，可直接使用 scikit‑learn、XGBoost、LightGBM 等模型。 |
| **可视化** | 通过 Plotly、Seaborn 等库实现交互式报告与仪表盘。 |
| **CLI 与 API** | 提供命令行工具与 Python API 两种调用方式，方便批处理与脚本集成。 |
| **可扩展插件** | 支持自定义插件接口，用户可轻松添加新的数据源、特征或模型。 |

## 功能模块

| 模块 | 功能 |
|------|------|
| `loader` | 数据加载器，支持多种格式与数据库。 |
| `preprocess` | 数据清洗、缺失值处理、标准化等。 |
| `feature` | 特征提取与转换工具。 |
| `graph` | 图构建、节点嵌入、社区检测。 |
| `model` | 机器学习管道与模型训练。 |
| `visualize` | 报告生成与交互式可视化。 |
| `cli` | 命令行入口，快速执行常用流程。 |

## 安装与使用

```bash
# 克隆仓库
git clone https://github.com/opendatalab/MinerU.git
cd MinerU

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 可选：安装开发依赖
pip install -r dev-requirements.txt
```

### 通过 Python API

```python
from mineru.loader import CSVLoader
from mineru.preprocess import DataCleaner
from mineru.feature import TextVectorizer
from mineru.model import SimplePipeline
from mineru.visualize import plot_cluster

# 1. 加载数据
loader = CSVLoader('data/sample_users.csv')
df = loader.load()

# 2. 数据清洗
cleaner = DataCleaner()
df_clean = cleaner.clean(df)

# 3. 特征工程
vectorizer = TextVectorizer()
X = vectorizer.fit_transform(df_clean['comment'])
y = df_clean['label']

# 4. 模型训练
pipeline = SimplePipeline(models=['logreg', 'rf'])
pipeline.fit(X, y)

# 5. 可视化
plot_cluster(X, pipeline.predict(X))
```

### 通过 CLI

```bash
# 读取、清洗、特征化并训练模型
mineru run --input data/sample_users.csv \
           --output results/ \
           --model random_forest \
           --plot
```

## 示例

```bash
mineru run \
  --input data/users.csv \
  --output results/ \
  --model xgboost \
  --cluster kmeans \
  --plot
```

> 以上命令会完成：  
> 1. 从 `data/users.csv` 读取数据  
> 2. 自动清洗与特征化  
> 3. 训练 XGBoost 模型  
> 4. 对用户进行 K‑Means 聚类  
> 5. 输出预测结果与聚类可视化到 `results/`

## 贡献

欢迎提交 Issue 与 Pull Request。请先阅读 `CONTRIBUTING.md`，遵循代码规范与测试要求。

## 许可证

MIT © OpenDataLab

---