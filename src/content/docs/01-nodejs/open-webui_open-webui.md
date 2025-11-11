---
title: open-webui
---

# open‑webui/open‑webui

## 项目地址

[https://github.com/open-webui/open-webui](https://github.com/open-webui/open-webui)

## 主要特性

- **Web UI 接口**：提供可视化、易用的前端页面，适配默认 `OpenAI API` 与自建模型。
- **多模型支持**：可调用多种 LLM（如 GPT‑4、Claude、Vicuna 等），并支持自定义模型路径。
- **实时响应**：内置 WebSocket 支持，能够实现流式（Streaming）对话输出。
- **多用户/会话管理**：通过 `Auth` 实现用户注册、登录，支持多会话记录与恢复。
- **插件系统**：可通过 JSON 文件或 Swagger 接口实现第三方插件扩展，支持 Pipelines 插件框架。
- **语言支持**：默认多语言（英文、中国）切换是可配置，支持国际化（i18n）。
- **自定义数据层**：支持 SQLite、PostgreSQL、MySQL 等数据库，方便存储会话、历史等信息。
- **基于 Docker**：提供 Docker Compose 脚本，快速部署，支持 `nginx`、`traefik` 等反向代理。
- **RAG 集成**：内置本地 RAG 支持，支持文档交互和 Web 搜索增强。
- **图像生成**：集成 AUTOMATIC1111 API、ComfyUI 或 OpenAI DALL-E 进行图像生成。
- **语音/视频通话**：支持免提语音和视频通话功能。
- **模型构建器**：通过 Web UI 轻松创建 Ollama 模型，自定义角色和代理。
- **Python 函数调用**：内置代码编辑器，支持纯 Python 函数集成。
- **多模型对话**：同时与多个模型对话，利用各自优势。
- **角色-based 访问控制**：精细权限管理，确保安全访问。

## 功能说明

| 功能          | 说明                                                                                   |
| ------------- | -------------------------------------------------------------------------------------- |
| **对话**      | 文字输入后获取模型回应，可开启流式显示，支持多模型同时对话                             |
| **历史记录**  | 记录本地或数据库存储的聊天历史                                                         |
| **配置管理**  | 通过 `/settings` 页面设置 API Key、模型、基本参数（temperature, top_p, max_tokens 等） |
| **插件**      | 在 `tools` 页面启用或禁用内置工具（搜索、脚本、文件系统等），支持 Pipelines 扩展       |
| **多语言**    | UI 字段可按需切换，默认支持中文与英文，支持国际化                                      |
| **安全**      | 通过 `JWT`、`SSO` 或 SCIM 2.0 方式实现用户身份验证和权限管理                           |
| **RAG**       | 本地文档库和 Web 搜索集成，使用 `#` 命令查询文档或网站                                 |
| **图像生成**  | 集成图像生成工具，丰富对话内容                                                         |
| **语音/视频** | 支持免提语音和视频通话                                                                 |
| **模型构建**  | 通过 UI 创建和自定义模型、角色和代理                                                   |

## 快速使用（基于 Docker）

1. **克隆仓库**

   ```bash
   git clone https://github.com/open-webui/open-webui.git
   cd open-webui
   ```

2. **配置环境变量**

   ```bash
   cp .env.example .env
   # 填写你的 OpenAI API_KEY 或自建模型地址
   ```

3. **启动服务**

   ```bash
   docker compose up -d
   ```

4. **访问**  
   在浏览器中打开 `http://localhost:8787`（可根据自定义端口调整）即可使用 Web UI。

> **Tips**
>
> - 若想使用自建模型，只需在env`中设置`LANGCHAIN_ENDPOINT`与`LANGCHAIN_TRACING_V2`。
> - 开启 `SECURITY_ENABLED=true` 可启用登录保护。
> - `DATABASE_URL` 支持多种数据库，直接修改向量化存储类型即可。

## 本地开发

```bash
# 安装依赖
npm install
# 生成前端
npm run build
# 开发模式
npm run dev
```

> 本项目使用 Next.js + React + Tailwind CSS，所有路由均在 `src/pages` 目录。

## 文档与社区

- 官方文档：https://open-webui.com/docs
- 讨论组（Discord/Telegram）：可在官网首页链接查看。

---

> 以上内容为 open‑webui 的核心特性、功能与使用方式的简要说明，提供快速上手与部署指南。
