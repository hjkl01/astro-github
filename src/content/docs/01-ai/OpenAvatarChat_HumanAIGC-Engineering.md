
---
title: OpenAvatarChat
---

# OpenAvatarChat 项目

## 项目地址
[GitHub 项目地址](https://github.com/HumanAIGC-Engineering/OpenAvatarChat/blob/main/readme_cn.md)

## 主要特性
OpenAvatarChat 是一个开源的多模态 AI 聊天项目，专注于构建可自定义的头像聊天系统。它支持文本、语音和视觉输入的集成，旨在提供自然、互动的 AI 对话体验。主要特性包括：
- **多模态支持**：结合文本、图像和语音，实现丰富的交互形式。
- **自定义头像**：用户可以上传或生成个性化头像，支持实时动画和表情变化。
- **开源框架**：基于 Python 和主流 AI 模型（如 Llama 或 Stable Diffusion），便于扩展和二次开发。
- **实时响应**：优化了延迟，支持流式输出，提升用户体验。
- **隐私保护**：本地部署选项，避免数据泄露。

## 主要功能
- **聊天交互**：支持文本聊天、语音输入/输出，以及基于图像的上下文理解（如描述图片内容）。
- **头像生成与动画**：集成 AI 模型生成虚拟头像，并通过动画引擎实现唇同步和表情动画。
- **模型集成**：兼容 Hugging Face 模型，支持本地或云端部署。
- **多语言支持**：包括中文界面和输入处理，适用于全球用户。
- **扩展插件**：提供 API 接口，便于集成到 Web 或移动应用中。

## 用法
1. **环境准备**：
   - 克隆仓库：`git clone https://github.com/HumanAIGC-Engineering/OpenAvatarChat.git`
   - 安装依赖：`pip install -r requirements.txt`（需 Python 3.8+ 和 PyTorch）。

2. **配置模型**：
   - 下载预训练模型（如从 Hugging Face Hub）。
   - 编辑 `config.yaml` 文件，设置模型路径、API 密钥（如果使用云服务）。

3. **运行项目**：
   - 启动服务器：`python app.py`
   - 访问 Web 界面（默认 http://localhost:8000），上传头像或选择预设。
   - 输入文本/语音开始聊天，系统将生成响应并动画化头像。

4. **自定义开发**：
   - 修改 `src/` 目录下的模块以添加新功能。
   - 测试：运行 `pytest` 进行单元测试。

更多细节请参考项目 README 文件。