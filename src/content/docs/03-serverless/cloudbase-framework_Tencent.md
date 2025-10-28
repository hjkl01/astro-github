
---
title: cloudbase-framework
---

# CloudBase Framework

## 项目地址
[https://github.com/Tencent/cloudbase-framework](https://github.com/Tencent/cloudbase-framework)

## 主要特性
CloudBase Framework 是腾讯云云开发（CloudBase）推出的开源框架，专为云原生应用开发设计。它基于 Serverless 架构，提供一站式解决方案，帮助开发者快速构建、部署和管理云端应用。主要特性包括：
- **Serverless 支持**：无缝集成腾讯云的云函数、云数据库、静态托管等服务，实现无服务器开发，降低运维成本。
- **多框架兼容**：支持 Vue.js、React、Next.js 等前端框架，以及 Node.js 等后端框架，适用于 Web、移动端和小游戏开发。
- **自动化部署**：通过 YAML 配置描述应用架构，一键部署到云端，支持 CI/CD 集成。
- **资源管理**：内置环境管理、域名配置、SSL 证书自动申请等功能，简化云资源操作。
- **安全性与扩展性**：集成腾讯云安全服务，支持自定义插件扩展，适用于企业级应用。
- **开源与社区**：完全开源，基于 Apache 2.0 许可，社区活跃，提供丰富模板和文档。

## 主要功能
- **应用模板**：预置多种应用模板，如单页应用（SPA）、全栈应用、微信小程序等，加速项目启动。
- **云资源编排**：使用 `cloudbase.yaml` 文件定义云函数、数据库表、存储桶等资源，实现声明式部署。
- **本地开发工具**：提供 CLI 工具，支持本地调试、热重载和模拟云环境。
- **监控与日志**：集成云开发控制台，实现实时监控、日志查询和性能分析。
- **多环境支持**：支持开发、测试、生产等多环境隔离管理，便于团队协作。
- **集成扩展**：可与 GitHub Actions、Jenkins 等工具集成，实现自动化流水线。

## 用法
1. **安装 CLI**：
   - 通过 npm 安装：`npm install -g @cloudbase/cli`
   - 或使用腾讯云 CLI：下载并配置腾讯云账号。

2. **初始化项目**：
   - 运行 `cloudbase init` 初始化项目，选择模板或自定义配置。
   - 编辑 `cloudbase.yaml` 文件，定义资源（如云函数路径、数据库 schema）。

3. **本地开发**：
   - 使用 `cloudbase dev` 启动本地服务器，模拟云环境进行开发和测试。
   - 支持热更新，修改代码后自动同步。

4. **部署应用**：
   - 运行 `cloudbase deploy` 一键部署到腾讯云环境。
   - 指定环境：`cloudbase deploy --env prod`。

5. **管理与扩展**：
   - 使用 `cloudbase env` 管理环境，`cloudbase functions` 操作云函数。
   - 集成插件：通过 `cloudbase plugin` 添加自定义功能，如数据库迁移。
   - 查看文档：参考 GitHub 仓库的 README 和示例项目进行高级用法。

更多细节请参考项目仓库的文档和示例。