---
title: vega-lite
---

# Vega-Lite 项目

## 项目地址
[GitHub 项目地址](https://github.com/vega/vega-lite)

## 主要特性
Vega-Lite 是一个声明式的可视化语法，基于 Vega 库构建。它允许用户通过简洁、高层次的 JSON 规范来创建交互式图表，而无需编写低级绘图代码。主要特性包括：
- **声明式语法**：使用 JSON 或 YAML 格式定义图表，强调数据、标记和编码，而不是像素级细节。
- **简洁表达**：支持层叠图表、变换和多视图组成，减少规范的复杂性。
- **交互性**：内置工具提示、缩放、平移和选择等交互功能，支持动态数据绑定。
- **跨平台兼容**：生成基于 Web 标准的 SVG、Canvas 或 WebGL 输出，适用于 Web、Jupyter 和 React 等环境。
- **扩展性**：集成 Vega 的高级功能，如自定义变换和模块化组件。
- **主题支持**：提供内置主题和自定义选项，优化美观性和可访问性。

## 主要功能
Vega-Lite 的核心功能聚焦于数据可视化，支持多种图表类型和数据处理：
- **图表类型**：包括条形图、折线图、散点图、热力图、箱线图、地图等多种标记（marks），如 bar、line、point、area、rect 等。
- **数据变换**：内置过滤、聚合、窗口函数、层叠和连接等操作，支持从 CSV、JSON 或远程 URL 加载数据。
- **编码通道**：通过位置（x/y）、颜色、形状、大小等通道映射数据，支持定量、序数、名义和时间类型。
- **多视图和组成**：创建 facet、concat、layer 和 repeat 等复合视图，实现仪表板式布局。
- **交互和动画**：支持信号（signals）定义参数化交互、过渡动画和事件处理。
- **导出与嵌入**：生成静态图像、交互嵌入代码，或集成到工具如 Observable、D3.js 中。

## 用法
Vega-Lite 的用法简单，通常通过 JSON 规范定义图表，然后渲染。以下是基本步骤和示例：

### 1. 安装与环境
- 通过 npm 安装：`npm install vega vega-lite vega-embed`。
- 在浏览器中使用 CDN：`<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>` 和 `<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>`。
- 支持 Python（Altair 库）或 R（vegawidget）绑定。

### 2. 创建基本规范
使用 JSON 对象定义图表。示例：简单条形图。

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "条形图示例",
  "data": {
    "values": [
      {"category": "A", "value": 28},
      {"category": "B", "value": 55},
      {"category": "C", "value": 43}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "category", "type": "nominal"},
    "y": {"field": "value", "type": "quantitative"}
  }
}
```

### 3. 渲染图表
使用 Vega-Embed 库嵌入到 HTML：
```html
<div id="view"></div>
<script type="text/javascript">
  vegaEmbed('#view', spec).then(function(result) {
    // 图表渲染完成
  }).catch(console.error);
</script>
```
- `spec` 是上述 JSON 对象。
- 对于在线编辑，使用 [Vega Editor](https://vega.github.io/editor/) 测试规范。

### 4. 高级用法
- **数据加载**：从 URL 或内联数据源指定 `"url": "data.csv"`。
- **交互添加**：在规范中添加 `"selection": {...}` 或 `"params": [...]`。
- **自定义**：扩展以支持地理投影或自定义标记。
- **文档与示例**：参考官方教程（https://vega.github.io/vega-lite/docs/）获取更多规范示例和 API 细节。