
---
title: nvim-web-devicons
---


# nvim-web-devicons

> GitHub 地址: https://github.com/nvim-tree/nvim-web-devicons

## 简介
`nvim-web-devicons` 是一个为 Neovim 提供文件类型图标的插件。它基于 Nerd Fonts，利用 Unicode 字符与字体图标，在文件树、状态栏、代码提示等场景中为不同类型文件展示精美图标。该插件是多款 Neovim 生态插件（如 `nvim-tree.lua`, `telescope.nvim`, `lualine.nvim` 等）的共享依赖。

## 主要特性
- **多平台支持**：兼容 neovim 0.5+，支持 Linux / macOS / Windows 终端或 GUI 客户端。
- **高性能**：使用 Lua 写成，启动速度快。
- **可自定义**：用户可通过 Lua API 注册、修改或定义图标颜色。
- **主题友好**：默认提供多套流行图标主题（Meteor、Catppuccin、Gruvbox 等），可在 `devicons.mappings` 中切换。
- **自动更新**：与 `nvim-tree.lua` 等插件一起自动更新所使用的图标映射。

## 主要功能
- **注册图标**  
  `devicons.register("lua", {"", "#51afef"})`  
  为指定文件后缀或 `filetype` 注册自定义图标与颜色。

- **获取图标**  
  `devicons.get_icon("main.rs", "rust", "❓", "#FF5733")`  
  根据文件名、文件类型或回退参数返回图标与颜色。

- **获取所有图标映射**  
  `devicons.get_icons()`  
  返回当前已注册的完整映射表。

- **调试信息**  
  `devicons.set_log_level("debug")`  
  可视化调试日志。

## 用法

### 安装
以 `packer.nvim` 为例：
```lua
use {
  'nvim-tree/nvim-web-devicons',
  config = function()
    -- 默认即可使用
  end
}
```

### 基本使用
```lua
local devicons = require('nvim-web-devicons')

-- 1. 自动获取图标（最常用）
local icon, color = devicons.get_icon('init.lua', 'lua', '❓', '#607d8b')
print(icon, color)   --   #51afef

-- 2. 注册自定义图标
devicons.register('magic', {
  icon = "🌈",
  color = "#DAF7A6",
})

-- 3. 在 nvim-tree 中集成
require('nvim-tree').setup{
  renderer = {
    icons = {
      show = {
        git = true,
        file = true,
        folder = true,
        file = true,
      },
      glyphs = {
        default = devicons.get_icon('file', 'text'),
        symlink = devicons.get_icon('symlink', 'link'),
        -- ...其他图标配置
      }
    }
  }
}
```

### 常见配置
```lua
-- 禁用所有图标（仅文件名显示）
devicons.set_default_icon('')

-- 更改默认颜色
devicons.set_color_scheme('gruvbox')

-- 只在特定插件使用
require('nvim-tree').setup{
  renderer = {
    icons = { show = { file = true, folder = true } }
  }
}
```

### 兼容性
- **终端**：请确保使用支持 TrueColor 的终端（如 iTerm2、Alacritty、Windows Terminal 等），否则可能出现颜色失真。
- **GUI**：如 Neovide、goneovim 也能直接使用，无需额外配置。

---

> 以上信息摘自官方文档及使用案例，供快速上手与参考。若需更深层自定义，请参阅插件 `README.md` 与 `api.md`。