
---
title: typer
---

# Typer 项目

**GitHub 项目地址:** [https://github.com/tiangolo/typer](https://github.com/tiangolo/typer)

## 主要特性
Typer 是一个基于 Python 3.6+ 的现代命令行界面 (CLI) 库，由 Sebastián Ramírez (tiangolo) 开发。它利用 Python 类型提示 (Type Hints) 来自动生成命令行接口，具有以下核心特性：
- **类型驱动的接口生成**：通过 Python 类型注解自动创建参数、选项和子命令，无需手动解析。
- **自动帮助生成**：基于类型提示自动生成详细的帮助文本、默认值和验证。
- **高性能和简单性**：依赖 Click 库，但提供更简洁的 API，减少样板代码。
- **丰富验证支持**：内置支持如文件路径、枚举、日期等类型验证。
- **可扩展性**：易于创建复杂 CLI 应用，支持子命令、组命令和自定义行为。
- **零配置启动**：最小代码即可构建功能完整的 CLI 工具。
- **跨平台兼容**：在 Windows、macOS 和 Linux 上运行良好。

Typer 旨在让 CLI 开发像编写普通 Python 函数一样直观，适合脚本、工具和应用的后端接口。

## 主要功能
- **命令和子命令**：定义主命令及其子模块，支持嵌套结构。
- **参数和选项**：支持位置参数、标志选项（短/长格式，如 `-h/--help`），并自动处理类型转换。
- **输入验证和错误处理**：自动检查类型错误，提供用户友好的错误消息。
- **帮助和文档**：内置 `--help` 支持，生成结构化的帮助输出。
- **回调和钩子**：允许自定义前/后处理逻辑。
- **集成其他库**：无缝与 Pydantic、FastAPI 等 tiangolo 生态集成，用于数据验证和 API 构建。

## 用法示例
安装 Typer：
```bash
pip install typer
```

基本用法：创建一个简单的 CLI 脚本 `main.py`。

```python
import typer

app = typer.Typer()

@app.command()
def hello(name: str, age: int = typer.Option(..., help="年龄")):
    """问候用户"""
    print(f"你好，{name}！你今年 {age} 岁。")

if __name__ == "__main__":
    app()
```

运行命令：
```bash
python main.py hello Alice --age 30
# 输出: 你好，Alice！你今年 30 岁。

python main.py hello --help
# 显示帮助信息
```

添加子命令：
```python
import typer

app = typer.Typer()

@app.command()
def create(name: str):
    print(f"创建用户: {name}")

@app.command()
def delete(name: str):
    print(f"删除用户: {name}")

if __name__ == "__main__":
    app()
```

运行：
```bash
python main.py create Bob
python main.py delete Bob
```

更多高级用法请参考官方文档：https://typer.tiangolo.com/