
---
title: python-dotenv
---

# python-dotenv 项目

## 项目地址
[GitHub 项目地址](https://github.com/theskumar/python-dotenv)

## 主要特性
- **简单易用**：python-dotenv 是一个轻量级的 Python 库，用于从 `.env` 文件轻松读取配置变量。
- **环境变量管理**：支持将 `.env` 文件中的键值对加载到系统的环境变量中，便于在开发环境中管理敏感信息如 API 密钥、数据库凭证等。
- **跨平台兼容**：适用于 Windows、macOS 和 Linux 等操作系统。
- **无外部依赖**：核心功能依赖 Python 标准库，安装简单。
- **支持多行值和引号**：正确处理包含空格、引号或多行的环境变量值。
- **安全性**：鼓励将 `.env` 文件添加到 `.gitignore`，避免敏感信息泄露到版本控制中。

## 主要功能
- **加载 .env 文件**：从项目根目录的 `.env` 文件读取键值对，并将其设置到 `os.environ` 中。
- **自定义路径加载**：允许指定自定义的 .env 文件路径进行加载。
- **覆盖现有变量**：可以选择是否覆盖已存在的环境变量。
- **集成流行框架**：常与 Flask、Django 等 Web 框架结合使用，简化配置管理。
- **命令行工具**：提供 CLI 命令来运行脚本时自动加载 .env 文件。

## 用法示例
1. **安装**：
   ```
   pip install python-dotenv
   ```

2. **创建 .env 文件**（在项目根目录）：
   ```
   DB_HOST=localhost
   DB_PORT=5432
   API_KEY=your_secret_key
   ```

3. **在 Python 代码中使用**：
   ```python
   from dotenv import load_dotenv
   import os

   # 加载 .env 文件
   load_dotenv()

   # 读取环境变量
   db_host = os.getenv('DB_HOST')
   print(db_host)  # 输出: localhost
   ```

4. **自定义路径**：
   ```python
   load_dotenv('/path/to/your/.env')
   ```

5. **CLI 用法**（运行脚本时加载 .env）：
   ```
   dotenv run -- python your_script.py
   ```

更多详情请参考项目 README。