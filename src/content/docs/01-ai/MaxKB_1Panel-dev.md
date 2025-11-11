---
title: MaxKB
---

# MaxKB

## 项目简介

MaxKB 是一个开源的企业级智能体构建平台，由 1Panel-dev 开发。它集成了检索增强生成 (RAG) 管道，支持强大的工作流，并提供先进的 MCP 工具使用能力。MaxKB 广泛应用于智能客服、企业内部知识库、学术研究和教育等领域。

## 主要功能

### RAG 管道

- 支持直接上传文档/自动爬取在线文档
- 具备自动文本分割、向量化功能
- 有效减少大模型幻觉，提供卓越的智能问答交互体验

### 代理工作流

- 配备强大的工作流引擎、函数库和 MCP 工具使用
- 能够编排 AI 流程，满足复杂业务场景需求

### 无缝集成

- 实现零代码快速集成到第三方业务系统
- 快速为现有系统配备智能问答能力，提升用户满意度

### 模型无关性

- 支持各种大模型，包括私有模型（如 DeepSeek、Llama、Qwen 等）和公共模型（如 OpenAI、Claude、Gemini 等）

### 多模态支持

- 原生支持文本、图像、音频和视频的输入和输出

## 技术栈

- 前端：Vue.js
- 后端：Python / Django
- LLM 框架：LangChain
- 数据库：PostgreSQL + pgvector

## 快速开始

使用以下 Docker 命令启动 MaxKB 容器：

```bash
docker run -d --name=maxkb --restart=always -p 8080:8080 -v ~/.maxkb:/opt/maxkb 1panel/maxkb
```

访问 MaxKB Web 界面：`http://your_server_ip:8080`

默认管理员凭据：

- 用户名：admin
- 密码：MaxKB@123..

> 中国用户如遇到 Docker 镜像拉取失败问题，请参照[离线安装文档](https://maxkb.cn/docs/v2/installation/offline_installtion/)进行安装。

## 许可证

本项目采用 GPL-3.0 许可证。
