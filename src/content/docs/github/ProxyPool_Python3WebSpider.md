
---
title: ProxyPool
---

# ProxyPool 项目

## 项目地址
[GitHub 项目地址](https://github.com/Python3WebSpider/ProxyPool)

## 主要特性
- **代理池管理**：自动采集、验证和管理大量代理IP，形成高效的代理池，支持HTTP/HTTPS/SOCKS等多种协议。
- **高可用性**：实时检测代理可用性，自动过滤无效代理，确保池中代理的高可用率。
- **API 接口**：提供RESTful API，便于集成到爬虫或其他应用中，支持随机获取、指定类型代理等操作。
- **分布式支持**：可部署在多节点环境中，实现代理池的分布式采集和同步。
- **轻量级设计**：基于Python Flask框架，易于部署和扩展，支持Docker容器化。
- **数据存储**：使用Redis作为后端存储，支持代理的分数机制（基于可用性评分）。

## 主要功能
- **代理采集**：从多个免费/付费代理源（如免费代理网站、API）自动爬取代理IP。
- **代理验证**：通过多线程验证代理的延迟、可用性和匿名度，支持自定义验证规则。
- **代理调度**：根据分数机制调度代理，提供API接口如 `/get`（随机获取）、`/count`（统计数量）等。
- **代理更新**：定时任务自动更新代理池，移除失效代理，添加新代理。
- **监控与日志**：内置日志记录和简单监控，支持代理池状态查询。
- **扩展性**：模块化设计，便于添加自定义采集源或验证器。

## 用法
1. **环境准备**：
   - 安装Python 3.x 和 Redis。
   - 克隆仓库：`git clone https://github.com/Python3WebSpider/ProxyPool.git`
   - 进入目录：`cd ProxyPool`

2. **安装依赖**：
   ```
   pip install -r requirements.txt
   ```

3. **配置**：
   - 编辑 `config.py` 文件，设置 Redis 连接信息、API 端口等。
   - 确保 Redis 服务运行（默认 localhost:6379）。

4. **启动服务**：
   - 运行采集模块：`python run.py`（启动 Flask API 服务，默认端口 5000）。
   - 运行调度模块：`python schedule.py`（定时采集和验证代理）。
   - 或使用 Docker：构建镜像并运行容器。

5. **使用 API**：
   - 获取随机代理：`GET http://localhost:5000/get?type=http`（返回可用 HTTP 代理）。
   - 获取代理数量：`GET http://localhost:5000/count`。
   - 删除指定代理：`DELETE http://localhost:5000/delete?ip=xxx.xxx.xxx.xxx`。
   - 更多接口详见项目 README。

项目适用于 Web 爬虫、数据采集等场景，避免 IP 封禁。建议在生产环境中结合付费代理源使用。