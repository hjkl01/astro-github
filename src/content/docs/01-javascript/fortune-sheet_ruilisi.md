---
title: fortune-sheet
---

# Fortune Sheet 项目概述

## 项目地址
[https://github.com/ruilisi/fortune-sheet](https://github.com/ruilisi/fortune-sheet)

## 主要特性
Fortune Sheet 是一个开源的在线电子表格项目，类似于 Google Sheets 或 Excel，提供高性能的浏览器端表格编辑功能。主要特性包括：
- **纯前端实现**：无需后端服务器，完全在浏览器中运行，支持离线使用。
- **高性能渲染**：使用 Canvas 技术实现大规模数据渲染，支持数万行数据的高速加载和编辑。
- **丰富的编辑功能**：支持单元格编辑、公式计算、排序、过滤、条件格式化等标准表格操作。
- **多主题支持**：内置暗黑模式和自定义主题，适应不同用户界面需求。
- **插件扩展**：可通过插件系统扩展功能，如图表、数据导入/导出等。
- **移动端适配**：响应式设计，支持触摸设备上的操作。
- **开源免费**：基于 MIT 许可，允许自由修改和商业使用。

## 主要功能
- **数据管理**：导入/导出 CSV、Excel 文件，支持 JSON 数据绑定。
- **公式引擎**：内置 JavaScript 公式解析器，支持 SUM、AVERAGE、IF 等常见函数。
- **协作编辑**：通过 WebSocket 支持实时多人协作（需后端集成）。
- **图表与可视化**：集成 ECharts 等库，实现柱状图、折线图等数据可视化。
- **自定义配置**：支持 API 配置表格布局、列宽、冻结窗格等。
- **国际化**：多语言支持，包括中文界面。

## 用法
1. **安装与引入**：
   - 通过 npm 安装：`npm install fortune-sheet`。
   - 或直接从 CDN 引入：`<script src="https://unpkg.com/fortune-sheet/dist/fortune-sheet.min.js"></script>`。

2. **基本初始化**：
   在 HTML 中创建一个容器 div，例如 `<div id="fortune-sheet"></div>`。
   ```javascript
   import FortuneSheet from 'fortune-sheet';

   const options = {
     title: '我的表格',
     data: [{ name: 'Sheet1', celldata: [], merge: [], row: 100, column: 26 }]  // 初始数据
   };
   FortuneSheet.create(options, '#fortune-sheet');
   ```

3. **高级用法**：
   - **加载数据**：使用 `FortuneSheet.loadData(data)` 方法导入外部数据。
   - **事件监听**：监听编辑事件，如 `sheet.on('cellUpdate', callback)`。
   - **导出数据**：调用 `FortuneSheet.getData()` 获取表格数据，或 `exportSheet()` 导出为文件。
   - **集成插件**：在 options 中添加插件配置，例如图表插件。

详细文档和示例请参考 GitHub 仓库的 README 和 demo 文件。