
---
title: Font-Awesome
---

# Font Awesome

**GitHub 仓库地址**：[https://github.com/FortAwesome/Font-Awesome](https://github.com/FortAwesome/Font-Awesome)

## 项目简介

Font Awesome 是一套开源矢量图标字体与 CSS 工具集，广泛应用于网页和应用程序的 UI 设计中。项目提供数千个图标，支持多种显示尺寸、颜色和动画效果，兼容主流前端框架与工具。

## 主要特性

- **丰富的图标库**：超过 1,600 个可自定义的图标，涵盖网页、商务、设计、交通等多种主题。  
- **矢量化 + 字体**：图标以 SVG 和 Web 字体（`ttf/woff2`）形式提供，既适合高分辨率显示，又可通过 CSS 样式完成个性化调整。  
- **可自定义属性**：支持 `size`, `color`, `rotate`, `flip`, `pulse`, `spin` 等 CSS 类快速设置图标外观。  
- **响应式设计**：图标尺寸随浏览器窗口调整而自适应，同时提供缩放选项（`fa-xs`, `fa-sm`, `fa-lg`, `fa-2x` 等）。  
- **渐进式兼容**：支持 SVG + VML 回退方案，兼容各种浏览器。  
- **社区驱动**：任何人都可以提交图标和改进，项目持续迭代更新。  
- **API 与 CLI**：CLI 工具（`fa`）可下载图标集并输出 CSS/Sass 代码；API 文档详细说明使用方式。  

## 安装方式

### 1. 直接通过 CDN 引入

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
```

### 2. NPM/Yarn 包

```bash
npm install @fortawesome/fontawesome-free
# 或者
yarn add @fortawesome/fontawesome-free
```

然后在项目中引入：

```js
import '@fortawesome/fontawesome-free/css/all.min.css';
```

### 3. 独立下载

访问官网 `https://fontawesome.com`，下载 `free` 或 `pro` 版本的压缩包，解压后直接引用。

## 使用方法

### 基本用法

```html
<i class="fas fa-camera"></i>
```

- `fa-` 前缀：表示 Font Awesome 图标。  
- `fas`：Solid 样式（实心图标）。  
- `fab`：Brands 样式（品牌图标）。  
- `far`：Regular 样式（线描图标）。  

### 调整大小

```html
<i class="fas fa-camera fa-lg"></i>
<i class="fas fa-camera fa-2x"></i>
```

### 改变颜色

```html
<i class="fas fa-camera" style="color: #e74c3c;"></i>
```

### 动画效果

```html
<i class="fas fa-sync fa-spin"></i>
<i class="fas fa-sync fa-pulse"></i>
```

### 组合使用

```html
<div class="btn btn-primary">
  <i class="fas fa-check mr-2"></i> 确认
</div>
```

## 进阶功能

- **Icon Picker**：可通过 `@fortawesome/fontawesome-free/js/all.js` 初始化图标选择器。  
- **Sass Mixins**：使用 `@fortawesome/fontawesome-free/scss/all.scss` 获取 Sass 变量与 mixin，进一步自定义。  
- **自定义图标**：将自己的 SVG 导入 `fa` 声明并注册，创建自定义图标集。  

## 文档与资源

- 官方文档：<https://fontawesome.com/docs>  
- 示例页面：<https://fontawesome.com/icons>  
- API 参考：<https://fontawesome.com/docs/web/use-with>  

---

> 如需进一步探索和使用 Font Awesome，建议阅读官方文档中的入门指南与进阶教程。