
---
title: Luckysheet
---


# Luckysheet

> 项目地址: https://github.com/dream-num/Luckysheet

---

## 主要特性

- **网页端电子表格**：纯前端实现，支持在浏览器中直接打开、编辑和保存表格。
- **完整公式引擎**：内置功能强大的公式系统，支持常用函数（SUM、IF、VLOOKUP 等）以及自定义函数。
- **多种视图**：支持普通表格、图表视图、SQL 查询视图，用户可以将表格数据导出为 csv、xlsx、xls 等多种格式。
- **协作与数据同步**：通过 WebSocket 与后端同步数据，可实现多人协作编辑。
- **插件生态**：支持插件机制，开发者可以按需扩展功能。
- **可视化渲染**：表格、图表、树形结构等多种可视化组件，满足数据可视化需求。

---

## 主要功能

| 功能 | 描述 |
|------|------|
| **单元格编辑** | 支持文本、数值、日期、布尔值等数据类型，支持复制粘贴、自动填充等操作。 |
| **公式运算** | 内置 300+ 函数，支持自定义函数，可在单元格内直接输入公式。 |
| **图表插件** | 包括柱状图、折线图、饼图、散点图等，支持在线调节样式。 |
| **筛选与排序** | 可按列进行多条件筛选、升序/降序排序。 |
| **数据关联** | 支持多表关联查询，可通过 SQL 语句进行交叉查询。 |
| **导入/导出** | 支持 csv、xlsx、xls 等文件的导入导出，支持自动拆分工作表。 |
| **权限管理** | 支持读写权限控制，可为工作簿、工作表或单元格设置不同权限。 |
| **插件系统** | 开放插件 API，第三方可实现自定义拡展。 |

---

## 快速使用

### 1. 安装

```bash
# 克隆仓库
git clone https://github.com/dream-num/Luckysheet.git
cd Luckysheet

# 安装依赖
npm install
```

### 2. 启动

```bash
# 本地开发模式
npm run dev
```

默认会在 `http://localhost:5173` 打开 Luckysheet 页面。

### 3. 打开工作簿

```javascript
// 在 JS 代码中初始化 LuckySheet
const luckysheet = LuShare.setUp({
  container: "luckysheet",          // 在页面中定义 id 为 luckysheet 的容器
  lang: "zh-CN",                    // 语言
  sheetData: [],                    // 初始工作簿数据
});
```

### 4. 读取/写入数据

```javascript
// 获取当前工作簿
const currentData = luckysheet.getAllSheet() ;

// 写入单元格
luckysheet.setCellValue({
  r: 0,        // 行
  c: 0,        // 列
  v: 123,      // 值
  i: "",       // 内部值
});
```

### 5. 导入/导出文件

```javascript
// 导出为xlsx
luckysheet.exportExcel({
  filename: "demo.xlsx",
  exportmode: "xlsx"
});
```

### 6. 添加公式

```excel
=C1+D1   // 在单元格中直接输入等号开头的公式即可
```

### 7. 开发插件

```javascript
// 在 plugins 目录下创建插件
class MyPlugin {
  constructor() {
    this.id = "myPlugin";
    this.name = "MyPlugin";
  }
  onCreate() {
    // 插件初始化逻辑
  }
}
export default MyPlugin;
```

然后在主入口引入：

```javascript
import MyPlugin from './plugins/MyPlugin';
luckysheet.addPlugin(new MyPlugin());
```

---

## 文档与社区

- 文档与示例：`https://doc.dream-num.com/luckysheet`
- 社区讨论：`https://github.com/dream-num/Luckysheet/discussions`
- 项目地址（源码）：[GitHub](https://github.com/dream-num/Luckysheet)

> 以上内容可直接粘贴到 `src/content/docs/00/Luckysheet_dream-num.md`。祝你使用愉快！