
---
title: parcel
---

# Parcel 项目

## 项目地址
[https://github.com/parcel-bundler/parcel](https://github.com/parcel-bundler/parcel)

## 主要特性
Parcel 是一个零配置的 Web 应用打包工具，旨在简化前端开发流程。其核心特性包括：
- **零配置**：无需复杂的配置文件，开箱即用，支持多种文件类型和框架。
- **高速构建**：采用多进程并行处理和缓存机制，构建速度极快。
- **热重载（HMR）**：支持热模块替换，实现代码更改时的即时更新，提高开发效率。
- **自动代码分割**：根据依赖关系自动拆分代码，优化加载性能。
- **内置支持**：原生支持 JavaScript、TypeScript、CSS、Sass、图像、字体等多种资产类型，以及 React、Vue、Angular 等框架。
- **生产优化**：自动压缩、混淆代码，并生成 Source Maps 以便调试。
- **跨平台**：兼容 Windows、macOS 和 Linux 系统。

## 主要功能
Parcel 的功能覆盖前端开发的全生命周期：
- **开发服务器**：启动本地服务器，提供实时预览和热重载。
- **打包优化**：处理依赖、转译代码、注入 polyfills，并支持 Tree Shaking 去除未用代码。
- **资产处理**：自动处理静态资源，如图像优化、CSS 后缀处理和 PostCSS 集成。
- **环境支持**：内置 Babel 支持 ES6+ 语法，并兼容模块系统（CommonJS、ES Modules）。
- **插件扩展**：虽为零配置，但支持自定义插件以扩展功能，如自定义打包器或解析器。
- **诊断工具**：提供详细的错误报告和性能分析，帮助开发者快速定位问题。

## 用法
Parcel 的用法简单，只需 Node.js 环境（推荐 v14+）。以下是基本步骤：

### 安装
全局安装 Parcel：
```bash
npm install -g parcel
```

### 基本用法
1. **创建项目**：在项目根目录初始化（例如使用 `npm init`）。
2. **入口文件**：准备 HTML 入口文件（如 `index.html`），Parcel 会自动检测依赖。
3. **开发模式**：运行开发服务器：
   ```bash
   parcel index.html
   ```
   这将启动服务器，默认在 `http://localhost:1234` 上访问，支持热重载。
4. **生产构建**：生成优化后的生产文件：
   ```bash
   parcel build index.html
   ```
   输出目录默认为 `dist`，包含压缩的 JS、CSS 和资产文件。

### 配置（可选）
虽然零配置，但可通过 `.parcelrc` 文件自定义：
```json
{
  "extends": "@parcel/config-default",
  "parsers": {
    "**/*.jsx": ["babel"]
  }
}
```

### 示例项目结构
```
my-project/
├── index.html
├── src/
│   ├── index.js
│   └── style.css
└── package.json
```

更多详情请参考官方文档：https://parceljs.org/