
---
title: react
---


# React (来自 Facebook)

**项目地址**：<https://github.com/facebook/react>

## 主要特性

| 特性 | 说明 |
|-----|------|
| **组件化** | 通过可重用的 `Component`（函数式和类式）构建 UI。 |
| **JSX** | 让 JavaScript 与声明式 UI 语法相融合，简化 DOM 操作。 |
| **虚拟 DOM** | 高效 diff 计算，最小化真实 DOM 操作，提升性能。 |
| **单向数据流** | Props 只读，State 在组件内部管理，避免意外副作用。 |
| **Hooks** | `useState`, `useEffect`, `useReducer`, `useContext` 等 API，方便在函数组件中使用状态与副作用。 |
| **生命周期 & 卸载** | `useEffect` 的清理回调可以模拟 `componentDidMount`, `componentWillUnmount` 等。 |
| **ReactDOM 抽象** | 分离前端 (`react-dom`)、服务器 (`react-dom/server`) 与 React Native 的实现。 |
| **Server‑Side Rendering（SSR）** | `react-dom/server` 提供 `renderToString()`、`renderToStaticMarkup()` 等 API。 |
| **Concurrent Mode / Suspense** | 支持并发渲染与懒加载，提升用户体验。 |
| **React Native** | 同一套组件模型可生成原生移动端 UI。 |

## 核心功能

1. **组件定义**  
   ```jsx
   function Hello({name}) {
     return <h1>Hello, {name}!</h1>;
   }
   ```

2. **状态管理**  
   ```jsx
   const [count, setCount] = useState(0);
   ```

3. **副作用处理**  
   ```jsx
   useEffect(() => {
     document.title = `You clicked ${count} times`;
   }, [count]);
   ```

4. **Context 全局共享**  
   ```jsx
   const ThemeContext = React.createContext('light');
   ```

5. **懒加载 + Suspense**  
   ```jsx
   const LazyComponent = React.lazy(() => import('./LazyComponent'));

   <Suspense fallback={<div>Loading...</div>}>
     <LazyComponent />
   </Suspense>
   ```

6. **服务器渲染**  
   ```js
   const { renderToString } = require('react-dom/server');
   const appString = renderToString(<App />);
   ```

## 如何使用

```bash
# 依赖安装
npm install react react-dom
# 若使用 TypeScript 可安装类型声明
npm install --save-dev @types/react @types/react-dom
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  const [msg, setMsg] = React.useState('Hello, React!');

  return (
    <div>
      <h1>{msg}</h1>
      <button onClick={() => setMsg('You clicked the button!')}>
        Click Me
      </button>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```

> **提示**  
> - 组件命名需大写字母开头。  
> - 只能在函数组件内部调用 Hooks。  
> - 路径以 `import` 语句统一管理（如 `components/Button.jsx`）。  

---

**文档来源**: 官方 GitHub 仓库 <https://github.com/facebook/react>。  
