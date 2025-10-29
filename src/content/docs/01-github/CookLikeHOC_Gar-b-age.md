
---
title: CookLikeHOC
---


# CookLikeHOC

**项目地址**  
[https://github.com/Gar-b-age/CookLikeHOC](https://github.com/Gar-b-age/CookLikeHOC)

---

## 简介  
CookLikeHOC 是一个专为 React 设计的 Higher‑Order Component（HOC）工具库，帮助开发者快速创建、组合与复用 HOC。它提供了一套通用的 HOC 工具，支持数据获取、错误边界、状态注入等常见需求，旨在降低重复代码、提升开发效率。

---

## 核心特性

| 特性 | 说明 |
|------|------|
| **组合 HOC** | 通过 `composeHOCs` 将多个 HOC 合并为一个 HOC，支持任意深度组合。 |
| **数据加载** | `withAsyncData` 接收 API 函数，自动管理 loading / error / 成功状态。 |
| **错误边界** | `withErrorBoundary` 自动捕获子组件报错并展示可定制的错误 UI。 |
| **可注入状态** | `withStore` 允许注入全局或本地 store，支持上下文或 Redux。 |
| **无副作用** | 所有 HOC 基于纯函数实现，易于测试与维护。 |
| **TypeScript 支持** | 完整类型定义，保证类型安全。 |

---

## 提供的 HOC 工具

| 工具 | 用法（示例） |
|------|--------------|
| `composeHOCs(...hocs)` | `const Enhanced = composeHOCs(withErrorBoundary, withAsyncData(fetchUser))(BaseComponent)` |
| `withAsyncData(fetchFn)` | `const withUser = withAsyncData(() => api.getUser()); const UserProfile = withUser(Profile);` |
| `withErrorBoundary(options?)` | `const Safe = withErrorBoundary({ fallback: <ErrorView /> })(Component);` |
| `withStore(mapStateToProps)` | `const Connected = withStore(state => ({items: state.items}))(List);` |
| `useCook(...hocs)` | `const Component = useCook(withAsyncData(fetchFn), withStore(mapState));` |

（更多工具请参阅源码或官方文档，示例可在 [docs] 目录中找到）

---

## 安装

```bash
# npm
npm install cooklikehoc --save

# yarn
yarn add cooklikehoc
```

---

## 使用方法

```tsx
import React from 'react';
import {
  composeHOCs,
  withAsyncData,
  withErrorBoundary,
} from 'cooklikehoc';

// 基础组件
const UserProfile: React.FC<{ user: User }> = ({ user }) => (
  <div>
    <h2>{user.name}</h2>
    <p>{user.email}</p>
  </div>
);

// 组合 HOC
const getUser = () => fetch('/api/user').then(r => r.json());
const EnhancedProfile = composeHOCs(
  withErrorBoundary({ fallback: <div>加载失败</div> }),
  withAsyncData(getUser)
)(UserProfile);

// 渲染
const App = () => <EnhancedProfile />;
```

---

## 贡献

1. Fork 该仓库。  
2. 创建特性分支：`git checkout -b feature/new-cook`.  
3. 编写代码并通过测试。  
4. 提交 PR 并阐明改动动机。

有任何问题，可以提交 Issue 或参与讨论。

---