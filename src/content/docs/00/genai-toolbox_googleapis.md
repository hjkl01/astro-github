
---
title: genai-toolbox
---


# genai-toolbox

## 项目地址
[https://github.com/googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox)

## 主要特性
- **统一的工具集**：提供一套通用 API 与封装，帮助快速构建和管理 GenAI 项目。
- **可插拔组件**：支持轻量化引入多种模型、数据格式、后端服务，方便（再）组合使用。
- **跨框架兼容**：兼容 TensorFlow、PyTorch、JAX 等主流深度学习框架。
- **可视化与监控**：集成日志、指标收集与展示功能，支持对模型训练与推理全过程的跟踪。
- **社区驱动**：开放、可扩展的插件系统，允许社区贡献新功能与工具。

## 功能概览
| 功能 | 说明 |
|------|------|
| 模型包装 | 对多种 GenAI 模型（包括 LLM, 视觉模型等）统一接口包装，简化调用 |
| 数据预处理 | 提供 Tokenization、Segment、归一化等常用文本/视觉预处理工具 |
| 评估工具 | 包含 BLEU、ROUGE、METEOR 等文本指标以及 PER 等视觉指标 |
| 监控与报告 | 实时记录训练/推理指标，生成可视化报告 |
| 服务部署 | 支持基于 FastAPI、Flask 等框架的模型服务封装 |
| 示例代码 | 丰富的“一键运行”示例，演示多种用例（问答、摘要、推荐等） |

## 用法示例

```bash
# 1. 安装 genai-toolbox
pip install git+https://github.com/googleapis/genai-toolbox.git

# 2. 调用示例（以 LLM 文本生成为例）
python -m genai_toolbox.examples.text_generation \
  --model_name="text-generation-model" \
  --prompt="请介绍一下人工智能的未来趋势。"
```

> 进一步帮助与使用文档请参阅项目 README 和各子模块的详细说明。