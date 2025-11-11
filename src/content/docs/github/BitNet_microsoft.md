---
title: BitNet
---

# BitNet

BitNet 是微软开发的官方推理框架，专为 1-bit 大型语言模型 (LLMs) 设计，如 BitNet b1.58。它提供了一套优化的内核，支持在 CPU 和 GPU 上进行快速且无损的 1.58-bit 模型推理。

## 功能特性

- **高效推理**：在 ARM CPU 上实现 1.37x 到 5.07x 的速度提升，在 x86 CPU 上实现 2.37x 到 6.17x 的速度提升。
- **节能**：减少能量消耗 55.4% 到 82.2%。
- **大规模支持**：可在单 CPU 上运行 100B 参数的 BitNet b1.58 模型，速度相当于人类阅读速度 (5-7 tokens/秒)。
- **多平台**：支持 CPU 和 GPU 推理 (NPU 支持即将到来)。
- **开源**：基于 llama.cpp 框架，采用 MIT 许可证。

## 支持的模型

- BitNet-b1.58-2B-4T (官方模型)
- bitnet_b1_58-large (0.7B 参数)
- bitnet_b1_58-3B (3.3B 参数)
- Llama3-8B-1.58-100B-tokens
- Falcon3 和 Falcon-E 系列模型

## 安装和构建

### 要求

- Python >= 3.9
- CMake >= 3.22
- Clang >= 18
- Conda (推荐)

### 构建步骤

1. 克隆仓库：

   ```bash
   git clone --recursive https://github.com/microsoft/BitNet.git
   cd BitNet
   ```

2. 创建并激活 Conda 环境：

   ```bash
   conda create -n bitnet-cpp python=3.9
   conda activate bitnet-cpp
   pip install -r requirements.txt
   ```

3. 下载模型并设置环境：

   ```bash
   huggingface-cli download microsoft/BitNet-b1.58-2B-4T-gguf --local-dir models/BitNet-b1.58-2B-4T
   python setup_env.py -md models/BitNet-b1.58-2B-4T -q i2_s
   ```

4. 构建项目：
   ```bash
   # 构建命令会自动执行
   ```

## 用法

### 基本推理

运行推理：

```bash
python run_inference.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf -p "You are a helpful assistant" -cnv
```

参数说明：

- `-m`: 模型文件路径
- `-p`: 提示词
- `-cnv`: 启用聊天模式
- `-t`: 线程数
- `-c`: 上下文大小
- `-temp`: 温度参数

### 基准测试

运行基准测试：

```bash
python utils/e2e_benchmark.py -m /path/to/model -n 200 -p 256 -t 4
```

参数：

- `-m`: 模型路径
- `-n`: 生成 token 数
- `-p`: 提示 token 数
- `-t`: 线程数

### 从 Safetensors 转换

转换模型：

```bash
huggingface-cli download microsoft/bitnet-b1.58-2B-4T-bf16 --local-dir ./models/bitnet-b1.58-2B-4T-bf16
python ./utils/convert-helper-bitnet.py ./models/bitnet-b1.58-2B-4T-bf16
```

## 演示

提供了一个在 Apple M2 上运行 BitNet b1.58 3B 模型的演示视频。

更多详情请参考 [GitHub 仓库](https://github.com/microsoft/BitNet) 和相关论文。
