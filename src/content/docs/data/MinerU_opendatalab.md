---
title: MinerU
---

# MinerU (OpenDataLab)

> **项目地址**
> https://github.com/opendatalab/MinerU

## 简介

MinerU 是一个将 PDF 转换为机器可读格式（如 markdown、JSON）的工具，便于提取到任何格式。MinerU 在 InternLM 的预训练过程中诞生。我们专注于解决科学文献中的符号转换问题，并希望为大模型时代的技术发展做出贡献。与知名的商业产品相比，MinerU 还很年轻。如果您遇到任何问题或结果不符合预期，请在 [issue](https://github.com/opendatalab/MinerU/issues) 中提交，并**附上相关 PDF**。

## 主要特性

- **语义连贯性**：移除页眉、页脚、脚注、页码等，确保语义连贯。
- **可读顺序输出**：以人类可读的顺序输出文本，适用于单列、多列和复杂布局。
- **结构保留**：保留原始文档的结构，包括标题、段落、列表等。
- **多媒体提取**：提取图像、图像描述、表格、表格标题和脚注。
- **公式转换**：自动识别并将文档中的公式转换为 LaTeX 格式。
- **表格转换**：自动识别并将文档中的表格转换为 HTML 格式。
- **OCR 支持**：自动检测扫描 PDF 和乱码 PDF 并启用 OCR 功能。
- **多语言 OCR**：OCR 支持检测和识别 109 种语言。
- **多种输出格式**：支持多种输出格式，如多模态和 NLP Markdown、按阅读顺序排序的 JSON，以及丰富的中间格式。
- **可视化结果**：支持各种可视化结果，包括布局可视化和跨度可视化，以高效确认输出质量。
- **纯 CPU 运行**：支持在纯 CPU 环境中运行，也支持 GPU(CUDA)/NPU(CANN)/MPS 加速。
- **跨平台兼容**：兼容 Windows、Linux 和 Mac 平台。

## 安装与使用

### 安装 MinerU

#### 使用 pip 或 uv 安装 MinerU

```bash
pip install --upgrade pip
pip install uv
uv pip install -U "mineru[core]"
```

#### 从源码安装 MinerU

```bash
git clone https://github.com/opendatalab/MinerU.git
cd MinerU
uv pip install -e .[core]
```

### 使用 MinerU

最简单的命令行调用是：

```bash
mineru -p <input_path> -o <output_path>
```

您可以通过命令行、API 和 WebUI 等多种方式使用 MinerU 进行 PDF 解析。详细说明请参考 [使用指南](https://opendatalab.github.io/MinerU/usage/)。

## 示例

```bash
# 解析单个 PDF
mineru -p sample.pdf -o output/

# 批量解析
mineru -p pdfs/ -o results/
```

> 以上命令会将 PDF 转换为 markdown 和 JSON 格式，提取文本、表格、公式等内容。

## 贡献

欢迎提交 Issue 与 Pull Request。请先阅读 `CONTRIBUTING.md`，遵循代码规范与测试要求。

## 许可证

MIT © OpenDataLab

---
