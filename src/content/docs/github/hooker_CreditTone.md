
---
title: hooker
---

# Hooker 项目

## 项目地址
[https://github.com/CreditTone/hooker](https://github.com/CreditTone/hooker)

## 主要特性
Hooker 是一个基于 Python 的动态函数钩子（hooking）工具，主要用于拦截和修改程序运行时的函数调用。它支持多种钩子机制，包括函数入口/出口钩子、参数修改和返回值篡改。核心特性包括：
- **跨平台支持**：兼容 Windows、Linux 和 macOS 系统。
- **低侵入性**：无需修改源代码，即可动态注入钩子。
- **灵活的钩子配置**：支持正则表达式匹配函数名、自定义回调函数。
- **日志记录**：内置详细的调用日志和性能监控。
- **模块化设计**：易于扩展，支持插件式钩子加载。

## 主要功能
- **函数拦截**：实时捕获指定函数的调用，支持入口钩子（pre-hook）和出口钩子（post-hook）。
- **参数与返回值操作**：允许修改输入参数或伪造输出结果，用于调试、测试或安全分析。
- **性能分析**：监控函数执行时间和调用频率，提供统计报告。
- **集成支持**：可与 Frida 或其他动态分析工具结合使用，适用于逆向工程和软件测试场景。
- **错误处理**：内置异常捕获机制，确保钩子失败不影响主程序运行。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/CreditTone/hooker.git`
   - 安装依赖：`pip install -r requirements.txt`（通常包括 `frida`、`ctypes` 等）。

2. **基本配置**：
   - 编辑 `config.py` 文件，指定目标进程或模块，例如：
     ```python
     TARGET_MODULES = ['example.dll']
     HOOK_PATTERNS = [r'func_\w+']  # 正则匹配函数名
     ```

3. **运行钩子**：
   - 启动目标程序后，执行钩子脚本：
     ```bash
     python hooker.py --target process.exe --hook entry,exit
     ```
   - 示例钩子回调（在 `hooks.py` 中自定义）：
     ```python
     def on_entry(args):
         print(f"Function called with args: {args}")
         return args  # 可修改参数

     def on_exit(return_value):
         print(f"Return value: {return_value}")
         return 42  # 篡改返回值
     ```

4. **高级用法**：
   - 对于脚本化钩子，使用 API 注册：
     ```python
     from hooker import Hooker
     h = Hooker()
     h.attach_to_process('target.exe')
     h.hook_function('example_func', on_entry, on_exit)
     h.run()
     ```
   - 查看日志：运行后检查 `logs/hook.log` 文件。

更多细节请参考仓库的 README.md 和示例目录。