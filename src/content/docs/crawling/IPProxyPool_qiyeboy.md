---
title: IPProxyPool
---

# IPProxyPool 项目

## 项目地址
[GitHub 项目地址](https://github.com/qiyeboy/IPProxyPool)

## 主要特性
- **代理池管理**：自动采集、验证和存储高质量IP代理，支持多种来源的代理获取。
- **高可用性**：内置验证机制，确保代理IP的可用性和速度，支持定时更新代理列表。
- **模块化设计**：包括采集器、验证器、存储器和API服务器等模块，便于扩展和自定义。
- **支持多种协议**：兼容HTTP、HTTPS和SOCKS代理。
- **轻量级部署**：基于Python开发，使用SQLite或Redis作为存储后端，易于部署在各种环境中。

## 主要功能
- **代理采集**：从免费代理网站、API等来源自动爬取IP代理。
- **代理验证**：通过多线程验证代理的有效性，包括连通性、匿名度和响应速度测试。
- **代理存储与管理**：将有效代理存入数据库，支持按分数排序和淘汰无效代理。
- **API 接口**：提供RESTful API，用于获取随机代理、指定类型代理或代理列表。
- **调度任务**：使用APScheduler定时执行采集和验证任务，确保代理池的实时更新。
- **监控与日志**：内置日志记录和简单监控，便于调试和维护。

## 用法
1. **安装依赖**：
   - 克隆仓库：`git clone https://github.com/qiyeboy/IPProxyPool.git`
   - 进入目录：`cd IPProxyPool`
   - 安装Python依赖：`pip install -r requirements.txt`

2. **配置**：
   - 编辑 `config.py` 文件，设置数据库类型（SQLite 或 Redis）、API 端口等参数。
   - 如果使用 Redis，需安装并启动 Redis 服务。

3. **运行**：
   - 启动调度器（采集和验证任务）：`python run.py`
   - 启动 API 服务器：`python api.py`
   - 访问 API，例如获取随机代理：`http://localhost:5000/random`

4. **使用 API**：
   - `/random`：返回一个随机有效代理。
   - `/count`：返回代理池中代理数量。
   - `/all`：返回所有代理列表（支持分页）。

更多细节请参考项目 README 文件。