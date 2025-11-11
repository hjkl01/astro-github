---
title: Ciphey
---

# Ciphey 项目

**GitHub 项目地址:** [https://github.com/Ciphey/Ciphey](https://github.com/Ciphey/Ciphey)

## 主要特性

Ciphey 是一个完全自动化的解密/解码/破解工具，使用自然语言处理和人工智能，以及一些常识。主要特性包括：

- **50+ 加密/编码支持**：包括二进制、摩尔斯码、Base64、经典密码（如凯撒密码、维吉尼亚密码）和现代加密。
- **人工智能驱动**：使用自定义构建的人工智能模块（AuSearch）来回答“使用了什么加密？”的问题。
- **自定义自然语言处理模块**：Ciphey 可以确定文本是明文还是加密的，是否是JSON、CTF标志或英语。
- **多语言支持**：目前支持德语和英语（包括AU、UK、CAN、USA变体）。
- **支持加密和哈希**：这不是其他工具如CyberChef Magic所支持的。
- **C++ 核心**：非常快的。

## 主要功能

- **文本解密**：输入加密文本，Ciphey 会自动尝试多种解密方法，并输出最可能的明文。
- **字典攻击**：集成词典支持，用于暴力破解常见密码或短语。
- **熵分析**：计算文本的熵值，以确定解密结果的自然度（例如，英语文本的熵通常在3-4之间）。
- **批量处理**：支持处理多个输入文件或字符串。
- **可视化输出**：提供解密过程的日志和评分。

## 用法

### 安装

- **Python**：`python3 -m pip install ciphey --upgrade`
- **Docker**：`docker run -it --rm remnux/ciphey`
- **MacPorts**：`sudo port install ciphey`
- **Homebrew**：`brew install ciphey`

### 运行 Ciphey

有3种运行方式：

1. 文件输入：`ciphey -f encrypted.txt`
2. 非限定输入：`ciphey -- "Encrypted input"`
3. 正常方式：`ciphey -t "Encrypted input"`

要关闭进度条、概率表和所有噪音，使用安静模式：`ciphey -t "encrypted text here" -q`

完整参数列表：`ciphey --help`

### 导入 Ciphey

`from Ciphey.__main__ import main`

更多细节请参考项目 README 和官方文档。
