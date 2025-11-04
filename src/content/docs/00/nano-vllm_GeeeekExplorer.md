
---
title: nano-vllm
---

# nano-vllm (GeeeekExplorer)

项目地址: https://github.com/GeeeekExplorer/nano-vllm

## 主要特性
- **轻量级**: 专为小型 GPU/CPU 设计，显存占用低，可在 RTX 6000 / 4090 等显卡上高效运行。  
- **多模型支持**: 兼容 LLaMA、ChatGLM、Phi 等开源模型，支持多种精度（fp8、int4、int8 等压缩权重）。  
- **高吞吐量**: 与标准 vLLM 相比，性能提升可达 1.5×，显著降低延迟。  
- **模型压缩**: 自带低位宽压缩存储与算子，支持模型微调后自动切换到压缩格式。  
- **统一 API**: 提供 `model.load()`, `model.generate()` 与 `model.stream_generate()` 等统一接口。  

## 功能概览
1. **模型加载**：支持 `.bin` / `.safetensors` 读取，压缩后直接放回磁盘。  
2. **推理**：批处理、流水线推理；可通过 `max_new_tokens`, `p`, `temperature` 等参数细调生成质量。  
3. **分词**：根据模型不同使用合适 tokenizer。  
4. **流式返回**：`stream_generate()` 提供按 token 逐步输出，适用于聊天机器人。  
5. **PyTorch 兼容**：内部使用 PyTorch Tensor，并可调用 `to("cuda")`，保持与原生 vLLM 的一致性。  
6. **性能调优**：提供 autotune 的几种策略，包括卷积+softmax fusion、低阶矩阵乘互换。  

## 用法示例

```python
from nano_vllm import NanoModel, NanoTokenizer

# 初始化模型
model = NanoModel(
    model_path="path/to/llama-7b-8bit",
    device="cuda:0",
    max_seq_len=4096
)

# 加载 tokenizer
tokenizer = NanoTokenizer.from_pretrained("path/to/llama-7b-8bit")

# 生成文本
prompt = "请解释一下量子力学的基本原理："
input_ids = tokenizer.encode(prompt, return_tensors="pt").to(model.device)

output_ids = model.generate(
    input_ids,
    max_new_tokens=50,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(generated_text)

# 流式输出
for token_id in model.stream_generate(
    input_ids,
    max_new_tokens=50,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
):
    print(tokenizer.decode(token_id, skip_special_tokens=True), end="", flush=True)
```

## 环境依赖
- Python ≥ 3.9  
- PyTorch ≥ 2.0 (CUDA 12.x / CPU)  
- transformers 4.30+ (tokenizer)  
- numba 0.55+ (为压缩运算加速)  

## 开发与贡献
请参阅 repo 内的 `CONTRIBUTING.md` 与 `docs/` 目录获取详细的开发流程与代码规范。  

---  

> 🛠️ **快速启动**

```bash
pip install -e .
# 或者直接从 PyPI 安装
pip install nano-vllm
