---
title: folium
---

# Folium 项目介绍

## 项目地址
[GitHub 项目地址](https://github.com/python-visualization/folium)

## 主要特性
Folium 是一个 Python 库，用于创建交互式地图。它基于 Leaflet.js（一个开源的 JavaScript 地图库），允许用户通过 Python 代码生成高度交互式的地图可视化。主要特性包括：
- **交互式地图**：支持缩放、平移和多层叠加，生成纯 HTML/JavaScript 地图，无需额外服务器。
- **多种图层支持**：包括标记（Markers）、热力图（Heatmaps）、 choropleth 地图（人口统计图）、GeoJSON 叠加等。
- **插件集成**：内置多种 Leaflet 插件，如时间序列地图（Timestamped GeoJSON）和测距工具（Measure Control）。
- **简单易用**：基于 Pandas 和其他 Python 生态工具，易于与数据分析结合。
- **轻量级**：生成的地图文件小巧，可嵌入 Jupyter Notebook 或 Web 页面。
- **开源免费**：MIT 许可，社区活跃，支持自定义扩展。

## 主要功能
- **基础地图创建**：使用 OpenStreetMap、Stamen 等瓦片提供商生成基础地图。
- **数据可视化**：将地理数据（如经纬度、形状文件）映射到地图，支持颜色编码和弹出窗口（Popups）。
- **高级可视化**：热力图、聚类标记、路径绘制、多边形填充等，用于地理数据分析。
- **导出与分享**：保存为 HTML 文件，便于分享或嵌入网站。
- **与库集成**：无缝兼容 Pandas DataFrame、GeoPandas 等，用于处理地理数据。

## 用法示例
安装 Folium：`pip install folium`

### 基本用法
```python
import folium

# 创建地图，中心点为北京 (纬度，经度)，缩放级别 10
m = folium.Map(location=[39.9042, 116.4074], zoom_start=10)

# 添加标记
folium.Marker(
    location=[39.9042, 116.4074],
    popup="北京",
    tooltip="点击查看"
).add_to(m)

# 保存为 HTML 文件
m.save("beijing_map.html")
```
这将生成一个交互式地图文件 `beijing_map.html`，可在浏览器中打开查看。

### 高级用法示例：热力图
```python
import folium
from folium.plugins import HeatMap

m = folium.Map(location=[39.9042, 116.4074], zoom_start=10)

# 示例数据：位置和强度
data = [[39.9042, 116.4074, 1], [39.9, 116.4, 0.5]]  # [lat, lon, intensity]

HeatMap(data).add_to(m)
m.save("heatmap.html")
```

更多用法请参考官方文档：https://python-visualization.github.io/folium/