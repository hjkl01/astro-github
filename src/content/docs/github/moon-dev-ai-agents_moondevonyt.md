
---
title: moon-dev-ai-agents
---


# moon-dev-ai-agents

**GitHub 地址**  
[https://github.com/moondevonyt/moon-dev-ai-agents](https://github.com/moondevonyt/moon-dev-ai-agents)

## 项目简介
`moon-dev-ai-agents` 是一个基于 OpenAI API 的多智能体框架，支持在自定义环境中搭建、训练、评估与部署 AI 代理。项目通过统一的 Agent API、环境抽象与任务管理，实现了多 Agent 协作与竞争的实验平台。

## 主要特性
- **多 Agent 支持**：一次性管理、启动及监控多个代理，支持 Team/Cooperative 与 Competition 两种模式。  
- **环境抽象**：提供 `BaseEnvironment` 与 `BaseTask` 基类，用户可快速自定义游戏/仿真环境。  
- **可插拔模型**：支持 GPT 系列、Claude、Claude+、Claude-1.3 等多种 LLM，且可通过配置文件切换。  
- **多轮对话**：Agent 内置多轮对话管理，支持历史窗口、上下文长度限制。  
- **性能监控**：默认记录性能指标（token 消耗、时延、奖励等），可导出 CSV/JSON。  
- **可视化**：集成 `gymnasium` 环境可视化、`tensorboard` 训练日志与监控。  
- **脚本化训练**：提供 `train.py` 与 `evaluate.py` 脚本，可通过命令行参数完成完整实验流程。  
- **Docker 支持**：包含 `Dockerfile`，可快速构建并运行容器化实验环境。  

## 功能概览

| 功能 | 说明 |
|------|------|
| **Agent** | 负责决策、执行、与环境交互。支持自定义策略、奖励函数、语言模型。 |
| **Environment** | 包含状态、动作空间、奖励逻辑。可继承自 OpenAI Gym 或自定义。 |
| **Task** | 任务管理器，负责调度环境与 Agent，收集统计信息。 |
| **Trainer** | 训练循环，支持多 Agent 同时训、评估。 |
| **Evaluator** | 对已训练 Agent 进行多轮评估，生成报告。 |
| **Logger** | 统一日志、追踪与可视化。 |
| **Config** | 通过 YAML/JSON 配置文件统一管理实验参数。 |

## 快速上手

1. **克隆仓库**  
   ```bash
   git clone https://github.com/moondevonyt/moon-dev-ai-agents.git
   cd moon-dev-ai-agents
   ```

2. **创建并激活虚拟环境**  
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **配置 API Key**  
   在项目根目录创建 `.env` 并添加  
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

4. **运行示例**  
   ```bash
   python train.py --config configs/sample.yaml
   ```

   - `configs/sample.yaml` 里包含 Agent、Environment、Task、Trainer 的配置。  
   - 训练完成后会在 `results/` 生成日志与模型文件。

5. **评估**  
   ```bash
   python evaluate.py --config configs/sample.yaml --model_path results/model.pt
   ```

6. **Docker 部署（可选）**  
   ```bash
   docker build -t moon-dev-ai-agents .
   docker run -e OPENAI_API_KEY=your_api_key_here moon-dev-ai-agents python train.py --config configs/sample.yaml
   ```

## 定制化

- **自定义环境**  
  继承 `BaseEnvironment` 并实现 `reset()`、`step(action)`、`render()`。  
- **自定义 Agent**  
  继承 `BaseAgent` 并实现 `act(state)`。  
- **自定义任务**  
  继承 `BaseTask` 并实现 `run()`，可自定义多 Agent 的协同/竞争逻辑。

## 贡献

欢迎提交 Issue 与 Pull Request。请参考 `CONTRIBUTING.md` 了解贡献流程。

---

**项目地址**  
[https://github.com/moondevonyt/moon-dev-ai-agents](https://github.com/moondevonyt/moon-dev-ai-agents)
