---
title: react-router
---

# React Router

## 项目简介

React Router 是由 Remix 团队开发的 React 路由库，提供声明式的路由解决方案。它支持从 React 18 到 React 19 的桥接，可以最大化用作完整的 React 框架，也可以最小化用作独立的库。

## 主要功能

- **声明式路由**：通过组件化的方式定义路由规则
- **多策略路由**：支持不同的路由策略和架构
- **框架模式**：提供完整的框架功能，包括开发工具、服务器端渲染等
- **库模式**：作为轻量级库使用，适合自定义架构
- **React 版本兼容**：桥接 React 18 到 React 19

## 核心包

- `react-router`：核心路由库
- `@react-router/dev`：开发工具
- `@react-router/node`：Node.js 环境支持
- `@react-router/cloudflare`：Cloudflare 环境支持
- `@react-router/serve`：服务器工具
- `@react-router/fs-routes`：文件系统路由

## 基本用法

### 安装

```bash
npm install react-router-dom
```

### 框架模式使用

```jsx
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
  },
  {
    path: '/about',
    element: <About />,
  },
]);

function App() {
  return <RouterProvider router={router} />;
}
```

### 库模式使用

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}
```

## 升级指南

- [从 v6 升级](https://reactrouter.com/upgrading/v6)
- [从 Remix 升级](https://reactrouter.com/upgrading/remix)

## 文档和资源

- [官方文档](https://reactrouter.com)
- [GitHub 仓库](https://github.com/remix-run/react-router)
- [变更日志](https://github.com/remix-run/react-router/blob/main/CHANGELOG.md)
