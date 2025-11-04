
---
title: vllm-ascend
---


# vllm-ascend

> **项目地址**  
> https://github.com/vllm-project/vllm-ascend

---

## 项目概述
vllm-ascend 是基于 **vLLM** 的高性能大模型推理框架，在华为 Ascend AI 处理器上实现了显著的加速与优化。它兼容原生 vLLM 的 API，支持多种大模型（如 LLaMA、ChatGLM、Mistral 等），专门针对 Ascend 设备做了内存管理、算子优化与并行调度，能够在 Ascend 910/910P/910B 等芯片上实现低延迟、高吞吐的推理。

---

## 主要特性
- **Ascend 专属优化**  
  - 针对 Ascend 910 系列的算子实现（如 BF16、FP16、INT8）
  - 内存复用与梯度裁剪，显存占用大幅降低
  - 动态批处理与流水线调度，提升吞吐量

- **兼容 vLLM 接口**  
  - 直接替换 `vllm.LLMEngine`、`vllm.LLM` 等，可无缝迁移
  - 支持 `vLLM` 现有的 `auto_chat`, `pipeline` 等函数

- **多模型支持**  
  - LLaMA、ChatGLM、Mistral、Falcon、InternLM、Mixtral 等
  - 提供模型下载脚本与配置文件

- **高可扩展性**  
  - 支持多卡（Ascend 910P/910B）并行推理
  - 通过 `--num-gpus` 参数轻松切换单卡/多卡模式

- **易用的部署方式**  
  - Docker 镜像内置 Ascend 运行时
  - 纯 Python 包可直接 `pip install vllm-ascend`

---

## 功能亮点

| 功能 | 说明 |
|------|------|
| **高吞吐** | 单卡上可达 5× vLLM 原生 FP16 吞吐，内存占用 70% 以内 |
| **低延迟** | 动态批处理混合推理，平均响应 < 500ms |
| **混合精度** | 支持 BF16 / FP16 / INT8，按需切换 |
| **内存复用** | 通过 `MemoryManager` 自动复用显存，显存峰值降低 |
| **多卡并行** | 采用 `torch.distributed` + `ascend` 通道，能在 4 卡上实现 10× 吞吐提升 |
| **Python API** | 兼容 `vLLM` 的 `LLMEngine`、`LLM`、`ChatCompletion` 等接口 |

---

## 快速开始

### 1. 安装

```bash
# 直接 pip 安装
pip install vllm-ascend

# 或者使用 Docker（推荐）
docker pull registry.cn-beijing.aliyuncs.com/ascend/vllm-ascend:latest
```

### 2. 运行示例

```python
from vllm import LLM, SamplingParams

# 初始化模型（自动使用 Ascend 优化）
llm = LLM(
    model="meta-llama/Llama-2-7b-chat-hf",
    dtype="float16",            # BF16/FP16/INT8 可选
    device="ascend",            # 自动使用 Ascend
    max_model_len=2048,
    gpu_memory_utilization=0.7  # 70% 显存占用
)

prompt = "请用简体中文介绍一下大模型推理。"

# 采样参数
params = SamplingParams(temperature=0.1, top_p=0.95, max_tokens=128)

# 推理
outputs = llm.generate([prompt], params)

for output in outputs:
    print(output.text)
```

### 3. 多卡部署

```bash
# 在 4 卡环境下启动
python -m torch.distributed.launch \
    --nproc_per_node=4 \
    --master_port=29500 \
    your_script.py
```

### 4. Docker 部署示例

```bash
docker run -it --gpus all \
    -v /path/to/models:/models \
    registry.cn-beijing.aliyuncs.com/ascend/vllm-ascend:latest \
    python -m vllm.entrypoints.openai.api_server \
    --model /models/meta-llama/Llama-2-7b-chat-hf \
    --dtype float16 \
    --device ascend
```

---

## 依赖与兼容性

- Python 3.8+  
- PyTorch 2.0+（Ascend 版本）  
- `vllm` 0.3.x 及以上  
- Ascend AI 处理器（910/910P/910B）  
- Ascend AI 运行时（Ascend SDK 5.0+）

---

## 贡献

欢迎提交 PR、issue 或者加入社区讨论。请遵循项目的 [贡献指南](https://github.com/vllm-project/vllm-ascend/blob/main/CONTRIBUTING.md)。

---

## 参考文档

- 官方文档: https://github.com/vllm-project/vllm-ascend  
- vLLM 文档: https://docs.vllm.ai/  
- Ascend 开发者社区: https://developer.huawei.com/consumer/en/ascend

---