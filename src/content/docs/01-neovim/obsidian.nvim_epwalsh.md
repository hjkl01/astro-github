
---
title: obsidian.nvim
---

# obsidian.nvim

> **项目地址**: <https://github.com/epwalsh/obsidian.nvim>

---

## 简介
`obsidian.nvim` 是一个为 Neovim 设计的 Obsidian 同步插件，利用 Neovim 的强大编辑功能，让你在本地即可完整体验 Obsidian 的笔记体系。插件通过读取 Obsidian vault 内部结构，实现双向链接、文件管理、图表渲染、代码执行等核心功能，并兼容 Obsidian 的各种插件生态。

---

## 主要特性

| 功能 | 说明 |
|------|------|
| **双向链接与预览** | 在编辑器中即时显示 `[[link]]` 的目标内容，并支持跳转。 |
| **文件树 & 搜索** | 通过 `:ObsidianOpen` 打开文件树，支持 fuzzy search、文件创建与重命名。 |
| **任务与列表** | 支持 `- [ ]` 任务列表，自动更新完成状态，支持 `:ObsidianTasks` 统计。 |
| **代码块执行** | 通过 `:ObsidianRunCodeBlock` 或快捷键执行当前代码块，输出结果嵌入笔记。 |
| **图表渲染** | 支持 Mermaid、Flowchart 等图表语法，自动渲染为图片。 |
| **日历视图** | 通过 `:ObsidianCalendar` 打开日历快捷入口，快速定位每日笔记。 |
| **元数据与标签** | 读取 YAML front matter 与标签，支持过滤与搜索。 |
| **与 Obsidian 同步** | 通过 `obsidian.json` 配置自动保持本地与 Obsidian 服务器同步。 |
| **自定义命令与快捷键** | 允许用户自定义命令、键位绑定，满足个人工作流。 |

---

## 快速上手

### 1. 安装
#### 使用 `lazy.nvim`
```lua
{
  "epwalsh/obsidian.nvim",
  branch = "main",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-telescope/telescope.nvim",
  },
  opts = {
    dir = "~/Documents/ObsidianVault", -- Obsidian vault 路径
    notes_subdir = "notes",
    daily_notes = {
      folder = "daily",
      date_format = "%Y-%m-%d",
    },
    templates = {
      subdir = "templates",
      date_format = "%Y-%m-%d",
      time_format = "%H:%M",
    },
  },
}
```

### 2. 配置
```lua
-- ~/.config/nvim/lua/obsidian.lua
local obsidian = require("obsidian")
obsidian.setup({
  dir = "~/Documents/ObsidianVault",
  notes_subdir = "notes",
  daily_notes = {
    folder = "daily",
    date_format = "%Y-%m-%d",
  },
  templates = {
    subdir = "templates",
    date_format = "%Y-%m-%d",
    time_format = "%H:%M",
  },
  completion = {
    nvim_cmp = true,
    min_chars = 2,
  },
  mappings = {
    -- 例子：跳转到笔记
    ["<leader>oo"] = { cmd = "ObsidianOpen", desc = "Open Obsidian" },
    ["<leader>ol"] = { cmd = "ObsidianLink", desc = "Create Link" },
    ["<leader>ot"] = { cmd = "ObsidianTemplate", desc = "Insert Template" },
  },
})
```

### 3. 常用命令

| 命令 | 作用 |
|------|------|
| `:ObsidianOpen` | 打开文件树，搜索并打开笔记 |
| `:ObsidianLink` | 在当前位置插入双向链接 |
| `:ObsidianTemplate` | 根据模板创建新笔记 |
| `:ObsidianDailyNote` | 打开/创建当天笔记 |
| `:ObsidianTasks` | 显示任务列表与统计 |
| `:ObsidianRunCodeBlock` | 执行当前代码块并插入结果 |
| `:ObsidianCalendar` | 打开日历视图 |
| `:ObsidianRefreshBookmarks` | 刷新书签 |

### 4. 快捷键示例

```vim
nnoremap <leader>oo :ObsidianOpen<CR>
nnoremap <leader>ol :ObsidianLink<CR>
nnoremap <leader>ot :ObsidianTemplate<CR>
nnoremap <leader>od :ObsidianDailyNote<CR>
nnoremap <leader>ot :ObsidianTasks<CR>
nnoremap <leader>on :ObsidianRunCodeBlock<CR>
```

### 5. 自定义代码块执行
在 `init.lua` 添加：
```lua
require("obsidian").setup({
  -- ...
  code_execute = {
    python = "python3 - <<'PY'\n%s\nPY",
    lua = "nvim -c 'luafile %s'",
    -- 其他语言配置
  }
})
```

---

## 进阶使用

- **自定义图表渲染**：将 `mermaid` 渲染为 SVG 并显示在 Neovim 内置预览（需安装 `mermaid-cli`）。
- **Obsidian 插件桥接**：使用 `obsidian.json` 将 Neovim 与 Obsidian 同步，支持多设备协作。
- **集成 Telescope**：使用 `:Telescope obsidian find_notes` 搜索笔记，配合 fuzzy finder 体验更佳。

---

## 贡献与支持

- 代码托管在 GitHub，使用 MIT 许可证。
- Issues 与 PR 受欢迎，常见问题请先查阅 [Wiki](https://github.com/epwalsh/obsidian.nvim/wiki)。

---

> **请务必** 在使用前确认 Neovim 已编译 `+clipboard`、`+job` 等功能，以获得完整体验。祝你玩得开心!