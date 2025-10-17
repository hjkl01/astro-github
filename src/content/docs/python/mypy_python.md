
---
title: mypy
---

# mypy 项目

**GitHub 项目地址:** [https://github.com/python/mypy](https://github.com/python/mypy)

## 主要特性
- **静态类型检查**: mypy 是一个 Python 静态类型检查器，支持渐进式类型检查，无需修改现有代码即可逐步添加类型注解。
- **PEP 484 兼容**: 严格遵循 Python 类型提示标准（PEP 484），支持类型注解如 `int`、`str`、`List[str]` 等。
- **渐进式采用**: 可以只检查部分代码，支持 `--check-untyped-defs` 等选项，适合从无类型代码迁移。
- **插件支持**: 可扩展插件系统，用于处理第三方库或自定义类型检查规则。
- **跨平台**: 支持 Windows、macOS 和 Linux，集成多种 IDE 如 VS Code、PyCharm。
- **错误报告**: 提供详细的类型错误信息，包括行号和建议修复，帮助开发者快速定位问题。

## 主要功能
- **类型推断**: 自动推断变量、函数和类的类型，减少手动注解负担。
- **类型验证**: 检查函数参数、返回值和变量是否符合类型注解，防止运行时类型错误。
- **支持高级特性**: 处理泛型、联合类型（Union）、可选类型（Optional）、协议（Protocol）和类型别名。
- **配置文件支持**: 通过 `mypy.ini` 或 `pyproject.toml` 配置检查规则，如忽略特定模块或启用严格模式。
- **与 stub 文件集成**: 使用 `.pyi` 存根文件为无源代码的库提供类型信息。
- **CI/CD 集成**: 易于集成到持续集成管道中，如 GitHub Actions 或 Travis CI，用于自动化类型检查。

## 用法
1. **安装**: 使用 pip 安装：`pip install mypy`。
2. **基本检查**: 在命令行运行 `mypy your_script.py` 检查单个文件，或 `mypy .` 检查当前目录的所有 Python 文件。
3. **配置选项**:
   - `--strict`: 启用严格模式，检查所有类型错误。
   - `--ignore-missing-imports`: 忽略缺失导入的错误。
   - `--python-version 3.8`: 指定 Python 版本以匹配运行环境。
4. **示例**:
   ```python
   # example.py
   def greet(name: str) -> str:
       return f"Hello, {name}"

   greet(42)  # mypy 会报告类型错误
   ```
   运行 `mypy example.py` 将输出错误：`error: Argument 1 to "greet" has incompatible type "int"; expected "str"`。
5. **IDE 集成**: 在 VS Code 中安装 mypy 扩展，即可实时显示类型错误。
6. **高级用法**: 使用 `dmypy` 作为守护进程加速重复检查，或 `stubgen` 生成存根文件。更多细节见官方文档。