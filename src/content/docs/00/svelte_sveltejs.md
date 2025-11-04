
---
title: svelte
---


# Svelte (sveltejs/svelte)

**项目地址**  
[https://github.com/sveltejs/svelte](https://github.com/sveltejs/svelte)

## 主要特性
- **零运行时开销**：编译阶段将组件转化为高效 JavaScript，运行时无框架负担。  
- **响应式语法**：使用 `$:` 简单声明响应式表达式，自动跟踪依赖。  
- **局部状态与全局 Store**：`writable`, `readable` 等 API 轻松创建共享状态。  
- **自动化 DOM 更新**：仅更新受数据变化影响的最小 DOM 节点。  
- **组件化开发**：`.svelte` 单文件组件，包含 `<script>`, `<style>`, `<template>` 三部分。  
- **内置动画与过渡**：`fade`, `slide`, `fly` 等 API 简化动画实现。  
- **丰富的生态插件**：支持 TypeScript、SCSS、PostCSS、Vite、Rollup 等构建工具。  

## 功能概览
| 功能 | 说明 |
|------|------|
| **编译器** | 将 `.svelte` 文件编译为原生 JavaScript。 |
| **生命周期钩子** | `onMount`, `onDestroy`, `beforeUpdate`, `afterUpdate` 等。 |
| **事件处理** | `on:eventName` 与 `event.stopPropagation()`、`event.preventDefault()`。 |
| **绑定** | `bind:value`, `bind:checked`, `bind:this` 等。 |
| **条件渲染** | `{#if condition}`、`{#else}`、`{:else if}`。 |
| **列表渲染** | `{#each items as item, index (item.id)}`。 |
| **错误边界** | `<ErrorBoundary>` 用于捕获渲染错误。 |
| **SSR 与 SvelteKit** | 支持服务器端渲染与完整的框架 SvelteKit。 |

## 用法示例

### 1. 安装
```bash
npm init svelte@next my-app
cd my-app
npm install
npm run dev
```

### 2. 创建组件 (`src/App.svelte`)
```svelte
<script>
  import { onMount } from 'svelte';
  import Counter from './Counter.svelte';

  let name = 'Svelte';

  onMount(() => {
    console.log('App mounted');
  });
</script>

<main>
  <h1>Hello {name}!</h1>
  <Counter />
</main>

<style>
  main { text-align: center; }
</style>
```

### 3. Counter 组件 (`src/Counter.svelte`)
```svelte
<script>
  let count = 0;
  function increment() {
    count += 1;
  }
</script>

<button on:click={increment}>
  Count: {count}
</button>

<style>
  button { font-size: 1.5rem; }
</style>
```

### 4. 运行
```bash
npm run dev
```
浏览器访问 `http://localhost:5173` 即可看到效果。

> 以上示例基于 Vite + SvelteKit 项目结构，亦可直接使用 Rollup 或 Webpack 进行构建。  
> 进一步配置可参考官方文档：<https://svelte.dev/docs>  

---  
**文件路径**: `src/content/docs/00/svelte_sveltejs.md`
