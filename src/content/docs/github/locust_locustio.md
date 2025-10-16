
---
title: locust
---

# Locust 项目描述

## 项目地址
[https://github.com/locustio/locust](https://github.com/locustio/locust)

## 主要特性
Locust 是一个开源的负载测试工具，专为 Python 开发，采用分布式和可扩展的设计。主要特性包括：
- **纯 Python 实现**：用户可以直接用 Python 代码定义用户行为，无需 YAML 或其他配置文件，易于编写和维护测试脚本。
- **分布式测试支持**：支持多机分布式运行，能模拟数百万用户的并发负载，适用于大规模性能测试。
- **Web UI 界面**：提供实时 Web 界面监控测试进度、响应时间、请求速率等指标，便于可视化分析。
- **高灵活性**：支持自定义 HTTP、WebSocket 等协议测试，集成任务调度、断言等高级功能。
- **轻量级**：基于 gevent 实现异步 I/O，资源消耗低，适合长时间运行的压力测试。

## 主要功能
- **负载模拟**：模拟大量虚拟用户（User）并发执行任务，如 HTTP 请求、API 调用等，测试系统在高负载下的性能。
- **性能指标监控**：实时收集 RPS（每秒请求数）、响应时间、错误率等数据，并生成报告。
- **脚本化测试**：通过定义 HttpUser 类和任务（@task 装饰器）来模拟真实用户行为，支持变量参数化和条件逻辑。
- **集成与扩展**：可与 Jenkins、Docker 等工具集成，支持自定义客户端和事件钩子。
- **报告生成**：测试结束后自动生成 HTML 报告，包含图表和统计数据。

## 用法
1. **安装**：使用 pip 安装 Locust，例如 `pip install locust`。确保 Python 版本为 3.6+。
2. **编写测试脚本**：创建一个 Python 文件（如 `locustfile.py`），示例代码：
   ```python
   from locust import HttpUser, task, between

   class WebsiteUser(HttpUser):
       wait_time = between(1, 5)  # 用户间等待时间

       @task
       def index_page(self):
           self.client.get("/")  # 发送 GET 请求

       @task(3)  # 权重为3，执行频率更高
       def view_item(self):
           item_id = random.randint(1, 100)
           self.client.get(f"/item/{item_id}", name="/item")
   ```
3. **运行测试**：
   - 命令行模式：`locust -f locustfile.py --host=https://example.com --users 1000 --spawn-rate 10 --run-time 1m`（模拟 1000 用户，生成速率 10/s，运行 1 分钟）。
   - Web UI 模式：`locust -f locustfile.py --host=https://example.com`，然后在浏览器访问 http://localhost:8089 配置并启动测试。
4. **分布式运行**：在主节点运行 `locust --master`，在从节点运行 `locust --worker --master-host=主节点IP`。
5. **查看结果**：通过 Web UI 或命令行输出监控统计；测试后使用 `--html=report.html` 生成报告文件。

Locust 适用于 Web 应用、API 和微服务的性能测试，简单高效，适合开发者和 QA 团队使用。