
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
- **插件系统**：可通过 JSON 文件或 Swagger 接口实现第三方插件扩展。  
- **语言支持**：默认多语言（英文、中国）切换是可配置。  
- **自定义数据层**：支持 SQLite、PostgreSQL、MySQL 等数据库，方便存储会话、历史等信息。  
- **基于 Docker**：提供 Docker Compose 脚本，快速部署，支持 `nginx`、`traefik` 等反向代理。  

## 功能说明  

| 功能 | 说明 |
|------|------|
| **对话** | 文字输入后获取模型回应，可开启流式显示 |
| **历史记录** | 记录本地或数据库存储的聊天历史 |
| **配置管理** | 通过 `/settings` 页面设置 API Key、模型、基本参数（temperature, top_p, max_tokens 等） |
| **插件** | 在 `tools` 页面启用或禁用内置工具（搜索、脚本、文件系统等） |
| **多语言** | UI 字段可按需切换，默认支持中文与英文 |
| **安全** | 通过 `JWT` 或 `SSO` 方式实现用户身份验证 |

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
> - 若想使用自建模型，只需在env` 中设置 `LANGCHAIN_ENDPOINT` 与 `LANGCHAIN_TRACING_V2`。  
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
