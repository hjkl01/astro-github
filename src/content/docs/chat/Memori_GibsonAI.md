---
title: Memori
---

## 简介

Memori 是一个开源的 SQL 原生内存引擎，专为大语言模型 (LLM)、AI 代理和多代理系统设计。它允许任何 LLM 记住对话、从交互中学习，并在会话间保持上下文，只需一行代码 `memori.enable()`。内存存储在标准的 SQL 数据库中，用户完全拥有和控制这些数据。

## 主要功能

- **一行代码集成**：与 OpenAI、Anthropic、LiteLLM、LangChain 等任何 LLM 框架兼容。
- **SQL 原生存储**：使用标准 SQL 数据库（如 SQLite、PostgreSQL、MySQL）存储内存，便于查询、审计和移植。
- **成本节省**：无需昂贵的向量数据库，可节省 80-90% 的成本。
- **无供应商锁定**：可将内存导出为 SQLite 文件，随意迁移。
- **智能内存**：自动提取实体、映射关系和优先级排序上下文。

## 用法

### 快速开始

1. 安装 SDK：

   ```bash
   pip install memorisdk
   ```

2. 初始化并启用：

   ```python
   from memori import Memori
   from openai import OpenAI

   # 初始化
   memori = Memori(conscious_ingest=True)
   memori.enable()

   client = OpenAI()

   # 第一次对话
   response = client.chat.completions.create(
       model="gpt-4o-mini",
       messages=[{"role": "user", "content": "我在构建一个 FastAPI 项目"}]
   )

   # 后续对话 - Memori 自动提供上下文
   response = client.chat.completions.create(
       model="gpt-4o-mini",
       messages=[{"role": "user", "content": "帮我添加认证"}]
   )
   # LLM 自动知道你的 FastAPI 项目
   ```

### 数据库支持

Memori 支持多种 SQL 数据库：

- **SQLite**：`sqlite:///my_memory.db`
- **PostgreSQL**：`postgresql://user:pass@localhost/memori`
- **MySQL**：`mysql://user:pass@localhost/memori`

### 配置选项

- **持久存储**：指定数据库连接字符串。
- **内存模式**：
  - 意识模式 (Conscious Mode)：一次性工作内存注入。
  - 自动模式 (Auto Mode)：每次查询动态搜索。
  - 组合模式：两者结合。

### 架构概述

Memori 通过拦截 LLM 调用来工作：在调用前注入上下文，调用后记录信息。包括检索代理、记忆代理和意识代理等组件，实现高效的内存管理。

## 示例和集成

项目提供多种示例，如基本用法、个人助手、多用户应用等。支持与 AgentOps、Agno、LangChain 等框架集成。

更多详情请参考 [官方文档](https://www.gibsonai.com/docs/memori) 或加入 [Discord 社区](https://discord.gg/abD4eGym6v)。
