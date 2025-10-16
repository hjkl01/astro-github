
---
title: docling
---

# Docling 项目

**GitHub 项目地址：** [https://github.com/DS4SD/docling](https://github.com/DS4SD/docling)

## 主要特性
Docling 是由 DS4SD（Deep Search for Scientific Discovery）开发的一个开源文档转换工具，主要针对 PDF 等复杂文档格式，提供高精度转换到结构化 Markdown 或 JSON 的能力。其核心特性包括：
- **高级文档解析**：支持处理科学论文、报告和多语言文档，自动识别布局、表格、图像和公式。
- **AI 集成**：利用机器学习模型（如 LayoutLM 和 Table Transformer）实现精确的元素提取和重组，避免传统 OCR 的局限性。
- **模块化设计**：可扩展的架构，支持自定义模型和插件，便于集成到更大系统中。
- **开源与免费**：基于 Apache 2.0 许可，社区驱动开发，适用于研究和企业应用。
- **多格式支持**：输入包括 PDF、图像等，输出为 Markdown、HTML 或 JSON，便于后续处理如 RAG（Retrieval-Augmented Generation）。

## 主要功能
- **文档转换**：将 PDF 转换为可读的 Markdown，保留原文档的结构和语义。
- **元素提取**：自动检测并提取表格、图表、标题、段落和参考文献，支持数学公式渲染（LaTeX）。
- **质量优化**：内置后处理步骤，提升转换准确率，处理扫描文档或低质量 PDF。
- **批量处理**：支持命令行批量转换多个文件，适用于大规模文档库。
- **API 接口**：提供 Python API，便于嵌入到自定义工作流中。

## 用法
### 安装
1. 确保 Python 3.8+ 环境。
2. 通过 pip 安装：
   ```
   pip install docling
   ```
3. 对于高级功能（如 GPU 支持），安装额外依赖：
   ```
   pip install docling[full]
   ```

### 基本用法
- **命令行转换**：
  ```
  docling convert input.pdf --output output.md
  ```
  这将 PDF 转换为 Markdown 文件。

- **Python API 示例**：
  ```python
  from docling.document_converter import DocumentConverter
  from docling.datamodel.base_models import InputFormat
  from pathlib import Path

  # 初始化转换器
  converter = DocumentConverter()

  # 转换文档
  source = Path("input.pdf")
  result = converter.convert(source, format=InputFormat.PDF)

  # 输出 Markdown
  with open("output.md", "w", encoding="utf-8") as f:
      f.write(result.document.export_to_markdown())
  ```

### 高级用法
- **自定义模型**：通过配置文件加载特定模型，例如：
  ```
  docling convert input.pdf --model-config custom_model.yaml
  ```
- **集成到项目**：Docling 可与 LangChain 或 Hugging Face 结合，用于文档 AI 管道。
- 更多细节请参考项目 README 和示例文件夹。