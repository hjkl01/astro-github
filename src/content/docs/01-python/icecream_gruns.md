---
title: icecream
---

# IceCream 项目

## 项目地址
[https://github.com/gruns/icecream](https://github.com/gruns/icecream)

## 主要特性
IceCream 是一个极简的 Python 调试打印工具，旨在提供更优雅、易读的调试输出替代传统的 `print` 语句。其核心特性包括：
- **简洁输出**：自动格式化变量值，显示为 `ic(variable)` 形式，便于快速识别来源。
- **上下文信息**：自动包含函数名、文件名、行号等调试上下文，无需手动添加。
- **支持多种类型**：处理字符串、列表、字典、对象等复杂数据结构，提供清晰的表示。
- **无依赖**：纯 Python 实现，轻量级，不引入额外依赖。
- **自定义配置**：支持调整输出格式、颜色、深度等选项。
- **跨平台兼容**：适用于 Python 2.7+ 和 3.x 版本。

## 主要功能
- **调试打印**：快速打印变量值和表达式结果，便于代码调试。
- **表达式求值**：支持 `ic()` 函数直接求值并打印表达式，如 `ic(1 + 2)`。
- **错误追踪**：在异常发生时自动打印上下文，帮助定位问题。
- **集成支持**：可与 Jupyter Notebook、IPython 等环境无缝集成。
- **性能优化**：生产环境中可轻松禁用输出，避免影响性能。

## 用法
### 安装
```bash
pip install icecream
```

### 基本用法
1. **导入并使用**：
   ```python
   from icecream import ic

   def greet(name):
       ic(name)  # 打印变量 name 的值
       return f"Hello, {name}!"

   greet("World")  # 输出: ic| name='World'
   ```

2. **打印表达式**：
   ```python
   ic(1 + 2 * 3)  # 输出: ic| 1 + 2 * 3: 7
   ```

3. **自定义配置**：
   ```python
   from icecream import ic, install

   ic.configure(output_function=print, context_absorb=False)  # 自定义输出函数
   ```

4. **禁用输出**（生产环境）：
   ```python
   ic.disable()  # 临时禁用
   ```

更多细节请参考项目 README。