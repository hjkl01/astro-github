---
title: Hands-On-Large-Language-Models
---

# Hands-On Large Language Models

## 项目简介

这是 O'Reilly 书籍《Hands-On Large Language Models》的官方代码仓库，由 Jay Alammar 和 Maarten Grootendorst 编写。该书通过近 300 张自定义图表，以视觉教育的方式，帮助读者学习使用大型语言模型的实用工具和概念。

## 功能

该仓库包含书籍中所有示例的代码，涵盖大型语言模型的各个方面：

- **第1章：语言模型介绍** - 基础概念和概述
- **第2章：Tokens 和 Embeddings** - 文本分词和嵌入表示
- **第3章：深入 Transformer LLM** - 理解 Transformer 架构内部工作原理
- **第4章：文本分类** - 使用 LLM 进行文本分类任务
- **第5章：文本聚类和主题建模** - 无监督学习应用
- **第6章：Prompt Engineering** - 提示工程技巧
- **第7章：高级文本生成技术和工具** - 文本生成方法
- **第8章：语义搜索和检索增强生成 (RAG)** - 信息检索和增强
- **第9章：多模态大型语言模型** - 处理多种模态的数据
- **第10章：创建文本嵌入模型** - 构建嵌入模型
- **第11章：微调表示模型用于分类** - BERT 微调
- **第12章：微调生成模型** - 生成模型微调

此外，还包括奖励内容，如 Mamba、量化、Stable Diffusion、Mixture of Experts 等视觉指南。

## 用法

### 推荐环境：Google Colab

建议使用 Google Colab 运行所有示例，因为它提供免费的 T4 GPU（16GB VRAM），所有示例主要在 Colab 上构建和测试。

每个章节都有对应的 Colab notebook 链接，可以直接在浏览器中打开和运行。

### 本地安装

如果要在本地运行：

1. 克隆仓库：

   ```bash
   git clone https://github.com/HandsOnLLM/Hands-On-Large-Language-Models.git
   cd Hands-On-Large-Language-Models
   ```

2. 安装依赖：
   - 检查 `.setup` 文件夹中的快速开始指南
   - 使用 `requirements.txt` 或 `requirements_min.txt` 安装 Python 包
   - 对于 conda 环境，参考 `.setup/conda` 文件夹

3. 运行 notebook：
   使用 Jupyter Notebook 或 JupyterLab 打开各章节的 `.ipynb` 文件。

注意：根据操作系统、Python 版本和依赖项的不同，结果可能略有差异，但应与书籍中的示例相似。

## 引用

如果您在研究中使用了本书，请考虑引用：

```
@book{hands-on-llms-book,
  author       = {Jay Alammar and Maarten Grootendorst},
  title        = {Hands-On Large Language Models},
  publisher    = {O'Reilly},
  year         = {2024},
  isbn         = {978-1098150969},
  url          = {https://www.oreilly.com/library/view/hands-on-large-language/9781098150952/},
  github       = {https://github.com/HandsOnLLM/Hands-On-Large-Language-Models}
}
```
