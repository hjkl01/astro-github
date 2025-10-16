
---
title: bpmn-js
---

# BPMN.js 项目

**GitHub 项目地址:** [https://github.com/bpmn-io/bpmn-js](https://github.com/bpmn-io/bpmn-js)

## 主要特性
BPMN.js 是一个开源的 JavaScript 库，用于在浏览器中渲染和编辑 BPMN 2.0（Business Process Model and Notation）图表。它基于 BPMN-IO 团队开发，提供轻量级、高性能的图形编辑器，支持 BPMN、DMN 和其他流程建模标准。主要特性包括：
- **可视化渲染**：精确渲染 BPMN 2.0 兼容的图表，支持自定义样式和元素。
- **拖拽编辑**：内置拖放、连接线创建和属性编辑功能，允许用户交互式修改流程图。
- **扩展性强**：模块化设计，支持插件扩展，如自定义元素、验证规则和导出功能。
- **轻量级**：核心库体积小（约 200KB），适合嵌入 Web 应用。
- **跨浏览器兼容**：支持现代浏览器，无需额外依赖（如 jQuery）。

## 主要功能
- **图表渲染**：从 XML 文件或 JSON 数据加载并显示 BPMN 图，支持缩放、平移和搜索。
- **编辑工具**：提供工具栏、属性面板和画布，支持添加任务、网关、事件等 BPMN 元素，并自动生成连接线。
- **导入/导出**：支持 BPMN 2.0 XML 的导入和导出，可集成到工作流引擎（如 Camunda）。
- **验证与模拟**：内置 BPMN 规则验证，防止无效流程；可选集成模拟功能。
- **自定义集成**：可与 Angular、React 或 Vue 等框架结合，用于企业级流程建模工具。

## 用法
1. **安装**：通过 npm 安装 `npm install bpmn-js`，或直接从 GitHub 下载 dist 文件。
2. **基本集成**（HTML/JS 示例）：
   ```html
   <!DOCTYPE html>
   <html>
   <head>
     <script src="https://unpkg.com/bpmn-js@latest/dist/bpmn-viewer.production.min.js"></script>
   </head>
   <body>
     <div id="canvas" style="height: 500px;"></div>
     <script>
       const viewer = new BpmnJS({ container: '#canvas' });
       viewer.importXML('path/to/diagram.bpmn').then(({ warnings }) => {
         if (warnings.length) console.warn('导入警告:', warnings);
       });
     </script>
   </body>
   </html>
   ```
   - 对于编辑器，使用 `bpmn-js` 包替换 `bpmn-viewer`，并添加工具栏：`new BpmnModeler({ container: '#canvas', additionalModules: [ ... ] })`。
3. **高级用法**：
   - **自定义模块**：通过 `additionalModules` 配置扩展，如添加自定义调色板或规则检查。
   - **事件监听**：监听 `import.render.complete` 或 `elements.changed` 等事件处理交互。
   - **示例项目**：仓库中提供 demos（如 viewer、modeler），可直接运行测试。
   - 文档参考：项目 README 和 [bpmn.io 官网](https://bpmn.io) 获取完整 API 和教程。

该项目适用于构建流程设计工具、自动化工作流系统等场景，社区活跃，支持商业使用（MIT 许可）。