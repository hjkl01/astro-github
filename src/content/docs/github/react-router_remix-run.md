---
title: react-router
---

# React Router

React Router 是由 Remix 团队开发的用于 React 应用的声明式路由库。它提供了一种灵活的方式来管理单页应用（SPA）的导航和 URL 路由，支持从 React 18 到 React 19 的桥接。

## 主要功能

- **声明式路由**：通过组件化的方式定义路由规则，使路由逻辑更加直观和易于维护。
- **多策略支持**：可以作为完整的 React 框架使用（最大化模式），或作为轻量级库集成到现有架构中（最小化模式）。
- **服务器端渲染（SSR）**：支持 SSR 和客户端渲染（CSR），适用于现代 React 应用。
- **嵌套路由**：支持路由嵌套，允许构建复杂的页面结构。
- **代码分割**：与 React 的懒加载结合，支持按需加载组件，提高应用性能。
- **类型安全**：提供 TypeScript 支持，确保路由参数和状态的类型安全。

## 安装和使用

### 安装

使用 npm 或 yarn 安装 React Router：

```bash
npm install react-router-dom
```

或

```bash
yarn add react-router-dom
```

### 基本用法

1. **设置路由器**：在应用的根组件中包装 `BrowserRouter`（用于客户端路由）或 `HashRouter`（用于哈希路由）。

```jsx
import { BrowserRouter } from 'react-router-dom';

function App() {
  return <BrowserRouter>{/* 应用内容 */}</BrowserRouter>;
}
```

2. **定义路由**：使用 `Routes` 和 `Route` 组件定义路由规则。

```jsx
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import About from './About';
import Contact from './Contact';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}
```

3. **导航链接**：使用 `Link` 或 `NavLink` 组件创建导航链接。

```jsx
import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <nav>
      <Link to="/">首页</Link>
      <Link to="/about">关于</Link>
      <Link to="/contact">联系我们</Link>
    </nav>
  );
}
```

4. **动态路由和参数**：使用路径参数传递数据。

```jsx
// 定义带参数的路由
<Route path="/user/:id" element={<User />} />;

// 在组件中使用 useParams 获取参数
import { useParams } from 'react-router-dom';

function User() {
  const { id } = useParams();
  return <div>用户 ID: {id}</div>;
}
```

## 高级用法

- **嵌套路由**：在父路由中定义子路由，实现页面布局。
- **路由守卫**：使用 `Navigate` 组件进行重定向，或自定义钩子检查权限。
- **数据加载**：结合 React Router 的数据 API（如 `loader` 和 `action`）进行服务端数据获取。
- **错误处理**：使用 `ErrorBoundary` 处理路由错误。

React Router 提供了丰富的 API 和钩子，如 `useNavigate`、`useLocation` 等，帮助开发者构建复杂的路由逻辑。更多详细信息请参考 [官方文档](https://reactrouter.com)。
