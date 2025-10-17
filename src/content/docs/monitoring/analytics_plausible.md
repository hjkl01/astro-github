
---
title: analytics
---

# Plausible Analytics 项目概述

## 项目地址
[https://github.com/plausible/analytics](https://github.com/plausible/analytics)

## 主要特性
Plausible Analytics 是一个开源的、注重隐私的网站分析工具，旨在提供轻量级、透明的流量统计解决方案。它避免了传统分析工具（如 Google Analytics）常见的跟踪 cookie 和数据收集问题。主要特性包括：
- **隐私优先**：不使用 cookie 或个人数据跟踪，符合 GDPR 和 CCPA 等隐私法规。
- **轻量级脚本**：JavaScript 跟踪代码体积小（约 1KB），加载速度快，不影响网站性能。
- **开源与自托管**：完全开源，用户可以自托管实例，避免依赖第三方服务。
- **简单仪表盘**：提供直观的实时仪表盘，显示访客数量、页面浏览、来源等核心指标。
- **无广告和数据出售**：不显示广告，不出售用户数据，强调伦理数据处理。
- **多站点支持**：支持管理多个网站，并提供团队协作功能。

## 主要功能
- **核心指标跟踪**：实时监控独特访客数、页面浏览量、跳出率、会话时长等。
- **流量来源分析**：识别直接访问、搜索引擎、社交媒体、推荐链接等来源。
- **设备与位置统计**：按操作系统、浏览器、设备类型和地理位置（国家/城市级别）分类数据。
- **事件跟踪**：支持自定义事件，如按钮点击、表单提交等。
- **导出与 API**：数据可导出为 CSV，支持 REST API 集成其他工具。
- **自托管部署**：使用 Elixir 和 Phoenix 框架构建，支持 Docker 部署，便于扩展。

## 用法
1. **安装与部署**：
   - 克隆仓库：`git clone https://github.com/plausible/analytics.git`。
   - 使用 Docker 快速启动：运行 `docker-compose up`（需配置环境变量，如数据库连接）。
   - 或者从源码构建：安装 Elixir 和 PostgreSQL，运行 `mix deps.get` 和 `mix ecto.setup`，然后启动服务器。

2. **集成到网站**：
   - 在网站 `<head>` 标签中添加跟踪脚本：
     ```
     <script defer data-domain="yourdomain.com" src="https://your-plausible-instance.js"></script>
     ```
   - 对于自托管实例，将 `your-plausible-instance.js` 替换为你的服务器地址。

3. **使用仪表盘**：
   - 访问你的 Plausible 实例 URL，登录后添加网站域名。
   - 查看实时数据、生成报告，或通过 API 查询（如 `GET /api/v1/stats/aggregate?site_id=your-site&period=30d`）。

4. **高级用法**：
   - 配置自定义事件：使用 `plausible('EventName', {props: {key: 'value'}})` 在 JS 中触发。
   - 扩展：修改源代码添加插件，或集成 CI/CD 进行自动化部署。

该项目适合注重隐私的开发者、网站所有者和企业，用于替代传统分析工具。