
---
title: ultrajson
---

# UltraJSON 项目

## 项目地址
[https://github.com/ultrajson/ultrajson](https://github.com/ultrajson/ultrajson)

## 主要特性
UltraJSON (ujson) 是一个用 C 语言实现的超快速 JSON 解析和编码库，专为 Python 设计。它是标准库 json 模块的替代品，专注于高性能和低内存占用。主要特性包括：
- **极高性能**：比 Python 标准 json 模块快数倍，适合处理大型 JSON 数据。
- **低内存使用**：优化了内存分配和解析过程，减少开销。
- **兼容性强**：完全兼容 JSON 标准，支持 Python 2.7+ 和 Python 3.x。
- **C 扩展**：核心用 C 编写，提供可选的 Cython 构建支持。
- **Unicode 支持**：高效处理 Unicode 字符串和编码。

## 主要功能
- **JSON 编码 (dumps/encode)**：将 Python 对象转换为 JSON 字符串，支持自定义选项如确保 ASCII、缩进等。
- **JSON 解码 (loads/decode)**：将 JSON 字符串解析为 Python 对象，支持精确浮点数和自定义解码器。
- **流式处理**：支持从文件或流中读取/写入 JSON 数据。
- **错误处理**：提供详细的异常信息，如解析错误或编码错误。

## 用法示例
安装：使用 pip 安装 `pip install ujson`。

### 基本编码和解码
```python
import ujson

# 编码：Python 对象转 JSON
data = {'name': 'Alice', 'age': 30, 'cities': ['Beijing', 'Shanghai']}
json_str = ujson.dumps(data)
print(json_str)  # 输出: {"name": "Alice", "age": 30, "cities": ["Beijing", "Shanghai"]}

# 解码：JSON 转 Python 对象
parsed_data = ujson.loads(json_str)
print(parsed_data['name'])  # 输出: Alice
```

### 高级用法
```python
# 从文件读取
with open('data.json', 'r') as f:
    data = ujson.load(f)

# 编码选项：确保 ASCII
ujson.dumps(data, ensure_ascii=False)

# 解码选项：精确浮点数
ujson.loads('{"pi": 3.14159}', precise_float=True)
```

更多细节请参考项目 README 和文档。