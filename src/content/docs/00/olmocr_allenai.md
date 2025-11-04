
---
title: olmocr
---


# OLMOCR (AllenAI) – 开源 OCR 解决方案

**项目地址**  
<https://github.com/allenai/olmocr>

---

## 1. 主要特性

| 特性 | 描述 |
|------|------|
| **端到端 OCR** | 支持文字检测、定位、识别与布局分析，覆盖 PDF、扫描图像、表格等多种文档类型。 |
| **基于 LayoutLM 系列** | 集成了 LayoutLMv3/4 等最新模型，兼顾视觉与文本信息，提升复杂文档的识别准确率。 |
| **多语言支持** | 预训练模型覆盖中英日等多种语言，亦可轻松自定义训练新语言。 |
| **可扩展的推理框架** | 提供 `olmocr.inference`、`olmocr.pipeline` 等模块，支持单张图像、批量推理以及 ONNX 导出。 |
| **训练与微调工具** | 通过 `olmocr.train` 包含简易脚本，可在 Hugging Face 数据集或自定义数据集上快速微调。 |
| **轻量级依赖** | 仅依赖 `torch`, `transformers`, `datasets`, `pillow`, `opencv-python` 等常用库，安装简便。 |
| **文档与示例** | 完整的使用手册、教程与 Jupyter Notebook 示例，帮助快速上手。 |

---

## 2. 功能概览

### 2.1 OCR Pipeline
```python
from olmocr.pipeline import OLMORCPipeline

pipeline = OLMORCPipeline.from_pretrained("allenai/olmocr-base")
result = pipeline("sample_document.jpg")
print(result["text"])          # 识别文本
print(result["layout"])        # 文字框坐标与层级
```

### 2.2 文字检测 & 识别
```python
from olmocr.inference import OLMOCRInference

inference = OLMOCRInference.from_pretrained("allenai/olmocr-base")
detections = inference.detect("sample_document.jpg")
recognitions = inference.recognize("sample_document.jpg")
```

### 2.3 ONNX 导出
```python
inference.export_onnx("olmocr_base.onnx")
```

### 2.4 训练 / 微调
```bash
# 克隆仓库
git clone https://github.com/allenai/olmocr.git
cd olmocr

# 安装依赖
pip install -r requirements.txt

# 训练
python train.py \
  --model_name_or_path allenai/olmocr-base \
  --dataset_name my_dataset \
  --output_dir ./runs/olmocr_finetune
```

---

## 3. 快速开始

1. **安装**  
   ```bash
   pip install olmocr
   ```

2. **推理示例**  
   ```python
   from olmocr.pipeline import OLMORCPipeline

   pipeline = OLMORCPipeline.from_pretrained("allenai/olmocr-base")
   output = pipeline("docs/samples/sample_page.png")
   print(output["text"])
   ```

3. **自定义数据集**  
   - 按照 `datasets` 格式准备 `train.json` / `validation.json`  
   - 运行 `train.py` 进行微调

4. **部署**  
   - 生成 ONNX 模型后，可在 TensorRT、OpenVINO 等推理引擎中部署  
   - 或使用 `FastAPI` + `uvicorn` 快速部署接口

---

## 4. 相关资源

- **文档**：<https://allenai.github.io/olmocr>
- **演示 Notebook**：<https://github.com/allenai/olmocr/tree/master/notebooks>
- **社区讨论**：AllenAI Discord / GitHub Issues

---

**备注**：本文档仅提供核心信息，更多细节请参阅官方仓库与文档。祝使用愉快！```
```

（请将上述内容保存为 `src/content/docs/00/olmocr_allenai.md`。）