
---
title: PySnooper
---

# PySnooper 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/cool-RR/PySnooper)

## 主要特性
PySnooper 是一个 Python 调试工具，类似于一个“Python 打印调试器”，它可以自动跟踪和记录代码执行过程中的变量变化、函数调用和返回值，而无需手动添加 print 语句。主要特性包括：
- **自动跟踪变量**：监控本地和全局变量的变化，包括类型和值。
- **函数调用栈**：显示函数调用序列和返回点。
- **代码行级跟踪**：逐行记录代码执行过程，便于定位问题。
- **自定义输出**：支持输出到文件、日志级别控制，以及忽略特定变量。
- **无侵入性**：只需添加一个装饰器或上下文管理器，即可启用调试，而不修改原有代码逻辑。
- **支持异步代码**：兼容 async/await 语法。
- **轻量级**：纯 Python 实现，无需额外依赖。

## 主要功能
- **实时调试**：在代码运行时输出详细的执行日志，帮助开发者快速诊断 bug。
- **变量监视**：自动捕获变量的修改、赋值和使用情况。
- **异常处理**：在代码崩溃时提供完整的执行轨迹，便于调试。
- **性能优化**：通过分析日志，可以识别代码中的性能瓶颈或逻辑错误。
- **集成简单**：适用于脚本、Web 应用或大型项目，支持 Python 3.5+。

## 用法
### 1. 安装
使用 pip 安装：
```
pip install pysnooper
```

### 2. 基本用法
#### 作为装饰器（适用于函数）
```python
import pysnooper

@pysnooper.snoop()
def my_function():
    x = 5
    y = x * 2
    return y

my_function()
```
这将输出函数执行的每一步，包括变量变化。

#### 作为上下文管理器（适用于代码块）
```python
import pysnooper

with pysnooper.snoop():
    x = 5
    y = x * 2
    print(y)
```

### 3. 高级选项
- **输出到文件**：`@pysnooper.snoop(output='log.txt')`
- **深度控制**：`@pysnooper.snoop(depth=2)`（限制嵌套调用深度）
- **忽略变量**：`@pysnooper.snoop(ignore=['sensitive_var'])`
- **日志级别**：`@pysnooper.snoop(level='DEBUG')`
- **异步支持**：`@pysnooper.snoop()` 自动处理 async 函数。

更多细节请参考项目 README。