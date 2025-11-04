
---
title: monaco-editor
---


# Monaco Editor（Microsoft）

**项目地址**: https://github.com/microsoft/monaco-editor

Monaco Editor 是微软为 Web 开发的轻量级、可嵌入的代码编辑器，核心源代码来自 VS Code，旨在为浏览器提供与 VS Code 相同的编辑体验。

## 主要特性

| 序号 | 功能 | 说明 |
|------|------|------|
| 1 | **多语言支持** | 内置 40+ 语言（JavaScript、TypeScript、Python、Java、C/C++、HTML、CSS 等） |
| 2 | **语法高亮 & 自动补全** | 支持自动补全、参数提示、片段、代码片段、错误诊断 |
| 3 | **主题与样式** | 预置多种主题（默认 dark / light）、可自定义范围、字体、缩进 |
| 4 | **Emmet** | 快速写出 HTML/CSS 代码 |
| 5 | **代码片段** | 支持自定义片段、键盘快捷键 |
| 6 | **IntelliSense** | 支持自动补全、错误检测、格式化、代码导航 |
| 7 | **多光标 / 多选** | 增强编辑体验 |
| 8 | **可靠的性能** | 通过 Web Workers 运行解析，避免 UI 卡顿 |
| 9 | **可扩展插件** | 通过 `monaco-extension-api` 进行插件开发 |
| 10 | **发布 API** | 通过 `monaco-editor` NPM 包安装，支持 CommonJS / AMD / ES Modules |

## 核心功能

- **编辑器实例化**：创建、销毁、获取实例  
- **编辑状态管理**：获取/设置值、光标位置、编辑状态、语言、主题  
- **事件系统**：监听 `onDidChangeModelContent`、`onDidChangeCursorPosition`、`onDidCreateModel` 等  
- **代码分析**：使用 Language Server 通过 `monaco-languageclient` 与 LSP 交互  
- **代码格式化**：支持内置或外部格式化器  
- **折叠 / 代码行信息**：代码折叠、行号、标尺、可视化标记  
- **代码行动**：修复建议、符号引用、跳转到定义  

## 安装

```bash
# NPM
npm install monaco-editor

# Yarn
yarn add monaco-editor
```

> **注意**：在 CDN 方式使用时，需要单独加载 `monaco-editor` 的默认加载器。

## 基础用法

```html
<!-- index.html -->
<link rel="stylesheet" data-name="vs/editor/editor.main" href="node_modules/monaco-editor/min/vs/editor/editor.main.css" />
<script src="node_modules/monaco-editor/min/vs/loader.js"></script>
<script>
require.config({ paths: { 'vs': 'node_modules/monaco-editor/min/vs' }});
require(['vs/editor/editor.main'], function () {
  monaco.editor.create(document.getElementById('container'), {
      value: [
          'function hello() {',
          '\tconsole.log("Hello, world!");',
          '}'
      ].join('\n'),
      language: 'javascript',
      theme: 'vs-dark',
      automaticLayout: true
  });
});
</script>
```

```tsx
// 通过 React
import * as monaco from 'monaco-editor';
import { useEffect, useRef } from 'react';

const MonacoEditor = () => {
  const editorRef = useRef<HTMLDivElement | null>(null);
  const monacoRef = useRef<monaco.editor.IStandaloneEditorConstructionOptions | null>(null);

  useEffect(() => {
    if (!editorRef.current) return;
    const editor = monaco.editor.create(editorRef.current, {
      value: 'console.log("Hello");',
      language: 'typescript',
      theme: 'vs-light',
      automaticLayout: true,
    });
    return () => editor.dispose();
  }, []);

  return <div ref={editorRef} style={{ height: '500px', width: '100%' }}></div>;
};

export default MonacoEditor;
```

## 进一步扩展

- **Language Client**：结合 `monaco-languageclient` 与 WebSocket 或 Service Worker 接入 LSP  
- **Diff 编辑器**：使用 `createDiffEditor` 对比版本  
- **Notebook / Markdown**：结合 `monaco-editor` 与自定义语法插件实现笔记本、Markdown 预览  
- **自定义主题**：通过 `monaco.editor.defineTheme` 定义颜色映射  

## 文档与资源

- 官方 GitHub 👉 https://github.com/microsoft/monaco-editor  
- 官方 Demo 👉 https://microsoft.github.io/monaco-editor/playground.html  
- 文档搜索 👉 https://github.com/microsoft/monaco-editor/search  

> 以上内容可直接粘贴至 `src/content/docs/00/monaco-editor_microsoft.md` 并使用 Markdown 渲染即可。
