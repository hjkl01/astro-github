---
title: Trl
---

# TRL - Transformer Reinforcement Learning

## 功能

TRL 是一个用于使用强化学习后训练基础模型的全面库。支持先进技术如监督微调 (SFT)、近端策略优化 (PPO) 和直接偏好优化 (DPO)。基于 🤗 Transformers 生态，支持各种模型架构和模态，可扩展到各种硬件设置。

### 亮点

- **Trainers**: 提供如 `SFTTrainer`、`GRPOTrainer`、`DPOTrainer`、`RewardTrainer` 等训练器。
- **高效可扩展**: 利用 🤗 Accelerate 进行分布式训练，支持 PEFT 进行量化/LoRA/QLoRA，集成 Unsloth 加速训练。
- **命令行界面 (CLI)**: 无需编写代码即可微调模型。

## 用法

### 安装

```bash
pip install trl
```

或从源码安装：

```bash
pip install git+https://github.com/huggingface/trl.git
```

### 快速开始

#### SFTTrainer 示例

```python
from trl import SFTTrainer
from datasets import load_dataset

dataset = load_dataset("trl-lib/Capybara", split="train")

trainer = SFTTrainer(
    model="Qwen/Qwen2.5-0.5B",
    train_dataset=dataset,
)
trainer.train()
```

#### GRPOTrainer 示例

```python
from datasets import load_dataset
from trl import GRPOTrainer

dataset = load_dataset("trl-lib/tldr", split="train")

def reward_num_unique_chars(completions, **kwargs):
    return [len(set(c)) for c in completions]

trainer = GRPOTrainer(
    model="Qwen/Qwen2-0.5B-Instruct",
    reward_funcs=reward_num_unique_chars,
    train_dataset=dataset,
)
trainer.train()
```

#### DPOTrainer 示例

```python
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import DPOConfig, DPOTrainer

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
dataset = load_dataset("trl-lib/ultrafeedback_binarized", split="train")
training_args = DPOConfig(output_dir="Qwen2.5-0.5B-DPO")
trainer = DPOTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    processing_class=tokenizer
)
trainer.train()
```

### CLI 用法

**SFT:**

```bash
trl sft --model_name_or_path Qwen/Qwen2.5-0.5B \
    --dataset_name trl-lib/Capybara \
    --output_dir Qwen2.5-0.5B-SFT
```

**DPO:**

```bash
trl dpo --model_name_or_path Qwen/Qwen2.5-0.5B-Instruct \
    --dataset_name argilla/Capybara-Preferences \
    --output_dir Qwen2.5-0.5B-DPO
```

更多详情请参考 [官方文档](https://huggingface.co/docs/trl/index)。
