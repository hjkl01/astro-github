
---
title: PyWebIO
---

# PyWebIO 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/pywebio/PyWebIO)

## 主要特性
PyWebIO 是一个简单易用的 Python Web UI 工具包，它允许开发者使用纯 Python 代码构建交互式 Web 界面，而无需编写 HTML、CSS 或 JavaScript。主要特性包括：
- **纯 Python 开发**：所有 UI 元素和逻辑均用 Python 编写，支持同步和异步编程。
- **零前端知识要求**：无需前端开发经验，即可快速创建 Web 应用。
- **组件丰富**：内置多种 UI 组件，如按钮、输入框、表格、图表等，支持实时交互。
- **支持多种运行模式**：可作为 Web 应用运行，也可嵌入 Flask/Django 等框架，或作为命令行工具。
- **跨平台兼容**：基于 Tornado Web 服务器，支持 Windows、Linux 和 macOS。
- **轻量级**：安装简单，依赖少，适合快速原型开发和小型 Web 应用。

## 主要功能
PyWebIO 的核心功能聚焦于 Web UI 的构建和交互：
- **输出功能**：如 `put_text()`、`put_image()`、`put_table()` 等，用于渲染文本、图片、表格和 Markdown 内容。
- **输入功能**：如 `input()`、`textarea()`、`select()` 等，用于收集用户输入，支持验证和默认值。
- **交互组件**：按钮 (`put_buttons()`)、进度条 (`put_progress()`)、文件上传 (`FileZone`) 等，实现动态响应。
- **布局管理**：使用 `put_row()`、`put_column()` 和 `put_scope()` 组织界面布局。
- **事件处理**：通过回调函数处理用户交互，支持异步操作（如 AJAX 请求）。
- **会话管理**：内置会话机制，支持多用户并发和状态持久化。
- **扩展支持**：集成第三方库，如 Matplotlib 用于图表、Pandas 用于数据展示。

## 用法
### 安装
使用 pip 安装：
```
pip install pywebio
```

### 基本用法
1. **导入模块**：
   ```python
   from pywebio.input import input, TEXT
   from pywebio.output import put_text, use_browser_url
   from pywebio import start_server
   ```

2. **编写简单应用**：
   ```python
   def hello():
       name = input("请输入您的姓名", type=TEXT)
       put_text(f"你好，{name}！")
   
   if __name__ == "__main__":
       start_server(hello, port=8080, debug=True)
   ```
   - 运行后，访问 `http://localhost:8080` 即可看到交互界面。

3. **高级用法**：
   - **异步支持**：使用 `async/await` 处理网络请求。
     ```python
     import asyncio
     from pywebio.output import put_text
     
     async def async_task():
         await asyncio.sleep(1)
         put_text("异步任务完成")
     ```
   - **集成框架**：在 Flask 中嵌入：
     ```python
     from flask import Flask
     from pywebio import platform
     
     app = Flask(__name__)
     
     def index():
         # PyWebIO 代码
         pass
     
     app.add_url_rule('/', index, methods=['GET', 'POST'])
     platform.FLASK_DRIVER.run(app)
     ```
   - **布局示例**：
     ```python
     from pywebio.output import put_row, put_column, put_button
     
     put_row([put_button("按钮1"), put_button("按钮2")])
     put_column([put_text("上"), put_text("下")])
     ```

更多细节请参考官方文档：https://pywebio.readthedocs.io/