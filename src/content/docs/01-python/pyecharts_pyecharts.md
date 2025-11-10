---
title: pyecharts
---

# pyecharts 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/pyecharts/pyecharts)

## 主要特性
pyecharts 是一个用于生成 ECharts 图表的 Python 库，它将 Python 的数据处理能力与 ECharts 的交互式可视化功能相结合。主要特性包括：
- **支持多种图表类型**：涵盖折线图、柱状图、散点图、饼图、热力图、地图、仪表盘等多种 ECharts 图表，支持 2D 和 3D 渲染。
- **交互式可视化**：生成的图表具有丰富的交互功能，如缩放、拖拽、提示框、点击事件等，用户可轻松创建动态网页图表。
- **纯 Python 实现**：无需前端知识，只需 Python 代码即可生成 HTML 文件，支持 Jupyter Notebook 和 Flask/Django 等框架集成。
- **数据兼容性强**：支持 Pandas DataFrame、NumPy 数组等多种数据源，便于数据科学工作流。
- **主题和自定义**：内置多种主题（如浅色、深色），并允许自定义颜色、样式和动画效果。
- **跨平台**：生成的图表可在浏览器中运行，支持现代浏览器，无需额外服务器。

## 主要功能
- **图表生成**：快速创建静态或动态图表，并导出为 HTML、PNG 或嵌入网页。
- **数据绑定**：自动将 Python 数据转换为 ECharts 配置，支持实时更新和动画过渡。
- **组件化设计**：提供 Bar、Line、Scatter 等类，便于组合复杂图表（如多轴图、子图布局）。
- **地图支持**：内置中国地图、世界地图等地理可视化功能，可叠加热力图或标记点。
- **事件处理**：支持 JavaScript 回调，实现图表与 Python 后端的交互。
- **性能优化**：适用于大数据集，通过分层渲染和懒加载提升效率。

## 用法示例
安装：`pip install pyecharts`

基本用法（Python 代码）：
```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode

# 创建柱状图
bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("销量", [5, 20, 36, 10, 10, 20])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题"))
    .dump_options()  # 生成 JSON 配置，或使用 .render() 导出 HTML
)
```

- **渲染图表**：调用 `bar.render("bar_chart.html")` 生成 HTML 文件，在浏览器中查看交互图表。
- **Jupyter 集成**：在 Notebook 中直接显示：`bar.render_notebook()`。
- **高级用法**：结合 Pandas：`df = pd.DataFrame(data); bar.add_yaxis("系列", df['value'].tolist())`。
- **文档参考**：项目提供详细 API 文档和示例，适合从简单图表到复杂仪表板的开发。