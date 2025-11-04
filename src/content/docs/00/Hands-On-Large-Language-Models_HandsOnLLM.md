
---
title: Hands-On-Large-Language-Models
---


# Hands-On-Large-Language-Models

> 🔗 **GitHub 地址**: <https://github.com/HandsOnLLM/Hands-On-Large-Language-Models>

## 主要特性

| 特性 | 简述 |
|------|------|
| **多模型支持** | 包含 Llama 2、Mixtral、OpenAI GPT 系列等主流 LLM，方便对比与实验 |
| **易用的 Notebook** | Jupyter Notebook 集成了从数据预处理、微调、推理到评估的完整流程 |
| **Prompt Engineering** | 多种提示模板与策略，示例覆盖零样本、少样本与微调后提示 |
| **训练与微调** | 提供基于 Hugging Face Transformers 的 fine‑tuning 脚本，支持 LoRA、PEFT 等技术 |
| **评估与基准** | 内置对话生成、阅读理解、推理等任务的评测脚本，支持自定义数据集 |
| **可扩展的项目结构** | 统一的 `src/` 、`data/`、`notebooks/` 等目录，方便插件式开发 |
| **CI/CD 与自动化** | GitHub Actions 自动化测试与构建，确保代码质量 |

## 核心功能

1. **环境搭建**  
   - 依赖 `requirements.txt` / `environment.yml`，支持 CPU / GPU / CUDA 版本
2. **模型下载与缓存**  
   - 脚本 `scripts/download_models.py` 可一次性下载所需预训练权重
3. **数据预处理**  
   - `scripts/preprocess_data.py` 支持 JSON, CSV, Markdown 等多种格式转换为 trainer 输入
4. **模型微调**  
   - `train_lora.py` / `train_peft.py`：针对 LLM 微调，支持 LoRA、QLoRA、QLoRA 等
5. **推理接口**  
   - `infer.py`：提供 RESTful API 与命令行工具两种使用方式
6. **评估工具**  
   - `evaluate.py`：集成 BLEU, ROUGE, METEOR, GPTScore 等指标
7. **实验记录**  
   - Jupyter Notebook 自动生成实验日志，方便复现与对比

## 用法示例

```bash
# 1. 克隆仓库
git clone https://github.com/HandsOnLLM/Hands-On-Large-Language-Models.git
cd Hands-On-Large-Language-Models

# 2. 创建并激活虚拟环境
conda env create -f environment.yml      # 或者 pip install -r requirements.txt
conda activate llm-experiment

# 3. 下载模型权重
python scripts/download_models.py --model llama2-13b

# 4. 预处理数据（可选）
python scripts/preprocess_data.py --input data/raw/train.json --output data/processed/train.pkl

# 5. 微调（示例: LoRA）
python train_lora.py --model llama2-13b --dataset data/processed/train.pkl --output_dir checkpoints/llama2-13b-lora

# 6. 推理
python infer.py --model checkpoints/llama2-13b-lora --prompt "请解释量子纠缠。"

# 7. 评估
python evaluate.py --model checkpoints/llama2-13b-lora --dataset data/processed/dev.pkl
```

> **注意**  
> - 若使用 GPU，请确认已安装对应的 CUDA 驱动与 cuDNN。  
> - 运行过程中如遇到显存不足，可使用 `--low_cpu_mem_usage` 或启用梯度累积。  

---

> 以上内容可直接复制保存为  
> `src/content/docs/00/Hands-On-Large-Language-Models_HandsOnLLM.md`
```

💝 Support this free API: https://www.paypal.com/donate/?hosted_button_id=XS3CAYT8LE2BL