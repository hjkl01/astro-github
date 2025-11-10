---
title: fullPage.js
---

# fullPage.js 项目

## 项目地址
[GitHub 项目地址](https://github.com/alvarotrigo/fullPage.js/tree/master/lang/chinese#fullpagejs)

## 主要特性
fullPage.js 是一个轻量级的 JavaScript 库，用于创建全屏滚动网站（full page scrolling）。它支持响应式设计、触摸设备兼容，并提供丰富的动画和交互选项。主要特性包括：
- **全屏垂直滚动**：将页面内容分为多个全屏部分，实现平滑的垂直滚动效果。
- **水平滑动支持**：在每个全屏部分内支持水平滑块（slides），允许多层交互。
- **响应式设计**：自动适应不同设备和屏幕尺寸，支持移动端触摸滑动。
- **自定义动画**：集成 CSS3 过渡和多种缓动效果，支持自定义滚动速度和动画类型。
- **导航菜单**：自动生成锚点导航，支持自定义菜单和工具栏。
- **扩展性强**：兼容多种浏览器（IE 9+），并提供回调函数钩子用于扩展功能。
- **多语言支持**：内置中文等语言包，便于国际化。

## 主要功能
- **自动索引**：为每个部分和滑块分配唯一 ID 和锚点，便于 URL 导航和 SEO 优化。
- **键盘与鼠标控制**：支持键盘箭头键、滚轮和触摸手势控制滚动。
- **懒加载**：优化性能，仅在滚动到视口时加载图像和内容。
- **回调事件**：提供 onLeave、onSlideLeave 等事件，用于在滚动前后执行自定义逻辑。
- **插件集成**：可与 jQuery、Bootstrap 等框架结合使用，并支持视频背景和视差效果。

## 用法
### 安装
1. 通过 CDN 引入：
   ```html
   <script src="https://cdn.jsdelivr.net/npm/fullpage.js/dist/fullpage.min.js"></script>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fullpage.js/dist/fullpage.min.css">
   ```
2. 或通过 npm 安装：
   ```bash
   npm install fullpage.js
   ```

### 基本用法
1. **HTML 结构**：
   ```html
   <div id="fullpage">
       <div class="section">第一个部分</div>
       <div class="section">
           <div class="slide">滑块1</div>
           <div class="slide">滑块2</div>
       </div>
       <div class="section">第三个部分</div>
   </div>
   ```

2. **JavaScript 初始化**：
   ```javascript
   new fullpage('#fullpage', {
       // 基本配置
       autoScrolling: true,  // 启用自动滚动
       scrollHorizontally: true,  // 启用水平滚动
       navigation: true,  // 显示导航点
       navigationPosition: 'right',  // 导航位置
       anchors: ['home', 'about', 'contact'],  // 锚点数组
       // 回调示例
       onLeave: function(origin, destination, direction) {
           console.log('离开部分：' + origin.index);
       }
   });
   ```

3. **高级配置**：
   - 设置滚动速度：`scrollingSpeed: 700`（毫秒）。
   - 启用循环：`loopBottom: true`。
   - 移动端优化：`fitToSection: false` 以避免过度调整。
   - 更多选项详见官方文档。

### 注意事项
- 确保页面无溢出内容，以实现完美全屏效果。
- 对于复杂项目，推荐结合 fullpage.js 的扩展插件，如视频背景或表单集成。
- 测试时在不同设备上验证响应式行为。