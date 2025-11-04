
---
title: lazy.nvim
---


# lazy.nvim - 按需加载 Neovim 插件

地址: https://github.com/folke/lazy.nvim

---

## 1. 概述
lazy.nvim 是一款轻量、按需加载的 Neovim 插件管理器。它使用 Lua 编写，旨在提供更快的启动速度、更简洁的插件配置和更高的可维护性。相比传统插件管理器，lazy.nvim 侧重于：
- 仅在需要时加载插件
- 支持插件之间的依赖关系管理
- 提供多种触发机制（按键、文件类型、事件等）
- 自动化懒加载与插件更新

---

## 2. 主要特性

| 特性 | 说明 |
|------|------|
| **懒加载** | 通过指定 `event`、`cmd`、`keys`、`ft` 等键值延迟加载。 |
| **插件依赖** | 通过 `dependencies` 指定插件间依赖，自动按顺序加载。 |
| **自动更新** | `lazy = true` 时会在 `:Lazy sync` 中自动更新所有插件。 |
| **简化配置** | 支持大部分插件的默认配置，只需极少代码即可使用。 |
| **多种加载方式** | `event`, `cmd`, `keys`, `ft`, `cond` 等多种触发方式。 |
| **高可用** | 内置错误捕获与回退策略，保证 Neovim 进程稳定。 |
| **插件升级** | 内置 `:Lazy update`, `:Lazy check`, `:Lazy sync` 等命令。 |
| **多引擎兼容** | `packer`, `vim-plug`, `dein` 皆可与之对接，兼容性好。 |
| **可组合插件** | 通过 `opts` 与 `config` 组合插件配置表；支持返回函数。 |

---

## 3. 快速上手

### 3.1 安装

```bash
# 使用 git 直接克隆到 Neovim 插件目录
git clone https://github.com/folke/lazy.nvim.git ~/.local/share/nvim/site/pack/lazy/start/lazy.nvim
```

> `~/.local/share/nvim/site/pack/lazy/start/` 为 Neovim 默认的插件目录。

### 3.2 基本配置

在 `init.lua` 或 `lua/setup.lua` 中添加：

```lua
require('lazy').setup({
  -- 示例插件：nvim-treesitter
  { "nvim-treesitter/nvim-treesitter", run = ":TSUpdate", lazy = true },

  -- 示例插件：nvim-cmp（完成框架）
  { "hrsh7th/nvim-cmp" },

  -- 示例插件：telescope.nvim（模糊查找）
  { "nvim-telescope/telescope.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    cmd = "Telescope",
    opts = { defaults = { layout_strategy = "vertical" } },
  },

  -- 示例插件：lualine.nvim（状态栏）
  { "nvim-lualine/lualine.nvim",
    cond = function() return vim.o.termguicolors end,
    config = function()
      require('lualine').setup { options = { theme = 'gruvbox' } }
    end,
  },

  -- 单行安装其他插件
  "neovim/nvim-lspconfig",
  { "williamboman/mason.nvim", lazy = false }, -- 需要立即加载
})
```

*注：`setup` 接受一个表格，支持多种字段：`lazy`, `cmd`, `keys`, `ft`, `cond`, `dependencies`, `config`, `opts`, `run` 等。*

### 3.3 常用命令

| 名称 | 功能 | 用法 |
|------|------|------|
| `:Lazy` | 查看插件状态 | `:Lazy` |
| `:Lazy sync` | 同步插件（安装/删除/更新） | `:Lazy sync` |
| `:Lazy update` | 更新插件 | `:Lazy update` |
| `:Lazy check` | 检测插件更新 | `:Lazy check` |
| `:Lazy clear` | 清除懒加载缓存 | `:Lazy clear` |

---

## 4. 典型用法示例

### 4.1 按文件类型加载

```lua
{ "pangloss/vim-javascript",
  ft = { "javascript", "javascriptreact", "typescriptreact" },
}
```

### 4.2 按键触发加载

```lua
{ "tpope/vim-fugitive",
  keys = {
    { "<leader>gg", "<cmd>Git<CR>", desc = "Git status" },
  },
}
```

### 4.3 条件加载

```lua
{ "kylechui/nvim-surround",
  cond = function()
    return vim.fn.has("nvim-0.8.1") == 1
  end,
}
```

### 4.4 链式配置

```lua
{ "gruvbox-community/gruvbox", config = function()
    vim.o.background = "dark"
    vim.cmd([[colorscheme gruvbox]])
  end
}
```

---

## 5. 常见问题

- **为什么启动变慢？**  
  确认插件是否都设置了 `lazy = true` 或者合适的触发方式；若有插件没有懒加载，尝试手动开启。

- **如何查看插件查看错误？**  
  启用 `:Lazy` 页面，点击 `Errors` 列表即可查看已报错的插件。

- **想用 `packer.nvim` 兼容？**  
  lazy.nvim 自带 `packer` 兼容方案：  
  ```lua
  require('lazy').setup({
    -- your pugin config here
  }, { trades = { 'packer' } })
  ```

--- 

**简而言之**：lazy.nvim 通过声明式配置，极大提升 Neovim 启动速度与插件管理体验。只需少量代码即可实现按需加载、依赖管理、自动更新等高级功能，适合现代 Neovim 用户。祝玩得开心!

