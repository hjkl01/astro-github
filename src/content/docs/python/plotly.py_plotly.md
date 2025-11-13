---
title: plotly.py
---

# Plotly.py 项目

**GitHub 项目地址:** [https://github.com/plotly/plotly.py](https://github.com/plotly/plotly.py)

## 主要特性

Plotly.py 是 Plotly 公司开发的开源 Python 图形库，基于 JavaScript 的 Plotly.js 引擎构建。它支持创建交互式、高质量的可视化图表，具有以下主要特性：

- **交互性强**：生成的图表支持缩放、悬停提示、点击事件和动画，用户可以实时交互探索数据。
- **多种图表类型**：内置支持 40 多种图表类型，包括散点图、线图、柱状图、热力图、3D 图表、地图、饼图等，适用于科学计算、数据分析和机器学习可视化。
- **跨平台输出**：可以生成静态图像（PNG、SVG、PDF）、HTML 文件或嵌入 Jupyter Notebook，支持离线和在线模式。
- **高性能**：优化了大数据集的渲染，支持 WebGL 加速的 3D 和复杂图表。
- **主题和自定义**：提供多种内置主题（如 Plotly、ggplot2），并允许高度自定义颜色、布局、轴标签和注解。
- **与其他库集成**：无缝集成 Pandas、NumPy、SciPy 等科学计算库，以及 Dash（Plotly 的 Web 应用框架）用于构建交互式仪表板。
- **开源与社区支持**：Apache 2.0 许可，活跃的社区和详细文档。

## 主要功能

- **基本绘图**：快速创建 2D 和 3D 图表，支持子图布局（subplots）和多轴图。
- **统计图表**：包括箱线图、 violin 图、分布图和直方图，用于数据分布分析。
- **科学可视化**：支持等高线图、表面图、等值线图，以及金融图表（如蜡烛图、OHLC 图）。
- **动画与地图**：创建动态动画图表，以及 choropleth 地图和散点地图，用于地理数据可视化。
- **导出与分享**：一键导出为图像或 HTML，支持 Plotly Chart Studio 在线分享和协作。
- **API 设计**：采用声明式 API，类似于 Matplotlib，但更注重交互性和 Web 友好性。

## 用法

### 安装
使用 pip 安装：
```
pip install plotly
```
对于 Jupyter Notebook 支持，还需安装 `kaleido` 用于静态导出：
```
pip install "kaleido>=0.2.1"
```

### 基本用法示例

1. **导入库并创建简单散点图**：
   ```python
   import plotly.express as px
   import pandas as pd

   # 示例数据
   df = pd.DataFrame({
       'x': [1, 2, 3, 4],
       'y': [10, 11, 12, 13]
   })

   # 使用 Plotly Express（简化 API）创建图表
   fig = px.scatter(df, x='x', y='y', title='简单散点图')
   fig.show()  # 在浏览器中显示交互式图表
   ```

2. **使用低级 Graph Objects API 创建自定义图表**：
   ```python
   import plotly.graph_objects as go

   fig = go.Figure()
   fig.add_trace(go.Scatter(x=[1, 2, 3], y=[10, 11, 12], mode='lines+markers'))
   fig.update_layout(title='自定义线图')
   fig.show()
   ```

3. **导出图表**：
   ```python
   fig.write_html("chart.html")  # 保存为 HTML 文件
   fig.write_image("chart.png")  # 保存为静态图像
   ```

4. **在 Jupyter Notebook 中使用**：
   在 Notebook 单元格中直接运行 `fig.show()`，图表会内嵌显示。确保安装 `jupyterlab-plotly` 扩展以获得最佳交互体验。

更多高级用法，请参考官方文档：https://plotly.com/python/。该库适合数据科学家、工程师和分析师，用于快速原型设计和生产级可视化。