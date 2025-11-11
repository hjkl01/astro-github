---
title: Material UI
---

# Material UI

Material UI 是一个全面的 React 组件库，它实现了 Google 的 Material Design 系统。该库由数千名开源贡献者在超过十年的开发中经过严格测试，因此受到全球一些最优秀产品团队的信任。

## 功能

- **全面的组件库**：提供丰富的 React 组件，包括按钮、表单、导航、布局等。
- **Material Design 实现**：独立实现 Google 的 Material Design 系统，确保一致性和美观性。
- **扩展性**：核心功能由 MUI X 扩展，提供复杂组件用于高级用例。
- **免费永久使用**：MIT 许可证，完全免费。
- **TypeScript 支持**：提供完整的 TypeScript 类型定义。
- **主题化和定制**：支持自定义主题、颜色、字体等。
- **响应式设计**：组件默认支持响应式布局。
- **无障碍性**：遵循无障碍性标准，提供键盘导航和屏幕阅读器支持。

## 用法

### 安装

使用 npm 或 yarn 安装：

```bash
npm install @mui/material @emotion/react @emotion/styled
```

或

```bash
yarn add @mui/material @emotion/react @emotion/styled
```

### 基本使用

首先，在应用入口处设置主题提供者：

```jsx
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      {/* 你的应用内容 */}
    </ThemeProvider>
  );
}
```

然后使用组件：

```jsx
import Button from '@mui/material/Button';

function MyComponent() {
  return (
    <Button variant="contained" color="primary">
      Hello World
    </Button>
  );
}
```

### 常用组件

- **Button**：按钮组件，支持多种变体和颜色。
- **TextField**：文本输入字段。
- **Card**：卡片组件，用于展示内容。
- **AppBar**：应用栏，通常用于导航。
- **Drawer**：抽屉组件，用于侧边导航。
- **Dialog**：对话框组件。

### 主题定制

```jsx
const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});
```

### 更多信息

详细文档和示例请访问：[Material UI 官方文档](https://mui.com/material-ui/getting-started/)

Material UI 还提供了 Joy UI（实验性组件库），但推荐新项目使用 Material UI。
