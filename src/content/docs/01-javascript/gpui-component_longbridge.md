
---
title: gpui-component
---


# gpui-component

> GitHub 项目地址: [https://github.com/longbridge/gpui-component](https://github.com/longbridge/gpui-component)

## 项目简介  
`gpui-component` 是一套为企业级 Web 应用而设计的 UI 组件库，基于 React + TypeScript/JavaScript 开发。  
它整合了组件复用、主题自定义、响应式适配、无障碍支持等功能，专门满足长桥（LongBridge）内部项目的统一界面需求。

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **完整的组件集合** | 覆盖常用 UI 组件：按钮、输入框、选择器、下拉框、表格、表单、模态框、分页等。 |
| **主题与样式自定义** | 支持全局主题（默认蓝色/深色）并可通过 `themeProvider` 或 CSS 变量自由切换。 |
| **响应式布局** | 内置栅格系统，兼容移动端与桌面端。 |
| **无障碍支持** | 所有组件遵循 WAI-ARIA 标准，支持键盘操作和屏幕阅读器。 |
| **TypeScript 支持** | 所有组件均提供完整类型定义，IDE 自动补全友好。 |
| **国际化（i18n）** | 通过 `react-intl` 集成，支持多语言切换。 |
| **文档与 Demo** | 通过 Storybook 展示使用案例，便于快速上手。 |
| **插件化** | 通过 `gpui-plugin` 机制，用户可额外新增自定义组件。 |

---

## 功能模块

| 模块 | 说明 |
|------|------|
| **基础组件** | Button、Input、Select、Checkbox、Radio、DatePicker 等。 |
| **数据展示** | Table、Tree、Tag、Badge、Tooltip、Popover、Skeleton、Spin 等。 |
| **交互组件** | Modal、Drawer、Confirm、Dropdown、Notification、Message 等。 |
| **布局组件** | Grid、Flex、Space、Layout、Navigation、Tabs、Breadcrumb 等。 |
| **表单组件** | Form、FormItem、Validation、FormContext 等。 |
| **工具类** | useDebounce、useOnclickOutside、useToggle、classnames 等。 |

---

## 使用方法

### 1. 安装

```bash
# npm
npm install gpui-component

# yarn
yarn add gpui-component
```

### 2. 引入样式

```js
import 'gpui-component/dist/index.css';
```

> 如需自定义主题，请在样式加载前先覆盖 CSS 变量或使用 themeProvider。

### 3. 基础使用示例

```tsx
import React from 'react';
import { Button, Input, Modal, Table } from 'gpui-component';

function Demo() {
  const [isModalOpen, setModalOpen] = React.useState(false);

  return (
    <div>
      <Button onClick={() => setModalOpen(true)} primary>
        打开弹窗
      </Button>

      <Modal visible={isModalOpen} onClose={() => setModalOpen(false)}>
        <h3>示例弹窗</h3>
        <Input placeholder="请输入内容" />
      </Modal>

      <Table columns={[{ title: '姓名', dataIndex: 'name' }]} dataSource={[]} />
    </div>
  );
}
```

### 4. 主题自定义（示例）

```tsx
import { ThemeProvider } from 'gpui-component';

const customTheme = {
  primaryColor: '#ff5722',
  secondaryColor: '#4caf50',
  // 其他主题变量...
};

<ThemeProvider theme={customTheme}>
  <App />
</ThemeProvider>;
```

---

## 开发与贡献

- Fork 本仓库，提交 PR 前请先跑 `yarn` 与 `yarn build`，确保代码通过 ESLint 与单元测试。  
- 组件代码位于 `src/components`，文档 Demo 位于 `src/docs`。  
- 每个组件应附带自动生成的 Storybook 页面及相应的 TypeScript 类型文件。

---

## 许可证

MIT © LongBridge

```
