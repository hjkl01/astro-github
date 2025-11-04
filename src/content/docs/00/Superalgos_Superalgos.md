
---
title: Superalgos
---


# Superalgos
[GitHub 地址](https://github.com/Superalgos/Superalgos)

Superalgos 是一个开源的量化交易平台，旨在让交易者、开发者和研究者能够快速搭建、测试、部署和优化自动化交易策略。该项目通过可视化界面与脚本化接口相结合，降低了构建复杂交易系统的门槛。

---

## 主要特性

| 类别 | 功能描述 |
|------|----------|
| **可视化工作流** | 通过拖拽式图形界面创建交易流程，支持多资产、跨交易所的数据输入与策略输出。 |
| **实时市场数据** | 支持 Binance、Coinbase、BitMEX 等主流交易所的 WebSocket 和 REST 接口；可自定义行情来源。 |
| **回测与优化** | 内置强大回测框架，支持多周期、多策略并行回测。可对参数进行网格搜索或遗传算法优化。 |
| **实时交易** | 通过统一的交易接口完成下单、撤单、查询账户、持仓等操作；支持模拟与真实账户。 |
| **监控与报警** | 实时监视策略运行、资金曲线、指标；可通过 Discord、Telegram、邮件等渠道触发报警。 |
| **插件化扩展** | 通过 JSON 描述文件添加自定义策略、指标、事件处理器；支持模块化团队协作。 |
| **社区与文档** | 维护完整的教程、示例项目和社区对接文档，方便上手与快速迭代。 |

---

## 关键功能

- **多资产 & 跨交易所**：一次配置即可接入多个交易所，进行多币种套利与分散交易。
- **策略集成**：支持基于布林带、移动均线、RSI、MACD 等技术指标的标准策略；亦可导入自定义指标。  
- **资金管理**：提供风控模块（最大连胜、止损、分批建仓等），保证策略稳健性。  
- **机器学习**：集成 TensorFlow、PyTorch 等框架，可直接导入训练好的模型进行预测交易。  
- **实时事件驱动**：事件总线机制实现高效分布式消息传递，支持交易逻辑与系统监控无缝耦合。  
- **监控面板**：内置 Grafana 风控，支持自定义仪表盘查看实时指标。  

---

## 用法一览

1. **克隆仓库**

   ```bash
   git clone https://github.com/Superalgos/Superalgos.git
   cd Superalgos
   ```

2. **安装依赖**

   项目基于 Node.js（>= 18）和 .NET Core（>= 7），以及 Python（可选）：

   ```bash
   # Node
   npm install

   # .NET Core
   dotnet restore
   ```

3. **配置连接与账户**

   编辑 `configurations/TradingAccounts.yaml`，填入交易所 API Key/Secret。  
   同时可在 `configurations/Feeds.yaml` 配置数据源。

4. **创建/编辑策略（可视化）**

   - 启动 Studio：`npm run start` 进入交互式界面。  
   - 通过拖拽 “Strategy” → “Indicator” → “Action” 等模块构建工作流。  
   - 保存为项目文件（`.yaml` 或 `.json`）。

5. **回测**

   ```bash
   npm run backtest --project=MyStrategy
   ```

   可在 `output/backtests` 查看回测结果、持仓曲线。

6. **实时交易**

   ```bash
   npm run run --project=MyStrategy
   ```

   账户实时监控、下单、止损等功能会自动触发。

7. **监控与报警**

   - 在 `configurations/Alerts.yaml` 配置报警渠道（Discord, Email 等）。  
   - 启动监控服务 `npm run monitor`。

---

## 典型使用场景

| 场景 | 说明 |
|------|------|
| **算法交易** | 通过回测验证策略逻辑后直接投放实时交易。 |
| **量化研究** | 结合数据分析与机器学习模型快速迭代。 |
| **教育与培训** | 可视化界面降低学习门槛，适合教学或团队协作。 |
| **风控与合规** | 集成资金管理、交易限额、合规报告生成。 |

---

> **注**：项目持续更新，请关注 GitHub 里的发布版与文档维护。  
> 若需帮助，可加入官方 Discord 讨论组，或在 Issues 提问。

---