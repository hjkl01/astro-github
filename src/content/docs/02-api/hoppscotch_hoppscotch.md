---
title: hoppscotch
---


# Hoppscotch

[项目地址](https://github.com/hoppscotch/hoppscotch)

## 主要特性

- **轻量级的 API 调试工具**：与 Postman 类似，但完全开源、免费、无联网限制。  
- **多协议支持**：REST、GraphQL、WebSocket、gRPC 等协议均在同一界面可直接操作。  
- **环境与变量管理**：可自定义环境（如开发/测试/生产）、全局变量、会话变量，支持批量导入/导出。  
- **收藏夹与请求列表**：按项目/文件夹组织请求，支持标签、收藏、搜索。  
- **团队协作**：通过项目标识（Project）实现团队共享请求、环境与 API 文档。  
- **本地存储**：使用 IndexedDB / localStorage，数据可离线使用；支持导入/导出 `JSON-LM` 包。  
- **插件化/扩展**：可通过配置实现自定义请求头、脚本、OAuth2 授权等。  
- **快速生成**：支持 Postman、cURL、HTTPie 等格式的导出与生成。  
- **响应可视化**：自动格式化 JSON、XML、HTML、图片、二进制文件；支持头信息、Cookies、网络监控等。  
- **安全功能**：支持自定义 TLS、证书、代理、代理验证、IP 白名单等。  

## 功能模块

| 模块 | 说明 |
|------|------|
| **REST** | 标准的 GET/POST/PUT/DELETE 请求，支持多种 Content‑Type 与 Body 类型。 |
| **GraphQL** | 代码高亮、Schema Introspection、变量 & 请求片段管理，支持 GraphQL Playground 样式。 |
| **WebSocket** | 消息订阅、发送、断开重连，支持多会话并行。 |
| **gRPC** | 通过 Protocol Buffers 可视化请求；支持文件拖拽、自动生成请求。 |
| **Fuzz** | 随机数据生成与测试，支持多种输入策略。 |
| **Tracker** | 请求监控与历史记录，支持过滤、导出为 CSV/JSON。 |

## 快速使用

```bash
# 克隆项目
git clone https://github.com/hoppscotch/hoppscotch.git
cd hoppscotch

# 安装依赖（推荐 pnpm）
pnpm i

# 本地开发
pnpm dev
```

- 访问 `http://localhost:5173`，即可使用 web 端。  
- 直接拖入 `.json` 或 `.har` 文件快速导入请求。  
- 在左侧面板中切换 **REST / GraphQL / WebSocket / gRPC**。  
- 使用 `Ctrl+S`（Windows）/`Cmd+S`（Mac）保存请求并同步到本地存储。  
- 点击 **Share** 按钮可生成可访问链接，供团队成员查看与编辑。  
- 在 **Settings → Environments** 中添加或编辑环境变量，支持 `{{varName}}` 语法在请求中使用。  

## 开发与贡献

```bash
# 打包
pnpm build
# 生成静态文件（可部署到 Vercel, Netlify 等）
pnpm preview
```

- 项目基于 **Vue 3 + Pinia + Vite**，代码结构按 `src/` 下的文件夹划分。  
- Pull Request 前请先运行 `pnpm lint` 与 `pnpm test`，确保通过代码检查与单元测试。  
- 任何关于功能、Bug 或文档改进的建议可通过 Issues 或 PR 进行提交。  

---  

> 这份 Markdown 文档仅作本地展示使用，若需同步到仓库，请自行将其放置在 `src/content/docs/00/hoppscotch_hoppscotch.md` 路径下。