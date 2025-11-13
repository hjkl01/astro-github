---
title: qlib
---

src/content/docs/00/qlib_microsoft.md
```markdown
# QLib（Microsoft 版本）

**项目地址**  
[https://github.com/microsoft/qlibhttps://github.com/microsoft/qlib)

## 主要特性

- **统一的金融量化框架**：提供从数据采集、特征工程、模型训练、回测、到实盘部署的一站式流程。
- **高性能计算**：支持 CPU 与 GPU 并行计算，能在 10W+ 行金融数据上完成高频特征处理与模型训练。
- **可扩展的数据管理**：内置 `QLib` 数据仓库，可轻松切换数据源（CSV、数据库、Quantopian 等），并支持增量更新。
- **模块化训练与评估**：基于 PyTorch Lightning 封装训练循环，支持多任务、迁移学习和超参数搜索。
- **多资产组合与风险管理**：提供组合构造、动态资金管理、VaR、ES 等风险指标异步计算。
- **回测与实时交易接口**：对接多家券商（e.g., Interactive Brokers、Alpaca）、支持 paper trading 与 live trading。

## 核心功能

| 功能 | 描述 |
|------|------|
| **数据层** | `qlib.data` 包含 `DataHandler`, `DataLoader`, `FeatureEngine` 以统一格式读取并预处理金融数据。 |
| **特征工程** | 支持自定义离线和在线特征，使用 Pandas/XGBoost/TSFresh 等库。 |
| **模型层** | `qlib.model` 提供多种模型模板（LSTM, GRU, Transformer, XGBoost, LightGBM）以及自定义模型 API。 |
| **策略层** | `qlib.strategy` 用于定义交易逻辑、交易频率、止损/止盈等。 |
| **回测层** | `qlib.backtest` 提供高频/低频回测引擎，支持多资产并行、滑点、佣金模型。 |
| **风险层** | `qlib.portfolio` 负责仓位管理、风险估计、组合优化。 |
| **实盘层** | `qlib.execution` 对接券商 API，支持 `paper` 与 `live` 模式。 |

## 快速使用

1. **安装**  
   ```bash
   pip install qlib
   ```

2. **初始化数据仓库**（可选，但建议）  
   ```python
   import qlib
   qlib.init(provider_uri="~/.qlib/")

   # 下载示例数据，例如美股
   from qlib.data import D
   D.set_provider("yfinance", symbol_list="AAPL, MSFT, GOOGL")
   # 或者使用自定义 CSV
   # D.set_provider("csv", path="/path/to/csv")
   ```

3. **特征工程**  
   ```python
   from qlib.feature import Feature
   feats = ("close", "volume", "macd", "bollinger")
   feature = Feature(feats)
   X = feature.fit_transform(bar_df)   # bar_df 是 OHLC 数据
   ```

4. **模型训练**  
   ```python
   from qlib.model import MLPRegressor
   clf = MLPRegressor(hidden_units=[64, 32], lr=1e-3, epochs=200)
   clf.fit(X_train, y_train)
   y_pred = clf.predict(X_val)
   ```

5. **回测**  
   ```python
   from qlib.backtest import back_test
   ret_df = back_test(
       strategy="RegressionStrategy",
       trade_interval=5,            # 5 天持有
       frequency="1D",
       account_kapital=1e6,
       )

   print(ret_df.summary())
   ```

6. **实盘部署**（示例）  
   ```python
   from qlib.execution import IBClient
   client = IBClient()
   client.connect()

   # 依据回测结果发送订单
   for order in ret_df['actions'].iteritems():
       client.send(order)
   ```

> **提示**：更多示例代码请参考官方文档 `docs/source/tutorial.md`。

## 文档与社区

- 官方教程与 API 文档：<https://microsoft.github.io/qlib/>
- 示例项目与 notebooks：<https://github.com/microsoft/qlib/tree/main/notebooks>
- 讨论与提问：GitHub Issues、Discussions，或者加入官方 Discord 讨论区。

---
*此文件为快速概览，详细使用请参阅官方完整文档。*
