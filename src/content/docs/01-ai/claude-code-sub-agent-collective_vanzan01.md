
---
title: claude-code-sub-agent-collective
---


# Claude Code Sub‑Agent Collective

**项目地址**  
<https://github/vanzan01/claude-code-sub-agent-collective>

## 1. 主要特性
| 序号 | 特性 | 说明 |
|------|------|------|
| 1 | **多 Agent 合作** | 集成了多个子代理（Code Generation、Code Execution、Code Evaluation），在 Claude 之上实现端到端代码开发流水线。 |
| 2 | **高效代码生成** | 通过自定义 prompt 与上下文，快速生成满足业务需求的 Python/JavaScript/Go 等语言代码片段。 |
| 3 | **自动化执行与调试** | 代码片段会在沙盒环境中自动执行，捕获异常并返回错误日志，支持循环调试。 |
| 4 | **即时评估与改进** | 运行结果与预期做对比，使用评分模型给出改进建议，支持多轮迭代。 |
| 5 | **插件式扩展** | 通过 `REGISTERED_AGENT` 字典可轻松添加新的子代理，支持自定义功能。 |
| 6 | **可视化接口** | 基于 FastAPI + React 的 web UI，支持代码输入、执行日志查看与版本管理。 |

## 2. 功能概览
1. **Code Generation Agent**
   * 接受业务描述和约束（语言、代码风格、文件结构），返回完整代码或函数体。
2. **Code Execution Agent**
   * 在 Docker / sandbox 环境中执行代码，返回 stdout、stderr 和异常信息。
3. **Code Evaluation Agent**
   * 解析标准输入/输出或单元测试结果，对执行结果评分并生成改进建议。
4. **Workflow Manager**
   * 顺序调用上述 Agent，实现“描述 → 生成 → 执行 → 评估 → 迭代”的闭环流程。
5. **CLI 与 API**
   * `claude-sub-agent` CLI：`claude-sub-agent run <prompt>`  
   * REST API：`POST /run` (body: prompt, language, options)

## 3. 用法示例

### 3.1 安装
```bash
pip install -e .
```

### 3.2 运行命令行
```bash
claude-sub-agent generate "用 Python 实现快速排序" --lang python
```

### 3.3 调用 REST API
```bash
curl -X POST http://localhost:8000/run \
     -H "Content-Type: application/json" \
     -d '{
           "prompt":"实现一个读取 CSV 的函数",
           "lang":"python"
         }' | jq .
```

### 3.4 在项目中扩展
```python
from claude_code_sub_agent_collective import AgentRegistry

# 自定义 Agent
class MyCustomAgent:
    def run(self, input_text: str) -> str:
        # 你的实现
        return "自定义结果"

# 注册
AgentRegistry.register("my_custom_agent", MyCustomAgent)
```

## 4. 开发规范
- **代码风格**：遵循 PEP8（Python）或对应语言规范。  
- **单元测试**：使用 `pytest`，所有子代理至少包含 80% 覆盖率。  
- **CI/CD**：项目已集成 GitHub Actions，自动化测试并发布 Docker 镜像。  

## 5. 贡献
1. Fork 本仓库。  
2. 新建 Feature 分支。  
3. 提交 PR 并说明所实现的功能。  

---
*如需更多细节，请参阅项目 README 与 Wiki。*

