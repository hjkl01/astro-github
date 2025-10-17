
---
title: proxypool
---

# Proxypool 项目

## 项目地址
[https://github.com/henson/proxypool](https://github.com/henson/proxypool)

## 主要特性
- **代理池管理**：自动采集、验证和维护代理IP池，支持多种代理类型（如HTTP、HTTPS、SOCKS）。
- **高可用性**：实时监控代理可用性，自动过滤无效代理，确保池中代理的高质量。
- **API 接口**：提供RESTful API，便于集成到其他应用中获取代理。
- **Web 界面**：内置简单Web面板，可视化管理代理池状态。
- **可扩展性**：支持自定义采集源和验证规则，易于扩展。
- **轻量级**：基于Python实现，资源占用低，适合部署在服务器上。

## 主要功能
- **代理采集**：从多个免费/付费源自动抓取代理IP。
- **代理验证**：通过速度、延迟和可用性测试验证代理的有效性。
- **代理存储**：使用SQLite或Redis存储代理数据，支持持久化。
- **代理分发**：通过API随机或按策略分发可用代理。
- **定时任务**：支持定时更新代理池，保持池的活跃度。
- **日志与监控**：记录采集和验证过程，便于调试和监控。

## 用法
1. **安装依赖**：
   - 克隆仓库：`git clone https://github.com/henson/proxypool.git`
   - 进入目录：`cd proxypool`
   - 安装Python依赖：`pip install -r requirements.txt`

2. **配置**：
   - 编辑`config.py`文件，设置数据库路径、API端口、采集源等参数。
   - 如需Redis支持，配置Redis连接信息。

3. **运行**：
   - 启动代理池：`python main.py`
   - 访问Web界面：默认http://localhost:8899
   - 使用API获取代理：例如GET http://localhost:8899/api/random 返回随机代理。

4. **高级用法**：
   - 自定义采集器：修改`fetcher`模块添加新源。
   - 部署到生产：使用Gunicorn或Docker部署，支持环境变量配置。
   - 集成示例：在应用中通过requests库调用API获取代理并使用。