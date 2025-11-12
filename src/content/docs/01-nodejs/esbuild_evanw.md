---
title: esbuild
---

## 项目简介

esbuild 是一个极快的 JavaScript 和 TypeScript 打包器，由 Evan Wallace 开发。它旨在提供比现有构建工具快 10-100 倍的性能，同时保持易用性。esbuild 支持多种现代 web 开发技术，并提供简洁的 API。

## 主要功能

- **极快速度**：无需缓存即可实现极高性能的打包。
- **内置支持**：原生支持 JavaScript、CSS、TypeScript 和 JSX。
- **模块打包**：支持 ESM 和 CommonJS 模块的打包。
- **CSS 处理**：包括 CSS 模块的打包和 @supports 规则。
- **优化功能**：树摇（tree shaking）、代码压缩（minification）和源码映射（source maps）。
- **开发工具**：提供本地服务器、监视模式和插件系统。
- **装饰器支持**：支持 JavaScript 装饰器提案和元数据。
- **对象 rest 和 spread**：支持对象 rest 和 spread 语法。
- **私有类字段**：支持私有类字段、方法和操作符。
- **异步 super**：支持异步 super 关键字使用。
- **资源管理**：支持 using 关键字进行资源管理。
- **导入属性**：支持 import attributes 和 glob 导入。
- **导出别名**：支持关键字作为导出别名。
- **顶部级 await**：支持顶部级 await 在 ECMAScript 模块中。

## 用法

### 安装

通过 npm 安装 esbuild：

```bash
npm install esbuild --save-dev
```

### 基本用法

#### CLI 使用

打包单个文件：

```bash
esbuild input.js --outfile=output.js
```

打包并压缩：

```bash
esbuild input.js --outfile=output.js --minify
```

监视模式（自动重新打包）：

```bash
esbuild input.js --outfile=output.js --watch
```

启动本地服务器：

```bash
esbuild --serve input.js
```

#### JavaScript API

```javascript
const esbuild = require('esbuild');

esbuild
  .build({
    entryPoints: ['input.js'],
    outfile: 'output.js',
    bundle: true,
    minify: true,
  })
  .catch(() => process.exit(1));
```

#### 转换代码

```javascript
esbuild.transform('let x = 1', { loader: 'js' }).then((result) => {
  console.log(result.code);
});
```

#### 构建选项

```javascript
esbuild
  .build({
    entryPoints: ['input.js'],
    bundle: true,
    metafile: true,
  })
  .then((result) => {
    console.log(result.metafile.outputs);
  });
```

更多详细信息，请参考 [官方文档](https://esbuild.github.io/api/) 和 [入门指南](https://esbuild.github.io/getting-started/)。
