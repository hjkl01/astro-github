
---
title: scrapydweb
---

# ScrapydWeb 项目

**GitHub 项目地址:** [https://github.com/my8100/scrapydweb](https://github.com/my8100/scrapydweb)

## 主要特性
ScrapydWeb 是一个基于 Web 的 Scrapyd 管理工具，专为 Scrapy 项目设计。它提供了一个直观的图形化界面，用于管理和监控 Scrapy 爬虫任务。主要特性包括：
- **任务调度与监控**：支持 Scrapy 项目的部署、调度和实时监控，包括任务日志查看和性能统计。
- **多 Scrapyd 实例支持**：可以连接和管理多个 Scrapyd 服务器，实现分布式爬虫管理。
- **用户认证与安全**：内置用户登录系统，支持自定义用户和权限控制，增强安全性。
- **API 接口**：提供 RESTful API，便于与其他工具集成。
- **仪表盘与可视化**：实时显示爬虫运行状态、统计图表和历史记录，便于调试和优化。
- **日志与错误处理**：支持详细日志查看、错误追踪和自动重试机制。
- **跨平台兼容**：基于 Python 和 Flask 开发，支持 Windows、Linux 和 macOS 等操作系统。

## 主要功能
- **项目部署**：通过 Web 界面上传和部署 Scrapy 项目，支持 egg 文件或源码部署。
- **任务执行**：手动或定时调度爬虫任务，支持参数配置和并发控制。
- **监控与日志**：实时跟踪任务进度、查看输出日志，并支持日志过滤和导出。
- **统计分析**：生成爬虫运行统计报告，包括成功率、耗时和数据量等指标。
- **配置管理**：自定义 Scrapyd 配置、项目设置和 Web 界面主题。
- **通知与警报**：集成邮件或 Webhook 通知，及时报告任务异常。

## 用法
1. **安装**：
   - 确保已安装 Scrapyd 和 Scrapy。
   - 使用 pip 安装 ScrapydWeb：`pip install scrapydweb`。
   - 或者从 GitHub 克隆仓库：`git clone https://github.com/my8100/scrapydweb.git`，然后 `pip install -e .`。

2. **启动**：
   - 运行命令：`scrapydweb`（默认监听 5000 端口）。
   - 可通过配置文件 `scrapydweb.cfg` 自定义端口、Scrapyd 地址等设置，例如：
     ```
     [scrapydweb]
     host = 0.0.0.0
     port = 5000
     username = admin
     password = password
     ```

3. **访问界面**：
   - 在浏览器打开 `http://localhost:5000`。
   - 首次访问需设置用户名和密码。

4. **使用步骤**：
   - **部署项目**：在 Web 界面上传 Scrapy 项目文件，选择 Scrapyd 目标服务器。
   - **调度任务**：选择项目，配置参数（如 spider 名称、设置），点击运行或调度。
   - **监控任务**：在仪表盘查看任务列表、日志和统计；支持停止或重启任务。
   - **高级操作**：通过 API 调用任务，例如使用 curl 发送 POST 请求到 `/schedule.json`。

更多详情请参考项目 README 和文档。