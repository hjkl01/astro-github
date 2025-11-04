
---
title: IronCalc
---


# IronCalc

> **Github** – https://github.com/ironcalc/IronCalc

IronCalc 是一个基于 JavaScript 的纯前端电子表格实现，旨在为 Web 应用提供轻量、可嵌入的表格功能。它兼容 Excel、Google Sheets 等常见电子表格的多项核心特性，同时保持模块化、可扩展的设计。

## 主要特性

| 特性 | 说明 |
|------|------|
| **支持公式** | 通过 `=SUM(A1:B2)`、`=IF(A1>10, "大", "小")` 等 Excel 语法编写公式。 |
| **多工作表** | 通过 `Sheet1`、`Sheet2` … 的方式，在同一文件中使用多张工作表。 |
| **单元格格式化** | 数字、日期、文本、货币等多种格式，支持条件格式（如自定义颜色）。 |
| **自定义函数** | 可以在 JavaScript 侧注册 `myFunc(x, y)` 并在表格中 `=MYFUNC(A1, B1)` 调用。 |
| **交互式编辑** | 支持单元格双击编辑、键盘快捷键、粘贴/拖拽填充等体验。 |
| **强类型和安全** | 采用 TypeScript 开发，出错信息友好，避免传统脚本注入安全风险。 |
| **可嵌入** | 通过 `IronCalcViewer`、`IronCalcEditor` 组件将表格引入现有页面。 |
| **开放式 API** | 通过 `sheet.getCell`, `sheet.setCell`, `sheet.getRangeValue` 等方法操作表格。 |
| **插件化** | 提供 API 供社区开发插件，例如导入导出、图表、数据校验等。 |
| **移动友好** | 响应式布局，触摸屏支持，适配不同尺寸设备。 |

## 常用 API

```ts
import { IronCalc, IronCalcSheet } from 'ironcalc';

// 创建 Excel 兼容实例
const editor = new IronCalc({ editor: 'myEditor' });

// 添加工作表
const sheet: IronCalcSheet = editor.addSheet('Sheet1');

// 写入单元格
sheet.getCell('A1').setValue(10);

// 设公式
sheet.getCell('B1').setFormula('=SUM(A1:A10)');

// 读取值
const val = sheet.getCell('B1').getValue();

// 注册自定义函数
editor.addFunction('MYFUNC', (x: number, y: number) => x + y);

// 监听单元格变化
sheet.on('change', (cell) => {
   console.log(`Cell ${cell.id} changed to ${cell.getValue()}`);
});
```

## 用法示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>IronCalc Demo</title>
  <link rel="stylesheet" href="https://unpkg.com/ironcalc/dist/ironcalc.min.css" />
</head>
<body>
  <div id="calc"></div>

  <script type="module">
    import { IronCalcEditor } from 'https://unpkg.com/ironcalc/dist/ironcalc.esm.js';

    const editor = new IronCalcEditor('calc');
    const sheet = editor.addSheet('Sheet1');

    // 添加几行测试数据
    forValue(i);
    }

    // 计算合计
    sheet.getCell('B1').setFormula('=SUM(A1:A5)');
  </script>
</body>
</html>
```

## 进一步阅读

- 文档与示例：`https://github.com/ironcalc/IronCalc`  
- 插件开发与贡献指南：请参阅仓库 `CONTRIBUTING.md` 与 `plugins/` 目录。  

```markdown
# End of file
