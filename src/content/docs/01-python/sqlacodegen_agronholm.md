
---
title: sqlacodegen
---

# SQLACodegen 项目

## 项目地址
[GitHub 项目地址](https://github.com/agronholm/sqlacodegen)

## 主要特性
- **自动生成 SQLAlchemy 模型**：基于现有数据库架构，自动生成 SQLAlchemy ORM 模型类，支持多种数据库方言。
- **支持多种数据库**：兼容 PostgreSQL、MySQL、SQLite 等常见数据库，通过 SQLAlchemy 的反射机制工作。
- **自定义配置**：允许用户指定表名过滤、关系映射、列类型自定义等选项，提高生成代码的灵活性。
- **命令行工具**：提供简单易用的 CLI 接口，便于集成到开发流程中。
- **开源与维护**：由知名开发者维护，代码简洁，支持 Python 3.x。

## 主要功能
- **数据库反射**：从数据库中读取表结构、列定义、外键关系等信息。
- **代码生成**：生成 Python 文件，包含 SQLAlchemy 的 Base、模型类及其 __repr__ 方法。
- **关系处理**：自动检测并生成 one-to-many、many-to-one 等关联关系。
- **选项扩展**：支持生成 Flask-Admin 集成代码、自定义模板等高级功能。

## 用法
1. **安装**：
   ```
   pip install sqlacodegen
   ```

2. **基本用法**（命令行生成模型）：
   ```
   sqlacodegen mysql://username:password@host/dbname --outfile models.py
   ```
   - `mysql://...`：替换为你的数据库 URL（支持 sqlite://, postgresql:// 等）。
   - `--outfile models.py`：指定输出文件路径。

3. **高级选项**：
   - `--tables table1,table2`：仅生成指定表的模型。
   - `--noinflect`：禁用名称转换（例如，表名到类名的驼峰式）。
   - `--noclasses`：仅生成表定义，不生成类。
   - `--flask`：生成兼容 Flask 的代码。
   示例：
   ```
   sqlacodegen postgresql://user:pass@localhost/mydb --tables users,posts --outfile app/models.py --flask
   ```

4. **集成到脚本**：
   ```python
   from sqlacodegen import codegen

   codegen.db_url = "sqlite:///example.db"
   codegen.outfile = "models.py"
   codegen.run()
   ```

更多细节请参考项目 README。