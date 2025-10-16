
---
title: X6
---

# X6 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/antvis/X6)

## 主要特性
X6 是由 AntV 团队开发的 React 流程图库，专为构建复杂图编辑器而设计。它基于 HTML 和 SVG 技术，提供高性能的图形渲染和交互能力。主要特性包括：

- **节点与边支持**：支持自定义节点形状、样式和行为，包括矩形、圆形、流程图符号等。边支持直线、曲线、正交连接等多种类型。
- **布局算法**：内置多种布局引擎，如有向图布局（dagre）、力导向布局（force）和网格布局，支持自动调整节点位置。
- **交互功能**：提供拖拽、缩放、选择、多选、连接器拖拽等交互，支持事件监听和自定义工具栏。
- **渲染引擎**：使用 Canvas 和 SVG 双渲染模式，确保在不同场景下的高性能和兼容性。
- **扩展性**：支持插件系统，可集成Stencil（形状库）、MiniMap（小地图）和 Grid（网格）等组件，便于扩展自定义功能。
- **兼容性**：基于 React 开发，支持 Vue 和纯 JavaScript 集成，适用于流程图、ER 图、UML 图等可视化场景。

## 主要功能
X6 的核心功能聚焦于图编辑器的构建：
- **图谱管理**：创建、编辑和导出图谱数据，支持 JSON 格式的序列化/反序列化。
- **连接与路由**：自动路由边线，避免节点重叠，支持磁吸和对齐辅助。
- **工具集成**：内置画布工具，如橡皮擦、撤销/重做、导出 PNG/SVG 等。
- **数据绑定**：支持与外部数据源绑定，实现动态图谱更新。
- **主题与样式**：提供暗黑/明亮主题，自定义 CSS 变量和动画效果。
- **性能优化**：虚拟化渲染和懒加载，适用于大规模节点（数千级）场景。

## 用法
X6 的用法简单，通过 React 组件集成。以下是基本步骤：

1. **安装**：
   ```bash
   npm install @antv/x6 @antv/x6-react-shape
   ```

2. **基本示例**（React 中使用）：
   ```jsx
   import React from 'react';
   import { Graph } from '@antv/x6';

   const MyGraph = () => {
     const graph = new Graph({
       container: document.getElementById('container'), // 指定容器
       width: 800,
       height: 600,
       layout: { type: 'dagre' }, // 使用布局算法
     });

     // 添加节点
     graph.addNode({
       id: 'node1',
       x: 100,
       y: 100,
       width: 80,
       height: 40,
       label: '节点1',
     });

     // 添加边
     graph.addEdge({
       source: 'node1',
       target: 'node2',
       label: '连接',
     });

     return <div id="container" />;
   };

   export default MyGraph;
   ```

3. **高级用法**：
   - **自定义节点**：使用 `ReactShape` 注册 React 组件作为节点。
   - **事件监听**：`graph.on('node:selected', ({ node }) => { console.log(node); });`。
   - **Stencil 集成**：导入形状库，实现拖拽添加节点。
   - **导出**：`graph.toJSON()` 保存数据，或 `graph.toSVG()` 导出图像。

详细文档和示例请参考 GitHub 仓库的 README 和 examples 目录。X6 适用于流程设计、架构图和数据可视化工具的开发。