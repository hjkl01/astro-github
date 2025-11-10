---
title: Leaflet
---

# Leaflet 项目概述

## 项目地址
[https://github.com/Leaflet/Leaflet](https://github.com/Leaflet/Leaflet)

## 主要特性
Leaflet 是一个开源的 JavaScript 库，用于创建交互式地图。它设计简洁、模块化，轻量级（核心库仅约 42 KB），支持现代浏览器，包括 IE6 及以上版本。主要特性包括：
- **高性能**：高效渲染地图，支持大规模数据可视化。
- **插件生态**：丰富的插件系统，可扩展功能，如标记、弹出框、图层控制等。
- **移动端友好**：响应式设计，支持触摸交互，适用于手机和平板。
- **无外部依赖**：纯 JavaScript 实现，不依赖 jQuery 等库。
- **开源协议**：采用 BSD 许可，免费用于商业和非商业项目。
- **跨平台支持**：兼容多种地图提供商，如 OpenStreetMap、Mapbox 等。

## 主要功能
Leaflet 提供核心地图功能和扩展工具：
- **地图创建与显示**：初始化地图视图，添加瓦片层（Tile Layers）以显示底图。
- **交互元素**：支持标记（Markers）、弹出框（Popups）、路径（Polylines/Polygons）、圆形（Circles）等图形元素。
- **事件处理**：监听地图事件，如点击、拖拽、缩放，支持自定义事件。
- **图层管理**：多图层叠加、切换和控制，包括矢量图层和栅格图层。
- **控件集成**：内置缩放控件、属性控件、全屏模式等，可自定义。
- **动画与过渡**：平滑缩放、飞入动画，提升用户体验。
- **地理编码与测距**：集成地理位置服务，支持距离计算和坐标转换。

## 用法
Leaflet 的用法简单，通过 HTML 和 JavaScript 集成。以下是基本步骤和示例：

### 1. 安装与引入
- 通过 CDN 引入（推荐快速启动）：
  ```html
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  ```
- 或通过 npm 安装：`npm install leaflet`，然后导入 CSS 和 JS。

### 2. 创建地图
在 HTML 中添加一个 `<div id="map">` 容器，然后用 JavaScript 初始化：
```javascript
// 初始化地图，中心点为 [纬度, 经度]，缩放级别 13
var map = L.map('map').setView([51.505, -0.09], 13);

// 添加 OpenStreetMap 瓦片层
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
```

### 3. 添加交互元素
- 添加标记和弹出框：
  ```javascript
  L.marker([51.5, -0.09]).addTo(map)
      .bindPopup('这是一个标记！')
      .openPopup();
  ```
- 添加多边形：
  ```javascript
  var polygon = L.polygon([
      [51.509, -0.08],
      [51.503, -0.06],
      [51.51, -0.047]
  ], {color: 'red'}).addTo(map);
  ```

### 4. 高级用法
- **事件监听**：`map.on('click', function(e) { console.log(e.latlng); });`
- **插件集成**：如使用 Leaflet.Draw 插件添加绘图功能，需额外引入插件文件。
- **自定义**：通过 CSS 类或选项配置样式和行为。
- **文档与示例**：官方文档（https://leafletjs.com/）提供详细 API 和互动示例，便于学习和调试。

Leaflet 适合 Web 应用、移动 App 和数据可视化项目，易于上手且高度可定制。