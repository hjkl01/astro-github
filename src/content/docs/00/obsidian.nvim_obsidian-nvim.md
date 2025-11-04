
---
title: obsidian.nvim
---

# Obsidian.nvim

GitHub: https://github.com/obsidian-nvim/obsidian.nvim

## 主要特性

| 功能 | 说明 |
|------|------|
| **笔记管理** | 通过 `:ObsidianDaily`, `:ObsidianNew`, `:ObsidianOpen` 等命令快速创建、打开笔记。 |
| **每日笔记** | 自动生成今日笔记文件（支持自定义路径与模板）。 |
| **标签导航** | 利用 `:ObsidianTags`（或 Telescope）展示并跳转到标签。 |
| **反链视图** | `:ObsidianBacklinks`/`ToggleBacklinks` 打开/关闭当前笔记的反链列表。 |
| **全局搜索** | `:ObsidianSearch` 为 Obsidian 卷提供全文检索。 |
| **集成 Telescope** | 选项 `telescope` 通过 fuzzy finder 搜索、筛选标签、反链等。 |
| **自定义 Hook** | 用户可在每个关键流程（如新建、打开等）添加前后 Hook。 |
| **快捷键绑定** | 支持自定义键位，默认映射以 `gr` 开头，例如 `grr` 开启反链。 |

## 功能细节

1. **创建与打开笔记**  
   - `:ObsidianNew <name>` 用 `<name>` 创建新笔记。  
   - `:ObsidianOpen <name>` 打开已有笔记。  
   - `:ObsidianOpenPrompt` 在命令行提示输入笔记名。

2. **每日笔记**  
   - `:ObsidianDaily` 创建或打开今日笔记。  
   - 通过 `require("obsidian").new()` 可获取 `ObsidianDaily` 相关信息。

3. **标签与反链**  
   - `:ObsidianTags` 列出所有标签并跳转。  
   - `:ObsidianToggleBacklinks` 切换当前文件的反链显示。

4. **搜索**  
   - `:ObsidianSearch <query>` 在 Obsidian 卷中搜索。  
   - `:ObsidianSearchAll <query>` 搜索所有文件与标签。

5. **Telescope 集成**  
   - `telescope.search_note()` 搜索笔记文件。  
   - `telescope.search_tag()` 搜索标签。  
   - `telescope.search_backlinks()` 搜索反链。

## 用法示例

```lua
-- init.lua / init.vim
require("obsidian").setup({
  dir = "~/vault",              -- Obsidian 卷路径
  notes_subdir = "思维地图",    -- 默认子目录
  daily_notes = {
    folder = "日记",
    date_format = "%Y-%m-%d",
    template = "模版/每日.md",
  },
  mappings = {
    -- 默认快捷键
    ["grr"] = { action = "toggle_backlinks", mode = "n" },
    ["grt"] = { action = "tags", mode = "n" },
  },
  attachments = {
    image_path = "images",  -- 附件存放路径
  },
})
```

```vim
" 按键设置 (可选)
nnoremap grr :ObsidianToggleBacklinks<CR>
nnoremap grt :ObsidianTags<CR>
```

### 完整使用流程

1. **安装插件**  
   使用 plugin manager（如 lazy.nvim、packer.nvim、vim-plug 等）。  
   ```lua
   use { "obsidian-nvim/obsidian.nvim", branch = "main", requires = { "nvim-lua/plenary.nvim" } }
   ```

2. **配置**  
   按上述示例将 `obsidian.nvim` 配置在 `init.lua` 或 `init.vim`。

3. **打开/创建笔记**  
   - `:ObsidianNew ProjectPlan`  → 新建 ProjectPlan.md  
   - `:ObsidianOpen ProjectPlan`  → 打开 ProjectPlan.md  
   - `:ObsidianDaily`  → 打开 `日记/2025-11-01.md`

4. **标签与反链**  
   - `:ObsidianTags` 或 `grt`  → 列表选择并跳转  
   - `:ObsidianToggleBacklinks` 或 `grr`  → 切换反链视图

5. **搜索**  
   - `:ObsidianSearch 思维`  → 在笔记内搜索“思维”  

6. **Telescope**  
   - `<leader>gb` → Telescope 搜索反链  
   - `<leader>gt` → Telescope 搜索标签  

这样即可在 Neovim 内流畅地管理 Obsidian 卷，享受笔记编写与维护的高效体验。