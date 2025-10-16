
---
title: bokeh
---

# Bokeh 项目

**项目地址:** [https://github.com/bokeh/bokeh](https://github.com/bokeh/bokeh)

## 主要特性
Bokeh 是一个交互式可视化库，主要用于 Python，支持创建优雅且交互式的图表和应用程序。它强调浏览器端的渲染，使用 WebGL 和 HTML5 Canvas 技术，能够处理大规模数据。关键特性包括：
- **交互性强**：支持缩放、平移、悬停提示、点击事件等交互功能，用户可在浏览器中实时探索数据。
- **多语言支持**：核心为 Python，但也支持 JavaScript、R 和 Julia 等语言。
- **灵活的输出**：可生成静态 HTML 文件、嵌入 Jupyter Notebook，或构建独立的 Web 应用。
- **组件丰富**：内置多种图表类型，如线图、散点图、柱状图、热力图、地图等，还支持自定义布局和工具栏。
- **高性能**：优化了大数据可视化，支持服务器端动态更新数据。
- **开源免费**：基于 BSD 许可证，社区活跃，易于扩展。

## 主要功能
Bokeh 的功能聚焦于数据可视化和交互式 Web 应用开发：
- **数据可视化**：快速创建 2D 图表，支持时间序列、地理数据和统计图。
- **交互模型**：通过 glyphs（图形元素）和 models（模型）定义可视化组件，支持事件处理和回调函数。
- **服务器应用**：使用 Bokeh Server 构建实时应用，可连接数据源如 Pandas、NumPy 或数据库，实现动态更新。
- **集成工具**：与 Jupyter、IPython 和其他科学计算库无缝集成，支持导出为 PNG/SVG 等格式。
- **自定义主题**：提供主题系统和 CSS 自定义，适应不同设计需求。

## 用法
安装 Bokeh 非常简单，使用 pip：
```
pip install bokeh
```

### 基本用法示例
1. **导入库并创建简单图表**：
   ```python
   from bokeh.plotting import figure, show
   from bokeh.io import output_file

   # 输出到 HTML 文件
   output_file("example.html")

   # 创建图形对象
   p = figure(title="简单线图", x_axis_label="x", y_axis_label="y")

   # 添加数据
   x = [1, 2, 3, 4, 5]
   y = [6, 7, 2, 4, 5]
   p.line(x, y, legend_label="趋势线", line_width=2)

   # 显示图表
   show(p)
   ```
   这将生成一个交互式 HTML 文件，用户可在浏览器中查看并交互。

2. **在 Jupyter Notebook 中使用**：
   ```python
   from bokeh.plotting import figure, show
   from bokeh.io import output_notebook

   output_notebook()  # 初始化 Notebook 输出

   p = figure()
   p.circle([1, 2, 3], [4, 5, 6])  # 添加散点
   show(p)
   ```

3. **构建服务器应用**：
   创建一个 `app.py` 文件：
   ```python
   from bokeh.plotting import curdoc
   from bokeh.models import Slider
   from bokeh.layouts import column

   # 定义滑块和图形
   slider = Slider(start=0, end=10, value=1, step=0.1, title="参数")
   p = figure()

   def update(attr, old, new):
       # 更新逻辑
       pass

   slider.on_change('value', update)
   layout = column(slider, p)
   curdoc().add_root(layout)
   ```
   运行 `bokeh serve app.py` 启动服务器，在浏览器访问 `localhost:5006/app`。

更多用法详见官方文档：https://docs.bokeh.org/en/latest/。Bokeh 适合数据科学家、分析师和 Web 开发者，用于快速原型和生产级可视化。