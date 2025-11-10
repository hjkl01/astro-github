---
title: prefect
---

# Prefect 项目概述

## 项目地址
[https://github.com/PrefectHQ/prefect](https://github.com/PrefectHQ/prefect)

## 主要特性
Prefect 是一个开源的工作流编排平台，主要用于数据工程、机器学习和自动化任务的管理。它强调简单性、可扩展性和可靠性，支持动态工作流、错误处理和监控。核心特性包括：
- **动态工作流**：允许在运行时构建和修改工作流，支持参数化和条件逻辑。
- **内置错误处理**：自动重试、缓存和状态跟踪，确保任务鲁棒性。
- **分布式执行**：支持本地、云端（如 AWS、Kubernetes）和混合环境部署。
- **监控与可视化**：提供仪表板、日志和警报，帮助跟踪工作流状态。
- **版本控制集成**：与 Git 等工具无缝集成，便于 CI/CD 管道。
- **开源与社区支持**：免费开源，Prefect Cloud 提供托管服务以增强企业级功能。

## 主要功能
Prefect 的功能聚焦于工作流自动化：
- **任务定义**：使用 Python 装饰器（如 `@task` 和 `@flow`）定义可重用任务和整个工作流。
- **调度与执行**：内置调度器，支持 cron-like 表达式或事件驱动执行。
- **数据处理**：集成 Pandas、Dask 等库，适合 ETL、数据管道和 ML 工作流。
- **安全与合规**：支持秘密管理、RBAC（角色-based 访问控制）和审计日志。
- **扩展性**：通过插件系统添加自定义集成，如数据库连接或 API 调用。
- **Prefect Cloud**：可选的 SaaS 版本，提供协作、UI 和高级分析。

## 用法
Prefect 的用法简单，以 Python 为基础。安装后，通过脚本定义和运行工作流。

### 安装
```bash
pip install prefect
```

### 基本用法示例
1. **定义任务和工作流**：
   ```python
   from prefect import flow, task

   @task
   def hello(name: str) -> str:
       return f"Hello, {name}!"

   @flow
   def my_flow(name: str):
       result = hello(name)
       print(result)

   if __name__ == "__main__":
       my_flow("World")
   ```

2. **运行工作流**：
   ```bash
   python your_script.py
   ```

3. **部署与调度**：
   - 使用 `prefect deploy` 命令部署到服务器或云端。
   - 通过 UI 或 API 配置调度，例如每天运行：`@flow(schedule=CronSchedule("0 9 * * *"))`。

更多细节请参考官方文档：https://docs.prefect.io/。