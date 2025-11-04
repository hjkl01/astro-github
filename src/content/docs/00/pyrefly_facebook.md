
---
title: pyrefly
---

以下为 **pyrefly**（Facebook 维护的 Python 反射工具库）的中文简要介绍与使用示例。请将其保存为 `src/content/docs/00/pyrefly_facebook.md`。

```markdown
# pyrefly (Facebook)

> 项目地址：[https://github.com/facebook/pyrefly](https://github.com/facebook/pyrefly)

---

## 📌 项目简介

`pyrefly` 是一款轻量级、纯 Python 机器的运行时反射工具。它在标准库 `inspect` 与 `pkgutil` 的基础上，提供了更丰富、更易用的 API，用于：

1. **模块与包扫描** – 自动遍历指定路径，识别所有可导入的模块、类、函数、方法、属性等。
2. **类/子类关系查询** – 快速获取某个基类的所有子类，或检查类是否在某个继承链上。
3. **装饰器/注解过滤** – 通过自定义标记（装饰器或自定义属性）来筛选感兴趣的对象。
4. **类型与签名分析** – 获取函数/方法的参数类型、返回值类型以及类型注解。
5. **缓存与性能** – 可选的 LRU 缓存机制，减少重复扫描，提升大型项目的性能。
6. **导出与序列化** – 支持将扫描结果导出为 JSON、YAML 或自定义格式，便于后续分析与文档生成。

> 典型应用场景：  
> - 自动生成 API 文档  
> - 动态插件系统（基于装饰器标记）  
> - 代码质量与安全审计（检测特殊注解、继承关系）  
> - 运行时依赖分析与可视化

---

## 🚀 安装

```bash
pip install pyrefly
```

> `pyrefly` 仅依赖 Python 3.8+ 标准库，无需额外插件。

---

## ✨ 核心 API 使用示例

下面基于一个假想的 `my_project` 包进行演示。

```python
# 假设 my_project/__init__.py
# my_project/handlers.py
# my_project/models.py
# ...
```

```python
from pyrefly import Ref, Annotation

# 1️⃣ 扫描包，返回 Ref 对象
ref = Ref.scan('my_project')

# 2️⃣ 获取所有可见类
all_classes = ref.get_classes()
print(f"全部类: {[cls.__name__ for cls in all_classes]}")

# 3️⃣ 通过子类关系筛选
class BaseHandler: pass  # 预先定义基类

handler_subclasses = ref.get_subclasses(BaseHandler)
print(f"BaseHandler 子类: {[cls.__name__ for cls in handler_subclasses]}")

# 4️⃣ 按装饰器/注解过滤 (假设 @route 注解)
@Annotation('route')
def route(path: str):
    def decorator(fn):
        fn._route = path
        return fn
    return decorator

@route('/users')
def get_users():
    pass

annotated_funcs = ref.get_functions_by_annotation('route')
print(f"带 @route 的函数: {[fn.__name__ for fn in annotated_funcs]}")

# 5️⃣ 读取函数签名信息
for fn in annotated_funcs:
    sig = ref.get_signature(fn)
    print(f"{fn.__name__} -> {sig}")

# 6️⃣ 导出扫描结果为 JSON
ref.export('scan_result.json')
```

> **提示**  
> - `Ref.scan()` 会在内部使用 `pkgutil.walk_packages` + `inspect.getmembers`，非常高效。  
> - 若仅关心某个模块，可直接 `Ref.scan('my_project.handlers')`。  
> - 默认缓存大小为 128，可通过 `Ref.cache_size=512` 调整。  

---

## 📦 CLI 方式

`pyrefly` 还提供了命令行工具，便于快速集成到 CI/CD 或开发脚本。

```bash
# 仅扫描并打印类名
pyrefly scan my_project --classes

# 导出完整结果为 YAML
pyrefly scan my_project --yaml output.yaml

# 只查询某个注解
pyrefly scan my_project --annotation route
```

CLI 选项：

| 选项 | 说明 |
|------|------|
| `--classes` | 仅打印所有类 |
| `--functions` | 仅打印所有函数 |
| `--annotation <name>` | 过滤带有指定注解的对象 |
| `--json <file>` / `--yaml <file>` | 将结果导出为 JSON/YAML |

> 进一步可在 `setup.cfg` 或 `pyproject.toml` 配置扫描入口，配合 `pre-commit` 钩子自动生成文档。

---

## 🧩 进一步阅读

- 官方文档：`docs/`
- 示例项目：`examples/`
- 代码仓库中的 `tests/` 目录提供了对每个模块的完整单元测试。

---

> **温馨提示**  
> `pyrefly` 在大规模项目中表现良好，但若项目使用大量动态加载（如插件系统）时，可能会漏掉未显式导入的模块。此时请在扫描前手动导入目标模块（或使用 `--force-import` 选项）。

---

**结束语**  
`pyrefly` 让 Python 运行时的反射更“可视化”，从而帮助你更快地理解、使用以及生成文档。希望它能够成为你项目中不可或缺的工具之一！

``` 
```

---