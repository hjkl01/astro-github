
---
title: pydantic
---

# Pydantic 项目

**GitHub 项目地址:** [https://github.com/samuelcolvin/pydantic](https://github.com/samuelcolvin/pydantic)

## 主要特性
Pydantic 是一个 Python 数据验证和设置管理库，使用 Python 类型注解进行数据验证和序列化。它基于 Python 3.7+ 的类型提示系统，具有以下核心特性：
- **数据验证**：自动验证输入数据是否符合定义的类型和约束，支持内置类型（如 int、str）和自定义验证。
- **序列化**：将数据模型转换为 JSON、字典或其他格式，便于 API 和数据交换。
- **类型安全**：利用 Python 的类型系统，提供运行时类型检查，减少运行时错误。
- **性能优化**：高效的验证机制，适用于高性能应用。
- **灵活配置**：支持环境变量、配置文件和命令行参数的设置管理。
- **扩展性**：支持自定义验证器、字段别名和嵌套模型。

## 主要功能
- **模型定义**：通过继承 `BaseModel` 创建数据模型，定义字段类型和验证规则。
- **数据解析**：从字典、JSON 或其他来源解析数据，并自动验证。
- **错误处理**：提供详细的验证错误信息，便于调试。
- **设置管理**：使用 `BaseSettings` 子类管理应用配置，支持多种来源（如环境变量）。
- **JSON 支持**：内置 JSON Schema 生成和序列化/反序列化功能。
- **集成性**：与 FastAPI 等框架无缝集成，常用于 Web API 的请求/响应模型。

## 用法示例
### 安装
```bash
pip install pydantic
```

### 基本模型定义和验证
```python
from pydantic import BaseModel, validator

class User(BaseModel):
    id: int
    name: str
    email: str

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v

# 创建实例并验证
user = User(id=1, name='Alice', email='alice@example.com')
print(user)  # id=1 name='Alice' email='alice@example.com'

# 无效数据会抛出 ValidationError
# user = User(id='not_an_int', name='Bob', email='invalid')
```

### 设置管理
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MyApp"
    database_url: str

settings = Settings()
print(settings.app_name)  # MyApp (默认值)
# database_url 从环境变量 DATABASE_URL 读取
```

更多用法请参考官方文档：https://pydantic-docs.helpmanual.io/