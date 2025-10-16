
---
title: better-exceptions
---

# Better Exceptions 项目

## 项目地址
[GitHub 项目地址](https://github.com/Qix-/better-exceptions)

## 主要特性
- **美化异常输出**：将 Python 的标准回溯（traceback）转换为更易读的彩色格式，使用 ANSI 颜色高亮显示变量值、代码行和异常信息，便于调试。
- **上下文高亮**：在异常回溯中突出显示相关代码上下文，包括变量的值和类型，而非原始的代码片段。
- **自定义格式**：支持自定义颜色主题和格式选项，适应不同终端环境。
- **轻量级**：纯 Python 实现，无需额外依赖，兼容 Python 2 和 3。
- **钩子集成**：通过钩子（hook）机制无缝集成到现有代码中，不会影响性能。

## 主要功能
- **Traceback 转换**：捕获并美化 Python 异常的回溯信息，使其更直观。
- **变量值显示**：在异常信息中直接显示局部和全局变量的值，帮助快速定位问题。
- **颜色编码**：使用颜色区分不同部分，如红色表示错误、蓝色表示变量名，提高可读性。
- **格式化输出**：支持 JSON 或其他自定义输出格式，用于日志记录或集成到 IDE 中。
- **兼容性**：适用于各种 Python 环境，包括 Jupyter Notebook 和 Web 框架。

## 用法
1. **安装**：
   使用 pip 安装：
   ```
   pip install better-exceptions
   ```

2. **启用钩子**（推荐方式）：
   在 Python 脚本开头添加：
   ```python
   import better_exceptions
   better_exceptions.hook()
   ```
   这将自动美化所有异常输出。

3. **命令行使用**：
   在 Python 解释器中运行时，使用环境变量：
   ```
   PYTHONBETTEREXCEPTIONS=1 python your_script.py
   ```

4. **自定义选项**：
   ```python
   import better_exceptions
   better_exceptions.hook(color_scheme='Default', theme='Default')
   ```
   - `color_scheme`：选择颜色方案（如 'Default', 'Monokai'）。
   - `theme`：自定义主题文件路径。

5. **示例**：
   运行一个抛出异常的简单脚本：
   ```python
   import better_exceptions
   better_exceptions.hook()

   def divide(a, b):
       return a / b

   divide(10, 0)  # 将显示美化的 ZeroDivisionError
   ```
   输出将以彩色、结构化的方式显示异常细节，包括变量 `a` 和 `b` 的值。

更多细节请参考项目 README。