---
title: nicegui
---


# NiceGUI 介绍

**GitHub 地址**: https://github.com/zauberzeug/nicegui

NiceGUI 是一个用 Python 编写的现代 Web UI 框架，基于 FastAPI + Vue.js，允许开发者用纯 Python 代码快速构建交互式 Web 应用。其核心特性、功能以及使用方法如下：

## 主要特性

| 特性 | 说明 |
|------|------|
| **Python 原生** | 所有 UI 组件、路由、后端逻辑均使用 Python 编写，无需 JavaScript。 |
| **实时响应** | 通过 WebSocket 自动将组件状态同步，支持双向绑定。 |
| **FastAPI 集成** | 与 FastAPI 无缝配合，支持路由、依赖注入、后台任务。 |
| **Vue.js 前端** | 内置 Vue 组件库，提供丰富的 UI 组件（Button、Input、Table、Chart 等）。 |
| **主题与自定义** | 支持自定义主题、颜色、字体，易于美化。 |
| **文件上传/下载** | 原生支持文件上传、下载、流式传输。 |
| **实时日志** | 在浏览器内实时显示后端日志，方便调试。 |
| **权限与认证** | 通过 FastAPI 的 OAuth2、JWT 等方式实现权限控制。 |
| **部署灵活** | 可单独运行、Docker 化、嵌入现有 FastAPI 项目。 |

## 主要功能

- **UI 组件**：按钮、输入框、下拉选择、表格、图表、地图、弹窗、对话框等。
- **布局**：Grid、Flex、Sidebar、Tabs、Accordion、Dialog 等布局组件。
- **交互**：事件绑定（on_click、on_change）、表单验证、拖拽排序。
- **数据可视化**：集成 Chart.js、Plotly、ECharts 等，可绘制折线图、柱状图、饼图等。
- **文件操作**：上传、下载、文件浏览器、文件预览。
- **后台任务**：通过 `BackgroundTask` 或 `asyncio` 运行耗时任务，结果实时回传。
- **权限管理**：内置 `@app.get("/admin", auth=Auth(...))` 方式实现访问控制。

## 使用方法

1. **安装**

   ```bash
   pip install nicegui
   ```

2. **创建简单应用**

   ```python
   from nicegui import ui

   ui.label('Hello, NiceGUI!')

   def submit():
       print('Button clicked!')

   ui.button('Click me', on_click=submit)

   ui.run()
   ```

3. **运行**

   ```bash
   python app.py
   ```

   浏览器访问 `http://localhost:8080` 即可看到界面。

4. **高级用法**（示例：表格 + 过滤）

   ```python
   from nicegui import ui

   data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

   table = ui.table(data=data, columns=['name', 'age'])

   def filter():
       keyword = ui.input().value
       table.update_data([d for d in data if keyword.lower() in d['name'].lower()])

   ui.button('Filter', on_click=filter)
   ui.run()
   ```

5. **集成 FastAPI**

   ```python
   from fastapi import FastAPI
   from nicegui import ui

   app = FastAPI()

   @app.get("/")
   async def index():
       return "Hello from FastAPI"

   ui.run(app=app)
   ```

6. **Docker 部署**（示例 `Dockerfile`）

   ```dockerfile
   FROM python:3.12-slim
   COPY . /app
   WORKDIR /app
   RUN pip install -r requirements.txt
   CMD ["python", "app.py"]
   ```

## 参考资源

- 官方文档: https://nicegui.io
- 示例仓库: https://github.com/zauberzeug/nicegui/tree/main/examples

> 以上内容概述了 NiceGUI 的核心特性、功能与典型使用方式，帮助你快速上手并构建高效的 Web 应用。