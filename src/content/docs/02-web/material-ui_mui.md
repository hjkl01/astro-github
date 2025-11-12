---
title: Material-UI
---

Material-UI 是一个全面的 React 组件库，实现了 Google 的 Material Design 系统。它提供了丰富的预构建组件，帮助开发者快速构建美观、响应式的用户界面。

## 功能

- **组件丰富**：包括按钮、表单、导航、布局等各种 UI 组件。
- **Material Design**：遵循 Google 的 Material Design 规范，确保一致性和美观性。
- **自定义主题**：支持主题定制，包括颜色、字体等。
- **TypeScript 支持**：提供完整的 TypeScript 类型定义。
- **无障碍性**：组件内置无障碍性支持。
- **扩展性**：核心功能可通过 MUI X 扩展，用于高级用例。

## 用法

1. **安装**：使用 npm 或 yarn 安装。

   ```bash
   npm install @mui/material @emotion/react @emotion/styled
   ```

2. **基本使用**：导入组件并在 React 应用中使用。

   ```jsx
   import React from 'react';
   import Button from '@mui/material/Button';

   function App() {
     return (
       <Button variant="contained" color="primary">
         Hello World
       </Button>
     );
   }

   export default App;
   ```

3. **主题定制**：使用 ThemeProvider 自定义主题。

   ```jsx
   import { ThemeProvider, createTheme } from '@mui/material/styles';

   const theme = createTheme({
     palette: {
       primary: {
         main: '#1976d2',
       },
     },
   });

   function App() {
     return <ThemeProvider theme={theme}>{/* 应用内容 */}</ThemeProvider>;
   }
   ```

更多详细信息，请参考 [官方文档](https://mui.com/material-ui/getting-started/)。
