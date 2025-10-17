
---
title: Gerapy
---

# Gerapy 项目

**GitHub 项目地址:** [https://github.com/Gerapy/Gerapy](https://github.com/Gerapy/Gerapy)

## 主要特性
Gerapy 是一个强大的 Scrapy 爬虫管理平台，基于 Python 和 Django 开发，具有以下核心特性：
- **可视化管理界面**：提供 Web 界面，便于管理和监控 Scrapy 爬虫项目，无需命令行操作。
- **爬虫部署与调度**：支持一键部署 Scrapy 项目，并通过 Celery 实现分布式任务调度和定时执行。
- **项目管理**：允许上传、编辑和管理多个 Scrapy 项目，支持版本控制和代码编辑器。
- **任务监控**：实时监控爬虫运行状态，包括日志查看、性能统计和错误诊断。
- **节点管理**：支持多节点分布式部署，实现爬虫任务的负载均衡和扩展。
- **插件扩展**：内置插件系统，可扩展功能，如结果存储、通知等。
- **安全与权限**：用户认证、角色权限控制，确保平台安全。

## 主要功能
- **项目上传与编辑**：通过 Web 界面上传 Scrapy 项目 ZIP 包，或直接在浏览器中编辑代码。
- **爬虫执行**：支持手动触发或定时调度爬虫任务，查看实时日志和结果输出。
- **监控仪表盘**：显示任务历史、成功率、爬取数据量等统计信息。
- **结果处理**：集成数据库存储爬取结果，支持导出为 JSON/CSV 等格式。
- **远程管理**：在多服务器环境下管理爬虫节点，实现高效的分布式爬取。

## 用法指南
1. **安装环境**：
   - 确保安装 Python 3.6+ 和 Scrapy。
   - 克隆仓库：`git clone https://github.com/Gerapy/Gerapy.git`。
   - 进入目录：`cd Gerapy`，安装依赖：`pip install -r requirements.txt`。
   - 初始化数据库：`python manage.py migrate`。

2. **启动服务**：
   - 创建超级用户：`python manage.py createsuperuser`。
   - 运行服务器：`python manage.py runserver`（默认端口 8000）。
   - 访问 Web 界面：http://localhost:8000/admin/ 登录管理后台。

3. **使用流程**：
   - **添加项目**：在“Projects”页面上传 Scrapy 项目 ZIP 文件，或通过 Git 导入。
   - **部署爬虫**：选择项目，配置参数（如 spiders、settings），一键部署到节点。
   - **调度任务**：在“Tasks”页面创建定时任务，使用 Celery 后台 worker 执行（需启动 `celery -A gerapy worker -l info`）。
   - **监控与调试**：查看“Monitors”页面，检查日志、统计数据；如遇错误，可在“Logs”中诊断。
   - **节点配置**：在“Nodes”页面添加远程服务器，实现分布式部署（需配置 SSH 密钥）。

4. **高级用法**：
   - 集成 Celery + Redis 作为消息队列，提升性能。
   - 使用 Docker 部署：仓库提供 Dockerfile，支持容器化运行。
   - 自定义插件：扩展功能，如集成 MySQL/PostgreSQL 存储结果。

更多细节请参考仓库的 README 和文档。