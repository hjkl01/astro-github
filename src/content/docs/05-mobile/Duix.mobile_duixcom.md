---
title: Duix.mobile
---

# Duix Mobile 项目

**GitHub 项目地址：** [https://github.com/duixcom/Duix.mobile/blob/main/README_zh.md](https://github.com/duixcom/Duix.mobile/blob/main/README_zh.md)

## 主要特性
Duix Mobile 是一个基于 React Native 开发的移动端 UI 组件库，专为跨平台应用设计，支持 iOS 和 Android。它的主要特性包括：
- **模块化设计**：提供丰富的 UI 组件，如按钮、输入框、列表、模态框等，支持按需引入，减少包体积。
- **主题自定义**：内置主题系统，支持暗黑模式和自定义颜色、字体等，适应不同品牌需求。
- **高性能**：优化了渲染性能，使用虚拟列表和懒加载机制，确保在大数据场景下的流畅体验。
- **国际化支持**：内置 i18n 支持，多语言切换，便于全球应用开发。
- **TypeScript 支持**：提供完整的类型定义，提升开发效率和代码可靠性。
- **响应式布局**：组件自适应不同屏幕尺寸，支持 Flexbox 和媒体查询。

## 主要功能
- **核心组件**：包括基础组件（View、Text）、交互组件（Button、Touchable）、导航组件（TabBar、Drawer）和数据展示组件（ListView、Carousel）。
- **工具函数**：提供实用工具，如日期格式化、动画库集成（支持 Animated API）和网络请求封装。
- **插件扩展**：可集成第三方库，如 Redux 用于状态管理，或 React Navigation 用于路由。
- **调试工具**：内置开发者模式，支持热重载和性能监控。

## 用法
1. **安装**：
   - 使用 npm 或 yarn 安装：`npm install duix-mobile` 或 `yarn add duix-mobile`。
   - 对于 React Native 项目，确保已安装 React Native 环境（版本 >= 0.60）。

2. **引入组件**：
   - 在代码中导入：`import { Button, Input } from 'duix-mobile';`。
   - 示例使用 Button：
     ```jsx
     import React from 'react';
     import { Button } from 'duix-mobile';

     const App = () => (
       <Button title="点击我" onPress={() => console.log('按钮被点击')} />
     );
     ```

3. **配置主题**：
   - 在应用入口文件设置：`import { setTheme } from 'duix-mobile'; setTheme({ primaryColor: '#007AFF' });`。

4. **构建与运行**：
   - 使用 React Native CLI 运行：`npx react-native run-android` 或 `npx react-native run-ios`。
   - 详细文档请参考项目 README 中的示例和 API 参考。

该项目适合快速构建高质量移动应用，鼓励开发者贡献代码和 issue。