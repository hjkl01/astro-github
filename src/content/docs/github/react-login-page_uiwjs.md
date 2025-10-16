
---
title: react-login-page
---

# React Login Page 项目

## 项目地址
[GitHub 项目地址](https://github.com/uiwjs/react-login-page)

## 主要特性
- **响应式设计**：基于 React 和 UIW 组件库，支持移动端和桌面端的自适应布局，提供现代化的登录界面。
- **多主题支持**：内置浅色和深色主题切换，易于自定义样式以匹配不同应用需求。
- **国际化**：支持多语言配置，便于全球用户使用。
- **组件化结构**：模块化设计，便于集成到现有 React 项目中，支持 TypeScript 类型定义。
- **轻量级**：体积小巧，加载速度快，不依赖过多外部库。

## 主要功能
- **登录表单**：提供用户名/密码登录、邮箱登录等多种表单类型，支持输入验证和错误提示。
- **第三方登录集成**：可扩展支持 OAuth（如 Google、GitHub）等第三方登录方式。
- **记住密码与自动登录**：内置本地存储功能，实现用户凭证保存和自动填充。
- **验证码与安全增强**：支持图形验证码、短信验证码集成，提升登录安全性。
- **自定义钩子**：使用 React Hooks 管理状态和副作用，便于处理登录逻辑和 API 调用。

## 用法
1. **安装依赖**：
   ```bash
   npm install react-login-page uiw
   # 或使用 yarn
   yarn add react-login-page uiw
   ```

2. **基本导入与使用**：
   在 React 组件中导入并渲染登录页面：
   ```jsx
   import React from 'react';
   import { LoginPage } from 'react-login-page';

   function App() {
     return (
       <div className="App">
         <LoginPage
           onSubmit={(values) => {
             console.log('登录数据:', values);
             // 处理登录逻辑，例如调用 API
           }}
         />
       </div>
     );
   }

   export default App;
   ```

3. **自定义配置**：
   - 通过 props 自定义标题、logo、按钮文本等：
     ```jsx
     <LoginPage
       title="我的应用"
       logo="https://example.com/logo.png"
       theme="dark" // 或 'light'
       onSubmit={handleLogin}
     />
     ```
   - 集成表单验证：结合 Formik 或 Yup 库添加数据校验。
   - 扩展第三方登录：修改组件内部逻辑，添加自定义按钮和处理函数。

4. **构建与部署**：
   - 在项目中运行 `npm run build` 编译。
   - 适用于 Create React App 或 Vite 等构建工具。
   - 参考 GitHub 仓库的 `examples` 文件夹获取更多高级用法示例。

更多细节请查看项目 README 和源代码。