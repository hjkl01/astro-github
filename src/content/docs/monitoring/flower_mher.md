---
title: flower
---

# Flower 项目

**GitHub 项目地址:** [https://github.com/mher/flower](https://github.com/mher/flower)

## 主要特性
Flower 是一个用于监控和管理 Celery 分布式任务队列的 Web 界面工具。它提供了一个直观的仪表盘，帮助用户实时查看任务状态、工人（worker）活动和队列信息。主要特性包括：
- **实时监控**：显示 Celery 任务的执行状态、成功/失败率和执行时间。
- **工人管理**：监控 Celery worker 的运行状态、资源使用和任务分配。
- **任务历史**：记录和查询任务日志，包括重试机制和错误详情。
- **队列可视化**：展示任务队列的长度、任务分发和优先级。
- **简单集成**：基于 Flask 框架，轻量级且易于部署，支持自定义主题和扩展。
- **开源免费**：MIT 许可，社区活跃，支持 Python 2/3。

## 主要功能
- **仪表盘概览**：首页显示任务统计、活跃工人和队列概况，支持图表可视化。
- **任务详情**：查看单个任务的输入参数、输出结果和执行轨迹。
- **工人控制**：重启或关闭 worker，监控 CPU/内存使用。
- **事件流处理**：实时处理 Celery 事件，支持过滤和搜索。
- **API 支持**：提供 RESTful API 接口，便于与其他工具集成。
- **安全性**：内置基本认证和 HTTPS 支持。

## 用法
### 安装
1. 确保已安装 Celery（Flower 依赖 Celery）。
2. 使用 pip 安装 Flower：
   ```
   pip install flower
   ```
3. 启动 Flower 服务器（假设 Celery broker 为 Redis）：
   ```
   celery -A myapp flower --port=5555
   ```
   - `-A myapp`：指定 Celery 应用模块。
   - `--port=5555`：指定 Web 端口（默认 5555）。
   - 支持其他选项，如 `--broker=redis://localhost:6379/0` 指定 broker。

### 基本使用
1. 启动 Celery worker 和 Flower 服务器。
2. 在浏览器访问 `http://localhost:5555`，即可看到监控界面。
3. 配置 Celery 时，确保启用事件（`--events` 选项）以实时更新数据：
   ```
   celery -A myapp worker --loglevel=info --events
   ```
4. 高级用法：通过命令行参数自定义，如 `--persistent=True` 启用数据持久化，或 `--basic_auth=username:password` 添加认证。

更多细节请参考项目 README 或官方文档。