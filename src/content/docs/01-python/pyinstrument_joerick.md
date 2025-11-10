---
title: pyinstrument
---

# pyinstrument 项目

## 项目地址
[GitHub 项目地址](https://github.com/joerick/pyinstrument)

## 主要特性
- **高精度性能分析**：pyinstrument 是一个 Python 性能分析器，使用采样方法（sampling profiler）来捕获代码执行的热点，精度高达毫秒级，支持异步代码（async/await）。
- **低开销**：采样方式确保对程序性能的影响最小，不会显著减慢代码执行。
- **易读输出**：生成易于理解的性能报告，包括调用栈、执行时间百分比和累计时间，支持多种输出格式如文本、HTML 和 JSON。
- **跨平台支持**：兼容 CPython、PyPy 和 Jython，支持 Python 3.7+ 版本。
- **无依赖**：核心功能无需额外依赖，轻量级安装。

## 主要功能
- **实时分析**：在代码运行过程中启动和停止分析，捕获 CPU 时间消耗。
- **异步支持**：无缝处理 asyncio 代码的性能瓶颈。
- **报告生成**：自动生成分层报告，显示函数调用层次、时间分布和热点函数。
- **集成友好**：可作为库集成到现有代码中，或通过命令行工具使用。
- **可视化**：支持导出 HTML 报告，便于浏览器查看交互式性能图表。

## 用法
### 安装
使用 pip 安装：
```
pip install pyinstrument
```

### 基本用法
1. **作为上下文管理器（推荐）**：
   ```python
   from pyinstrument import Profiler

   with Profiler() as profiler:
       # 你的代码
       for i in range(1000000):
           pass

   print(profiler.output_text())
   ```
   这会自动启动和停止分析，并打印文本报告。

2. **命令行工具**：
   运行 Python 脚本时使用：
   ```
   pyinstrument your_script.py
   ```
   它会自动分析脚本并输出报告。支持选项如 `--html` 生成 HTML 文件：
   ```
   pyinstrument --html report.html your_script.py
   ```

3. **手动启动/停止**：
   ```python
   profiler = Profiler()
   profiler.start()
   # 你的代码
   profiler.stop()
   print(profiler.output_text())
   ```

4. **输出格式**：
   - `output_text()`：纯文本报告。
   - `output_html()`：HTML 报告。
   - `output_json()`：JSON 数据，便于进一步处理。

更多细节请参考项目文档。