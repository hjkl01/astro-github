
---
title: heyui
---

# HeyUI 项目介绍

## 项目地址
[HeyUI GitHub 项目](https://github.com/heyui/heyui)

## 主要特性
HeyUI 是一个基于 Vue 3 和 TypeScript 的现代 UI 组件库，专为前端开发者设计。它强调简洁、灵活和高效，提供了一系列响应式组件，支持主题定制和国际化。主要特性包括：
- **组件丰富**：内置 50+ 高质量组件，如按钮、表单、表格、模态框、图表等，覆盖常见 UI 需求。
- **Vue 3 兼容**：充分利用 Composition API，支持 Vue 3 的所有特性，确保高性能和可维护性。
- **TypeScript 支持**：全量 TypeScript 编写，提供完整的类型定义，提升开发体验和代码可靠性。
- **主题系统**：内置 CSS-in-JS 主题引擎，支持暗黑模式和自定义主题，易于品牌适配。
- **无障碍访问**：所有组件遵循 WCAG 标准，支持 ARIA 属性和键盘导航。
- **Tree Shaking**：支持按需加载，减少打包体积，提高应用加载速度。
- **国际化**：内置 i18n 支持，轻松切换多语言。

## 主要功能
HeyUI 的核心功能聚焦于构建现代 Web 应用界面，提供从基础到高级的 UI 解决方案：
- **布局与导航**：Grid 布局系统、侧边栏、面包屑导航，帮助构建复杂页面结构。
- **表单处理**：表单组件集，包括输入框、选择器、验证器，支持实时校验和动态表单。
- **数据展示**：表格、卡片、列表，支持分页、排序、过滤和虚拟滚动，适用于大数据场景。
- **交互组件**：弹出层、提示、加载动画、拖拽功能，提升用户交互体验。
- **可视化**：集成 ECharts 等库，提供图表组件，支持数据驱动的动态渲染。
- **工具函数**：内置实用工具，如日期处理、动画库和状态管理钩子，简化开发流程。

## 用法指南
### 安装
使用 npm 或 yarn 安装：
```bash
npm install heyui
# 或
yarn add heyui
```

### 快速开始
1. 在 Vue 3 项目中引入：
   ```javascript
   // main.js
   import { createApp } from 'vue'
   import HeyUI from 'heyui'
   import 'heyui/lib/theme/index.css'  // 引入默认主题

   const app = createApp(App)
   app.use(HeyUI)
   app.mount('#app')
   ```

2. 使用组件：
   ```vue
   <template>
     <h-button type="primary">点击我</h-button>
   </template>

   <script setup>
   import { HButton } from 'heyui'
   </script>
   ```

### 高级用法
- **按需引入**（推荐，使用 unplugin-vue-components）：
  配置 Vite 或 Webpack 插件，实现自动导入组件，避免全量加载。
- **自定义主题**：
  通过 `HeyUI.config({ theme: { ... } })` 修改变量，如颜色、字体等。
- **文档与示例**：
  项目提供在线文档和示例代码，访问 GitHub 仓库的 docs 文件夹或部署的 demo 站点，快速上手组件 API 和最佳实践。
- **构建与部署**：
  支持 SSR（如 Nuxt.js）和静态生成，确保跨环境兼容。

HeyUI 适合中大型 Vue 项目，社区活跃，持续更新中。更多细节请参考官方文档。