
---
title: TradingAgents-CN
---


# TradingAgents-CN

> 项目地址: <https://github.com/hsliuping/TradingAgents-CN>

## 项目简介
`TradingAgents-CN` 是一个面向中文金融数据的多智能体交易框架。它基于 OpenAI Gym 兼容接口，提供了多种交易环境、标准化的数据预处理、可扩展的智能体模板以及完整的训练、评估与可视化工具。适用于强化学习、深度学习及传统机器学习方法在股票、期货、期权等资产上的交易策略研究。

## 主要特性
- **多环境支持**：单资产、组合资产、跨市场对冲等多种交易环境，均可直接使用 Gym 接口调用。
- **标准化数据接口**：支持 CSV、数据库、API 等多种数据源，统一为 `pandas.DataFrame` 形式，方便后续特征工程。
- **可插拔智能体**：内置多种经典智能体（DQN、DDPG、PPO、TD3、A2C 等），并提供模板可快速自定义新算法。
- **分布式训练**：支持 Ray、RLlib 等框架，可在多 GPU/多节点环境下加速训练。
- **评估与可视化**：内置收益曲线、夏普率、最大回撤等指标计算，并可导出 Matplotlib/Plotly 图表。
- **中文文档与示例**：所有代码均附有中文注释和示例脚本，降低学习门槛。

## 目录结构（核心）
```
TradingAgents-CN/
├── envs/              # 交易环境实现
├── agents/            # 代理实现与模板
├── data/              # 数据预处理脚本
├── configs/           # 训练与评估配置文件
├── scripts/           # 训练、评估、可视化脚本
├── requirements.txt
└── README.md
```

## 用法

### 1. 环境搭建
```bash
# 克隆仓库
git clone https://github.com/hsliuping/TradingAgents-CN.git
cd TradingAgents-CN

# 创建虚拟环境（推荐使用 conda）
conda create -n trading_agents python=3.10
conda activate trading_agents

# 安装依赖
pip install -r requirements.txt
```

### 2. 数据准备
```python
# 例：将 CSV 数据转化为标准格式
from trading_agents.data import dataset_loader

dataset = dataset_loader.load_csv(
    path="data/stock_2023.csv",
    columns=["date", "open", "high", "low", "close", "volume"]
)
dataset.to_pickle("data/stock_2023.pkl")
```

### 3. 训练示例
```bash
# 使用默认配置训练
python scripts/train.py --config configs/default.yaml
```
或自定义配置：
```bash
python scripts/train.py --config configs/my_agent.yaml
```

### 4. 评估与可视化
```bash
# 评估训练好的模型
python scripts/evaluate.py --model_path checkpoints/agent_1.pth --data_path data/stock_2023.pkl

# 绘制收益曲线
python scripts/plot_results.py --results_path results/agent_1.json
```

### 5. 自定义智能体
```python
# 在 agents/ 下创建 new_agent.py
from trading_agents.agents.base import BaseAgent

class MyAgent(BaseAgent):
    def __init__(self, env):
        super().__init__(env)
        # 初始化网络、优化器等

    def step(self, observation):
        # 根据 observation 计算动作
        return action
```
然后在配置文件中指定 `agent_class: MyAgent`。

## 贡献
欢迎提交 Issue 或 PR，帮助完善文档、扩展环境或添加新算法。

## 许可证
MIT License

--- 
> 以上内容已保存为 `src/content/docs/00/TradingAgents-CN_hsliuping.md`。