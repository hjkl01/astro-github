---
title: oil.nvim
---

# oil.nvim（stevearc）

**仓库地址**: <https://github.com/stevearc/oil.nvim>

## 主要特性

| 特性 | 说明 |
|------|------|
| **文件树视图** | 在 Neovim 窗口左侧（或任意位置）显示当前目录的树形结构，支持懒加载。 |
| **快速跳转** | `:Oil` 命令可切换到油视图，`<C-o>` 快捷键可在文件间快速跳转。 |
| **文件操作** | 右键（或 `gx`）可对文件执行打开、删除、复制、移动等操作。 |
| **Git 状态集成** | 自动显示文件/目录的 Git 状态（新增、修改、删除等）。 |
| **多功能过滤** | 支持正则过滤、隐藏文件与隐藏目录配置。 |
| **异步加载** | 目录读取与文件操作均非塞，提升编辑器响应速度。 |
| **键位映射自定义** | 通过 `oil.defaults.keymaps` 可自定义多种 UI 操作键位。 |
| **多窗格支持** | 可与 `bufremove`、`split` 等命令一起使用，保持可视化窗口状态。 |
| **可配置 UI 主题** | 提供多种颜色组，易于与其它插件或配色方案集成。 |
| **使用 API** | 允许插件开发者通过 Lua 脚本调用 `require('oil').open()` 等 API。 |

## 快速上手

```lua
-- lazy.nvim 示例
{
  "stevearc/oil.nvim",
  opts = {
    -- 目录图标
    default_file_text = "File",
    show_label = true,

    -- Git 状态颜色
    git_status_colors = {
      added = "green",
      modified = "yellow",
      deleted = "red",
    },

    -- 快捷键配置
    keymaps = {
      ["<CR>"] = "edit",
      ["<C-s>"] = "split",
      ["<C-v>"] = "vsplit",
      ["<C-x>"] = "close",
    },
  },
  cmd = "Oil",      -- 仅在执行 :Oil 时加载
  keys = { "<leader>oo", "<cmd>Oil<CR>", desc = "Open Oil file explorer" },
},
```

### 关键命令与键位

- `:Oil`：打开文件树视图。  
- `<C-o>`：在文件树中打开选中文件。  
- `gx` / `gX`：在树中执行打开/删除等操作。  
- `gd`：跳转到文件所在目录。  
- `:Oil /path/to/dir`：直接打开指定目录。  

## 配置示例（Lua）

```lua
-- init.lua 或 plugins/oil.lua
require('oil').setup({
  columns = {"icon", "name", "size"},   -- 列显示顺序
  win_options = {winblend = 0, number = false},
  height = 30,                          -- 视图高度
  width = 40,                           -- 视图宽度
})
```

## 常见用途

1. **文件管理**：快速打开、移动、复制或删除文件。  
2. **版本控制**：一眼即可看到 Git 状态。  
3. **多目录工作**：同时打开项目、缓存或配置文件夹的树形结构。  
4. **配合 Telescope**：在 `telescope.builtin.files` 里使用 `action = "oil"` 直接进入油视图。  

## 结语

`oil.nvim` 用直观的树形界面替代传统命令行文件浏览，使 Neovim 的文件管理与现代编辑器保持一致。通过简洁的 API 与高度可定制的键位映射，适合从新手到高级用户的各种工作流程。