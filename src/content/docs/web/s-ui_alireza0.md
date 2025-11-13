---
title: s-ui
---

# s-ui

**项目地址**  
<https://github.com/alireza0/s-ui>

## 简介

s-ui 是一套轻量级、模块化的 UI 组件库，旨在帮助开发者快速构建现代化 Web 界面。核心理念是「Simplicity（简单）」与「Scalability（可扩展）」，提供一系列可复用、可自定义的组件，兼容 Vue 3、React 以及 Svelte 等主流框架。

## 主要特性

- **按需加载**  
  所有组件支持 Tree Shaking，可通过 `import()` 按需引入，降低打包体积。
- **统一样式**  
  内置主题系统（暗黑/亮色），支持自定义 CSS 变量，主题切换一键完成。
- **响应式设计**  
  所有布局组件基于 Flexbox/Grid，兼容移动端与桌面端。
- **TypeScript 原生支持**  
  提供完整的类型声明，IDE 自动补全友好。
- **无依赖/轻量**  
  几乎不依赖第三方库（仅 Vue 3、React v18 或 Svelte 4），保持低内存占用。
- **组件丰富**  
  包含 Button、Input、Modal、Dropdown、Table、Chart、Tooltip、Alert 等常用组件；可根据需求自行扩展。

## 功能模块

| 组件 | 描述 |
|------|------|
| **Button** | 支持多种尺寸、形状、图标、加载状态、可禁用等。 |
| **Input** | 支持文字、密码、搜索、数字等多种输入方式，并可自定义验证规则。 |
| **Modal** | 可自定义标题、内容、确认/取消操作；支持 API 调用、portal 渲染。 |
| **Dropdown** | 下拉菜单与弹窗，支持多选、搜索等高级功能。 |
| **Table** | 支持分页、排序、搜索、隐藏列等功能，配合异步数据源使用。 |
| **Chart** | 基于 Chart.js 封装的通用图表组件，支持折线、柱状、饼图等。 |
| **Tooltip** | 自定义提示框，支持多方向定位与自适应。 |
| **Alert** | 弹出提示框，支持不同类型（success、error、warn、info）与自关闭。 |

## 用法

### 1. 安装

```bash
# npm
npm install @alireza0/s-ui

# yarn
yarn add @alireza0/s-ui

# pnpm
pnpm add @alireza0/s-ui
```

### 2. 在 Vue 3 中使用

```ts
// main.ts
import { createApp } from 'vue'
import App from './App.vue'
import { SUI } from '@alireza0/s-ui'

const app = createApp(App)

// 按需引入样式（全局表单样式）
import '@alireza0/s-ui/dist/style.css'

// 全局注册组件（可选，按需注册更节省 bundle）
app.use(SUI)

app.mount('#app')
```

**App.vue**

```vue
<template>
  <div>
    <!-- 按钮 -->
    <s-button type="primary" @click="openModal">打开 Modal</s-button>

    <!-- 模态框 -->
    <s-modal :visible="modalVisible" @close="modalVisible = false">
      <template #header>提示</template>
      <template #body>这是一条自定义内容。</template>
      <template #footer>
        <s-button @click="modalVisible = false">关闭</s-button>
      </template>
    </s-modal>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const modalVisible = ref(false)
function openModal() {
  modalVisible.value = true
}
</script>
```

### 3. 在 React 中使用

```tsx
import React, { useState } from 'react';
import { Button, Modal, useSUITheme } from '@ireza0/s-ui';
import '@alireza0/s-ui/dist/style.css';

export default function App() {
  const [visible, setVisible] = useState(false);
  const { theme, toggleTheme } = useSUITheme();

  return (
    <div style={{ padding: '20px' }}>
      <Button type="primary" onClick={() => setVisible(true)}>
        打开 Modal
      </Button>
      <Button onClick={toggleTheme}>
        切换主题 (当前: {theme})
      </Button>

      <Modal visible={visible} onClose={() => setVisible(false)}>
        <Modal.Header>提示</Modal.Header>
        <Modal.Body>这是一条自定义内容。</Modal.Body>
        <Modal.Footer>
          <Button onClick={() => setVisible(false)}>关闭</Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}
```

### 4. 在 Svelte 中使用

```svelte
<script>
  import { Button, Modal } from '@alireza0/s-ui  import '@alireza0/s-ui/dist/style.css';
  import { onMount } from 'svelte';
  let visible = false;
</script>

<Button type="primary" on:click={() => visible = true}>
  打开 Modal
</Button>

{#if visible}
  <Modal on:close={() => visible = false}>
    <ModalHeader>提示</ModalHeader>
    <ModalBody>这是一条自定义内容。</ModalBody>
    <ModalFooter>
      <Button on:click={() => visible = false}>关闭</Button>
    </ModalFooter>
  </Modal>
{/if}
```

## 贡献

项目欢迎 Issue 与 PR。若想贡献组件或改进，先 fork、create branch，提交符合 ESLint/Prettier 配置的代码，最后提交 Pull Request。

---
以上即为 **s-ui** 的主要特性、功能及使用方法。