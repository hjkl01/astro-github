
---
title: umi
---

# Umi 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/umijs/umi)

## 主要特性
Umi 是一个企业级的前端应用框架，基于 React 构建，强调可插拔、低门槛和高扩展性。其核心特性包括：
- **插件系统**：支持丰富的插件生态，可轻松扩展功能，如路由、布局、数据流等。
- **零配置启动**：默认提供开箱即用的配置，支持快速开发和构建。
- **路由支持**：内置 React Router，支持文件路由、嵌套路由和权限路由。
- **构建优化**：集成 Vite 或 Webpack，支持热重载、代码分割和 Tree Shaking。
- **国际化与主题**：内置 i18n 支持和 Ant Design 主题配置。
- **微前端**：兼容 Qiankun 等微前端方案，实现应用拆分和联邦。
- **TypeScript 支持**：原生支持 TS，提升开发体验和类型安全。

## 主要功能
Umi 提供了一站式的前端解决方案，涵盖开发、构建和部署的全流程：
- **开发模式**：快速启动开发服务器，支持 HMR（热模块替换）和错误边界。
- **路由与布局**：通过约定式路由（pages 目录）自动生成路由，支持布局组件和动态路由。
- **数据管理**：集成 Umi Request（基于 Axios 的请求库）和插件化的数据流管理。
- **构建与部署**：支持多环境配置、SSR（服务端渲染）和 PWA（渐进式 Web 应用）。
- **测试与调试**：内置 Jest 测试支持和 DevTools 调试工具。
- **生态集成**：无缝对接 Ant Design、Dva（状态管理）和 Umi Blocks（组件库）。

## 用法指南
### 安装与初始化
1. 确保 Node.js 版本 ≥ 14。
2. 使用 npx 创建项目：
   ```
   npx create-umi@latest my-app
   cd my-app
   ```
3. 安装依赖：
   ```
   yarn install
   # 或 npm install
   ```

### 开发启动
- 运行开发服务器：
  ```
  yarn dev
  # 或 npm run dev
  ```
- 项目默认在 http://localhost:8000 启动。

### 构建与部署
- 生产构建：
  ```
  yarn build
  # 或 npm run build
  ```
- 预览构建结果：
  ```
  yarn start
  # 或 npm run start
  ```

### 自定义配置
- 编辑 `config/config.ts` 文件进行配置，例如添加插件：
  ```typescript
  import { defineConfig } from 'umi';

  export default defineConfig({
    plugins: ['@umijs/preset-built-in'],
    routes: [
      { path: '/', component: '@/pages/index' },
    ],
  });
  ```
- 更多用法详见官方文档：https://umijs.org/docs