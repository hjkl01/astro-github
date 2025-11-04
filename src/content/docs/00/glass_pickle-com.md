
---
title: glass
---


# Glass - Pickle-com

[GitHub](https://github.com/pickle-com/glass)

## 主要特性

- **Glassmorphism**：提供一套专门用于实现玻璃质感 UI 的 CSS 变量与类。
- **可复用组件**：包含 Card、Button、Modal、Input 等常用组件，均支持透明、模糊、阴影等效果。
- **响应式**：所有组件自带响应式设计，可在不同设备上无缝适配。
- **主题切换**：支持浅色/深色主题切换，只需更改 CSS 变量即可。
- **易于集成**：可直接在任何前端项目（React/Vue/纯 HTML）中使用。

## 功能

| 功能 | 说明 |
|------|------|
| 透明背景 | 通过 `glass-bg` 类实现半透明背景。 |
| 背景模糊 | 使用 `glass-blur` 类或 `backdrop-filter` 实现模糊效果。 |
| 阴影 | `glass-shadow` 提供柔和阴影。 |
| 组件 | Card、Button、Modal、Input、Tabs、Accordion 等。 |
| 主题 | `--glass-theme` 变量控制深浅主题。 |

## 用法

### 安装

```bash
npm install @pickle-com/glass
# 或者
yarn add @pickle-com/glass
```

### 引入 CSS

```js
import '@pickle-com/glass/glass.css';
```

### 在 HTML 中使用

```html
<div class="glass-card">
  <h2 class="glass-title">标题</h2>
  <p>内容</p>
  <button class="glass-button">点我</button>
</div>
```

### 在 React 中使用

```jsx
import { GlassCard, GlassButton } from '@pickle-com/glass';

function App() {
  return (
    <GlassCard>
      <h2>标题</h2>
      <p>内容</p>
      <GlassButton>点我</GlassButton>
    </GlassCard>
  );
}
```

## 配置主题

```css
:root {
  --glass-bg-color: rgba(255, 255, 255, 0.15);
  --glass-blur: 10px;
  --glass-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}
```

## 贡献

欢迎提交 Issue 与 PR，参见 `CONTRIBUTING.md`。

## 许可证

MIT
