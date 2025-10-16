
---
title: dash
---

# Dash 项目

## 项目地址
[GitHub 项目地址](https://github.com/plotly/dash)

## 主要特性
Dash 是由 Plotly 开发的开源 Python 框架，用于构建交互式 Web 应用程序，特别是数据可视化和仪表板。它具有以下主要特性：
- **纯 Python 开发**：无需前端经验，仅使用 Python 代码即可创建完整的 Web 应用，支持 Flask、React.js 和 Plotly.js 等技术栈。
- **交互式可视化**：集成 Plotly 图表库，提供高性能的交互式图表，如散点图、柱状图和 3D 图，支持缩放、悬停和点击事件。
- **组件化设计**：内置丰富的 UI 组件，包括下拉菜单、滑块、按钮和表格等，支持回调函数实现动态交互。
- **响应式布局**：使用 CSS 网格和 Flexbox 构建响应式界面，适配桌面和移动设备。
- **实时更新**：支持 WebSocket 和长轮询，实现数据实时更新，适用于仪表板和监控应用。
- **易于部署**：可部署到 Heroku、AWS 或本地服务器，支持 Docker 容器化。
- **开源与社区支持**：MIT 许可，活跃社区，提供大量示例和扩展库如 Dash Bootstrap Components。

## 主要功能
Dash 的核心功能聚焦于数据驱动的 Web 应用开发：
- **仪表板构建**：快速创建数据仪表板，用于数据探索和分析，支持多页面应用（通过 Dash Pages）。
- **回调机制**：使用 `@app.callback` 装饰器定义输入输出关系，实现组件间交互，例如点击按钮更新图表。
- **数据处理集成**：无缝连接 Pandas、NumPy 等库处理数据，支持 SQL、CSV 和 API 数据源。
- **自定义主题**：通过主题工具或外部 CSS 自定义外观，支持暗黑模式。
- **扩展性**：可集成机器学习模型（如 scikit-learn）或外部 API，实现复杂功能如预测仪表板。
- **性能优化**：懒加载和虚拟化组件处理大数据集，避免界面卡顿。

## 用法
Dash 的用法简单，以下是基本步骤和示例：

### 安装
```bash
pip install dash
```

### 基本用法
1. **导入库**：
   ```python
   import dash
   from dash import dcc, html, Input, Output
   import plotly.express as px
   ```

2. **创建应用**：
   ```python
   app = dash.Dash(__name__)

   # 定义布局
   app.layout = html.Div([
       html.H1("我的 Dash 应用"),
       dcc.Graph(figure=px.scatter(x=[1, 2, 3], y=[4, 5, 6])),
       dcc.Slider(id='slider', min=0, max=10, value=5)
   ])

   # 定义回调
   @app.callback(
       Output('graph', 'figure'),
       Input('slider', 'value')
   )
   def update_graph(value):
       fig = px.scatter(x=[1, 2, 3], y=[value, value+1, value+2])
       return fig

   if __name__ == '__main__':
       app.run_server(debug=True)
   ```

3. **运行应用**：
   - 执行脚本后，访问 `http://127.0.0.1:8050/` 查看应用。
   - 使用 `app.run_server(host='0.0.0.0', port=8050)` 允许外部访问。

4. **高级用法**：
   - **多页面应用**：使用 `dash` 的页面注册器创建路由。
   - **数据加载**：集成 `dcc.Store` 存储数据，或使用 `dash.dash_table` 显示表格。
   - **部署**：使用 Gunicorn 或 Waitress 服务器部署生产环境。

更多示例和文档请参考官方 GitHub 仓库。