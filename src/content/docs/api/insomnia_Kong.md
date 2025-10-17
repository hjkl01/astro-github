
---
title: insomnia
---

# Insomnia 项目

## 项目地址
[https://github.com/Kong/insomnia](https://github.com/Kong/insomnia)

## 主要特性
Insomnia 是一个开源的跨平台 API 客户端工具，由 Kong 公司开发，主要用于设计、测试和文档化 RESTful API 和 GraphQL API。它具有以下核心特性：
- **直观的用户界面**：简洁的图形界面，支持拖拽操作，便于快速构建和测试 API 请求。
- **支持多种协议**：兼容 HTTP/1.1、HTTP/2、WebSocket、GraphQL 等协议。
- **环境管理和变量支持**：允许创建多个环境（如开发、生产），并使用变量动态替换请求参数，提高测试效率。
- **请求模板和代码生成**：支持保存请求模板，并自动生成 cURL、Node.js 等语言的代码片段。
- **插件扩展**：可通过插件系统扩展功能，如添加认证、数据格式化等。
- **团队协作**：支持工作区共享、API 文档导出，便于团队协作。
- **离线工作**：无需网络即可编辑请求，同步时自动上传。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 系统。

## 主要功能
- **API 请求构建**：轻松创建 GET、POST、PUT、DELETE 等 HTTP 请求，支持头部、查询参数、请求体（JSON、XML、表单等）配置。
- **认证处理**：内置多种认证方式，包括 Basic Auth、Bearer Token、OAuth 2.0、API Key 等。
- **响应查看与调试**：实时显示响应状态码、头部、响应体，支持语法高亮和 JSON 美化。
- **集合管理**：将相关 API 请求组织成集合，支持导入/导出 OpenAPI、Postman 等格式。
- **GraphQL 支持**：内置 GraphQL 查询编辑器，自动生成 schema 和 introspection。
- **性能测试**：集成简单负载测试功能，监控 API 响应时间和错误率。
- **API 文档生成**：自动从请求生成交互式文档，便于分享和维护。

## 用法
1. **安装**：从 GitHub 仓库下载最新版本的安装包（支持 .exe、.dmg、.deb 等），或通过包管理器如 Homebrew（macOS: `brew install --cask insomnia`）安装。启动后，无需额外配置即可使用。
2. **创建新请求**：
   - 打开 Insomnia，点击 “New Request” 创建新请求。
   - 选择 HTTP 方法（如 GET），输入 URL。
   - 在 Headers 或 Body 标签页添加参数，例如 JSON 体：`{"key": "value"}`。
   - 点击 “Send” 发送请求，查看响应。
3. **管理环境**：
   - 在左侧面板创建新环境，定义变量如 `base_url: https://api.example.com`。
   - 在请求中使用 `{{ base_url }}/endpoint` 引用变量。
4. **保存和组织**：
   - 将请求保存到工作区或集合中。
   - 使用插件市场安装扩展，如 GQL 插件增强 GraphQL 支持。
5. **导入/导出**：
   - 支持从 Postman、Swagger 等导入 API 定义。
   - 导出为文档或代码，便于集成到项目中。
6. **高级用法**：对于复杂场景，结合插件实现自动化测试，或使用命令行模式（insomnia-core）集成 CI/CD 管道。

Insomnia 适合开发者、测试人员和 API 设计师使用，免费开源版本已覆盖大部分需求，付费版提供企业级功能如云同步。