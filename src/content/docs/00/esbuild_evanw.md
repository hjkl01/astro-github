---
title: esbuild
---

# esbuild

## 项目简介

esbuild 是一个极快的 JavaScript 打包器（bundler），专为现代 Web 开发设计。它旨在提供比现有构建工具快 10-100 倍的性能，同时保持易用性和现代化的功能。

## 主要功能

- **极高性能**：无需缓存即可实现极快构建速度
- **内置支持多种语言**：
  - JavaScript
  - CSS（包括 CSS Modules）
  - TypeScript
  - JSX/TSX
- **模块打包**：支持 ESM 和 CommonJS 模块
- **代码优化**：
  - Tree shaking（死代码消除）
  - 代码压缩（minification）
  - Source maps 生成
- **开发工具**：
  - 本地开发服务器
  - 监听模式（watch mode）
  - 插件系统
- **多语言 API**：提供 CLI、JavaScript 和 Go 语言的 API

## 基本用法

### 安装

```bash
npm install esbuild --save-dev
# 或
yarn add esbuild --dev
```

### 命令行使用

```bash
# 打包单个文件
esbuild input.js --outfile=output.js

# 打包并压缩
esbuild input.js --outfile=output.js --minify

# 开发模式（监听文件变化）
esbuild input.js --outfile=output.js --watch

# 启动本地服务器
esbuild input.js --serve --outfile=output.js
```

### JavaScript API 使用

```javascript
const esbuild = require('esbuild');

// 简单打包
await esbuild.build({
  entryPoints: ['app.js'],
  outfile: 'out.js',
});

// 开发模式
await esbuild.build({
  entryPoints: ['app.js'],
  outfile: 'out.js',
  watch: true,
});
```

### 配置文件示例

创建 `esbuild.config.js`：

```javascript
const esbuild = require('esbuild');

esbuild
  .build({
    entryPoints: ['src/index.js'],
    bundle: true,
    outfile: 'dist/bundle.js',
    minify: true,
    sourcemap: true,
    target: ['chrome58', 'firefox57', 'safari11'],
  })
  .catch(() => process.exit(1));
```

## 适用场景

- 前端项目打包
- 开发环境热重载
- 生产环境代码优化
- 库的构建和发布

更多详细信息请参考 [官方文档](https://esbuild.github.io/)。
