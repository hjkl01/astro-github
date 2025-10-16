
---
title: upptime
---

# Upptime 项目

**项目地址:** [https://github.com/upptime/upptime](https://github.com/upptime/upptime)

## 主要特性
Upptime 是一个开源的 GitHub Actions 驱动的网站监控工具，具有以下核心特性：
- **自动化监控**：使用 GitHub Actions 自动 ping 网站，检测可用性和响应时间。
- **无服务器架构**：无需额外服务器，一切运行在 GitHub 上，免费且易于部署。
- **实时报告**：生成网站状态页面、历史图表和通知，支持 Slack、Discord 等集成。
- **自定义灵活**：支持多网站监控、自定义间隔、阈值和通知条件。
- **开源免费**：基于 MIT 许可，完全开源，用户可 fork 并自定义。

## 主要功能
- **网站 uptime 检查**：定期发送 HTTP 请求，记录成功率和响应时间。
- **性能指标**：显示平均响应时间、历史趋势图和 downtime 事件。
- **通知系统**：当网站 downtime 或响应慢时，自动发送警报到 webhook、邮件或聊天工具。
- **仪表板生成**：自动创建 GitHub Pages 托管的监控仪表板，包括实时状态和统计数据。
- **数据持久化**：所有监控数据存储在 GitHub 仓库中，便于版本控制和分析。

## 用法
1. **Fork 项目**：访问 [GitHub 项目地址](https://github.com/upptime/upptime)，点击 Fork 创建自己的仓库副本。
2. **配置网站**：编辑 `.upptimerc.yml` 文件，添加要监控的网站 URL、名称和检查间隔（默认 5 分钟）。
   示例配置：
   ```
   sites:
     - my-website: https://example.com
       status: https://example.com
       uptime: https://example.com
   ```
3. **设置通知**（可选）：在仓库设置中配置 GitHub Secrets（如 `NOTIFY_SLACK_WEBHOOK`）以启用通知。
4. **启用 Actions**：仓库默认启用 GitHub Actions，监控将自动开始。首次运行可能需几分钟。
5. **查看结果**：访问仓库的 GitHub Pages（通常在 `https://用户名.github.io/仓库名`），即可看到生成的监控仪表板。
6. **自定义**：修改 workflows 文件（如 `.github/workflows/uptime.yml`）调整检查逻辑，或添加更多站点。推送更改后，Actions 会自动更新。