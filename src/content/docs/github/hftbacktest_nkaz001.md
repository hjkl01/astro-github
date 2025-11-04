
---
title: hftbacktest
---


# hftbacktest

项目地址: https://github.com/nkaz001/hftbacktest

## 主要特性
- **高频交易回测框架**：基于事件驱动架构，支持秒级甚至毫秒级的 tick 数据回测。  
- **多种数据源**：支持 CSV、数据库（如 PostgreSQL）以及自定义数据接口，方便快速导入行情。  
- **策略接口统一**：`Strategy` 抽象类提供 `on_tick`、`on_bar`、`on_order` 等回调，用户只需实现业务逻辑即可。  
- **订单管理**：完整的订单生命周期管理（发送、成交、撤销、停盘等），并提供实时持仓、成交记录查询。  
- **风险与绩效指标**：内置常用指标（夏普比率、最大回撤、信息比率、卡玛比率等），并支持自定义指标。  
- **可视化工具**：基于 Matplotlib/Plotly 的图表模块，支持 K 线、成交量、持仓、指标叠加等多种视图。  
- **参数优化**：提供网格搜索、随机搜索以及贝叶斯优化（`optuna`）接口，支持多目标优化。  
- **分布式并行**：利用 `multiprocessing` 或 `dask` 可在多核机器上并行跑多组参数。  
- **插件化**：支持自定义插件（如自定义事件、数据处理器、策略模板），使框架易于扩展。  
- **易于部署**：提供 Dockerfile 与 CI/CD 配置，支持快速构建与测试。

## 功能概览
| 功能 | 描述 |
|------|------|
| 数据读取 | `DataLoader` 支持 CSV、数据库、实时流等多种数据源。 |
| K 线生成 | 自动从 tick 生成多周期（1s、5s、1min、5min 等）K 线。 |
| 订单撮合 | 内置模拟撮合引擎，支持限价、市价、止损、止盈等多种订单类型。 |
| 资金管理 | 预设初始资金、手续费、滑点模型，支持多种杠杆与保证金模式。 |
| 绩效评估 | 计算收益率、年化收益、波动率、最大回撤、夏普比率、Sortino 比率等。 |
| 可视化 | `Chart` 模块支持绘制行情、持仓、交易信号、指标等多图。 |
| 参数优化 | `Optimizer` 提供网格搜索、随机搜索、Optuna 等多种优化算法。 |
| 日志与监控 | 通过 `logging` 输出详细运行日志，支持实时监控与告警。 |
| 单元测试 | 项目自带完整测试套件，覆盖核心模块。 |
| 文档与示例 | 内置完整 Markdown 文档与示例策略，帮助快速上手。 |

## 用法示例
```python
from hftbacktest import Backtest, Strategy, DataLoader, Chart

# 1. 加载数据
loader = DataLoader.from_csv("data/tick_data.csv")
data = loader.load()  # 返回 DataFrame

# 2. 定义策略
class MyStrategy(Strategy):
    def on_tick(self, tick):
        # 简单移动平均交叉示例
        if self.ma_short > self.ma_long:
            self.buy()
        elif self.ma_short < self.ma_long:
            self.sell()

# 3. 运行回测
bt = Backtest(data, MyStrategy, initial_capital=1e6, slippage=0.0005, commission=0.0003)
result = bt.run()

# 4. 查看绩效
print(result.summary())
print(result.performance)

# 5. 可视化
chart = Chart(data, result)
chart.plot()
```

### 参数优化
```python
from hftbacktest import Optimizer

opt = Optimizer(
    strategy=MyStrategy,
    data=data,
    param_grid={"ma_short": [5, 10, 20], "ma_long": [50, 100, 200]},
    metric="sharpe",  # 或 "max_drawdown"
)
best_params, best_result = opt.run()
print("Best params:", best_params)
```

### Docker 运行
```bash
docker build -t hftbacktest .
docker run -v $(pwd)/data:/data hftbacktest python run_backtest.py
```

> **注意**  
> - 回测时请确保 tick 数据已按时间顺序排序。  
> - 对于高频数据，建议使用 SSD 并开启多线程读取。  
> - 详细 API 文档请参见 `docs/` 目录。

--- 

> 以上内容已保存至 `src/content/docs/00/hftbacktest_nkaz001.md`。