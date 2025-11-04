
---
title: text-embeddings-inference
---


# text-embeddings-inference

**GitHub 地址**：<https://github.com/huggingface/text-embeddings-inference>

## 主要特性
- **高效推理**：基于 ONNX(Runtime) 或 TorchScript，支持 CPU、GPU 与 INT8/FP16 量化模型。
- **多模型支持**：兼容多种 Hugging Face Transformer 预训练模型（如 `sentence-transformers/all-MiniLM-L6-v2`、`all-mpnet-base-v2` 等）。
- **易用接口**：提供 Python API、CLI 与 REST API 调用方式。
- **轻量部署**：可将模型导出为 ONNX 或 TorchScript，减少依赖，适合边缘设备。

## 核心功能
| 功能 | 说明 |
|------|------|
| `Embedder` 类 | 一键加载并推理任意支持模型、量化方式。 |
| Batch 推理 | 支持批量文本序列一次性处理。 |
| GPU 加速 | 通过 `use_cuda=True` 自动切换 CUDA 加速。 |
| 量化推理 | 量化模式（FP16/INT8）可显著降低内存占用，速度提升。 |
| REST API | 通过 `cli` 生成 FastAPI 微服务，支持 HTTP 请求。 |

## 安装方式
```bash
# pip 安装
pip install text-embeddings-inference
```

## 快速上手（Python API）
```python
from text_embeddings_inference import Embedder

# 加载模型（默认下载到缓存）
embedder = Embedder(model_name="sentence-transformers/all-MiniLM-L6-v2",
                    model_revision="main",
                    cache_dir=None,
                    device="cpu")

# 单个文本推理
embedding = embedder.encode("Hugging Face 的目标是加速 NLP 开发。")
print(embedding.shape)  # (384,) 或 (768,)

# 批量推理
texts = ["你好", "世界", "人工智能"]
batch_emb = embedder.encode(texts, batch_size=32)
print(batch_emb.shape)  # (3, 384)
```

## 快速上手（CLI + REST API）
```bash
# 运行 CLI
python -m text_embeddings_inference.cli --model sentence-transformers/all-MiniLM-L6-v2

# 默认在 http://0.0.0.0:8000/ 监听

# 通过 curl 调用
curl -X POST http://localhost:8000/encode \
  -H "Content-Type: application/json" \
  -d '{"text": ["我爱学习"], "device":"cpu"}'
```

## 进阶使用
- **量化推理**  
  ```python
  embedder = Embedder(model_name="sentence-transformers/all-mpnet-base-v2",
                      int8=True,  # 自动 INT8 量化
                      device="cpu")
  ```
- **自定义分词器**  
  通过 `tokenizer_kwargs` 参数传递 Hugging Face `tokenizer` 配置，例如 `padding='max_length'`。

## 许可证
MIT License – 详情见项目根目录的 `LICENSE` 文件。

---

> **提示**：在正式环境使用前，建议先阅读项目 `docs/` 目录下的完整使用手册和示例。
