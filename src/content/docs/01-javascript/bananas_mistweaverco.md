---
title: bananas
---

# Bananas 项目

## 项目地址
[GitHub 项目地址](https://github.com/mistweaverco/bananas)

## 主要特性
Bananas 是一个开源的 JavaScript 库，专注于简化前端开发中的动画和交互效果。其核心特性包括：
- **流畅动画支持**：内置多种动画类型，如淡入淡出、滑动和缩放，支持 CSS 过渡和 Web Animations API。
- **轻量级设计**：体积小巧，无需额外依赖，易于集成到现有项目中。
- **响应式适配**：自动适应不同设备和屏幕尺寸，确保动画在移动端和桌面端一致表现。
- **可扩展性**：提供插件系统，用户可以自定义动画效果和钩子函数。
- **性能优化**：使用 requestAnimationFrame 实现高效渲染，避免浏览器卡顿。

## 主要功能
- **动画控制**：支持启动、暂停、停止和反转动画，提供链式调用 API。
- **事件处理**：集成事件监听器，用于触发动画，如点击、滚动或 hover。
- **预设模板**：内置常见 UI 动画模板，例如加载 spinner、模态框弹出和列表项过渡。
- **调试工具**：包含开发模式下的日志和可视化工具，帮助开发者调试动画序列。
- **兼容性**：支持现代浏览器（Chrome 50+、Firefox 50+ 等），并提供 polyfill 选项。

## 用法
1. **安装**：
   - 通过 npm：`npm install bananas`
   - 或通过 CDN：在 HTML 中引入 `<script src="https://unpkg.com/bananas/dist/bananas.min.js"></script>`

2. **基本用法**：
   - 初始化：`const animator = new Bananas();`
   - 应用动画：`animator.animate(element, 'fadeIn', { duration: 500 });`  
     - `element`：DOM 元素。
     - `'fadeIn'`：动画类型（支持 'slideIn'、'bounce' 等）。
     - 选项：包括 duration（持续时间，ms）、easing（缓动函数，如 'ease-in-out'）等。

3. **高级用法**：
   - 链式动画：`animator.animate(el1, 'slideUp').then(() => animator.animate(el2, 'fadeIn'));`
   - 事件触发：`animator.on('click', element, 'bounce', options);`
   - 自定义动画：扩展 Bananas 类，重写 `createKeyframe` 方法定义关键帧。

更多细节请参考项目 README 和示例代码。