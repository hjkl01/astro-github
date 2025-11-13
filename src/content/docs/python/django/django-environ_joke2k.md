---
title: django-environ
---

# django-environ 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/joke2k/django-environ)

## 主要特性
django-environ 是一个 Django 环境变量解析库，主要用于简化 Django 项目中环境变量的读取和管理。它将环境变量转换为 Python 对象，支持多种数据类型（如字符串、整数、布尔值、列表、字典等），并提供灵活的默认值和验证机制。该库轻量级、无依赖，易于集成到 Django 项目中，帮助开发者更好地处理配置管理，避免硬编码敏感信息。

## 主要功能
- **环境变量解析**：从系统环境变量、.env 文件或其他来源读取配置，支持自动类型转换（如 int、bool、JSON 解析）。
- **默认值支持**：为每个环境变量设置默认值，防止未定义变量导致的错误。
- **文件支持**：可以从 .env 文件加载环境变量，类似于 python-dotenv，但专为 Django 优化。
- **Django 集成**：无缝集成到 Django 的 settings.py 中，支持 URL 格式的环境变量（如数据库连接字符串）。
- **类型安全**：内置类型检查和转换，减少运行时错误。
- **安全性**：鼓励使用环境变量存储敏感信息，如 API 密钥、数据库密码，避免代码泄露。

## 用法示例
1. **安装**：
   ```bash
   pip install django-environ
   ```

2. **在 Django settings.py 中使用**：
   ```python
   import environ
   import os

   # 初始化环境变量
   env = environ.Env(
       DEBUG=(bool, False)  # 默认值为 False，类型为 bool
   )

   # 从 .env 文件读取（可选）
   environ.Env.read_env(os.path.join(os.path.dirname(__file__), '.env'))

   # 读取环境变量
   DEBUG = env('DEBUG')
   SECRET_KEY = env('SECRET_KEY')
   DATABASES = {
       'default': env.db()  # 自动解析数据库 URL
   }
   ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost'])
   ```

3. **.env 文件示例**（在项目根目录）：
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgres://user:pass@localhost/dbname
   ALLOWED_HOSTS=example.com,localhost
   ```

通过这种方式，开发者可以轻松管理生产和开发环境的配置差异，确保项目安全和可移植性。