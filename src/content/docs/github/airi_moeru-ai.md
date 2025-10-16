
---
title: airi
---

# Airi 项目

**项目地址:** [https://github.com/moeru-ai/airi](https://github.com/moeru-ai/airi)

## 主要特性
Airi 是一个开源的 AI 聊天机器人项目，基于先进的语言模型构建。主要特性包括：
- **多模态支持**：支持文本聊天、图像生成和多语言交互。
- **自定义配置**：用户可以轻松集成各种 AI API，如 OpenAI、Stable Diffusion 等。
- **用户友好界面**：提供 Web 界面和命令行工具，便于部署和使用。
- **开源与可扩展**：使用 Python 开发，模块化设计，便于二次开发和插件扩展。
- **隐私保护**：本地部署选项，确保数据不外泄。

## 功能
- **聊天交互**：实时与 AI 对话，支持上下文记忆和角色扮演。
- **图像生成**：集成 AI 模型生成图片，根据文本提示创建艺术作品。
- **API 集成**：支持多种后端服务，如 Hugging Face 或本地模型。
- **自动化脚本**：可用于构建聊天机器人、内容生成工具或自动化助手。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 系统。

## 用法
1. **克隆仓库**：
   ```
   git clone https://github.com/moeru-ai/airi.git
   cd airi
   ```

2. **安装依赖**：
   ```
   pip install -r requirements.txt
   ```

3. **配置环境**：
   - 编辑 `config.yaml` 文件，设置 API 密钥（如 OpenAI API Key）。
   - 对于图像生成，安装额外依赖如 `diffusers`。

4. **运行项目**：
   - Web 界面：`python app.py`（默认在 http://localhost:5000 启动）。
   - 命令行模式：`python cli.py` 并输入提示。

5. **示例使用**：
   - 在 Web 界面中输入文本提示，如“描述一个未来城市”，AI 将生成响应或图像。
   - 对于开发者：通过 API 端点集成到其他应用中，参考 `docs/api.md`。

更多细节请参考仓库中的 README 和文档。