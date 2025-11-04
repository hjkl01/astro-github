
---
title: AP2
---

# AP2 - Google Agentic Commerce

> 项目地址: <https://github.com/google-agentic-commerce/AP2>

## 项目简介
AP2（Agentic Commerce Platform）是 Google 推出的基于多模态大型语言模型的端到端购物体验框架。它将商品浏览、购买、客服对话等环节统一到一个智能代理体系中，支持自动生成商品推荐、订单生成、客服回答等功能。

## 主要特性  
| 功能 | 说明 |
|---|---|
| **多模态交互** | 支持文本、视觉、语音三种输入模式，能处理图片标注、语音指令等多种交互方式。 |
| **端到端代理** | 由“用户代理（User Agent）”“商品代理（Item Agent）”等模块协同完成从商品展示到下单支付的完整流程。 |
| **可扩展数据管道** | 提供采集、预处理、检查、存储的一整套工具链，支持行业数据集与自定义数据集快速接入。 |
| **多模型融合** | 支持轻量化模型（如 LLaMA、Alpaca）与大型模型（如 Gemini、GPT‑4）组合使用，兼顾算力与性能。 |
| **高度可配置** | 通过 YAML 配置文件，灵活控制模型、超参、实验环境等。 |
| **开箱即用 Demo** | 集成 Jupyter Notebook 与 Streamlit Demo，快速可视化结果。 |

## 项目文件结构
```
AP2/
├─ data/              # 原始与处理后数据
├─ models/            # 预训练模型与微调后权重
├─ notebooks/         # 交互式实验脚本
├─ scripts/           # 训练、推理、评估脚本
├─ configs/           # YAML 配置中心
├─ src/               # 核心业务逻辑
│   ├─ agents/        # 代理类实现
│   ├─ utils/         # 工具函数
│   └─ pipelines/     # 推理流水线
└─ README.md
```

## 安装与运行
1. **克隆仓库**  
   ```bash
   git clone https://github.com/google-agentic-commerce/AP2.git
   cd AP2
   ```

2. **创建虚拟环境并安装依赖**  
   ```bash
   python -m venv venv
   source venv/bin/activate          # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **下载预训练模型与数据（可选）**  
   ```bash
   python scripts/download_assets.py
   ```

4. **运行 Demo**  
   - Notebook 版：  
     ```bash
     jupyter notebook notebooks/demo.ipynb
     ```  
   - Streamlit 版：  
     ```bash
     streamlit run apps/demo_app.py
     ```

5. **训练/微调模型（示例）**  
   ```bash
   python scripts/train_agent.py --config configs/agent.yml
   ```

## 快速使用示例
```python
from ap2.pipelines import AgentPipeline
from ap2.configs import load_config

config = load_config("configs/agent.yml")
pipeline = AgentPipeline(config)

response = pipeline.run("我要买一双运动鞋，推荐一下")
print(response)
```

## 参考资料
- 论文：*Agentic Commerce: End‑to‑End AI Shopping Experience*  
- 官方博客与视频：<https://blog.google/…>  

> 以上为 AP2 的主要特性与使用方法概览。根据需求可进一步细化配置与扩展。