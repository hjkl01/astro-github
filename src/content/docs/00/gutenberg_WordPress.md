
---
title: gutenberg
---


# Gutenberg（WordPress 区块编辑器）

> **项目地址**：<https://github.com/WordPress/gutenberg>

---

## 1 简介

Gutenberg 是 WordPress 官方的 **区块编辑器（Block Editor）**，替代传统的经典编辑器（TinyMCE）。它将内容拆分为可组合的区块 (block)，支持可视化、拖拽、嵌入、多媒体、表格、代码等多种内容类型，极大提升编辑体验与内容可维护性。

---

## 2 主要特性

| 关键特性 | 说明 |
| --- | --- |
| **区块化内容** | 将文章/页面拆成可独立编辑的区块，例如文本、图片、视频、音频、表格、引用、代码等。 |
| **可重用区块** | 选中的区块可以保存为“可重用区块”，在不同文章中直接插入。 |
| **可自定义区块** | 开发者可以使用 **Block API** 自己定义区块，支持动态区块、服务器端渲染等。 |
| **拖拽排序** | 支持拖拽操作，轻松调整区块顺序或层级。 |
| **文本与格式化** | 代码块、标题、列表、引用、卡片等文本区块，支持多种 HTML 标记、表情等。 |
| **多媒体嵌入** | 原生支持图片、视频、音频、YouTube、Vimeo 等媒体嵌入。 |
| **块模式与模板** | 对于大多数常见页面（如博客、产品页），提供预设块模式与模板，更快构建页面。 |
| **多语言与国际化** | 完全支持 I18n、L10n，适用于全球用户。 |
| **可预览 & PC/移动端化** | 在编辑器内部即可预览不同设备视图。 |
| **可访问性** | 专门关注无障碍友好，使用键盘、屏幕阅读器时也可畅顺操作。 |

---

## 3 关键功能

1. **编辑器核心（Editor Core）**  
   - 使用 **React** 与 **Redux** 构建，提供高性能、可扩展的编辑框架。  
2. **区块管理**  
   - `BlockList`、`BlockToolbar`、`BlockTools` 等组件，统一管理区块状态。  
3. **面板 & 工具栏**  
   - 侧边面板（Sidebar）、顶部工具栏（Toolbar）与区块工具栏，提供统一的编辑体验。  
4. **核心区块（Core Blocks）**  
   - 预置 20+ 核心区块，覆盖常见内容需求。  
5. **自定义区块（Custom Blocks）**  
   - 开发者使用 `registerBlockType()` 可快速创建自定义区块。  
6. **服务器区块（Server-side Rendered Blocks）**  
   - 区块渲染可在服务器端完成，确保客户端性能。  
7. **PWA & Gutenberg+**  
   - 通过插件可以将 Gutenberg 打包为 Progressive Web Apps，进一步扩展其功能。  

---

## 4 用法（快速上手）

### 4.1 在 WordPress 中启用 Gutenberg

- 主题默认会启用 Gutenberg（自 WordPress 5.0 起）。  
- 也可通过插件（如 `classic-editor`）禁用或仅在后台启用。  

### 4.2 新增/编辑文章

1. 登录后台 → `文章` → `添加新`。  
2. 通过 **+** 按钮选择任意核心区块（文本、标题、图片等）。  
3. 拖拽区块排序，使用侧边栏调整属性。  
4. 点击 **发布 / 更新** 完成。

### 4.3 开发自定义区块（示例）

```bash
# 在插件或主题根目录下创建插件
mkdir my-blocks
cd my-blocks
npm init
npm install @wordpress/scripts
```

在 `src/block.js`：

```js
import { registerBlockType } from '@wordpress/blocks';
import { RichText } from '@wordpress/block-editor';

registerBlockType( 'my-plugin/simple-text', {
    title: '简单文本',
    icon: 'smiley',
    category: 'layout',
    attributes: {
        content: { type: 'string', source: 'html', selector: 'p' }
    },
    edit: ({ attributes, setAttributes }) => (
        <RichText
            tagName="p"
            placeholder="输入文字..."
            value={attributes.content}
            onChange={(value) => setAttributes({ content: value })}
        />
    ),
    save: ({ attributes }) => <RichText.Content tagName="p" value={attributes.content} />
});
```

然后在 `index.js` 导入区块并构建：

```js
import './block';
```

运行 `npm run build，将生成 `dist` 目录，随后将插件压缩并通过后台安装使用。

---

## 5 参考资料

- 官方文档：[https://developer.wordpress.org/block-editor/](https://developer.wordpress.org/block-editor/)
- Github 仓库：[https://github.com/WordPress/gutenberg](https://github.com/WordPress/gutenberg)

---

> **此文件已保存至项目内 `src/content/docs/00/gutenberg_WordPress.md`。**