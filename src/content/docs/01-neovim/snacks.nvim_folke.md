
---
title: snacks.nvim
---


# snacks.nvim

> GitHub 地址: <https://github.com/folke/snacks.nvim>

---

## 简介
`snacks.nvim` 是一个极简 Neovim 插件，提供统一的 API 用于注册 **动作**（action）、**命令**（command）、**键映射**（keymap）以及 **自动命令**（autocmd）。核心目标是让插件配置更简洁、可复用。

---

## 核心概念

| 术语 | 说明 |
|------|------|
| **Action** | 一个可复用的功能函数，支持参数化。 |
| **Command** | 通过 Action 自动生成的 Vim 命令。 |
| **Keymap** | 通过 Action 自动生成的键映射。 |
| **Group** | 用于把相关的 Action/Command/Keymap/Autocmd 归类，便于管理与卸载。 |

---

## 主要功能

| 功能 | 说明 |
|------|------|
| **统一注册 API** | `snacks.register()` 一次性注册 action、command、keymap、autocmd。 |
| **可复用 Action** | 同一 Action 可绑定多个命令或键映射，避免重复代码。 |
| **自动完成** | 对命令提供自动补全，支持自定义补全函数。 |
| **灵活选项** | 支持 `noremap`, `silent`, `expr`, `buffer`, `silent!` 等常用 Vim 选项。 |
| **组管理** | `snacks.group(name)` 创建组，所有绑定可一次性移除。 |
| **简易配置** | 通过 Lua 表格描述所有绑定，便于维护。 |

---

## 安装

```lua
-- 使用 packer.nvim
use {
  'folke/snacks.nvim',
  config = function()
    require('snacks').setup()
  end
}
```

---

## 使用方法

### 1. 注册 Action

```lua
local snacks = require('snacks')

snacks.register({
  name = 'toggle_line_numbers',
  action = function(opts)
    vim.o.number = not vim.o.number
  end,
  desc = 'Toggle line numbers',
})
```

### 2. 创建命令

```lua
snacks.register({
  command = 'ToggleNumbers',
  action = 'toggle_line_numbers',
  desc = 'Toggle line numbers',
  nargs = 0,
})
```

### 3. 创建键映射

```lua
snacks.register({
  keymap = { 'n', '<leader>ln', 'toggle_line_numbers' },
  desc = 'Toggle line numbers with <leader>ln',
})
```

### 4. 自动命令

```lua
snacks.register({
  autocmd = {
    event = 'BufRead',
    pattern = '*.md',
    command = 'ToggleNumbers',
  },
})
```

### 5. 组管理

```lua
local grp = snacks.group('my_plugin')

grp:register({
  command = 'MyCmd',
  action = function() print('Hello!') end,
  desc = 'My command',
})

-- 在需要时卸载整个组
grp:unregister()
```

---

## 代码结构

- `src/init.lua` – 插件入口，注册 API 与默认配置。  
- `src/snacks.lua` – 核心实现，处理注册与组管理。  
- `src/utils.lua` – 辅助函数，如补全、错误处理等。

---

## 贡献与维护

- 代码遵循 `lspconfig` 风格，易于阅读。  
- 通过 PR 或 Issue 反馈问题；欢迎提交功能建议。  

---  

**注**：上述示例仅展示基本用法，完整功能请参考官方文档与源码。  
