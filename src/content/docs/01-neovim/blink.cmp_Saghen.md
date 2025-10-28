
---
title: blink.cmp
---

# blink.cmp

**项目地址**: <https://github.com/Saghen/blink.cmp>

---

## 主要特性

- **轻量级**：仅包含核心 UI 组件，体积小、加载快。  
- **组件化**：提供一套可复用的 UI 组件（按钮、输入框、弹框、卡片等），便于快速构建页面。  
- **兼容性**：支持 Vue3、React 和原生 JS 三种使用方式，适配大多数现代前端框架。  
- **主题定制**：通过 CSS 变量或配置文件即可自定义主题色、字体、间距等。  
- **无样式冲突**：所有组件采用 CSS Modules / Shadow DOM（视使用方式而定），避免全局样式污染。  

---

## 功能

| 组件 | 说明 |
|------|------|
| `Button` | 支持多种样式（primary、secondary、danger 等）与尺寸（small、medium、large）。 |
| `Input` | 支持文字、密码、搜索、数字等类型，并可配置校验规则。 |
| `Modal` | 可嵌套内容、可拖拽、支持响应式全屏模式。 |
| `Card` | 带有标题、内容、操作区的卡片布局，支持阴影与圆角。 |
| `Accordion` | 允许展开/收起子内容，支持多选与单选两种模式。 |
| `Dropdown` | 下拉选择框，支持搜索、懒加载与多选。 |
| `Alert` | 通知提示，支持多种类型（success、warning、error、info）。 |

---

## 用法

### 1. 安装

```bash
# npm
npm install @saghen/blink.cmp

# yarn
yarn add @saghen/blink.cmp
```

### 2. 在 Vue3 项目中使用

```js
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import BlinkCmp from '@saghen/blink.cmp'
import '@saghen/blink.cmp/dist/blink.cmp.css'

const app = createApp(App)
app.use(BlinkCmp)       // 全局注册
app.mount('#app')
```

```vue
<!-- 示例组件 -->
<template>
  <bk-button type="primary" @click="handleClick">点击我</bk-button>
</template>

<script setup>
const handleClick = () => console.log('按钮被点击')
</script>
```

### 3. 在 React 项目中使用

```js
// index.js
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
import { BlinkProvider } from '@saghen/blink.cmp'
import '@saghen/blink.cmp/dist/blink.cmp.css'

ReactDOM.render(
  <BlinkProvider>
    <App />
  </BlinkProvider>,
  document.getElementById('root')
)
```

```jsx
// 示例组件
import { Button } from '@saghen/blink.cmp'

function Demo() {
  return <Button type="primary" onClick={() => console.log('按钮被点击')}>点击我</Button>
}

export default Demo
```

### 4. 原生 JS（无框架）使用

```html
<link rel="stylesheet" href="node_modules/@saghen/blink.cmp/dist/blink.cmp.css">
<script type="module">
  import { Button } from '@saghen/blink.cmp'
  const btn = Button({ type: 'primary', onClick: () => console.log('按钮被点击') })
  document.body.appendChild(btn)
</script>
```

---

## 主题自定义

```scss
/* 在项目的 SCSS 中覆盖默认变量 */
$bk-bg-color: #f5f5f5
$bk-primary-color: #3a8ee6
@import '~@saghen/blink.cmp/scss/main.scss'
```

或者在使用时通过 `BlinkProvider` 的 `theme` 属性传递对象：

```jsx
<BlinkProvider theme={{ primaryColor: '#3a8ee6', backgroundColor: '#f5f5f5' }}>
  <App />
</BlinkProvider>
```

---

## 贡献

1. Fork 本仓库。  
2. 创建功能分支（`feature/xxx`）。  
3. 提交代码并推送。  
4. 发送 Pull Request，附上详细说明。  

---

**更多信息**请查看官方文档或直接访问 GitHub 仓库。