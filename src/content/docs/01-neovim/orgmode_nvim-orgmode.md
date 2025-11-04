
---
title: orgmode
---


# 项目概述
**nvim-orgmode** 是一个专为 Neovim 设计的 Org-mode 兼容插件，旨在让 Neovim 用户能够在熟悉的 Vim 生态中享受 Org-mode 强大的笔记、组织与项目管理功能。该插件在原始 Emacs Org-mode 的功能基础上，增添了许多 Neovim 本地的特性与优化，以实现流畅的使用体验。

## 项目地址
- GitHub: [https://github.com/nvim-orgmode/orgmode](https://github.com/nvim-orgmode/orgmode)

## 主要特性
| # | 功能 | 说明 |
|---|------|------|
| 1 | **多功能文档结构** | 支持标题、列表、任务、时间戳、标签等标准 Org-mode 语法。 |
| 2 | **TODO 自动化** | 任务状态（TODO/DONE/DELEGATED/WAITING 等）可直接在 Neovim 的状态栏或浮窗中显示。 |
| 3 | **快捷键集成** | 通过自定义映射快速切换节点、展开/收起、编辑、执行脚本。 |
| 4 | **日程与时间管理** | 任务的 `DEADLINE` 与 `SCHEDULED` 可与 Neovim 事件窗口集成，显示日历视图。 |
| 5 | **代码块执行** | 支持多语言代码块（如Python、Lua、Bash 等）的执行，并将结果插入文档。 |
| 6 | **导出功能** | 通过 `org-export` 支持导出至 Markdown、HTML、LaTeX、PDF 等格式。 |
| 7 | **Agenda 视图** | 生成整个 Org-mode 源文件的待办列表、日程表、标签索引。 |
| 8 | **Tree 结构视图** | 与 `nvim-tree` 兼容，可在侧栏直观看到文件树和节点层级。 |
| 9 | **插件兼容** | 与 Telescope、Telescope-Cmds、Telescope-Org、Notify、Diffview 等插件无缝配合。 |
|10 | **高性能渲染** | 采用 Treesitter 语法树解析 Org-mode，提高高亮和折叠性能。 |

## 关键功能与使用示例
### 1. 安装 & 初始化
```vim
" 在 init.lua (或 autoload/init.vim) 中添加
require('orgmode').setup({
  org_agenda_files = {'~/org/**/*'},
  agenda_start_day = "today",
  agenda_start_week = "monday",
  agenda_day_of_week = 7,
})
```

### 2. 快捷键操作
| 快捷键 | 操作 |
|--------|------|
| `<localleader>t` | 切换当前节点的 TODO 状态 |
| `<localleader>c` | 折叠/展开当前节点 |
| `<localleader>e` | 选中步骤执行代码块 |
| `<localleader>a` | 打开 Agenda 视图 |
| `<localleader>k` | 通过 Telescope 搜索关键字 |
| `<localleader>l` | 切换到流程视图（侧边栏） |

### 3. 代码块执行
```org
#+begin_src python
print("Hello Org!")
#+end_src
```
按 `<localleader>e` 后，结果会在代码块下面插入。

### 4. 日期与标签
```org
** TODO 会议纪要  <2024-10-20 Thu>
   :PROPERTIES:
   :CUSTOM_ID: meeting-20241020
   :END:
```

使用键 `y` 可将当前时间戳复制到剪贴板，便于快速插入。

### 5. 导出
```vim
:OrgExportToMD              " 导出为 Markdown
:OrgExportToHtml            " 导出为 HTML
```

**输出示例**  
`*.md`（示例文件 `meeting.md`）将包含标题、列表、代码块执行结果等完整格式。

## 开发与贡献
- 代码定位：`lua/orgmode.nvim`  
- 插件使用 Lua 语言编写  
- 贡献前请阅读 `CONTRIBUTING.md` 与 `CODE_OF_CONDUCT.md`  
- 拉取请求（PR）应包含对应的文档更新与必要的测试。

## 许可证
本项目基于 ISC 许可证发布，允许免费使用、修改与分发。详情请参见 `LICENSE` 文件。

---

> **Tip**：建议同时安装 `nvim-treesitter` 与 `telescope.nvim`，以获得最佳语法高亮与搜索体验。