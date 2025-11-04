
---
title: nautilus_trader
---

# Nautilus Trader

GitHub 地址: <https://github.com/nautechsystems/nautilus_trader>  

## 主要特性
- **高性能:** 采用事件驱动架构，支持高速行情与订单执行，毫秒级延迟。  
- **可扩展:** 模块化设计，便于自定义数据源、执行、风险管理、策略。  
- **多资产支持:** 同时支持股票、期货、期权、ETF、外汇等 instrument。  
- **实时与历史交易:** 兼容 WebSocket、REST、历史文件，支持回测与实盘同步。  
- **Thread‑safe & 并行:** 使用 asyncio 与多线程技术实现并发，保证数千条行情的流畅处理。  
- **跨平台:** 兼容 Linux、macOS、Windows；Docker 官方镜像供快速部署。  

## 核心功能
| 模块 | 主要职责 |
|------|----------|
| **Data Feed** | 统一接口解析多渠道行情，支持 `IBKR`, `PythoAPI`, `FIX`, `CSV` 等。 |
| **Execution** | 订单路由、撮合、状态跟踪，支持限价、市价、止损、止盈。 |
| **Position & Portfolio** | 自动维护持仓、成本、PnL、持仓限额。 |
| **Risk** | `PositionLimit`, `MarginCheck`, `MaxDrawdown` 等风险管理模块。 |
| **Strategy** | 生命周期回调 `on_start`, `on_tick`, `on_bar`, `on_order`, `on_trade`。 |
| **Backtesting Engine** | 回测接口、批量下载、滑点模型、手续费模型。 |
| **Trade Diary** | 记录交易日志、策略统计、报表导出。 |

## 用法

### 1. 环境搭建
```bash
# 安装依赖
pip install nautilus-trader

# 创建虚拟环境(可选)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 配置文件
创建 `config.yaml`（参考 `examples/config.yaml`）：
```yaml
broker:
  type: "IBKR"
  host: "127.0.0.1"
  port: 7497
  client_id: 1

data:
  provider: "IBKR"
  symbols: ["AAPL", "EURUSD", "ES"]

strategy:
  run_backtest: true
  data_path: "./backtest_data"
  start_date: "2022-01-01"
  end_date: "2022-12-31"
```

### 3. 编写策略
```python
# strategies/simple_moving_average.py
from nautilus_trader.strategies.base import Strategy

class MovingAverageStrategy(Strategy):
    def on_start(self):
        self.symbol = self.symbols[0]
        self.bar_window = 20
        self.add_bar(self.symbol, self.bar_window)

    def on_bar(self, bar):
        sma = bar.sma(self.bar_window)
        if bar.close > sma:
            self.market_order(self.symbol, 100)
        elif bar.close < sma:
            self.market_order(self.symbol, -100)
```

### 4. 运行
```bash
# 回测
nautilus run --config config.yaml --strategy strategies/simple_moving_average

# 实盘
nautilus run --config config.yaml --strategy strategies/simple_moving_average --live
```

### 5. 查看结果
- 回测报告保存在 `reports/`
- 实盘 Trade Diary 位于 `audit_log/`

---  

**备注:** 详细 API 文档参见 `docs/api`，或使用 `nautilus -h` 查看命令行帮助。