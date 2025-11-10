---
title: orjson
---

# orjson 项目

## 项目地址
[GitHub 项目地址](https://github.com/ijl/orjson)

## 主要特性
orjson 是一个 Rust 实现的快速 JSON 库，专为 Python 设计。它以极高的性能著称，比标准库 json 模块快 4-10 倍，支持多种高级特性：
- **高性能**：使用 Rust 编写，解析和序列化 JSON 数据速度极快，适合高负载应用。
- **兼容性**：输出符合 JSON 标准，支持 Python 的 datetime、date、timedelta、UUID 等类型序列化。
- **扩展功能**：支持选项如忽略 NaN/Inf 值、自定义序列化行为、严格模式（不解析非标准 JSON）。
- **安全性**：防止 JSON 解析中的常见漏洞，如深度嵌套导致的栈溢出。
- **轻量级**：无外部依赖，安装简单。

## 主要功能
- **JSON 解析（dumps/loads）**：快速将 Python 对象转换为 JSON 字符串，或从 JSON 字符串解析为 Python 对象。
- **序列化支持**：自动处理 Python 内置类型，包括 NumPy 数组（需额外安装）、自定义类。
- **选项控制**：通过 Option 类提供灵活配置，如 option_indent（格式化输出）、option_default（自定义序列化函数）。
- **错误处理**：提供详细的错误信息，支持部分解析。
- **基准测试**：内置基准测试工具，展示其在各种场景下的性能优势。

## 用法示例
安装：`pip install orjson`

### 基本用法
```python
import orjson

# 序列化
data = {"name": "Alice", "age": 30}
json_str = orjson.dumps(data)
print(json_str)  # b'{"name":"Alice","age":30}'

# 反序列化
parsed = orjson.loads(json_str)
print(parsed)  # {'name': 'Alice', 'age': 30}
```

### 高级用法
```python
import orjson
from datetime import datetime

# 支持 datetime 序列化
data = {"time": datetime.now()}
json_str = orjson.dumps(data, option=orjson.OPT_SERIALIZE_DATETIME)
print(json_str)  # b'{"time":"2023-10-01T12:00:00Z"}'

# 格式化输出
json_str = orjson.dumps(data, option=orjson.OPT_INDENT_2)
print(json_str.decode())  # 带缩进的 JSON 字符串
```

更多细节请参考项目 README。