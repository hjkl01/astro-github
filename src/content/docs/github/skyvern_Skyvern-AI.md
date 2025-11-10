---
title: skyvern
---


# Skyvern AI

**项目地址**  
[https://github.com/Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)

## 主要特性

| 特色 | 简述 |
|------|------|
| **Web 自动化** | 通过浏览器驱动（Puppeteer/Playwright）对指定页面进行自动化操作。|
| **GPT‑4 强化** | 利用 OpenAI GPT‑4 进行任务规划、自然语言理解和决策。|
| **策略与权限控制** | 通过 Policy Engine 对助手行为进行安全审查，防止恶意执行。|
| **可视化脚本化** | 任务以 YAML/JSON 描述，可视化编辑并快速复用。|
| **状态保持与恢复** | 记录执行状态，支持断点续作与多线程并发。|
| **插件化扩展** | 支持自定义 Action 与 Inspector，便于接入第三方 API。|

## 主要功能

1. **任务生成**  
   - 输入自然语言指令，模型生成可执行的步骤列表。  
   - 由 `TaskPlanner` 通过 `OpenAI` 做意图解析。  

2. **步骤执行**  
   `Executor` 调用浏览器动作（点击、输入、滚动等）。  
   - 支持多端实现，默认使用 Playwright。  

3. **数据采集**  
   - 在执行时自动收集页面表单、表格、文本块等。  
   - `Inspector` 模块可自定义要采集的元素。  

4. **安全审计**  
   - `PolicyEngine` 使用预定义规则校验即将执行的操作。  
   - 可以自定义白名单/黑名单对策略进行细粒度控制。  

5. **调试与日志**  
   - 完整的执行日志与截图追踪。  
   - 支持回滚与错误恢复。  

## 快速上手

```bash
# 1. 克隆仓库
git clone https://github.com/Skyvern-AI/skyvern.git
cd skyvern

# 2. 创建并激活虚拟环境
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\\Scripts\\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量
cp .env.example .env
# 在 .env 中填写 OPENAI_API_KEY 等参数

# 5. 启动浏览器驱动（Playwright）
playwright install

# 6. 运行示例
python examples/run_demo.py
```

> **提示**：如想在浏览器里实时观察执行过程，可开启 `DEBUG=true`。

## 高级使用

- **自定义 Action**  
  在 `actions/` 目录新增 Python/Python 函数，遵循 `ActionBase` 接口。  
- **策略自定义**  
  在 `policies/` 目录添加 JSON/YAML 规则，PloicyEngine 将自动加载。  
- **多线程并发**  
  配置 `config.yaml` 的 `concurrency` 参数，支持并行执行多个任务。  

## 文档与社区

- `docs/` 目录下包含完整使用手册与开发者指南。  
- 关注 `#skyvern-ai` 讨论，以获取最新更新与实战技巧。  

---  

> **说明**：本文档仅供快速参考，具体细节请参阅项目源文件与官方文档。  

_Path:_ `src/content/docs/00/skyvern_Skyvern-AI.md`
