---
title: fake2db
---

# fake2db 项目描述

## 项目地址
[https://github.com/emirozer/fake2db](https://github.com/emirozer/fake2db)

## 主要特性
fake2db 是一个命令行工具，用于生成假的数据库，旨在帮助开发者快速创建测试数据。它支持多种数据库类型，并利用 Faker 库生成逼真的假数据。主要特性包括：
- **多数据库支持**：兼容 SQLite、PostgreSQL、MySQL 等常见数据库。
- **自动化数据生成**：自动创建表结构和填充假数据，如姓名、地址、邮箱等。
- **自定义配置**：通过 YAML 或 JSON 文件定义表结构、字段类型和数据量。
- **轻量级工具**：无需复杂安装，适合开发和测试环境。
- **开源免费**：基于 Python 开发，易于扩展和贡献。

## 主要功能
- **生成数据库**：从配置文件中读取 schema，自动创建数据库文件或连接现有数据库，并插入假数据。
- **字段类型支持**：包括文本、数字、日期、布尔值等，支持 Faker 的各种提供者（如 en_US、zh_CN）。
- **批量操作**：可指定记录数量，高效生成大量测试数据。
- **导出与集成**：生成的数据库可直接用于应用测试、原型开发或数据分析。
- **错误处理**：内置日志和验证，确保数据生成过程可靠。

## 用法
1. **安装**：
   - 确保 Python 3.x 环境。
   - 通过 pip 安装：`pip install fake2db`。
   - 或从 GitHub 克隆仓库并安装依赖。

2. **创建配置文件**：
   - 使用 YAML 格式定义数据库结构，例如：
     ```
     tables:
       users:
         rows: 100
         fields:
           name: fake.name
           email: fake.email
           age: fake.random_int(min=18, max=80)
     ```

3. **运行命令**：
   - 基本用法：`fake2db -i config.yaml -d sqlite:///test.db`（生成 SQLite 数据库）。
   - PostgreSQL 示例：`fake2db -i config.yaml -d postgresql://user:pass@localhost/dbname`。
   - MySQL 示例：`fake2db -i config.yaml -d mysql://user:pass@localhost/dbname`。
   - 查看帮助：`fake2db --help`。

4. **注意事项**：
   - 确保数据库驱动已安装（如 psycopg2 for PostgreSQL）。
   - 生成的数据仅用于测试，非生产环境。
   - 支持自定义 Faker 区域设置，如 `-l zh_CN` 以生成中文假数据。