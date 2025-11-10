---
title: swc
---


# SWC（Speedy Web Compiler）项目

- **项目地址**: https://github.com/swc-project/swc

## 概述
SWC 是一个用 Rust 编写的高性能 JavaScript/TypeScript 编译器，旨在替代 Babel 提供更快的转译、打包和压缩性能。它支持现代前端生态的所有语法特性，并提供插件化体系结构，方便扩展。

## 主要特性
| 特性 | 说明 |
|------|------|
| **极速性能** | 编译速度比 Babel 快 10–30 倍（基于内部优化的缓存和并行执行）。 |
| **多语法支持** | JavaScript、TypeScript、JSX/TSX、Flow、ES Modules、CommonJS、AMD、SystemJS 等。 |
| **模块化打包** | 内置 twc‑bundler，支持多种输出模块（`es6`、`cjs`、`amd`、`umd`）。 |
| **压缩/混淆** | swc‑minify 提供无依赖的压缩功能，支持 treeshake 与 Uglify‑style 混淆。 |
| **插件化** | 通过 `@swc/core/lib` 或 `swc-plugin` 方式，可编写自定义转换器。 |
| **源码映射** | `--source-maps` 自动生成对应映射文件，便于调试。 |
| **CLI 与集成** | `swc-cli`（命令行工具）、`swc-loader`（Webpack）、`swc-node`（Node.js）、`swc-jest`（Jest）等。 |
| **生态兼容** | 可与 Next.js、Remix、Vue、React、Solid 等框架无缝协作。 |

## 上手指南

### 1. 安装

```bash
# 全局安装
npm i -g @swc/cli
# 或者项目局部安装
npm i @swc/cli --save-dev
```

### 2. 基本用法

#### CLI```bash
# 递归转译 src 目录至 dist
swc src -d dist

# 使用自定义配置文件
swc src -d dist --config-file swc.config.json
```

**swc.config.json 示例**

```json
{
  "jsc": {
    "parser": {
      "syntax": "typescript",
      "tsx": true,
      "decorators": true,
      "dynamicImport": true
    },
    "transform": {
      "decoratorMetadata": true,
      "decorators": { "decoratorVersion": "2021-09" }
    }
  },
  "module": {
    "type": "es6",
    "strict": true
  },
  "minify": true
}
```

#### 与 Webpack 结合

```js
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.(t|j)sx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'swc-loader',
          options: jsc: {
              parser: { syntax        }
      }
    ]
  }
};
```

#### 与 Node 直接运行

```bash
npx swc-node src/index.ts
```

## 常见应用场景

- **Next.js / Remix**：官方推荐使用 SWC 进行构建与热更新，显著提升启动时间。  
- **大规模项目迁移**：将 Babel 迁至 SWC，无需改动已有配置，享受更快编译。  
- **CI/CD 与生成型工具**：在 CI 流水线中使用 SWC 进行一次性编译与压缩，减少构建资源。  
- **Electron / React Native**：在打包前处理 TS/JS，生成为对应的模块贡献

- 采用 MIT 协议，开源社区活跃。  
- 文档与示例均在 GitHub 仓库 `docs/` 与 `examples/` 中提供。  
- 您可以通过 Pull Request、Issue 或社区讨论渠道参与改进。  

## 资源链接

- 官方网站 & 文档: https://swc.rs  
- GitHub 仓库: https://github.com/swc-project/swc  
- 测试场景示例: https://github.com/swc-project/swc/tree/main/examples  
- 在线 Playground: https://swc.rs/playground  

> 将上述内容保存为文件路径 `src/content/docs/00/swc_swc-project.md`。