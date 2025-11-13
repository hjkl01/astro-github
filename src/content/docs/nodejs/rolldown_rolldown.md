---
title: rolldown
---

## 功能介绍

Rolldown 是一个用 Rust 编写的快速 JavaScript/TypeScript 打包器，旨在作为 Vite 的未来打包器。它提供了 Rollup 兼容的 API 和插件接口，但在范围上更类似于 esbuild。

### 主要功能

- **高性能**：使用 Rust 编写，提供比传统 JavaScript 打包器更快的构建速度
- **兼容性**：支持 Rollup 的 API 和插件接口，便于迁移现有项目
- **现代化**：支持 JavaScript 和 TypeScript，内置压缩功能（目前处于 alpha 状态）
- **跨平台**：支持多种操作系统和架构，包括 macOS、Linux、Windows 和 WebAssembly

### 技术特点

- 基于 Rust 实现的核心打包逻辑
- 使用 oxc 作为底层解析器、解析器和源码映射支持
- 通过 napi-rs 提供 Node.js 插件支持
- 支持多种输出格式和优化选项

## 用法

### 安装

通过 npm 安装 Rolldown：

```bash
npm install rolldown
```

或者使用其他包管理器：

```bash
yarn add rolldown
pnpm add rolldown
```

### 基本用法

Rolldown 的 API 与 Rollup 高度兼容。以下是一个简单的使用示例：

```javascript
import { rolldown } from 'rolldown';

const bundle = await rolldown({
  input: 'src/main.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm',
  },
});

await bundle.write();
```

### 配置选项

Rolldown 支持丰富的配置选项，包括：

- **输入配置**：指定入口文件
- **输出配置**：定义输出格式、文件名等
- **插件系统**：支持自定义插件扩展功能
- **优化选项**：代码分割、压缩等

### 插件支持

Rolldown 兼容大多数 Rollup 插件，同时也支持专门为 Rolldown 设计的插件。

### 注意事项

- Rolldown 目前处于 beta 阶段，可能存在一些 bug 和不完善的地方
- 内置压缩功能仍处于 alpha 状态，不建议在生产环境中使用
- 对于复杂项目，建议先在测试环境中验证兼容性

更多详细信息请参考官方文档：[rolldown.rs](https://rolldown.rs)
