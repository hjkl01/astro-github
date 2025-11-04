
---
title: cesium
---


# CesiumJS

**项目地址**：<https://github.com/CesiumGS/cesium>

CesiumJS 是一个基于 WebGL 的跨平台、功能强大的 3D 地球与地图渲染引擎。它以开源方式提供了高效、可扩展的可视化框架，广泛应用于地理信息系统、航空航天、游戏开发等领域。

---

## 主要

| 特色 | 说明 |
|------|------|
| **高性能 3D 地球** | 利用 WebGL 与实例化渲染技术，支持数百万个多边形与动态几何体。 |
| **实时影像与三维 Tiles** | 支持 Bing Maps、DigitalGlobe、Cesium ion 以及自定义的3D Tiles 进行实时渲染。 |
| **时间动态** | 支持基于时间的动画与事件流，适合展示卫星轨道、气象变化等。 |
| **丰富的数据格式** | 兼容 GeoJSON、CZML、KML、Collada、OBJ、glTF、3D Tiles 等。 |
| **交互工具** | 具备完整的相机控制（轨道、飞行、跟随）、拾取、测距、标注与样式编辑。 |
| **插件化架构** | 可通过 `CesiumWidgets` 组合和自定义功能，方便扩展。 |
| **跨端支持** | Native Web 支持，亦可与 React、Vue 等框架配合使用。 |
| **CSS 主题与可定制** | 可以轻松切换数百种预设视觉风格，或开放 API 进行自定义。 |

---

## 核心功能

1. **地球与地图渲染**  
   - 支持 2D、3D、星图视图。  
   - 多元素（瓦片、矢量、模型、图像）层叠混合。

2. **几何体与模型**  
   - 传统三角网格、点云、曲面（Terrain）、粒子与路径。  
   - `Cesium3DTileset` 与 `Cesium3DTilesProvider` 用于大规模地理数据。

3. **动画与时间**  
   - `JulianDate`、`TimeIntervalCollection` 管理时间；  
   - `Clock` 控制时间轴与播放。

4. **相机与视图**  
   - `Camera` API：锁定、飞行、跟踪、投影转换。  
   - 移动控件：地形、轮盘、键盘与手势。

5. **事件与交互**  
   - `ScreenSpaceEventHandler` 处理点击、拖拽、双击。  
   - `CesiumViewer` 与 `DataSource` 对用户交互做回调。

6. **分析工具**  
   - 测距、测量面积、标注、热力图、视图遮挡。  
   - `Inspector` 用于调试与性能分析。

7. **插件与第三方集成**  
   - 与 `Cesium ion`、Leaflet、OpenStreetMap、Google Maps、3DTiles.io 交互。  
   - `IonResource`, `IonAccessToken` 轻松加载云端资源。

---

## 安装与使用

```bash
# npm（或 yarn）
npm install cesium
```

```html
<!-- CDN 方式 -->
<script src="https://cdn.jsdelivr.net/npm/cesium/Build/Cesium/Cesium.js"></script>
<link href="https://cdn.jsdelivr.net/npm/cesium/Build/Cesium/Widgets/widgets.css" rel="stylesheet" />
```

```ts
import Cesium from 'cesium/Cesium';
import 'cesium/Widgets/widgets.css';

const viewer = new Cesium.Viewer('cesiumContainer', {
  terrainServiceUrl: Cesium.IonTerrainProvider.defaultUrl,
});
```

### 基础示例

```js
const viewer = new Cesium.Viewer('cesiumContainer', {
  imageryProvider: new Cesium.BingMapsImageryProvider({
    url : 'https://dev.virtualearth.net',
    mapStyle : Cesium.BingMapsStyle.AerialWithLabel
  })
});

viewer.scene.globe.depthTestAgainstTerrain = true;

// 添加基准点
viewer.entities.add({
  name : 'Test Point',
  position : Cesium.Cartesian3.fromDegrees(-75.59777, 40.03883),
  point : {
      pixelSize : 10,
      color : Cesium.Color.RED
  }
});
```

---

## 示例与演示

- **Cesium 官方示例**：<https://cesium.com/learn/tutorials>  
- **Cesium 3D Tiles 示例**：<https://cesium.com/docs/tutorials/cesium-3d-tiling-system>  
- **Cesium 与 React**：`react-cesium`、`react-cesium-kit`。  

---

## 贡献

1. Fork 代码仓库。  
2. 创建 issue 或讨论想要实现的功能。  
3. 提交 PR，参考 `CONTRIBUTING.md`。  

---

## 参考文档

- 官方 API 文档：<https://cesium.com/docs/cesiumjs-ref-doc/>  
- 教程与演示：<https://cesium.com/docs/tutorials>  
- 发行说明：<https://github.com/CesiumGS/cesium/releases>  

> 以上即为 **CesiumJS** 的核心特性、功能与基本用法。请根据开发需求进一步探索官方提供的各种 API 与插件。