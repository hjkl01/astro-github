---
title: nvim-tree.lua
---

# nvim-tree.lua

[GitHub 项目地址](https://github.com/nvim-tree/nvim-tree.lua)

## 主要特性

- **文件资源管理器**：在 Neovim 中集成树形文件浏览器，支持快速定位、打开、编辑文件。
- **多功能操作**：新建、删除、重命名文件/文件夹；移动、复制、粘贴文件。
- **同步工作区**：`NvimTreeFindFile` 自动定位并打开当前文件。
- **图标与主题**：支持自定义文件图标、颜色主题，可与 `nvim-web-devicons` 配合使用。
- **同步与插件**：可与其他插件（如 Telescope、fzf 等）无缝配合。
- **可配置性强**：通过 Lua 配置文件自定义行为、快捷键、视窗尺寸等。

## 功能概览

| 功能 | 说明 | 默认快捷键 |
|------|------|------------|
| 打开/关闭 | 切换树视图 | `:NvimTreeToggle` |
| 同步当前文件 | 跟随光标定位 | `:NvimTreeFindFile` |
| 打开 | 双击/回车 | `l`、`o`、`Enter` |
| 新建 | 新建文件/文件夹 | `a`（file）/`A`（folder) |
| 删除 | 删除文件/文件夹 | `d` |
| 重命名 | 重命名 | `r` |
| 复制/粘贴 | 复制路径、粘贴 | `yy`、`p` |
| 展开/收起 | 切换子节点 | `u`（up）/`o`（open） |
| 搜索 | 模糊查询 | `/` |
| 刷新 | 更新文件列表 | `R` |

## 安装与配置

```lua
-- 使用 packer.nvim 作为依赖管理器示例
require('packer').startup(function()
  use {
    'nvim-tree/nvim-tree.lua',
    requires = { 'nvim-tree/nvim-web-devicons' }, -- 可选，提供图标
    config = function()
      require'nvim-tree'.setup {
        disable_netrw       = true,
        hijack_netrw        = true,
        open_on_setup       = false,
        sync_root_with_cwd  = true,
        update_focused_file = { enable = true },
        view = {
          width = 30,
          side = 'left',
          auto_resize = true
        }
      }
    end
  }
end)
```

- **安装图标插件**（可选）:
  ```lua
  use { 'nvim-tree/nvim-web-devicons', config = function() require'nvim-web-devicons'.setup { default = true } end }
  ```

- **快捷键映射**（自定义）:
  ```lua
  vim.api.nvim_set_keymap('n', '<leader>e', ':NvimTreeToggle<CR>', { noremap = true, silent = true })
  ```

## 用法示例

```bash
# 打开 nvim，自动显示文件树
nvim .
# 通过命令切换树
: NvimTreeToggle
# 让树随当前文件定位
: NvimTreeFindFile
```

> **提示**：在多数现代 Neovim 配置中，`nvim-tree.lua` 与 `telescope.nvim`、`fzf-lua` 等插件共同使用，提供更丰富的文件搜索和管理体验。

---
这样即可在 `src/content/docs/00/nvim-tree.lua_nvim-tree.md` 保存以上内容。