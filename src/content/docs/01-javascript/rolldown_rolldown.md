---
title: Rolldown
---

# Rolldown

Rolldown 是一个用 Rust 编写的快速 JavaScript/TypeScript 打包器，旨在作为 Vite 的未来打包器。它提供与 Rollup 兼容的 API 和插件接口，但在范围上更类似于 esbuild。

## 功能特性

- **高性能**：使用 Rust 编写，提供快速的打包速度。
- **兼容性**：支持 Rollup 的配置选项和插件 API。
- **多平台支持**：提供多种 CPU 架构和操作系统的预构建二进制文件。
- **内置功能**：包括内置的 minification（仍在 alpha 阶段）。
- **模块类型**：支持 ESM、CJS 等模块格式。
- **插件系统**：兼容大多数 Rollup 插件。

## 安装

使用 npm、pnpm、yarn 或 bun 安装：

```bash
npm install -D rolldown
pnpm add -D rolldown
yarn add -D rolldown
bun add -D rolldown
```

## 使用方法

### CLI 使用

创建简单的打包：

```bash
rolldown src/main.js --file bundle.js
```

运行打包后的文件：

```bash
node bundle.js
```

### 配置文件

创建 `rolldown.config.js`：

```js
import { defineConfig } from 'rolldown';

export default defineConfig({
  input: 'src/main.js',
  output: {
    file: 'bundle.js',
  },
});
```

运行打包：

```bash
rolldown -c
```

### JavaScript API

```js
import { rolldown, build } from 'rolldown';

// 使用 rolldown API
const bundle = await rolldown({
  input: 'src/main.js',
});

await bundle.write({
  file: 'bundle.js',
});

// 或使用 build API
await build({
  input: 'src/main.js',
  output: {
    file: 'bundle.js',
  },
});
```

### 监听模式

```js
import { watch } from 'rolldown';

const watcher = watch({
  input: 'src/main.js',
  output: {
    file: 'bundle.js',
  },
});

watcher.on('event', (event) => {
  console.log('Build event:', event);
});
```

## 注意事项

Rolldown 目前处于 beta 阶段，虽然可以处理大多数生产用例，但仍可能存在 bug 和粗糙边缘。内置的 minification 功能仍在早期工作状态。

更多信息请参考 [官方文档](https://rolldown.rs)。
