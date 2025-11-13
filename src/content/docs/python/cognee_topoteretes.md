---
title: Cognee
---

# Cognee

## 项目简介

Cognee 是一个开源工具和平台，将您的原始数据转换为持久且动态的 AI 代理内存。它结合了向量搜索和图数据库，使您的文档既可以通过含义进行搜索，又可以通过关系进行连接。

## 主要功能

- **数据互联**：互联任何类型的数据，包括过去的对话、文件、图像和音频转录。
- **替代 RAG 系统**：用基于图和向量的统一内存层替换传统 RAG 系统。
- **减少开发工作和基础设施成本**：同时提高质量和精度。
- **Pythonic 数据管道**：从 30 多种数据源进行摄取。
- **高度可定制**：通过用户定义的任务、模块化管道和内置搜索端点提供高可定制性。

## 用法

### 安装

使用 pip、poetry、uv 或您首选的 Python 包管理器安装 Cognee。

```bash
pip install cognee
```

### 配置 LLM

设置环境变量或创建 `.env` 文件。

```python
import os
os.environ["LLM_API_KEY"] = "YOUR_OPENAI_API_KEY"
```

### 运行管道

```python
import cognee
import asyncio

async def main():
    # 添加文本到 cognee
    await cognee.add("Cognee turns documents into AI memory.")

    # 生成知识图
    await cognee.cognify()

    # 添加内存算法到图
    await cognee.memify()

    # 查询知识图
    results = await cognee.search("What does Cognee do?")

    # 显示结果
    for result in results:
        print(result)

if __name__ == '__main__':
    asyncio.run(main())
```

### 使用 CLI

```bash
cognee-cli add "Cognee turns documents into AI memory."
cognee-cli cognify
cognee-cli search "What does Cognee do?"
cognee-cli delete --all
```

启动本地 UI：

```bash
cognee-cli -ui
```

## 更多信息

- [文档](https://docs.cognee.ai/)
- [演示](https://www.youtube.com/watch?v=1bezuvLwJmw&t=2s)
- [GitHub](https://github.com/topoteretes/cognee)
