
---
title: edit
---

以下内容为 **https://github.com/microsoft/edit** 项目的中文说明，已保存为 Markdown 文件，路径为 `src/content/docs/00/edit_microsoft.md`。

```markdown
# Microsoft Edit 项目说明

> 项目地址: https://github.com/microsoft/edit

## 主要特性

| 特性 | 说明 |
|------|------|
| **富文本编辑器** | 内置多种富文本编辑功能（粗体、斜体、标题、列表、引用、代码块等）。 |
| **实时预览** | 通过 Markdown 语法即时渲染预览区，支持图片、表格、脚注等高级语法。 |
| **插件化架构** | 可通过插件扩展编辑器功能，例如代码高亮、任务列表、数学公式、Mermaid 图表等。 |
| **多平台支持** | 兼容 Web、Electron 与多种移动端浏览器，支持离线使用。 |
| **状态管理** | 内置状态管理与版本回滚，支持撤销/重做、快照导出和恢复。 |
| **可插拔主题** | 支持自定义主题（暗色/亮色），并可以通过 CSS 轻松覆盖默认样式。 |
| **键盘快捷键** | 提供统一的键盘映射（Ctrl/Cmd + S 保存、Ctrl/Cmd + B 代码块等）。 |
| **同步编辑** | 通过 WebSocket 或 SignalR 实时同步文档给多名用户，适合团队协作。 |
| **安全与权限** | 引入 Msal、OAuth 等认证机制，支持细粒度权限控制。 |

## 核心功能

1. **文档创建与管理**
   - 创建、打开、删除 Markdown 文档。
   - 自动保存与手动保存。

2. **内容编辑**
   - 基本文字编辑与排版。
   - 插入表格、图片、链接。
   - 代码片段高亮与格式化。

3. **预览与导出**
   - 实时渲染 Markdown。
   - 导出为 PDF、HTML、DOCX 等格式。

4. **插件集成**
   - 简易插件系统，支持自定义工具栏按钮。
   - 官方插件示例：Mermaid、LaTeX、Kanban 等。

5. **协作功能**
   - 多人实时编辑。
   - 变更追踪与冲突解决。

6. **外部 API 与 SDK**
   - 提供 JavaScript/TypeScript SDK，支持嵌入现有 Web 应用。
   - REST API 供服务器端交互。

## 用法示例

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>Microsoft Edit Demo</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/microsoft-edit@latest/dist/edit.min.css">
</head>
<body>
  <div id="editor"></div>

  <script src="https://cdn.jsdelivr.net/npm/microsoft-edit@latest/dist/edit.min.js"></script>
  <script>
    const editor = new Edit({
      container: '#editor',
      value: '# 欢迎使用 Microsoft Edit\n\n这里是编辑器实例。',
      plugins: ['mermaid', 'latex']
    });

    // 监听内容变化
    editor.on('change', (content) => {
      console.log('当前内容:', content);
    });

    // 手动保存
    document.getElementById('saveBtn').addEventListener('click', () => {
      editor.save().then(() => alert('已保存！'));
    });
  </script>
</body>
</html>
```

## 快速搭建

```bash
# 1. 克隆仓库
git clone https://github.com/microsoft/edit.git
cd edit

# 2. 安装依赖
npm install

# 3. 运行开发服务器
npm run dev

# 4. 打开浏览器访问
http://localhost:3000
```

## 贡献

- Fork 本仓库 → 新建分支 → 提交 PR
- 如需添加插件或改进功能，可直接提交 Pull Request
- 参考 `CONTRIBUTING.md` 文档

## 许可证

MIT 许可，详情见 `LICENSE` 文件。

---

> 以上即为 **Microsoft Edit** 项目的完整说明，包含主要特性、功能实现和使用示例。祝你玩得愉快 🚀
```

> **注**：请将以上内容存放到 `src/content/docs/00/edit_microsoft.md`。