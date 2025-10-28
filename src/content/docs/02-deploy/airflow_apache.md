
---
title: airflow
---

# Apache Airflow 项目

## 项目地址
[GitHub 项目地址](https://github.com/apache/airflow)

## 主要特性
Apache Airflow 是一个开源的工作流编排平台，由 Apache 软件基金会维护。它具有以下主要特性：
- **DAG（Directed Acyclic Graph）工作流**：允许用户以代码形式定义工作流，避免手动配置复杂依赖关系。
- **高度可扩展**：支持插件架构，可以集成各种执行器（如 Celery、Kubernetes）和数据库后端。
- **调度与监控**：内置调度器，支持时间-based 或事件-based 触发，提供 Web UI 用于实时监控任务状态、日志和指标。
- **任务重试与错误处理**：自动重试失败任务，支持警报通知（如 Slack、Email）。
- **社区支持**：活跃的开源社区，提供丰富的运营商（Operators）来连接外部系统，如 AWS、Google Cloud、数据库等。
- **安全性**：支持 RBAC（角色-based 访问控制）和加密配置。

## 主要功能
Airflow 的核心功能聚焦于自动化和管理复杂的数据管道：
- **工作流定义**：使用 Python 代码编写 DAG 文件，定义任务、依赖和调度规则。
- **任务执行**：支持多种任务类型，包括 Bash、Python、SQL 等脚本执行，以及与大数据工具（如 Spark、Hive）的集成。
- **监控与调试**：通过 Web 界面查看 DAG 运行历史、任务日志和性能指标，支持 XCom（跨任务通信）机制。
- **扩展集成**：内置钩子（Hooks）和运营商（Operators）来与外部服务交互，如发送 HTTP 请求、操作数据库或云服务。
- **变量与连接管理**：安全存储敏感信息，如 API 密钥和数据库凭证。
- **测试与回填**：支持单元测试 DAG，并允许回填历史数据以重新运行任务。

## 用法
### 安装
1. 确保 Python 3.7+ 已安装。
2. 使用 pip 安装：`pip install apache-airflow`。
3. 初始化数据库：`airflow db init`。
4. 创建管理员用户：`airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com`。
5. 启动 Web 服务器和调度器：`airflow webserver --port 8080` 和 `airflow scheduler`（在不同终端）。

### 基本用法
1. **创建 DAG**：在 `~/airflow/dags` 目录下编写 Python 文件，例如：
   ```python
   from airflow import DAG
   from airflow.operators.bash import BashOperator
   from datetime import datetime

   dag = DAG('example_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily')

   task1 = BashOperator(task_id='print_date', bash_command='date', dag=dag)
   task2 = BashOperator(task_id='sleep', bash_command='sleep 5', dag=dag)

   task1 >> task2  # 定义依赖
   ```
2. **运行 DAG**：通过 Web UI（默认 http://localhost:8080）触发或调度 DAG。
3. **监控**：在 UI 中查看任务状态，检查日志或手动重试。
4. **高级用法**：使用 Airflow CLI 命令如 `airflow tasks test <dag_id> <task_id> <execution_date>` 测试任务，或集成自定义运营商扩展功能。

更多详情请参考官方文档：https://airflow.apache.org/docs/。