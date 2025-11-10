---
title: S2
---

# AntV S2 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/antvis/S2)

## 主要特性
AntV S2 是一个高性能的 Web 端多维数据分析引擎，专注于提供灵活、交互式的报表和表格可视化解决方案。其核心特性包括：
- **高性能渲染**：支持百万级数据量渲染，通过 Canvas 或 SVG 实现高效的表格绘制和交互。
- **多维数据支持**：兼容 OLAP（在线分析处理）模型，支持透视表、明细表和聚合分析。
- **丰富的交互功能**：内置排序、筛选、展开/折叠、拖拽等交互，支持自定义插件扩展。
- **灵活的布局系统**：支持行头、列头、数据区域的自定义布局，适应复杂报表需求。
- **跨框架兼容**：可无缝集成 React、Vue、Angular 等前端框架，也支持纯 JS 使用。
- **主题与样式自定义**：提供多种内置主题，并允许用户自定义颜色、字体和布局样式。
- **数据安全与优化**：支持数据加密、懒加载和虚拟滚动，提升大规模数据处理的效率。

## 主要功能
S2 的功能覆盖从数据处理到可视化的全流程：
- **数据透视与聚合**：自动处理多维度数据，支持 SUM、AVG、COUNT 等聚合函数，实现动态透视表。
- **报表类型**：支持明细表、汇总表、交叉表等多种报表形式，可处理行列混合布局。
- **交互分析**：用户可通过点击、拖拽进行维度切换、指标调整，实现自助式数据探索。
- **导出与打印**：内置 PDF/Excel 导出功能，支持打印优化。
- **插件系统**：扩展性强，可集成图表（如柱状图、热力图）或其他自定义组件。
- **移动端适配**：响应式设计，支持触屏交互，适用于 PC 和移动设备。
- **数据源集成**：兼容本地数据、远程 API（如 JSON、CSV），并支持与 AntV 生态（如 G2、L7）联动。

## 用法指南
### 安装
通过 npm 安装核心包：
```bash
npm install @antv/s2
```

### 基本用法（React 示例）
1. **导入组件**：
   ```jsx
   import { SheetComponent } from '@antv/s2';
   import '@antv/s2/dist/style.css';
   ```

2. **准备数据**：S2 使用标准数据格式（数组对象），例如：
   ```javascript
   const data = [
     { category: 'A', value: 100 },
     { category: 'B', value: 200 }
   ];
   ```

3. **渲染表格**：
   ```jsx
   <SheetComponent
     dataCfg={{ data, fields: { columns: ['category'], values: ['value'] } }}
     meta={[{ field: 'value', name: '数值' }]}
     sheetType={'pivot'} // 或 'table' 为明细表
   />
   ```

### 高级用法
- **自定义配置**：通过 `options` 属性设置主题、交互等，例如：
  ```javascript
  const s2Options = {
    width: 600,
    height: 480,
    interaction: { enableCopy: true },
    style: { layoutWidthType: 'adaptive' }
  };
  ```
- **事件监听**：监听范围选择、排序等事件：
  ```javascript
  sheet.on('range-selected', (cell) => console.log(cell));
  ```
- **集成框架**：在 Vue 中使用 `<template>` 包裹 SheetComponent；在纯 JS 中，通过 `new S2(canvas, config)` 初始化。
- **文档与示例**：详见 GitHub 仓库的 [文档](https://s2.antv.antgroup.com/docs) 和 [在线 Demo](https://s2.antv.antgroup.com/examples)，提供完整 API 和用例。

S2 适用于 BI 仪表盘、数据报表和分析工具开发，结合 AntV 生态可构建完整的数据可视化应用。