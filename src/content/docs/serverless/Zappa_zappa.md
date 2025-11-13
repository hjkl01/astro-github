---
title: Zappa
---

# Zappa 项目

## 项目地址

[https://github.com/zappa/Zappa](https://github.com/zappa/Zappa)

## 主要特性

Zappa 是一个开源的 Python 服务器无服务器框架，用于在 AWS Lambda + API Gateway 上构建和部署无服务器、事件驱动的 Python 应用程序（包括 WSGI Web 应用）。它提供无限扩展、零停机、零维护，并以传统部署成本的一小部分运行。主要特性包括：

- **无服务器部署**：自动处理 AWS Lambda、API Gateway 和其他资源的配置，无需手动管理服务器。
- **自动缩放**：支持自动水平扩展，根据流量需求动态调整资源。
- **简单配置**：通过单一的 `zappa_settings.json` 文件管理部署设置，支持多环境（如开发、生产）。
- **内置监控**：集成日志记录、错误追踪和性能监控，与 AWS CloudWatch 兼容。
- **热更新**：支持代码和依赖的快速更新，而不中断服务。
- **跨平台支持**：兼容多种 Python Web 框架，如 Flask、Django 和 Bottle。
- **事件驱动**：支持响应 AWS 事件，如 S3 上传、DynamoDB 更改、Kinesis 流等。
- **异步任务执行**：允许在单独的 Lambda 实例中运行异步函数，支持重试和补偿。
- **全局部署**：支持将应用部署到多个 AWS 区域，实现全球可用性。
- **安全与合规**：自动生成 IAM 角色和策略，支持自定义权限。
- **成本效益**：仅支付使用的毫秒数，远低于 VPS/PaaS 成本。

## 主要功能

- **部署应用**：将本地 Python Web 应用打包并上传到 AWS Lambda，支持 WSGI 标准。
- **环境管理**：创建、更新和管理多个部署环境（如 dev、staging、prod）。
- **静态文件处理**：自动处理静态资产的上传和分发，使用 S3 和 CloudFront。
- **自定义事件**：支持 Lambda 事件触发，如定时任务（Cron）和 S3 事件。
- **回滚与删除**：轻松回滚到先前版本或完全删除部署。
- **插件系统**：可扩展插件支持额外功能，如数据库集成或自定义钩子。

## 用法

### 安装

1. 确保已安装 Python 3.8/3.9/3.10/3.11/3.12/3.13 和 pip。
2. 通过 pip 安装 Zappa：
   ```
   pip install zappa
   ```

### 初始化

1. 在项目根目录运行：
   ```
   zappa init
   ```
   这会生成 `zappa_settings.json` 文件。编辑它以配置 AWS 区域、项目名称和环境变量。

### 部署

1. 部署到默认环境：
   ```
   zappa deploy
   ```
2. 更新现有部署：
   ```
   zappa update
   ```
3. 指定环境部署（如 production）：
   ```
   zappa deploy production
   ```

### 调度

- 调度函数定期执行：
  ```
  zappa schedule production
  ```
- 取消调度：
  ```
  zappa unschedule production
  ```

### 异步任务

- 使用 `@task` 装饰器执行异步函数。

### 事件响应

- 配置 `events` 在 `zappa_settings.json` 中响应 AWS 事件。

### 管理

- **管理控制台**：运行 `zappa manage production` 进入 Python shell 执行代码。
- **日志查看**：使用 `zappa tail production` 查看实时日志。
- **远程调用**：`zappa invoke production function_name` 执行远程函数。
- **回滚**：`zappa rollback production -n 1` 回滚到上一个版本。
- **删除**：`zappa undeploy` 移除部署。

### 示例配置 (zappa_settings.json)

```json
{
  "dev": {
    "app_function": "your_app.app",
    "aws_region": "us-east-1",
    "s3_bucket": "zappa-bucket",
    "profile_name": "default",
    "events": [
      {
        "function": "your_module.your_function",
        "expression": "rate(1 minute)"
      }
    ]
  }
}
```

更多细节请参考官方文档。
