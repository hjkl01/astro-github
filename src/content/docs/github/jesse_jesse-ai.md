
---
title: jesse
---

# Jesse - 适用于算法交易的框架

> 项目地址：<https://github.com/jesse-ai/jesse>

## 简介
Jesse 是一个用 Python 编写、面向消费级和专业交易者的算法交易框架。它支持多资产、多时间框架、自动化交易、回测与实时行情交互，帮助用户快速构建、测试、部署交易策略。

## 主要特性
| 特色 | 描述 |
|------|------|
| **多资产 & 多品种** | 支持股票、期货、外汇、ETF、加密货币等多种资产；一次部署即可交易多种品种。 |
| **多时间框架** | 单条策略可同时运行在日线、小时线、分钟线等多种周期，下单时自动同步。 |
| **离线回测 & 实时交易** | 同一接口可用于回测和实盘，策略代码无需修改即可切换。 |
| **自定义订单 & 路径** | 支持市价单、限价单、止盈止损、追踪止盈等。 |
| **数据源灵活** | 内置多种历史/实时行情接口（Binance、Kraken、Polygon、Alpha Vantage 等）。 |
| **容错与日志** | 自动重连、错误恢复；日志支持多级别和多输出（file, console, slack 等）。 |
| **易扩展** | 所有核心组件是开源、插件化，可自行添加自定义指标、信号生成器、风控模块。 |
| **社区 & 文档** | 维护活跃，文档齐全，示例策略覆盖常见用例。 |

## 主要功能

1. **策略开发**  
   - 纯 Python 代码编写，使用 `class` 或 `function` 形式定义策略。  
   - 支持 `on_tick`、`on_bar`、`on_order`、`on_position` 等回调，灵活响应市场事件。

2. **回测引擎**  
   - `backtesting` 与 `live` 模式共用接口，按时间序列逐帧执行。  
   - 支持多资产组合回测，生成收益曲线、Drawdown、夏普比率等指标。  
   - 支持离线历史数据多源与同义词转换。  

3. **实时交易**  
   - 与交易所（如 Binance、Kraken）实时连接，实时推送行情。  
   - 自动下单、撤单、获取订单状态、持仓信息。  
   - 支持多帐户多交易所并发交易。  

4. **风控 & 资金管理**  
   - 提供 `RiskManager`、`PositionSizer` 等内置组件。  
   - 可自定义风控策略：最大单笔风险、最大仓位、最大冲击损失等。  

5. **数据 & 策略仓库**  
   - `jaas`（Jesse Asset Aggregator System）自动下载和转换多源数据。  
   - 提供内置指标库（如 SMA, EMA, RSI, MACD、布林线等）。  

## 用法

1. **安装**  
   ```bash
   pip install jesse
   ```

2. **配置**  
   - 在项目根目录下创建 `config.py`，填写交易所 API Key、默认交易品种、时间框架等。  
   - 也可以通过 `jesse config set` 命令交互配置。

3. **编写策略**  
   - 在 `strategies` 目录下创建 `.py` 文件，继承 `Strategy`，实现所需回调。  
   ```python
   from jesse.strategies import Strategy

   class MyStrategy(Strategy):
       def __init__(self):
           super().__init__()
           # 初始化任何指标
       
       def on_bar(self):
           # 交易逻辑
           if self.ma_short > self.ma_long:
               self.buy()
   ```

4. **回测**  
   ```bash
   jesse backtest MyStrategy
   ```

5. **实时交易**  
   ```bash
   jesse start
   ```

   - 运行时会读取配置、加载策略、实时监听行情并执行交易。  

6. **查看报表**  
   回测完成后，报表自动生成在 `reports` 目录，可在浏览器打开 `index.html` 进行可视化评估。

## 相关资源
- 官方文档：https://jesse.ai/docs/  
- 示例策略：https://github.com/jesse-ai/jesse/tree/main/strategies  
- 社区讨论板块：https://github.com/jesse-ai/jesse/discussions  

---

