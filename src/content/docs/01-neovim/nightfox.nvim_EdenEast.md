
---
title: nightfox.nvim
---

# nightfox.nvim – EdenEast

> **GitHub 项目地址**  
> https://github.com/EdenEast/nightfox.nvim

---

## 📋 项目概述  
`nightfox.nvim` 是一款为 Neovim 设计的 **多风格配色方案** 插件。它提供了多种主题（`nightfox`、`dayfox`、`terafox`、`carbonfox` 等），旨在兼容丰富的插件生态，支持各种高亮组、语法、终端与 GUI 渲染，适用于日间与夜间工作场景。

---

## 🌟 主要特性

| 特性 | 说明 |
|------|------|
| **多主题** | 预置 4+ 个主题，支持即时切换，满足不同光照环境需求。 |
| **插件友好** | 自动为常用插件（如 Telescope、NvimTree、Lualine、GitSigns、Treesitter 等）补全高亮组，保持配色一致。 |
| **高亮细节** | 丰富的终端与 GUI 兼容性，支持 256 色、true‑color 与 background 透明。 |
| **配置灵活** | 通过 Lua table 自定义颜色、补全选项、插件高亮、透明度、亮度等。 |
| **轻量 & 性能** | 仅使用 Lua，无额外依赖，加载速度快。 |
| **可扩展** | 通过 `nightfox.nvim` 的 API 自定义主题或添加新主题。 |
| **文档完备** | 详细 README 与示例，快速上手。 |

---

## ⚙️ 安装

> 推荐使用 [Packer](https://github.com/wbthomason/packer.nvim) 或其他插件管理器。

```lua
-- packer.nvim 示例
use {
  'EdenEast/nightfox.nvim',
  config = function()
    require('nightfox').setup()  -- 默认配置
    vim.cmd('colorscheme nightfox')  -- 默认主题
  end
}
```

也可以直接克隆到 `~/.config/nvim/plugged/nightfox.nvim` 并手动 `:so`。

---

## 📦 基本使用

```lua
-- 设置主题
vim.cmd('colorscheme nightfox')          -- nightfox
vim.cmd('colorscheme dayfox')            -- dayfox
vim.cmd('colorscheme terafox')           -- terafox
vim.cmd('colorscheme carbonfox')         -- carbonfox

-- 切换主题（可在命令行或 Lua 中调用）
vim.cmd('colorscheme nightfox')
```

---

## ⚙️ 配置示例

```lua
require('nightfox').setup({
  options = {
    transparent = true,          -- 透明背景
    terminal_colors = true,      -- 设置终端颜色
    dim_inactive = false,        -- 是否暗化非活动窗口
    styles = { comments = 'italic' }, -- 高亮样式
  },
  palettes = {
    nightfox = {
      bg0 = '#1a1b26',
      fg0 = '#c0caf5',
      -- 可自定义更多颜色
    }
  },
  groups = {
    TelescopeNormal = { fg = '#c0caf5', bg = '#1a1b26' },
    -- 自定义插件高亮
  }
})
```

> **提示**：`nightfox.setup()` 需要在 `colorscheme` 之前调用。

---

## 🗂️ 主题列表

| 主题 | 适用场景 | 特色 |
|------|----------|------|
| `nightfox` | 夜间 | 经典深色调 |
| `dayfox` | 白天 | 轻量明亮 |
| `terafox` | 高对比 | 强调代码结构 |
| `carbonfox` | 低饱和 | 柔和配色 |
| `auto` | 自动 | 根据时间切换 `nightfox`/`dayfox` |

> 通过 `vim.cmd('colorscheme auto')` 可开启自动切换。

---

## 🔌 插件集成

插件 | 解决方案 |
------|----------|
Telescope | 自动补全 `TelescopePromptBorder` 等 |
NvimTree | 自动高亮 `NvimTreeNormal` |
Lualine | 自动匹配 `lualine_*` |
GitSigns | 自动匹配 `GitSigns_*` |
Treesitter | 自动高亮 `@comment` 等 |
NeoTree | 自动匹配 `NeoTreeNormal` |
BlackHole | 自动匹配 `BlackHole` |
... | 更多已内置，无需额外配置 |

> 若插件不在列表中，可自行在 `groups` 中添加对应高亮。

---

## 🎨 自定义主题

1. **复制已有主题**  
   ```lua
   require('nightfox').setup({
     palettes = {
       mytheme = vim.deepcopy(require('nightfox.palette').nightfox)
     },
     groups = {
       -- 覆盖已有高亮或添加新高亮
     }
   })
   ```
2. **修改颜色**  
   在 `palettes` 里更改对应键值，例如 `bg0`, `fg0` 等。
3. **修改高亮组**  
   在 `groups` 里指定 `MyGroup = { fg = '#ff0000', bg = '#000000' }`。

---

## 📌 贡献 & 维护

- **Issues**：提交 bug 或功能建议。  
- **PR**：欢迎提交主题改进、插件支持等 PR。  
- **文档**：README 中已提供详细使用说明，必要时可新增 `docs`。

---

## 📄 参考

- [官方 README](https://github.com/EdenEast/nightfox.nvim/blob/master/README.md)  
- [主题示例](https://github.com/EdenEast/nightfox.nvim/blob/master/preview.png)  

---