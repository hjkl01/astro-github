---
title: Magika
---

# Magika

Magika 是一个由 Google 开发的 AI 驱动的文件内容类型检测工具。它利用深度学习技术，提供快速且准确的文件类型识别。Magika 的核心模型仅占用几 MB 空间，即使在单 CPU 上也能在毫秒级内完成检测。

## 功能特点

- **高准确率**：在 100M+ 样本和 200+ 内容类型的数据集上训练，平均准确率达到 99%。
- **快速推理**：模型加载后，每个文件检测仅需约 5ms。
- **多格式支持**：支持二进制和文本文件格式，包括代码、文档、图像等。
- **多种输出模式**：提供高置信度、中置信度和最佳猜测模式。
- **大规模应用**：已在 Google 的 Gmail、Drive 和 Safe Browsing 中大规模使用，每周处理数百亿样本。
- **集成支持**：已集成到 VirusTotal 和 abuse.ch 等平台。

## 安装

### 命令行工具

通过 Python 包安装：

```bash
pipx install magika
```

或使用安装脚本：

```bash
curl -LsSf https://securityresearch.google/magika/install.sh | sh
```

### Python 包

```bash
pip install magika
```

### JavaScript 包

```bash
npm install magika
```

## 用法

### 命令行工具示例

检测单个文件：

```bash
magika example.txt
```

递归检测目录：

```bash
magika -r /path/to/directory
```

JSON 输出：

```bash
magika example.py --json
```

从标准输入检测：

```bash
cat example.ini | magika -
```

### Python API 示例

```python
from magika import Magika

# 初始化
m = Magika()

# 检测字节
res = m.identify_bytes(b'function log(msg) {console.log(msg);}')
print(res.output.label)  # javascript

# 检测文件路径
res = m.identify_path('./example.ini')
print(res.output.label)  # ini

# 检测文件流
with open('./example.ini', 'rb') as f:
    res = m.identify_stream(f)
print(res.output.label)  # ini
```

## 更多信息

- 官方网站：[https://securityresearch.google/magika/](https://securityresearch.google/magika/)
- 在线演示：[https://securityresearch.google/magika/demo/magika-demo/](https://securityresearch.google/magika/demo/magika-demo/)
- 研究论文：[https://securityresearch.google/magika/additional-resources/research-papers-and-citation/](https://securityresearch.google/magika/additional-resources/research-papers-and-citation/)
