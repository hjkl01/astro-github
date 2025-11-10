---
title: IPProxyTool
---

# IPProxyTool 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/awolfly9/IPProxyTool)

## 主要特性
- **高效代理池管理**：自动采集、验证和维护高可用IP代理池，支持多种代理类型（如HTTP、HTTPS、SOCKS）。
- **实时验证机制**：集成代理可用性检测，确保代理池中IP的有效性和稳定性，避免无效代理的使用。
- **自定义配置**：支持灵活的配置文件调整，包括代理源、验证频率、存储方式等，适应不同场景需求。
- **轻量级设计**：基于Python开发，资源占用低，易于部署和扩展。
- **开源免费**：MIT许可，社区贡献友好，便于二次开发。

## 主要功能
- **代理采集**：从免费/付费代理源（如API、爬虫）自动获取大量IP代理。
- **代理验证**：通过多线程验证代理的连通性、延迟和匿名度，过滤无效代理。
- **代理存储与管理**：使用数据库（如SQLite或Redis）存储代理，支持按可用性排序和定期更新。
- **API接口**：提供RESTful API，用于获取可用代理，支持集成到爬虫或自动化脚本中。
- **监控与日志**：内置日志系统和监控功能，实时跟踪代理池状态和错误。

## 用法
1. **安装依赖**：
   - 克隆仓库：`git clone https://github.com/awolfly9/IPProxyTool.git`
   - 进入目录：`cd IPProxyTool`
   - 安装依赖：`pip install -r requirements.txt`（假设有requirements.txt文件）

2. **配置**：
   - 编辑`config.yaml`或`settings.py`文件，设置代理源URL、验证阈值（如延迟<2s）、数据库路径等。

3. **运行**：
   - 启动代理池：`python main.py` 或 `python manage.py start`
   - 采集代理：`python scripts/collect.py`
   - 验证代理：`python scripts/verify.py`
   - 通过API获取代理：访问`http://localhost:5000/api/proxy?count=10`（默认端口5000）

4. **集成使用**：
   - 在Python脚本中导入：`from proxy_tool import ProxyPool`，然后调用`pool.get_proxy()`获取可用代理。
   - 示例：
     ```python
     from proxy_tool import ProxyPool
     pool = ProxyPool()
     proxy = pool.get_random_proxy()
     print(proxy)  # 输出: {'ip': '127.0.0.1', 'port': 8080, 'type': 'http'}
     ```

5. **停止与维护**：
   - 停止：`Ctrl+C` 或 `python manage.py stop`
   - 定期运行cron任务更新代理池。

更多详情请参考项目README.md文件。