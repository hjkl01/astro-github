
---
title: poseidon
---

# Poseidon 项目描述

## 项目地址
[https://github.com/Qihoo360/poseidon](https://github.com/Qihoo360/poseidon)

## 主要特性
Poseidon 是由奇虎360开发的开源项目，主要作为一个分布式任务调度系统。它具有以下核心特性：
- **高可用性**：支持集群部署，确保任务调度的高可靠性和故障恢复能力。
- **实时监控**：内置监控机制，可实时跟踪任务执行状态、资源使用和性能指标。
- **灵活扩展**：支持插件化架构，便于自定义任务类型和调度策略。
- **轻量级设计**：基于Go语言开发，资源占用低，启动快速。
- **支持多种协议**：兼容HTTP、RPC等多种通信方式，便于集成现有系统。

## 主要功能
- **任务调度**：实现定时、周期性和事件驱动的任务调度，支持依赖关系和优先级管理。
- **任务分发**：将任务均匀分发到工作节点，支持负载均衡和动态扩缩容。
- **执行管理**：提供任务执行、日志记录、重试机制和结果回调功能。
- **配置管理**：通过配置文件或API动态调整调度参数，支持热更新。
- **告警通知**：集成告警系统，当任务失败或异常时发送通知（如邮件、短信）。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/Qihoo360/poseidon.git`
   - 进入目录：`cd poseidon`
   - 构建：`go build -o poseidon`

2. **配置**：
   - 编辑 `config.yaml` 文件，设置服务器地址、数据库连接、任务队列等参数。
   - 示例配置：
     ```
     server:
       host: 0.0.0.0
       port: 8080
     database:
       driver: mysql
       dsn: root:password@tcp(localhost:3306)/poseidon
     ```

3. **启动**：
   - 运行服务器：`./poseidon server -c config.yaml`
   - 运行工作节点：`./poseidon worker -c config.yaml`

4. **使用**：
   - 通过API提交任务：使用POST请求到 `/api/tasks` 端点，传入任务参数（如JSON格式的脚本或函数）。
   - 示例curl命令：`curl -X POST http://localhost:8080/api/tasks -d '{"name":"test_task","cron":"* * * * *","command":"echo hello"}'`
   - 查看任务状态：访问 `/api/tasks/{id}` 获取执行详情。
   - 监控：通过Web界面（默认端口8081）或API查询仪表盘。

更多细节请参考项目README和文档。