
---
title: altair
---

# Altair 项目

**GitHub 项目地址：** [https://github.com/altair-viz/altair](https://github.com/altair-viz/altair)

## 主要特性
Altair 是一个声明式的统计可视化库，基于 Python 和 Vega/Vega-Lite 可视化规范构建。主要特性包括：
- **声明式语法**：通过简洁的 Python API 描述数据和可视化需求，而非手动编写底层绘图代码。
- **集成性强**：无缝集成 Pandas DataFrame，支持与 Jupyter Notebook 等环境协作。
- **交互式可视化**：生成交互式图表，支持缩放、悬停提示和动态过滤。
- **主题和自定义**：内置多种主题，支持自定义颜色、布局和样式。
- **多图表组合**：易于创建复合图表，如分面图、层叠图和重复图。
- **导出支持**：可导出为 HTML、SVG、PNG 等格式，便于分享和嵌入。

## 主要功能
Altair 专注于数据探索和统计可视化，支持多种图表类型：
- **基本图表**：线图、散点图、柱状图、面积图、条形图等。
- **高级功能**：分面（Facet）、层叠（Layer）、变换（Transform，如聚合、过滤、计算）。
- **统计功能**：内置统计变换，如回归线、箱线图、 violin 图。
- **交互与链接**：支持多视图链接，实现刷选和高亮交互。
- **数据处理**：自动处理数据类型推断和编码（位置、颜色、形状等）。
- **扩展性**：通过 Vega-Lite 规范，可扩展到复杂可视化场景。

## 用法示例
安装 Altair：`pip install altair`

### 基本用法
```python
import altair as alt
import pandas as pd

# 示例数据
data = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [1, 4, 2, 3]
})

# 创建散点图
chart = alt.Chart(data).mark_circle().encode(
    x='x',
    y='y'
)

# 在 Jupyter 中显示
chart
```

### 高级用法
```python
# 交互式线图
chart = alt.Chart(data).mark_line().encode(
    x='x:Q',
    y='y:Q',
    color='category:N'
).interactive()

chart
```

更多用法请参考官方文档：https://altair-viz.github.io/