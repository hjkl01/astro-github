---
title: ViewUI
---

# ViewUI 项目

## 项目地址
https://github.com/view-design/ViewUI

## 主要特性
ViewUI 是一个基于 Vue.js 的高性能 UI 组件库，专为现代 Web 应用设计。它提供了丰富的组件和工具，支持响应式布局、国际化（i18n）和主题定制。主要特性包括：
- **高性能与兼容性**：支持 Vue 2.x 和 Vue 3.x，组件优化良好，适用于各种浏览器。
- **丰富的组件库**：包含按钮、表单、表格、模态框、导航等 70+ 个常用 UI 组件。
- **主题定制**：内置主题系统，支持 Less 变量自定义，易于品牌化。
- **国际化支持**：内置多语言支持，便于全球应用开发。
- **响应式设计**：组件自适应不同设备屏幕大小。
- **无障碍访问**：遵循 WAI-ARIA 标准，提升可访问性。

## 主要功能
ViewUI 的核心功能围绕 UI 组件和工具展开，帮助开发者快速构建美观、交互丰富的界面：
- **基础组件**：如 Button、Icon、Input、Select 等，用于构建基本交互元素。
- **布局与导航**：Grid、Layout、Menu、Tabs 等，支持复杂页面结构。
- **数据展示**：Table、Tree、Carousel 等，用于高效呈现数据。
- **表单与交互**：Form、DatePicker、Upload、Modal 等，提供用户输入和反馈机制。
- **高级功能**：如 Poptip（提示框）、Spin（加载动画）和 Affix（固定定位），增强用户体验。
- **工具函数**：内置一些实用工具，如日期处理和动画效果。

## 用法
### 安装
使用 npm 或 yarn 安装：
```
npm install view-design --save
```
或
```
yarn add view-design
```

### 引入与使用（Vue 2.x 示例）
在 main.js 中全局引入：
```javascript
import Vue from 'vue'
import ViewUI from 'view-design'
import 'view-design/dist/styles/iview.css'
import App from './App.vue'

Vue.use(ViewUI)

new Vue({
  render: h => h(App)
}).$mount('#app')
```

组件使用示例（Button）：
```vue
<template>
  <div>
    <Button type="primary">Primary Button</Button>
  </div>
</template>

<script>
export default {
  name: 'Example'
}
</script>
```

### 引入与使用（Vue 3.x 示例）
ViewUI 6+ 支持 Vue 3：
```javascript
import { createApp } from 'vue'
import ViewUIPlus from 'view-ui-plus'
import 'view-ui-plus/dist/styles/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(ViewUIPlus)
app.mount('#app')
```

### 按需引入（推荐优化打包大小）
使用 babel-plugin-import：
```bash
npm install babel-plugin-import --save-dev
```

在 .babelrc 中配置：
```json
{
  "plugins": [["import", {"libraryName": "view-design", "libraryDirectory": "src/components"}]]
}
```

然后在组件中导入：
```javascript
import { Button } from 'view-design'
```

### 自定义主题
通过修改 Less 变量：
```less
// theme.less
@import '~view-design/src/styles/index.less';
@primary-color: #1890ff; // 自定义主色
```

在 main.js 中引入：
```javascript
import './theme.less'
```

更多用法详见官方文档：https://www.viewui.plus/