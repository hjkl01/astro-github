
---
title: zerox
---

# Zerox 项目

**GitHub 项目地址:** [https://github.com/getomni-ai/zerox](https://github.com/getomni-ai/zerox)

## 主要特性
Zerox 是一个开源的 AI 代理框架，由 Omni AI 开发，专注于简化 AI 代理的构建和部署。其核心特性包括：
- **模块化设计**：支持快速集成各种 LLM（大型语言模型）和工具链，便于自定义代理行为。
- **零配置部署**：提供一键式设置，减少开发者的配置负担，支持本地和云端运行。
- **多模态支持**：兼容文本、图像和工具调用，适用于聊天机器人、自动化任务等场景。
- **高效工具集成**：内置支持如 SerpAPI、浏览器自动化等工具，扩展性强。
- **安全性与可观测性**：包含日志记录、错误处理和 API 密钥管理，确保生产级应用的安全。

## 主要功能
- **代理构建**：允许开发者定义代理的角色、工具和提示模板，实现复杂任务自动化，如数据查询、内容生成。
- **工具链管理**：无缝集成外部 API 和本地工具，支持函数调用和状态管理。
- **交互式接口**：提供 Web UI 和 CLI 接口，便于测试和实时交互。
- **扩展性**：支持插件系统，用户可添加自定义工具或模型集成。
- **性能优化**：内置缓存机制和异步处理，提高响应速度。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/getomni-ai/zerox.git`
   - 进入目录：`cd zerox`
   - 安装依赖：`pip install -r requirements.txt`

2. **配置**：
   - 创建 `.env` 文件，添加 API 密钥（如 OpenAI API Key）。
   - 示例配置：
     ```
     OPENAI_API_KEY=your_key_here
     SERPAPI_API_KEY=your_serpapi_key
     ```

3. **运行示例**：
   - 启动 Web UI：`python app.py` 或使用 `streamlit run app.py`。
   - 通过 CLI 测试：`python zerox_cli.py --prompt "你的查询"`
   - 自定义代理：在 `agents/` 目录下编辑 YAML 文件定义代理逻辑，然后运行 `python run_agent.py`。

4. **高级用法**：
   - 集成自定义工具：继承 `Tool` 类并注册。
   - 部署到云端：使用 Docker 支持一键部署，参考 `Dockerfile`。

更多细节请参考仓库的 README 和文档。