---
title: django-sql-explorer
---

# SQL Explorer

## 项目地址

[GitHub 项目地址](https://github.com/explorerhq/sql-explorer)

## 简介

SQL Explorer 是一个基于 Django 的应用程序，用于快速、简单、无混淆地编写和分享 SQL 查询。提供令人愉悦的 SQL 编辑器，支持 AI 辅助。连接任何 Django 支持的 SQL 数据库，以及用户上传的 CSV、JSON 或 SQLite 文件。

## 主要特性

- **AI 辅助 SQL 助手**：添加 OpenAI 或其他提供商 API 密钥，获得 LLM 驱动的 SQL 助手，帮助编写和调试查询。
- **多连接支持**：管理员配置或用户提供的多个连接。
- **用户上传文件**：用户可以上传并立即查询 JSON、CSV 或 SQLite 文件。
- **查询快照**：定期快照查询，捕获变化数据。
- **查询历史和日志**：跟踪所有查询。
- **浏览器内统计**：快速统计、透视表和散点图。
- **参数化查询**：自动生成友好 UI，无需知道 SQL。
- **游乐场区域**：快速运行临时查询。
- **通过邮件发送结果**。
- **保存查询可作为 JSON API 暴露**。
- **模式信息**：快速访问模式信息，包括自动完成。
- **导出功能**：结果可导出为 CSV 等格式。

## 主要功能

- **查询编写和分享**：在简单、可用的 SQL 编辑器中编写和分享查询。
- **结果查看**：在浏览器中查看结果，保持信息流动。
- **AI 辅助**：LLM 帮助编写和调试查询，自动添加相关上下文和模式。
- **多数据库**：支持 Django 支持的任何 SQL 数据库。
- **用户友好**：重视简单性、直观使用、不显眼、稳定性和最小惊讶原则。

## 用法

### 快速开始

包含一个完整的测试项目，可用于试用。

1. 运行 `docker compose up`
2. 导航到 127.0.0.1:8000/explorer/
3. 使用 admin/admin 登录
4. 开始探索！

这还将运行 Vite 开发服务器，支持前端热重载。

### 安装

- 通过 pip 安装：`pip install django-sql-explorer`
- 在 Django 的 `settings.py` 中添加 `'explorer'` 到 `INSTALLED_APPS`。
- 运行迁移：`python manage.py migrate explorer`。
- 在 `urls.py` 中包含 URL：`path('explorer/', include('explorer.urls'))`。

### 配置 AI 助手

添加 OpenAI（或其他提供商）API 密钥以获得 LLM 驱动的 SQL 助手。

此项目适用于数据分析师和开发者快速编写和分享 SQL 查询。
