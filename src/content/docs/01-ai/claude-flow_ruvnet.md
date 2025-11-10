---
title: claude-flow
---


# Claude Flow (ruvnet)

**项目地址**: https://github.com/ruvnet/claude-flow

## 项目简介
Claude Flow 是一个轻量级、可扩展的工作流框架，专为与 Claude（OpenAI 的大语言模型）交互而设计。它通过“步骤（step）”的概念，帮助开发者将复杂的文本生成、数据转换与业务逻辑拆解为可复用、可组合的单元，从而实现高效、可维护的 AI 工作流。

## 主要特性
| 特性 | 说明 |
|------|------|
| **声明式步骤** | 使用装饰器 `@flow.step` 定义步骤，天然支持依赖注入与参数传递。 |
| **上下文管理** | 自动维护 `FlowContext`，在步骤间共享数据，支持 `yield` 输出与 `await` 异步调用。 |
| **错误恢复** | 内置重试机制，步骤失败后可配置继续执行或终止。 |
| **缓存 & 版本控制** | 支持结果缓存，避免重复调用 Claude，且可通过 `flow.version` 管理版本。 |
| **可视化调试** | 通过 `flow.debug()` 打印执行图，帮助定位瓶颈与错误。 |
| **插件体系** | 通过 `flow.register_plugin()` 可扩展第三方服务（如数据库、日志、监控）。 |
| **轻量依赖** | 仅需 `claude_api` 与 Python 标准库，无需额外的工作流引擎。 |

## 功能概述
- **Flow 类**：核心入口，用于注册、执行与管理步骤。  
- **Step 装饰器**：把普通函数变为可管理的步骤，支持同步与异步。  
- **FlowContext**：步骤间共享的上下文对象，支持键值存取。  
- **Result 处理**：统一返回结构，包含 `data`、`meta` 与 `error`。  
- **CLI 工具**：`claude-flow` 命令行可直接运行 `.flow.py` 脚本。  

## 快速开始

1. **安装**  
   ```bash
   pip install claude-flow
   ```

2. **创建工作流**  
   ```python
   from claude_flow import Flow

   flow = Flow(name="example_flow")

   @flow.step
   def hello(context):
       return f"Hello, {context.get('name', 'World')}!"

   @flow.step
   async def ask_claude(context):
       # 调用 Claude API（示例）
       response = await context.claude.complete(
           prompt=context['previous_output'],
           model="claude-3-haiku-20240307"
       )
       return response.output

   # 运行
   result = flow.run({"name": "Claude Flow"})
   print(result)
   ```

3. **使用缓存**  
   ```python
   @flow.step(cache=True)
   def expensive_step(context):
       # 长时间计算
       ...
   ```

4. **错误重试**  
   ```python
   @flow.step(retries=3)
   def unreliable_step(context):
       # 可能抛错
       ...
   ```

## 示例

### 1. 生成产品描述
```python
@flow.step
def get_product_info(context):
    return {
        "title": "超轻便笔记本",
        "features": ["14英寸屏幕", "轻量化设计", "续航长达12小时"]
    }

@flow.step
def generate_description(context):
    prompt = f"请根据以下信息生成产品描述：{context['product_info']}"
    response = await context.claude.complete(prompt, model="claude-3-5-sonnet-20240620")
    return response.output

result = flow.run()
print(result['generated_description'])
```

### 2. 多步对话
```python
@flow.step
def ask_user(context):
    return input("请输入你的问题：")

@flow.step
def ask_claude(context):
    prompt = context['user_question']
    response = await context.claude.complete(prompt, model="claude-3-haiku-20240307")
    return response.output

@flow.step
def summarize(context):
    return f"Claude 的回答是：{context['ask_claude_output']}"

flow.run()
```

## 文档与参考

- **完整 API 文档**: https://github.com/ruvnet/claude-flow/blob/main/docs/api.md  
- **示例项目**: https://github.com/ruvnet/claude-flow/tree/main/examples  
- **贡献指南**: https://github.com/ruvnet/claude-flow/blob/main/CONTRIBUTING.md  

> 该项目旨在简化与 Claude 的交互，帮助开发者快速构建可组合、可复用的 AI 工作流。欢迎贡献与讨论！

``` 
