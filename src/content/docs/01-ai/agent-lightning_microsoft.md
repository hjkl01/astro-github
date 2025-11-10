---
title: agent-lightning
---


# Agent Lightning（Microsoft）

## 项目地址
[https://github.com/microsoft/agent-lightning](https://github.com/microsoft/agent-lightning)

## 主要特性
- **轻量级框架**：专为快速构建对话型 AI 代理而设计，避免不必要的复杂性。
- **模块化组件**：Agent、Skill、Memory、Environment、Planner 等核心模块可独立组合。
- **可插拔的 LLM**：支持 OpenAI、Azure OpenAI、Anthropic 等多种后端。
- **链式思维**：自动生成 Chain of Thought，提升推理质量。
- **状态管理**：支持内存、外部数据库等多种状态存储方案。
- **可视化调试**：内置日志与调试工具，帮助开发者快速定位问题。

## 核心功能

| 功能 | 说明 |
|------|------|
| **Agent** | 负责决策与执行，调用注册的 Skills。 |
| **Skill** | 单一职责的功能模块，封装具体操作（如查询、计算、API 调用）。 |
| **Memory** | 存储对话历史、上下文信息，支持检索式记忆。 |
| **Planner** | 根据目标生成行动序列，支持多步推理。 |
| **Environment** | 定义 Agent 与外部世界交互的接口。 |

## 使用方式

1. **安装**  
   ```bash
   pip install agent-lightning
   ```

2. **创建 Agent**  
   ```python
   from agent_lightning import Agent, Skill, Memory

   class SummarizeSkill(Skill):
       def execute(self, input_text: str) -> str:
           # 调用 LLM 生成摘要
           return self.llm.generate(f"Summarize: {input_text}")

   memory = Memory()
   agent = Agent(memory=memory)
   agent.register_skill("summarize", SummarizeSkill())
   ```

3. **运行**  
   ```python
   response = agent.run("请帮我摘要下面的文章：<文章内容>")
   print(response)
   ```

4. **配置文件**（可选）  
   在项目根目录放置 `agent_lightning.yml`，示例内容：  
   ```yaml
   llm:
     provider: openai
     api_key: ${OPENAI_API_KEY}
     model: gpt-4o
   memory:
     type: in_memory
   skills:
     - name: summarize
       module: my_skills.summarize
   ```

5. **CLI**  
   ```bash
   agent-lightning run --config agent_lightning.yml
   ```

## 文档与示例
- 官方文档：<https://github.com/microsoft/agent-lightning/blob/main/docs/>
- 示例项目：<https://github.com/microsoft/agent-lightning/tree/main/examples>
