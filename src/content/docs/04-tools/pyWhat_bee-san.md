---
title: pyWhat
---

# pyWhat 项目

## 项目地址
[GitHub 项目地址](https://github.com/bee-san/pyWhat)

## 主要特性
pyWhat 是一个开源的 Python 工具，用于识别和分析文件、数据或输入的内容。它基于机器学习和规则匹配，能够快速检测输入的类型、格式和潜在用途。主要特性包括：
- **多类型识别**：支持识别图像、音频、视频、文档、密码、API 密钥、哈希值等多种文件或数据类型。
- **隐私友好**：本地运行，无需上传数据到云端，确保用户隐私。
- **扩展性强**：模块化设计，便于添加自定义识别规则。
- **跨平台支持**：兼容 Windows、macOS 和 Linux 系统。
- **轻量级**：依赖少，安装简单，适合开发者集成到其他项目中。

## 主要功能
- **文件类型检测**：自动识别上传或指定文件的格式，例如检测是否为加密文件、恶意软件或常见媒体文件。
- **敏感信息扫描**：扫描文本或代码，找出潜在的密码、令牌或个人信息泄露。
- **哈希和签名验证**：支持 MD5、SHA 等哈希值的识别，以及数字签名的初步检查。
- **输出详细报告**：提供识别结果的详细信息，包括置信度分数和建议行动。
- **命令行界面**：通过 CLI 快速运行扫描，支持批量处理。

## 用法
### 安装
1. 确保 Python 3.7+ 已安装。
2. 使用 pip 安装：
   ```
   pip install pywhat
   ```

### 基本用法
- **命令行扫描文件**：
  ```
  pywhat /path/to/your/file.txt
  ```
  这将输出文件类型的识别结果。

- **扫描目录**：
  ```
  pywhat /path/to/directory --recursive
  ```
  使用 `--recursive` 选项扫描子目录。

- **扫描字符串**：
  ```
  echo "your_api_key_here" | pywhat
  ```

- **高级选项**：
  - `--json`：以 JSON 格式输出结果，便于脚本解析。
  - `--verbose`：显示详细的识别过程。
  - `--no-color`：禁用彩色输出。

### 示例
扫描一个图像文件：
```
pywhat image.jpg
```
输出示例：
```
image.jpg: JPEG Image (confidence: 99%)
Potential: Standard photo, no sensitive data detected.
```

更多用法请参考 GitHub 仓库的 README 和文档。