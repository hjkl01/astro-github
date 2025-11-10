---
title: marshmallow
---

# Marshmallow 项目

## 项目地址
[https://github.com/marshmallow-code/marshmallow](https://github.com/marshmallow-code/marshmallow)

## 主要特性
Marshmallow 是一个轻量级的 Python 库，用于对象序列化和反序列化。它将复杂的对象转换为可互换的格式（如 JSON、XML），并反之。主要特性包括：
- **类型验证**：自动验证数据类型和约束，确保输入数据的完整性。
- **灵活的序列化**：支持自定义字段、嵌套对象和复杂数据结构。
- **无依赖设计**：核心功能不依赖外部库，易于集成到各种 Python 项目中。
- **错误处理**：提供详细的验证错误报告，便于调试。
- **扩展性**：支持插件和自定义验证器，适用于 REST API、数据管道等场景。

## 主要功能
- **Schema 定义**：通过类定义数据模式（Schema），指定字段类型和验证规则。
- **序列化（Serialization）**：将 Python 对象（如字典、模型实例）转换为原始数据类型。
- **反序列化（Deserialization）**：将原始数据转换为 Python 对象，并进行验证。
- **数据加载与转储**：内置 `load()` 和 `dump()` 方法处理数据转换。
- **集成支持**：与 Web 框架（如 Flask、FastAPI）和 ORM（如 SQLAlchemy）无缝集成。

## 用法示例
安装：`pip install marshmallow`

基本用法：
```python
from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True, validate=lambda x: x > 0)

# 序列化
user_data = {"name": "Alice", "age": 30}
schema = UserSchema()
serialized = schema.dump(user_data)  # 输出: {"name": "Alice", "age": 30}

# 反序列化与验证
try:
    deserialized = schema.load({"name": "Bob", "age": -5})
except ValidationError as err:
    print(err.messages)  # 输出验证错误
```

更多细节请参考项目文档。