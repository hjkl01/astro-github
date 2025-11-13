---
title: click
---

# Click 项目

**GitHub 项目地址:** [https://github.com/pallets/click](https://github.com/pallets/click)

## 主要特性
Click 是一个 Python 包，用于创建优雅的命令行界面（CLI）。它由 Pallets 项目团队维护，设计简单、灵活，支持从简单脚本到复杂应用的用户界面构建。主要特性包括：
- **装饰器驱动**：使用简单的装饰器（如 `@click.command()`）快速定义命令，无需编写复杂的解析代码。
- **参数和选项处理**：自动支持位置参数、选项（短/长格式）、布尔标志、多值输入等。
- **类型转换和验证**：内置类型提示和验证机制，支持字符串、整数、文件等常见类型。
- **子命令支持**：轻松构建嵌套命令结构，类似于 Git 或 AWS CLI 的风格。
- **提示和交互**：提供交互式输入提示、密码隐藏、确认对话框等功能。
- **错误处理和帮助**：自动生成帮助文本、错误消息，并支持自定义错误处理。
- **可组合性**：模块化设计，便于扩展和重用，支持上下文对象传递数据。
- **多语言和国际化**：易于添加本地化支持。
- **测试友好**：内置测试工具，便于单元测试 CLI 行为。

Click 遵循“简单即美”的哲学，适合初学者和专家，兼容 Python 3.7+。

## 主要功能
- **命令定义**：创建主命令和子命令，支持别名和分组。
- **输入处理**：解析命令行参数、选项，支持默认值、必需性检查和环境变量。
- **输出管理**：集成颜色输出、进度条（通过扩展）和格式化打印。
- **上下文管理**：使用 `Context` 对象在命令间共享状态。
- **扩展支持**：可与 Click 的插件系统集成，或结合其他库如 Rich 用于美化输出。
- **脚本集成**：适用于脚本自动化、工具开发和大型应用（如 Flask CLI）。

## 用法示例
安装 Click：`pip install click`

### 基本命令
```python
import click

@click.command()
@click.option('--name', default='World', help='Name to greet')
def hello(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    hello()
```
运行：`python script.py --name Alice` 输出 `Hello, Alice!`

### 子命令示例
```python
import click

@click.group()
def cli():
    pass

@cli.command()
def init():
    click.echo('Initialized project')

@cli.command()
@click.argument('filename')
def read(filename):
    click.echo(f'Reading {filename}')

if __name__ == '__main__':
    cli()
```
运行：`python script.py init` 或 `python script.py read file.txt`

更多用法请参考官方文档：https://click.palletsprojects.com/