
---
title: friendly-snippets
---

# friendly-snippets（rafamadriz）

**项目地址**: https://github.com/rafamadriz/friendly-snippets

---

## 概述

friendly‑snippets 是一个为多种编辑器（VS Code、Sublime Text、Atom、Vim 等）提供的统一片段（snippet）集合。它通过统一的片段格式，简化了跨编辑器和跨语言的片段管理，让开发者能够在任何支持 Snippet 的编辑器中都能获得一致、可扩展的代码片段体验。

---

## 主要特性

- **跨编辑器兼容**：支持 VS Code、Sublime Text、Atom、Vim、Emacs 等主流编辑器。
- **多语言覆盖**：内置数百种编程语言（JavaScript, Python, Go, Rust, HTML, CSS, Markdown 等）以及相关框架（React, Vue, Angular, Django, Rails 等）。
- **统一格式**：采用 JSON 结构，易于阅读、编辑和扩展。
- **可自定义**：每个片段都可通过 `prefix`, `body`, `description` 等字段自定义触发词、代码内容与说明。
- **易于扩展**：支持通过 `snippets` 文件夹添加自定义片段，或者直接在编辑器中编写片段。
- **社区驱动**：持续更新，集成社区贡献的片段。

---

## 主要功能

| 功能 | 描述 |
|------|------|
| **片段导入** | 通过插件或手动复制 JSON，快速将片段导入编辑器。 |
| **片段触发** | 在编辑器中键入 `prefix` 并按 Tab 或回车即可展开片段。 |
| **多光标编辑** | 片段中的 `$1`, `$2` 等占位符支持多光标跳转。 |
| **变量与函数** | 可使用 `${TM_FILENAME}` 等内置变量或自定义函数。 |
| **片段组合** | 支持片段内部嵌套，构建复合代码结构。 |
| **自动补全** | 通过语言服务器或编辑器功能，自动补全片段。 |

---

## 用法

### 1. 安装

#### VS Code

1. 在 Extensions 里搜索 `friendly-snippets` 并安装。  
2. 或者在终端执行：

```bash
code --install-extension formulahendry.friendly-snippets
```

#### Sublime Text

1. 在 Package Control 中搜索并安装 `friendly-snippets`。  
2. 或手动下载 `snippets` 文件夹，放入 `~/.config/sublime-text-3/Packages/`。

#### Vim / Neovim

1. 安装插件管理器（如 vim-plug）：

```vim
Plug 'rafamadriz/friendly-snippets'
```

2. 重新加载插件并执行 `:SnipMateInstall`。

### 2. 使用

- 在代码文件中键入片段前缀（如 `for`），然后按 `Tab` 或 `Enter` 即可展开。

```javascript
// 片段前缀: for
for (let i = 0; i < array.length; i++) {
    // TODO
}
```

- 片段中的 `$1`, `$2` 等占位符可通过 `Tab` 依次跳转。

### 3. 自定义片段

在项目根目录下的 `snippets` 文件夹中新增或修改 JSON 文件。例如，添加一个自定义 JavaScript 片段：

```json
{
    "myCustomSnippet": {
        "prefix": "myfun",
        "body": [
            "function ${1:name}(${2:args}) {",
            "    ${3:// TODO}",
            "}"
        ],
        "description": "自定义函数片段"
    }
}
```

保存后，在对应语言文件中使用 `myfun` 触发即可。

---

## 贡献

1. Fork 本仓库。  
2. 在 `snippets` 目录下添加或修改片段。  
3. 提交 PR 并说明新增/修改的片段细节。

---

## 许可证

本项目采用 MIT 许可证，详情请参见 `LICENSE` 文件。