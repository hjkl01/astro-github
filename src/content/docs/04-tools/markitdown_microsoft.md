---
title: markitdown
---

## 功能介绍

MarkItDown 是一个轻量级的 Python 工具，用于将各种文件和 Office 文档转换为 Markdown 格式，适用于 LLM 和相关文本分析管道。它专注于保留重要的文档结构和内容，如标题、列表、表格、链接等。

支持转换的文件类型包括：

- PDF
- PowerPoint
- Word
- Excel
- 图像（EXIF 元数据和 OCR）
- 音频（EXIF 元数据和语音转录）
- HTML
- 文本格式（CSV、JSON、XML）
- ZIP 文件（遍历内容）
- YouTube URL
- EPub
- 更多格式

## 用法

### 安装

需要 Python 3.10 或更高版本。推荐使用虚拟环境。

```bash
pip install 'markitdown[all]'
```

### 命令行使用

```bash
markitdown path-to-file.pdf > document.md
# 或指定输出文件
markitdown path-to-file.pdf -o document.md
# 管道输入
cat path-to-file.pdf | markitdown
```

### Python API

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)
result = md.convert("test.xlsx")
print(result.text_content)
```

### Docker 使用

```bash
docker build -t markitdown:latest .
docker run --rm -i markitdown:latest < ~/your-file.pdf > output.md
```

### 可选依赖

可以单独安装特定格式的依赖，如 `pip install 'markitdown[pdf, docx, pptx]'`。

### 插件支持

支持第三方插件，可通过 `--list-plugins` 列出，`--use-plugins` 启用。

### Azure Document Intelligence

支持使用 Azure Document Intelligence 进行转换，需要提供端点。

更多详情请查看 [GitHub 仓库](https://github.com/microsoft/markitdown)。
