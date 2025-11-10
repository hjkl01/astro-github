---
title: LogicFlow
---

# LogicFlow 项目

**GitHub 项目地址:** [https://github.com/didi/LogicFlow](https://github.com/didi/LogicFlow)

## 主要特性

LogicFlow 是一个基于 HTML5 的流程图引擎和低代码开发平台，由滴滴出行开源维护。它专注于提供高性能、可扩展的流程可视化解决方案，支持多种交互式编辑功能。主要特性包括：

- **高性能渲染**: 采用 Canvas 技术，支持大规模节点和边的渲染，适用于复杂流程图。
- **可扩展性强**: 提供插件系统，用户可以自定义节点、边、锚点等组件。
- **交互友好**: 支持拖拽、缩放、连接线自动吸附等交互操作，提升用户体验。
- **主题与样式自定义**: 内置多种主题，支持 CSS 变量自定义外观。
- **数据驱动**: 基于 JSON 数据结构，易于与后端集成，实现数据与视图的双向绑定。
- **多端适配**: 支持 PC 和移动端，兼容主流浏览器。
- **开源免费**: MIT 许可，社区活跃，提供详细文档和示例。

## 主要功能

LogicFlow 的核心功能聚焦于流程图的创建、编辑和交互，主要包括：

- **节点管理**: 支持自定义节点类型（如矩形、圆形、流程图标准形状），包括文本编辑、属性配置。
- **边与连接**: 自动路径计算、弯曲线、多锚点连接，支持直线、折线、贝塞尔曲线等样式。
- **画布操作**: 画布缩放、平移、多选、撤销/重做、复制/粘贴等编辑工具。
- **事件系统**: 丰富的生命周期事件（如节点选中、边连接），便于监听和扩展。
- **导出与导入**: 支持导出为 SVG、PNG、JSON 等格式，便于分享和持久化。
- **集成能力**: 可嵌入 React、Vue 等框架，支持与其他可视化库结合。
- **低代码支持**: 提供属性面板、工具栏等组件，实现拖拽式开发。

## 用法

### 安装
通过 npm 安装：
```bash
npm install @logicflow/core
# 或 yarn
yarn add @logicflow/core
```

### 基本用法
1. **引入和初始化**:
   ```javascript
   import { LogicFlow } from '@logicflow/core';
   import '@logicflow/core/dist/style/index.css';

   const lf = new LogicFlow({
     container: document.querySelector('#app'),  // 画布容器
     width: 1000,
     height: 800,
     grid: true,  // 显示网格
   });
   ```

2. **添加节点和边**:
   ```javascript
   // 添加节点
   lf.addNode({
     type: 'rect',
     x: 100,
     y: 100,
     text: '起始节点',
     width: 100,
     height: 60,
   });

   // 添加边
   lf.addEdge({
     type: 'default',
     sourceNodeId: 'node1',
     targetNodeId: 'node2',
   });
   ```

3. **渲染数据**:
   ```javascript
   const data = {
     nodes: [{ id: '1', type: 'rect', x: 100, y: 100, text: '节点1' }],
     edges: [{ id: 'e1', sourceNodeId: '1', targetNodeId: '2' }],
   };
   lf.render(data);
   ```

4. **监听事件**:
   ```javascript
   lf.on('node:click', ({ data }) => {
     console.log('节点点击:', data);
   });
   ```

5. **高级用法**:
   - **自定义节点**: 扩展 `BaseNode` 类，实现渲染逻辑。
   - **插件集成**: 如 `@logicflow/extension` 中的属性面板。
   - **React/Vue 示例**: 项目仓库提供官方示例代码，参考 `examples` 目录。

更多细节请参考官方文档：https://logicflow.didi.tech/guide/。