---
title: JioNLP
---

# JioNLP 项目介绍

**GitHub 项目地址:** [https://github.com/dongrixinyu/JioNLP](https://github.com/dongrixinyu/JioNLP)

## 主要特性
JioNLP 是一个开源的自然语言处理（NLP）工具包，专注于中文NLP任务。它基于深度学习模型，提供高效、易用的接口，支持多种预训练模型和自定义训练。核心特性包括：
- **模块化设计**：集成分词、词性标注、命名实体识别（NER）、文本分类、情感分析等核心NLP功能。
- **支持多种模型**：兼容BERT、RoBERTa等Transformer模型，以及传统模型如LSTM、CRF。
- **轻量级部署**：无需复杂环境，支持PyTorch和TensorFlow后端，适合学术研究和工业应用。
- **中文优化**：针对中文语料进行预训练和微调，提供高准确率的中文处理能力。
- **扩展性强**：支持插件式扩展，用户可轻松添加自定义模型或任务。

## 主要功能
- **文本预处理**：分词、去停用词、文本清洗。
- **序列标注任务**：词性标注（POS）、命名实体识别（NER）、依存句法分析。
- **分类任务**：文本分类、情感分析、意图识别。
- **生成任务**：文本摘要、机器翻译（部分支持）。
- **嵌入表示**：词向量、句子嵌入，支持相似度计算。
- **评估工具**：内置准确率、F1分数等指标计算。

## 用法
1. **安装**：
   ```bash
   pip install jionlp
   ```

2. **基本使用示例**（Python代码）：
   ```python
   from jionlp import JioNLP

   # 初始化
   jn = JioNLP()

   # 分词
   text = "这是一个测试句子。"
   seg_result = jn.segment(text)
   print(seg_result)  # 输出: ['这是', '一个', '测试', '句子', '。']

   # 命名实体识别
   ner_result = jn.ner(text)
   print(ner_result)  # 输出: [{'word': '测试', 'type': 'ENTITY'}]（示例）

   # 文本分类
   class_result = jn.classify(text, task='sentiment')
   print(class_result)  # 输出: {'label': 'positive', 'score': 0.85}
   ```

3. **自定义训练**：
   - 使用提供的API加载数据集，进行模型微调。
   - 示例：`jn.train(model_type='bert', data_path='your_data.json', task='ner')`。

详细文档和更多示例请参考项目仓库的README和examples目录。