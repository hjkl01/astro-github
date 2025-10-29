
---
title: freqtrade
---


# freqtrade

> **项目地址**: <https://github.com/freqtrade/freqtrade>

---

## 项目简介
freqtrade 是一款开源、用于加密货币交易的自研交易机器人。它支持多种交易所、策略回测、实时交易、风险管理与自定义指标，适合想要自动化交易的开发者和量化研究者。

## 主要特性
- **多交易所支持**：内置对 Binance、Bybit、KuCoin、Coinbase Pro 等多家交易所的接口，支持统一 API 调用。
- **回测框架**：提供高性能历史数据回测，支持多周期、多条件、循环策略评估。
- **策略模板**：内置多种经典策略模板（如 MACD、RSI、布林带等），开发者可自由继承并自定义。
- **风险管理**：支持止损、止盈、仓位控制、最大亏损限制等多种风险控制手段。
- **多线程/多进程**：支持多线程执行多币种多策略，最大化 CPU 利用率。
- **可视化与监控**：集成前端 Dashboard，实时查看交易状态、盈利曲线、策略日志。
- **插件系统**：支持自定义插件（如自定义指标、交易信号、数据源等），易于扩展。
- **自动化部署**：Docker、Kubernetes、CI/CD 集成，便于在不同环境快速部署。

## 核心功能
| 功能 | 说明 |
|------|------|
| **策略开发** | 通过继承 `IStrategy` 接口编写自定义策略，支持多周期、异步、事件驱动。 |
| **数据获取** | 通过内置或自定义数据源获取历史行情，支持 CSV、数据库、API 接口。 |
| **回测** | 通过 `freqtrade backtesting` 命令执行历史回测，输出策略性能指标（Sharpe、Max Drawdown 等）。 |
| **实时交易** | 通过 `freqtrade trade` 命令实时监控行情并下单，支持 AutoTP/AutoSL。 |
| **监控** | Web Dashboard（Flask + SocketIO）展示订单、持仓、交易日志。 |
| **日志与报警** | 支持邮件、Telegram、Discord 等报警渠道，实时推送异常/关键事件。 |
| **版本控制** | 通过 `freqtrade version` 查看当前版本，支持多版本共存。 |

## 用法示例

1. **安装依赖**  
   ```bash
   git clone https://github.com/freqtrade/freqtrade.git
   cd freqtrade
   pip install -r requirements.txt
   ```

2. **配置文件**  
   ```bash
   freqtrade create-userdir --userdir user_data
   freqtrade create-config --config user_data/config.json
   ```
   根据 `config.json` 中的 `exchange`、`api_key`、`api_secret` 等字段完成交易所配置。

3. **编写策略**  
   在 `freqtrade/user_data/strategies` 下创建 `MyStrategy.py`，示例：
   ```python
   from freqtrade.strategy import IStrategy

   class MyStrategy(IStrategy):
       INTERFACE_VERSION = 2
       minimal_roi = {"0": 0.05}
       stoploss = -0.1
       timeframe = '5m'

       def populate_indicators(self, dataframe, metadata):
           dataframe['rsi'] = ta.RSI(dataframe['close'])
           return dataframe

       def populate_buy_trend(self, dataframe, metadata):
           dataframe.loc[
               (dataframe['rsi'] < 30) & (dataframe['close'] > dataframe['open']),
               'buy'] = 1
           return dataframe

       def populate_sell_trend(self, dataframe, metadata):
           dataframe.loc[
               (dataframe['rsi'] > 70),
               'sell'] = 1
           return dataframe
   ```

4. **回测**  
   ```bash
   freqtrade backtesting --strategy MyStrategy
   ```

5. **实时交易**  
   ```bash
   freqtrade trade --strategy MyStrategy
   ```

6. **监控**  
   ```bash
   freqtrade trade --strategy MyStrategy --max-open-positions 5
   # 打开浏览器访问 http://localhost:8080
   ```

## 进一步资源
- 官方文档: <https://www.freqtrade.io/en/latest/>
- GitHub Issues: <https://github.com/freqtrade/freqtrade/issues>
- Discord 社区: <https://discord.gg/freqtrade>
```
