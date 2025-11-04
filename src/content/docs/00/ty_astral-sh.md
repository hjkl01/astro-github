
---
title: ty
---


# ty

**GitHub 地址**: https://github.com/astral-sh/ty

---

## 主要特性

- **轻量级 typed‑dict**：基于 `typing.TypedDict` 实现，提供最小化的 API。
- **运行时校验**：创建的对象在实例化时自动校验字段类型与约束。
- **默认值与可选字段**：支持在 schema 中直接声明 `default`、`optional`。
- **复杂类型支持**：`List[T]`、`Optional[T]`、`Union[T1, T2]`、`Any` 等。
- **嵌套结构**：可以在字段中使用其它 typed‑dict 作为子结构。
- **自定义验证器**：可为字段绑定自定义校验函数。
- **JSON Schema 生成**：一键把 typed‑dict 转成标准 JSON Schema。
- **与标准 `typing` 兼容**：可直接作为 type hint 使用。

---

## 核心 API

| 关键字 | 说明 | 典型用法 |
|--------|------|----------|
| `ty.Dict()` | 创建一个 typed‑dict schema | `User = ty.Dict({"name": str, "age": int})` |
| `ty.List` | 声明列表元素类型 | `tags: ty.List[str]` |
| `ty.Optional` | 声明可选字段 | `email: ty.Optional[str]` |
| `ty.Union` | 声明联合类型 | `value: ty.Union[int, str]` |
| `ty.validate(obj, schema)` | 校验对象是否符合 schema | `ty.validate(user, User)` |
| `ty.parse(data, schema)` | 将普通 dict 转成 typed‑dict 并验证 | `user = ty.parse(raw, User)` |
| `ty.to_dict(obj)` | 将 typed‑dict 转成普通 dict | `raw = ty.to_dict(user)` |
| `ty.schema_to_jsonschema(schema)` | 生成 JSON Schema | `js = ty.schema_to_jsonschema(User)` |
| `ty.Validator(func, type_)` | 为字段绑定自定义验证器 | `age: ty.Validator(validate_age, int)` |

---

## 使用示例

```python
from ty import ty

# 定义 schema
UserSchema = ty.Dict({
    "name": str,
    "age": int,
    "email": ty.Optional[str],
    "tags": ty.List[str],
    # 自定义验证器
    "score": ty.Validator(lambda v: 0 <= v <= 100, int),
})

# 创建实例（会自动校验）
user = UserSchema(name="Alice", age=30, email="alice@example.com", tags=["admin", "editor"], score=85)

# 校验已有对象
ty.validate(user, UserSchema)

# 解析普通 dict
raw = {"name": "Bob", "age": 25, "tags": ["user"], "score": 90}
user2 = ty.parse(raw, UserSchema)

# 转回普通 dict
raw2 = ty.to_dict(user2)

# 生成 JSON Schema
json_schema = ty.schema_to_jsonschema(UserSchema)
```

---

## 嵌套结构示例

```python
AddressSchema = ty.Dict({
    "city": str,
    "zip": str,
})

ProfileSchema = ty.Dict({
    "user": UserSchema,
    "address": AddressSchema,
})
```

---

## 进一步阅读

- 官方文档与示例代码请参见项目主页的 README 与 docs 目录。