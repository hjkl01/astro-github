---
title: highlight
---

# Highlight 项目

**GitHub 项目地址:** [https://github.com/highlight/highlight](https://github.com/highlight/highlight)

## 主要特性
Highlight 是一个开源的开发者体验平台，主要专注于实时会话录制、错误监控和性能分析。它提供以下核心特性：
- **会话重放（Session Replay）**：捕获用户在前端应用的交互行为，包括点击、滚动和输入，实现完整的用户会话回放，帮助开发者诊断用户体验问题。
- **错误监控（Error Monitoring）**：实时追踪前端和后端的错误、崩溃和异常，提供详细的堆栈跟踪和上下文信息，支持多语言（如 JavaScript、Python 等）。
- **性能监控（Performance Monitoring）**：分析应用性能指标，如加载时间、API 响应延迟和资源使用，帮助优化应用速度和效率。
- **日志管理和搜索**：集成日志收集，支持高级搜索和过滤，便于快速定位问题。
- **开源和可自托管**：完全开源，支持自托管部署，避免数据隐私问题；同时提供云端托管选项。
- **集成支持**：与多种框架和工具集成，如 React、Vue、Node.js、Kubernetes 等；支持 Slack、PagerDuty 等通知集成。
- **数据隐私合规**：内置隐私保护机制，如模糊敏感数据，符合 GDPR 等法规。

## 主要功能
- **实时监控仪表盘**：可视化界面显示错误率、性能指标和会话数据，支持自定义警报和团队协作。
- **代码级调试**：提供源映射（Source Maps）支持，直接在浏览器中重现错误位置。
- **分布式追踪**：追踪请求在微服务架构中的传播路径，识别瓶颈。
- **移动端支持**：兼容 iOS 和 Android 应用监控。
- **API 和 SDK**：提供 JavaScript、Python、Go 等语言的 SDK，便于集成到现有项目中。

## 用法
1. **安装和集成**：
   - 对于前端：通过 npm 安装 SDK，例如 `npm install @highlight-run/client`，然后在应用中初始化：`H.init('<project_id>')`。
   - 对于后端：使用相应语言的 SDK，如 Python 的 `pip install highlight-io`，并配置 `highlight.init('<project_id>', '<api_key>')`。
   - 详细集成指南见 [官方文档](https://www.highlight.io/docs)。

2. **自托管部署**：
   - 克隆仓库：`git clone https://github.com/highlight/highlight.git`。
   - 使用 Docker Compose 部署：运行 `docker-compose up`（需配置环境变量如数据库连接）。
   - 支持 Kubernetes 和 Helm Charts 部署，适用于生产环境。

3. **使用流程**：
   - 创建项目：在 Highlight 仪表盘中注册并生成 Project ID。
   - 集成 SDK 到你的应用中，自动开始收集数据。
   - 在仪表盘查看报告：搜索错误、回放会话或分析性能。
   - 设置警报：配置阈值通知，如错误率超过 5% 时发送 Slack 消息。

该项目适合开发团队用于提升应用可靠性和用户体验，社区活跃，更新频繁。