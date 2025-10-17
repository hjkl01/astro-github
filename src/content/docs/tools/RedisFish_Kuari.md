
---
title: RedisFish
---

# RedisFish 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/Kuari/RedisFish)

## 主要特性
RedisFish 是一个基于 Redis 的简单钓鱼工具或测试框架，主要用于模拟网络钓鱼场景或安全测试。它具有以下核心特性：
- **轻量级设计**：使用 Redis 作为后端存储，易于部署和扩展，支持快速响应。
- **模块化结构**：包含钓鱼页面生成、数据捕获和日志记录模块，便于自定义。
- **安全性考虑**：仅用于教育和合法安全测试目的，不鼓励用于非法活动。
- **跨平台支持**：基于 Python 实现，可在 Linux、Windows 和 macOS 上运行。

## 主要功能
- **钓鱼页面托管**：通过 Redis 存储和分发伪造的登录页面或表单，支持动态内容生成。
- **数据捕获**：实时捕获用户输入的数据（如用户名、密码），并存储到 Redis 数据库中。
- **日志与监控**：提供访问日志记录和实时监控功能，便于分析钓鱼效果。
- **自动化脚本**：内置脚本支持批量部署和模拟攻击场景，用于渗透测试。

## 用法
1. **安装依赖**：
   - 克隆仓库：`git clone https://github.com/Kuari/RedisFish.git`
   - 安装 Redis：确保本地或远程 Redis 服务运行（默认端口 6379）。
   - 安装 Python 依赖：`pip install -r requirements.txt`（假设有此文件）。

2. **配置**：
   - 编辑 `config.py` 文件，设置 Redis 连接参数（如 host、port、password）。
   - 配置钓鱼页面模板路径和目标 URL。

3. **运行**：
   - 启动 Redis 服务。
   - 运行主脚本：`python main.py`。
   - 访问本地服务器（默认 http://localhost:8080）查看钓鱼页面。
   - 数据将自动存储到 Redis，可通过 `redis-cli` 查询：`KEYS *` 或 `GET key_name`。

4. **注意事项**：
   - 此工具仅供合法使用，如安全研究或教育演示。使用前确保遵守当地法律法规。
   - 测试环境推荐使用虚拟机隔离。