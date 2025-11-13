---
title: DeepCode
---

# DeepCode

## 项目简介

DeepCode 是一个开源的代理编码平台，由香港大学数据智能实验室开发。它通过多代理系统实现从研究论文、自然语言描述到生产就绪代码的自动化转换。项目支持三大核心功能：Paper2Code（论文到代码）、Text2Web（文本到前端）和Text2Backend（文本到后端）。

## 主要功能

### 🚀 Paper2Code

- **算法实现自动化**：将复杂的研究论文算法转换为高质量、生产就绪的代码
- **加速算法复现**：帮助研究人员快速实现和验证学术论文中的算法

### 🎨 Text2Web

- **前端开发自动化**：将纯文本描述转换为功能齐全、美观的web前端代码
- **快速界面创建**：支持快速原型开发和界面设计

### ⚙️ Text2Backend

- **后端开发自动化**：从简单文本输入生成高效、可扩展的后端代码
- **服务器端开发简化**：自动化数据库设计、API开发等后端任务

## 技术架构

DeepCode 采用多代理架构，包括：

- **中央编排代理**：协调整个工作流程
- **意图理解代理**：分析用户需求
- **文档解析代理**：处理研究论文和技术文档
- **代码规划代理**：进行架构设计和技术栈优化
- **代码生成代理**：合成可执行代码

## 安装使用

### 安装

```bash
pip install deepcode-hku
```

### 配置

下载配置文件并设置API密钥：

```bash
curl -O https://raw.githubusercontent.com/HKUDS/DeepCode/main/mcp_agent.config.yaml
curl -O https://raw.githubusercontent.com/HKUDS/DeepCode/main/mcp_agent.secrets.yaml
```

编辑 `mcp_agent.secrets.yaml` 配置API密钥（OpenAI或Anthropic）。

### 运行

启动Web界面：

```bash
deepcode
```

或

```bash
streamlit run ui/streamlit_app.py
```

### 使用步骤

1. **输入**：上传研究论文、提供需求描述或粘贴URL
2. **处理**：多代理系统分析和规划
3. **输出**：获得包含测试和文档的生产就绪代码

## 实验结果

在OpenAI的PaperBench基准测试中，DeepCode表现出色：

- 超越人类专家：75.9% vs 72.4% (+3.5%)
- 优于商业代码代理：84.8% vs 58.7% (+26.1%)
- 领先科学代码代理：73.5% vs 51.1% (+22.4%)

## 项目链接

- **GitHub**: https://github.com/HKUDS/DeepCode
- **PyPI**: https://pypi.org/project/deepcode-hku/
- **许可证**: MIT
