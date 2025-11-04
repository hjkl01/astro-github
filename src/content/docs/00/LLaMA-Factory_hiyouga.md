
---
title: LLaMA-Factory
---

# LLaMA-Factory (hiyouga)

**GitHub 项目地址:**  
<https://github.com/hiyouga/LLaMA-Factory>

---

## 主要特性

- **多模型支持** – 兼容 LLaMA、LLaMA-2、LLaMA-3 等多版本模型。  
- **轻量化微调**  
  - **LoRA / QLoRA**：通过参数共享方式仅训练少量参数，显著降低显存占用与训练成本。  
  - **全参数微调**：支持在多卡环境下全参数微调，精度不受折损。  
- **分布式训练** – 内置基于 `accelerate` + `torch.distributed` 的多卡、混合精度训练方案。  
- **数据集加载与预处理** – 支持 `datasets`、Hugging Face Hub、JSON/Text/CSV 等多种格式。通过 `PromptTemplate`、`DatasetTemplate` 自定义对话格式。  
- **自动评估** – 集成 `BLEURT`、`ROUGE-L`、`perplexity` 等指标，支持多轮对话评估。  
- **推理接口** – 可直接使用 PyTorch 或 `transformers` Pipeline，配合 `fastapi` 一键部署推理服务。  
- **多语言支持** – 内置中文、英文等 Prompt 语料与模型软对齐。  
- **可视化工具** – 基于 `tensorboard` / `wandb` 的梯度与训练曲线实时监控。  

---

## 快速上手

```bash
# 1. 克隆项目
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory

# 2. 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. 安装依赖
pip install -e .[full]     # 所有依赖 + 可选插件

# 4. 准备数据 (以学术论文摘要对话为例)
mkdir data
# data/train.jsonl、data/validation.jsonl  → 每行 {"prompt": "...", "response": "..."} 格式

# 5. 训练 LoRA 模型（预设参数文件 config/train_lora.yaml）
llama_factory train configs/train_lora.yaml

# 6. 评估
llama_factory validate configs/train_lora.yaml

# 7. 推理
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("output/lora-result")
tokenizer = AutoTokenizer.from_pretrained("output/lora-result")
input_ids = tokenizer.encode("问：谁是乔布斯？", return_tensors="pt")
output = model.generate(input_ids, max_length=128)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

---

## 使用文档

- **配置文件**：`configs/` 目录下提供多种 YAML 示例（LoRA、QLoRA、全参数微调、推理等）。  
- **CLI 说明**：  
  - `llama_factory train <config.yaml>`：训练。  
  - `llama_factory validate <config.yaml>`：验证。  
  - `llama_factory predict <config.yaml> <prompt>`：推理。  
- **自定义数据**：在 `dataloader.py` 中实现 `DatasetTemplate`，示例代码已包含多种常用格式。  

如需更详细信息，请参阅官方仓库的 `docs/` 与 `README.md`。