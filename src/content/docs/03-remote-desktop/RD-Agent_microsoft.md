---
title: RD-Agent
---

# RD-Agent 项目

## 项目地址

[https://github.com/microsoft/RD-Agent](https://github.com/microsoft/RD-Agent)

## 主要特性

RD-Agent 是一个开源的 R&D（研究与开发）自动化框架，旨在通过 AI 驱动数据驱动的 AI，实现工业生产力提升的关键 R&D 流程自动化。主要特性包括：

- **开源免费**：基于 MIT 许可，完全开源，支持社区贡献。
- **多场景支持**：涵盖量化交易、数据科学、医疗预测等数据驱动场景。
- **AI 驱动**：利用大型语言模型（如 GPT-4、o1-preview）自动化研究、开发和迭代过程。
- **高性能**：在 MLE-bench 上领先，支持复杂任务如 Kaggle 竞赛和量化策略优化。
- **易于部署**：支持 Docker 和本地安装，提供 Web UI 和命令行接口。

## 主要功能

- **量化交易自动化**：迭代提出和实现因子模型与策略，优化交易性能。
- **数据科学代理**：自动化模型研究、特征工程和超参数调优，支持 Kaggle 等竞赛。
- **医疗预测模型**：自循环模型提案和实现，用于医疗数据分析。
- **通用模型研究**：从论文或报告中提取和实现模型结构。
- **多 LLM 支持**：集成 LiteLLM，支持多种 LLM 提供商。
- **Web 演示**：提供在线演示和文档，便于快速上手。

## 用法

1. **安装**：
   - 从 PyPI 安装：`pip install rdagent`
   - 或从源码：`git clone https://github.com/microsoft/RD-Agent && cd RD-Agent && make dev`

2. **配置**：
   - 设置环境变量：CHAT_MODEL、EMBEDDING_MODEL 等，支持 OpenAI、Azure 等。
   - 示例：`export CHAT_MODEL=gpt-4o; export OPENAI_API_KEY=your_key`

3. **运行场景**：
   - 量化交易：`rdagent fin_quant`
   - 数据科学：`rdagent data_science --competition <name>`
   - 医疗预测：`rdagent data_science --competition arf-12-hours-prediction-task`
   - 通用模型：`rdagent general_model <paper_url>`

4. **监控结果**：
   - 使用 `rdagent ui --port 19899 --log-dir <log_dir>` 查看日志和结果。

更多详情请参考项目文档：[https://rdagent.readthedocs.io/](https://rdagent.readthedocs.io/)
