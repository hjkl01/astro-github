---
title: n8n
---

# n8n 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/n8n-io/n8n)

## 主要特性
n8n 是一个开源的工作流自动化工具，类似于 Zapier 或 Node-RED，但完全免费且自托管。它基于 Node.js 构建，支持可视化拖拽式界面设计工作流。主要特性包括：
- **节点式工作流设计**：使用节点（nodes）连接各种服务和 API，实现自动化任务。
- **超过 400 个集成**：内置支持数百种应用和服务，如 Slack、Google Sheets、Email、数据库（MySQL、PostgreSQL 等）和自定义 HTTP 请求。
- **自托管与云部署**：可运行在本地服务器、Docker 或云平台，支持数据隐私控制。
- **AI 集成**：内置 AI 节点，支持 OpenAI、LangChain 等，实现智能自动化。
- **错误处理与重试**：内置机制确保工作流可靠运行，支持条件分支、循环和错误恢复。
- **开源与社区驱动**：MIT 许可，活跃社区贡献新节点和模板。
- **安全性**：支持 OAuth、API 密钥和环境变量配置，适合企业级使用。

## 主要功能
n8n 的核心功能是自动化重复性任务，例如：
- **数据同步**：从一个应用（如 Google Forms）拉取数据，处理后推送到另一个（如 Slack 或数据库）。
- **通知与警报**：监控事件（如新邮件或网站变化），自动发送通知。
- **API 集成**：连接 REST/GraphQL API，实现复杂的数据转换和处理。
- **定时任务**：使用 Cron 表达式调度工作流，支持 webhook 触发。
- **文件处理**：上传/下载文件、CSV/JSON 解析和生成报告。
- **协作与扩展**：支持团队共享工作流、自定义节点开发，以及与 GitHub 等工具集成。

## 用法指南
### 安装
1. **前提**：安装 Node.js（v18+）和 npm。
2. **快速启动**：
   - 克隆仓库：`git clone https://github.com/n8n-io/n8n.git`
   - 进入目录：`cd n8n`
   - 安装依赖：`npm install`
   - 启动：`npm start` 或使用 Docker：`docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`
3. **访问界面**：浏览器打开 `http://localhost:5678`，默认用户 `demo`，密码 `demo`（生产环境请修改）。

### 创建工作流
1. **登录界面**：点击 “New Workflow” 开始新建。
2. **添加节点**：从左侧面板拖拽节点（如 Trigger: Manual 或 Schedule Trigger）。
3. **连接节点**：拖线连接节点，配置每个节点的凭证和参数（例如，连接 Gmail 需要 OAuth 认证）。
4. **测试与激活**：点击 “Execute Workflow” 测试，满意后激活以实时运行。
5. **示例工作流**：
   - 监控 RSS 订阅：RSS 节点 → 过滤节点 → Slack 通知节点。
   - 数据备份：Cron 触发 → Google Drive 下载 → 数据库插入。
6. **高级用法**：使用表达式（如 `{{ $json.field }}`）动态数据传递；导出/导入 JSON 工作流；通过 API 管理工作流（`/api/v1/workflows`）。

更多细节参考官方文档：https://docs.n8n.io/