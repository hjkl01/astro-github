---
title: pipelex
---

# Pipelex

## 功能

Pipelex 是一个开源语言，用于 AI 代理创建和运行可重复的 AI 工作流。它开发了开放标准用于可重复的 AI 工作流，让用户编写业务逻辑，而不是 API 调用。

- 将任务分解为聚焦的步骤，每个管道（pipe）处理一个清晰的转换。
- 使用概念（Concepts，具有意义的类型）来确保管道有意义。
- Pipelex 语言（.plx 文件）简单且人类可读，即使对于非技术用户。
- 每个步骤可以结构化和验证，提供软件的可靠性与 AI 的智能。
- 支持多种 AI 提供商，包括 OpenAI、Anthropic、Google 等。
- 提供 CLI 和 Python API 用于运行工作流。

## 用法

1. 安装 Pipelex：

   ```
   pip install pipelex
   pipelex init
   ```

2. 获取 API 密钥：
   - 免费 Pipelex API 密钥：加入 Discord 社区并请求免费 API 密钥。
   - 或使用自己的 API 密钥（OpenAI、Anthropic、Google 等）。

3. 生成第一个工作流：

   ```
   pipelex build pipe "描述你的工作流" --output results/workflow.plx
   ```

4. 运行管道：
   - 通过 CLI：
     ```
     pipelex run results/workflow.plx --inputs inputs.json
     ```
   - 通过 Python：

     ```python
     import asyncio
     import json
     from pipelex.pipeline.execute import execute_pipeline
     from pipelex.pipelex import Pipelex

     async def run_pipeline():
         with open("inputs.json", encoding="utf-8") as f:
             inputs = json.load(f)

         pipe_output = await execute_pipeline(
             pipe_code="workflow",
             inputs=inputs
         )
         print(pipe_output.main_stuff_as_str)

     Pipelex.make()
     asyncio.run(run_pipeline())
     ```

5. 使用 AI 助手迭代：
   ```
   pipelex kit rules
   ```

参考 [Pipelex 文档](https://docs.pipelex.com/) 开始使用。
