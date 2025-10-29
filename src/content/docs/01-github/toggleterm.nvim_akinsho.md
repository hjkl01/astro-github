
---
title: toggleterm.nvim
---


# toggleterm.nvim

> 项目地址: <https://github.com/akinsho/toggleterm.nvim>

## 项目简介

**toggleterm.nvim** 是一个 Neovim Lua 插件，用于在当前窗口中快速切换、弹出和管理多终端。无需离开编辑器即可执行 shell 命令、启动 REPL、运行测试等。

---

## 主要特性

| 特色 | 简述 |
|------|------|
| **多终端管理** | 支持多窗口/分屏终端，您可以根据需要打开任意数量的终端实例。 |
| **键盘快捷键** | 默认按下 `Ctrl + \` 即可弹出或隐藏终端，支持自定义快捷键。 |
| **多种模式** | `horizontal`、`vertical`、`tab`、`float` 四种布局可自由切换。 |
| **分割自动关闭** | 终端关闭后自动隐藏相关窗口/栏，保持工作区整洁。 |
| **自定义命令** | 允许为每个终端实例指定默认启动命令，如 `bash`, `zsh`, `node`, `python` 等。 |
| **自动进入插入模式** | 终端启动时自动切换到 Insert 模式，射灵活** | 通过 Lua API 组合键盘映射，支持映射到 `vim.cmd`、`vim.api`。 |
| **与其他插件无冲突** | 通过 `<Tab>` 或其他快捷键可在终端和 Neovim 文本窗口之间自由切换。 |
| **可配置窗口尺寸** | 通过 `size` 选项自定义终端宽度或高度（占屏幕比例或像素）。 |
| **Tab 受支持** | 在 `max_height` 前置条件下可在 tab 里打开终端。 |

---

## 快速安装

> 以 **Packer** 为例：

```lua
use {
  'akinsho/toggleterm.nvim',
  config = function()
    require('toggleterm').setup()
  end
}
```

> 也可以使用 `vim-plug` 或 `lazy.nvim`（见插件文档）。

---

## 基本使用

1. **打开/隐藏终端**  
   默认快捷键 `Ctrl + \`  
   ```vim
   Ctrl + \
   ```
2. **切换到终端**  
   `Esc` 返回 Normal 模式后使用 `Ctrl + \` 交叉切换。  
3. **多终端实例**  
   `:ToggleTerm 1`、`:ToggleTerm 2` 等命令分别打开第 1、2 号终端。  
4. **在终端中执行命令**  
   直接输入 shell 命令即可。

---

## 高级配置

```lua
require('toggleterm').setup {
  size = 20,                     -- 终端尺寸：默认宽度为 20 列
  open_mapping = [[<c-\>]],     -- 自定义打开/关闭快捷键
  hide_numbers = true,           -- 隐藏行号
  shade_filetypes = {},          -- 使指定文件类型的窗口暗色
  shade_terminals = true,        -- 将终端窗口进行暗色处理
  shading_factor = 2,            -- 暗度，值越大越暗
  start_in_insert = true,        -- 启动时进入插入模式
  inserts = {                    -- 终端大小模式映射
    float = { direction = "float" },
    horizontal = { direction = "horizontal", size = 0.3 },
    vertical = { direction = "vertical", size = 0.3 },
  },
  direction = "float",            -- 默认方向
  close_on_exit = true,           -- 终端关闭时自动隐藏
  shell = vim.o.shell,            -- 终端默认 shell
}
```

**常见高级用法**:

| 用法 | 示例 |
|------|------|
| **自定义行号** | `hide_numbers = false` |
| **浮动终端自定义大小** | `size = function(term) return vim.o.lines * 0.4 end` |
| **自定义打开方向** | `direction = "vertical"` |
| **绑定自定义命令** | 在 `config` 里设置 `vim.api.nvim_buf_set_keymap(term.bufnr, 'n', 't', '<cmd>ToggleTermToggleAll<CR>', { noremap = true, silent = true })` |

---

## 贴士与技巧

- **在终端中打开相对路径**：`:w !nvim` 等等可在终端里直接编辑文件。  
- **键盘切换窗口**：终端与其他窗口均可使用 `Ctrl + h/j/k/l` 或默认的 `gt/;` 进行切换。  
- **多终端窗口**：在使用 `Ctrl + \` 之前输入 `:term` 可以手动打开任意终端实例。  
- **结合 NvimTree**：配合 `nvim-tree.lua` 使用时请保持终端在侧边栏外，以避免切换冲突。  

---

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| 终端窗口不按预期大小显示 | 确认 `size` 参数是否为数值或函数，根据屏幕宽高设置。 |
| 打开终端后不进入 Insert 模式 | 拷贝 `start_in_insert = true` 至配置中。 |
| 与其他插件键盘映射冲突 | 调整 `open_mapping` 至不冲突的组合键，例如 `Ctrl + t`。 |

---

## 结语

`toggleterm.nvim` 让 Neovim 拥抱终端，短暂离不开编辑轨道即可执行命令、运行脚本、跑测试，极大提升工作效率，适用于任何需要频繁交互终端的工作流。  

> 完整手册见: <https://github.com/akinsho/toggleterm.nvim>  

