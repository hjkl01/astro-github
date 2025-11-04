
---
title: candle
---


# Candle (Hugging Face)

**GitHub 地址**: <https://github.com/huggingface/candle>

Candle 是 Hugging Face 推出的一个轻量级、跨平台的深度学习库，基于 Rust 编写，提供高性能的推理、训练以及模型量化工具。它通过 Rust 的安全性和速度优势，为 Python 开发者提供了简洁易用的接口，支持主流模型格式（PyTorch、ONNX、Hugging Face Hub）。

## 主要特性

| 特性 | 说明 |
|------|------|
| **高性能** | Rust 语言实现，利用 SIMD、GPU 加速（CUDA、ROCm） |
| **跨平台** | 支持 Linux、macOS、Windows |
| **多框架兼容** | 直接加载 Hugging Face Hub、PyTorch、ONNX 模型 |
| **易用的 Python API** | `pip install candle-lightning` 或 `pip install candle` |
| **模型量化** | 8-bit/4-bit 量化，降低显存占用 |
| **训练与推理** | 支持微调、全流程训练、梯度累积 |
| **ONNX 生态** | 支持 ONNX 2.6+，可将 PyTorch 模型导出为 ONNX 并在 Candle 运行 |
| **Lightning 接口** | 与 PyTorch Lightning 对齐的训练脚本模板 |

## 核心组件

- **`candle`**：核心张量（Tensor）与算子（Ops）实现。  
- **`candle-transformers`**：Transformer 模型实现（BERT、GPT、T5 等）。  
- **`candle-optimizers`**：优化器（Adam、AdamW 等）。  
- **`candle-lightning`**：与 PyTorch Lightning 兼容的训练框架。  
- **`candle-quantization`**：模型量化工具。

## 安装

```bash
# 安装核心库（含 CUDA/ROCm 可选）
pip install candle

# 或者安装 Lightning 版（支持 Lightning 训练脚本）
pip install candle-lightning
```

## 快速使用

### 推理示例（BERT）

```python
from candle import Device, Tensor
from candle_transformers import BertModel, BertTokenizer

# 选择设备
device = Device.cuda()  # 或 Device.cpu()

# 加载 tokenizer 与模型
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased", device=device)

# 编码
inputs = tokenizer(["Hello, world!", "Candle is cool."], return_tensors="pt")
input_ids = Tensor.from_numpy(inputs["input_ids"].numpy()).to(device)
attention_mask = Tensor.from_numpy(inputs["attention_mask"].numpy()).to(device)

# 推理
outputs = model.forward(input_ids, attention_mask=attention_mask)
print(outputs.last_hidden_state.shape)  # (batch_size, seq_len, hidden_dim)
```

### ONNX 导出与推理

```python
# 将 PyTorch 模型导出为 ONNX
import torch
from transformers import AutoModel

torch_model = AutoModel.from_pretrained("bert-base-uncased")
torch_model.eval()
dummy_input = torch.randint(1000, (1, 128))
torch.onnx.export(
    torch_model,
    dummy_input,
    "bert-base-uncased.onnx",
    opset_version=13,
    input_names=["input_ids"],
    output_names=["output"],
)

# 在 Candle 中加载 ONNX
from candle import Device
from candle_onnx import OnnxModel

device = Device.cpu()
onnx_model = OnnxModel.from_file("bert-base-uncased.onnx", device=device)
input_ids = Tensor.from_numpy(dummy_input.numpy()).to(device)
output = onnx_model.forward(input_ids)
```

### 模型量化

```python
from candle_quantization import quantize

# 量化为 8-bit
quantized_model = quantize(
    model_path="bert-base-uncased",
    output_path="bert-base-uncased-quantized",
    bits=8,
    device=device
)
```

### Lightning 训练示例

```python
from candle_lightning import LightningModule, Trainer
from candle_transformers import BertForSequenceClassification

class SentimentModel(LightningModule):
    def __init__(self):
        super().__init__()
        self.model = BertForSequenceClassification.from_pretrained("bert-base-uncased")

    def training_step(self, batch, batch_idx):
        outputs = self.model(**batch)
        loss = outputs.loss
        self.log("train_loss", loss)
        return loss

trainer = Trainer(max_epochs=3, gpus=1)
model = SentimentModel()
trainer.fit(model, train_dataloader, val_dataloader)
```

## 贡献与支持

- 贡献指南请参阅 [CONTRIBUTING.md](https://github.com/huggingface/candle/blob/main/CONTRIBUTING.md)。
- 文档与示例在 `docs/` 目录下，包含 API 参考、FAQ 与教程。
- 如需进一步帮助，请在 GitHub Issues 或 Hugging Face 社区提交问题。

---

> 以上内容为项目 **Candle** 的核心特性、功能与使用示例，帮助开发者快速上手并在生产环境中部署高效的 NLP 模型。