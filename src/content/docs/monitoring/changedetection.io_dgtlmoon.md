---
title: changedetection.io
---

# ChangeDetection.io 项目

## 项目地址
[GitHub 项目地址](https://github.com/dgtlmoon/changedetection.io)

## 主要特性
ChangeDetection.io 是一个开源的网站变更检测工具，主要用于监控网站内容的更新和变化。它支持自托管部署，适合个人或团队使用。核心特性包括：
- **实时变更检测**：自动扫描指定网页，检测内容变化（如文本、图像或结构调整）。
- **多协议支持**：兼容 HTTP/HTTPS、JSON API 等多种数据源。
- **可视化差异比较**：使用 diff 算法突出显示新增、删除或修改的部分，支持侧边对比视图。
- **通知集成**：内置多种通知方式，包括电子邮件、Discord、Telegram、Slack、Pushover 等，支持自定义 webhook。
- **浏览器自动化**：通过 Playwright 支持 JavaScript 渲染的动态网站检测。
- **数据持久化**：使用 SQLite 或 PostgreSQL 存储历史变更记录，支持归档和导出。
- **用户界面友好**：简洁的 Web 界面，支持多用户管理和订阅分组。
- **轻量级部署**：Docker 支持，便于在服务器、NAS 或本地运行，低资源消耗。

## 主要功能
- **网站监控**：添加 URL 后，设置检测频率（从几分钟到几天），工具会定期抓取并比较内容。
- **自定义过滤**：使用 CSS 选择器或正则表达式过滤无关部分，只关注关键内容变化。
- **历史记录**：保存变更历史，支持回溯查看过去版本。
- **API 接口**：提供 RESTful API，便于与其他工具集成或自动化脚本调用。
- **主题和自定义**：支持暗黑模式和 UI 自定义，适用于不同设备。
- **安全性**：支持基本认证和 HTTPS，确保监控数据安全。

## 用法
1. **安装部署**：
   - 使用 Docker 快速启动：运行 `docker run -d --name changedetection -p 5000:5000 -v $(pwd)/data:/datastore dgtlmoon/changedetection.io`（需安装 Docker）。
   - 或者从源码克隆仓库，使用 Python 环境安装依赖：`pip install -r requirements.txt`，然后运行 `python changedetection.py`。
   - 访问 `http://localhost:5000` 打开 Web 界面。

2. **添加监控**：
   - 在界面点击“Add first watch”，输入要监控的 URL。
   - 配置检测选项：选择检查频率、通知方式、过滤规则（如 CSS 选择器）。
   - 保存后，工具开始后台扫描。

3. **查看和通知**：
   - 在“Watches”页面查看所有监控项的状态和历史变更。
   - 当检测到变化时，收到通知；点击变更记录可查看详细 diff。

4. **高级用法**：
   - 通过 API 添加监控：使用 POST 请求到 `/api/watch` 端点。
   - 自定义通知：编辑 `datastore/notifications.yaml` 文件配置更多集成。
   - 导出数据：使用界面按钮或 API 导出 JSON/CSV 格式的历史记录。

该工具适合开发者、记者或内容创作者监控网站更新，无需复杂配置即可上手。