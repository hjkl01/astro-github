
---
title: Ciphey
---

# Ciphey 项目

**GitHub 项目地址:** [https://github.com/Ciphey/Ciphey](https://github.com/Ciphey/Ciphey)

## 主要特性
Ciphey 是一个自动化解密工具，主要用于密码学和加密文本的逆向工程。它采用机器学习和自然语言处理技术，能够智能识别和破解各种加密类型，而无需用户手动指定加密算法。核心特性包括：
- **自动化加密检测**：自动识别加密类型，如 Base64、ROT13、凯撒密码等常见编码和简单加密。
- **机器学习驱动**：使用 AI 模型生成可能的解密候选，并根据自然语言的熵（随机性）评分，选择最可能的明文。
- **支持多种加密**：内置支持数百种加密算法和变体，包括经典密码（如维吉尼亚密码）和现代编码。
- **易用性和扩展性**：开源项目，支持自定义插件和模型训练，适用于密码破解、CTF 挑战和取证分析。
- **跨平台兼容**：基于 Python 开发，支持 Windows、macOS 和 Linux。

## 主要功能
- **文本解密**：输入加密字符串，Ciphey 会尝试多种解密方法，并输出最可能的明文结果。
- **字典攻击**：集成词典支持，针对常见密码或短语进行暴力破解。
- **熵分析**：计算文本的熵值，帮助判断解密结果的自然度（例如，英语文本的熵通常在 3-4 之间）。
- **批量处理**：支持处理多个输入文件或字符串，实现高效的批量解密。
- **可视化输出**：提供解密过程的日志和评分，帮助用户理解破解步骤。

## 用法
1. **安装**：
   - 确保安装 Python 3.7+。
   - 使用 pip 安装：`pip install ciphey`。
   - 或者克隆仓库并安装：`git clone https://github.com/Ciphey/Ciphey.git` 后运行 `pip install -r requirements.txt` 和 `python setup.py install`。

2. **基本命令行用法**：
   - 运行解密：`ciphey -t "加密文本"`（例如，`ciphey -t "SGVsbG8gV29ybGQ="` 会解密 Base64 为 "Hello World"）。
   - 指定语言：`ciphey -t "文本" -l en`（默认英语，支持多语言）。
   - 自定义词典：`ciphey -t "文本" -d /path/to/dictionary.txt`。
   - 详细模式：`ciphey -t "文本" -v`（显示详细过程）。

3. **高级用法**：
   - GUI 模式：运行 `ciphey-gui` 启动图形界面，便于交互式操作。
   - 插件开发：通过编写自定义解密模块扩展功能，参考文档中的插件指南。
   - 示例：对于一个 ROT13 加密的文本 "NOPQRSTUVWXYZ"，运行 `ciphey -t "NOPQRSTUVWXYZ"` 将输出 "ABCD"（假设上下文为简单移位）。

更多细节请参考项目 README 和官方文档。