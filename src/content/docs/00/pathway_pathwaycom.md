
---
title: pathway
---


# Pathway

项目地址: <https://github.com/pathwaycom/pathway>

## 概述

Pathway 是一款轻量级前端 UI 框架，提供可复用、响应式且可访问的组件。它支持自定义主题、设计系统集成，并可与 React、Vue、Svelte 等主流框架无缝配合。

## 主要特性

- **组件化**：含 Button、Input、Modal、Form 等高质量通用组件。
- **主题与设计系统**：基于 CSS 变量/SCSS 配置，支持多主题切换与自定义色彩／间距。
- **响应式 & 可访问性**：WAI‑ARIA 标准，键盘导航、屏幕阅读器友好。
- **自定义样式**：提供 Tailwind‑style 工具类，支持深度自定义。
- **CLI 与插件**：`pathway-cli` 用于生成样式、打包、测试以及与 Figma/Sketch 的集成。

## 安装

```bash
npm install @pathwaycom/pathway
# 或
yarn add @pathwaycom/pathway
```

## 快速使用

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>Pathway Demo</title>
  <link rel="stylesheet" href="node_modules/@pathwaycom/pathway/dist/pathway.css">
</head>
<body>
  <button class="pathway-btn pathway-primary">点击我</button>
  <script src="node_modules/@pathwaycom/pathway/dist/pathway.js"></script>
</body>
</html>
```

React 示例：

```jsx
import { Button } from '@pathwaycom/pathway/react';

export default function App() {
  return <Button type="primary">点击我</Button>;
}
```

## 配置主题

`src/theme.js`：

```js
import { createTheme } from '@pathwaycom/pathway/theme';

export const theme = createTheme({
  colors: {
    primary: '#4f46e5',
    secondary: '#6b7280',
  },
  spacing: {
    base: '8px',
    small: '4px',
    large: '16px',
  },
});
```

主题注入：

```jsx
import { ThemeProvider } from '@pathwaycom/pathway/react';
import { theme } from './theme';

export default function Root({ children }) {
  return <ThemeProvider theme={theme}>{children}</ThemeProvider>;
}
```

## 文档

- 官方文档: <https://pathwaycom.github.io/pathway>
- 示例与演示: <https://codesandbox.io/embed/pathway-demo>
- 贡献指南: `CONTRIBUTING.md`

``` 
（文件路径: src/content/docs/00/pathway_pathwaycom.md）
