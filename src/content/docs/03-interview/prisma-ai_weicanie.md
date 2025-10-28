---
title: Prisma-AI
---

# Prisma-AI

**项目地址：** https://github.com/weicanie/prisma-ai

## 主要特性

Prisma-AI 是一个开源免费的AI求职助手，旨在帮助用户优化项目、定制简历、匹配工作并准备面试。它基于先进的AI架构，包括Planer-Executor、CRAG和Human-in-the-loop，能够将想法转化为可执行计划。项目还集成了面试经验驱动的学习系统，并提供IT求职数据网站（https://pinkprisma.com）。

## 功能

- **AI核心**：基于LangChain、LangGraph和fastmcp等技术，提供精准上下文支持，支持多轮反馈优化输出质量。
- **简历优化与落地**：深度分析项目，自动打磨文案，挖掘可落地亮点，并通过AI Agent实现项目亮点。
- **岗位匹配与契合**：实时抓取岗位，使用本地向量检索重排，精准匹配适合用户的岗位，并针对目标岗位自动改写简历。
- **高效学习与备战**：提供前后端题库、思维导图和Anki集成，帮助用户理解与记忆。
- **面经数据库**：支持面经自动补全、标准答案、思维导图和版本管理，用户共建共享，越用越强。
- **便捷部署**：提供Docker一键部署，零配置启动。

## 用法

### Docker部署（推荐）

1. 克隆仓库：

   ```
   git clone https://github.com/weicanie/prisma-ai.git && cd prisma-ai
   ```

2. 配置环境（参考文档：[5分钟完成环境配置](https://github.com/weicanie/prisma-ai/blob/main/doc/%E6%95%99%E7%A8%8B%EF%BC%9A1%E3%80%81%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE.md)）。

3. 启动服务：

   ```
   ./scripts/start.sh
   ```

4. 浏览器访问 `http://localhost` 即可使用。

### 本地开发

1. 克隆并安装依赖：

   ```
   git clone https://github.com/weicanie/prisma-ai.git && cd prisma-ai && pnpm install
   ```

2. 配置环境（确保提供MySQL、Redis、MongoDB、MinIO等服务）。

3. 启动项目：
   ```
   pnpm run dev
   ```
