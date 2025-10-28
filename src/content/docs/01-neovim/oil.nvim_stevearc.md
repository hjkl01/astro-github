
---
title: oil.nvim
---

# oil.nvim

**项目地址**: <https://github.com/stevearc/oil.nvim>

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **文件浏览器** | 替代 `netrw`，以 Neovim 原生 UI 方式展示目录树。 |
| **多窗口支持** | 可以在浮动窗口、垂直 split、水平 split、或者普通缓冲区显示。 |
| **快捷键导航** | 默认使用 `h/l`、`j/k`、`Enter`、`gh` 等常用 Vim 键位，支持快速切换。 |
| **文件操作** | `dd` 删除、`yy` 复制、`p` 粘贴、`x` 重命名、`mkdir` 新建目录、`rm -r` 删除目录等。 |
| **自定义排序/过滤** | 可按字母、大小、时间、文件类型等排序；支持正则过滤隐藏文件。 |
| **可配置性** | 通过 `require('oil').setup{}` 完全可定制键位、外观、行为。 |
| **文件预览** | 按 `p` 或 `Ctrl+P` 可预览文件内容。 |
| **多标签页支持** | 每个目录打开一个油窗口，支持标签切换。 |
| **外部插件集成** | 与 `nvim-tree.lua`、`telescope.nvim` 等插件兼容。 |
| **远程文件浏览** | 通过 `oil://ssh://user@host/` 等 URI 访问远程文件系统。 |

---

## 安装

使用 `lazy.nvim`（或任何你喜欢的插件管理器）：

```lua
{
  'stevearc/oil.nvim',
  opts = {},          -- 这里可以传递默认配置
  keys = {            -- 快捷键映射（可根据需要自行修改）
    { "<leader>e", "<cmd>Oil<CR>", desc = "Open Oil" },
  },
}
```

或者使用 `packer.nvim`：

```lua
use {
  'stevearc/oil.nvim',
  config = function()
    require('oil').setup{}
  end
}
```

---

## 基本用法

| 命令 | 说明 |
|------|------|
| `:Oil` | 打开当前工作目录的油窗口。 |
| `:Oil .` | 打开当前缓冲区所在目录。 |
| `:Oil ..` | 打开父目录。 |
| `:Oil <path>` | 打开指定路径。 |
| `:Oil --float` | 以浮动窗口方式打开。 |
| `:Oil --vertical` | 垂直 split 打开。 |
| `:Oil --horizontal` | 水平 split 打开。 |

### 典型键盘操作

- `h` / `l` / `j` / `k` – 目录/文件移动
- `Enter` – 打开文件/进入目录
- `gh` – 返回上级目录
- `dd` – 删除文件/目录
- `yy` – 复制路径
- `p` – 粘贴路径
- `x` – 重命名
- `r` – 刷新
- `q` – 关闭油窗口

> 你可以在 `oil.setup` 中通过 `keymaps` 字段自定义或禁用任何键位。

---

## 高级配置

```lua
require('oil').setup({
  -- 关闭默认键位，改用自定义
  skip_confirm_for_simple_edit = true,
  view_options = {
    show_hidden = true,          -- 显示隐藏文件
    sort = "case_insensitive",   -- 按字母顺序排序
  },
  keymaps = {
    ["<C-]>"] = "actions.select",
    ["<C-^>"] = "actions.toggle_preview",
    -- 仅保留 Enter 和 gh
    ["h"] = "",  ["l"] = "", ["j"] = "", ["k"] = "",  -- 清除默认
  },
  win_options = {
    winblend = 10,   -- 浮动窗口透明度
  },
  -- 远程文件系统支持
  remote = {
    ssh = { port = 22 },
  },
})
```

### 示例：在浮动窗口中打开当前文件所在目录

```lua
vim.keymap.set('n', '<leader>of', function()
  require('oil').open_float(vim.fn.expand('%:p:h'))
end, { desc = 'Open Oil in floating window' })
```

---

## 与 Telescope 结合

```lua
require('telescope').load_extension('oil')
```

然后可以使用 `:Telescope oil` 来快速搜索和打开文件。

---

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| **油窗口无法关闭** | 按 `q` 或 `x`，如果失效请检查 `keymaps` 配置。 |
| **远程文件浏览不工作** | 确认 `ssh` 访问可用，且 `oil.nvim` 版本已支持 `remote`。 |
| **文件显示不完整** | 在 `oil.setup` 中开启 `view_options.show_hidden = true` 或调整 `win_options.wrap = false`。 |

---

## 结语

`oil.nvim` 让 Neovim 的文件浏览体验更像现代 IDE 的侧边栏，兼具速度、可定制性和与原生 UI 的无缝集成。通过简单的配置即可替代传统的 `netrw`，并在日常开发中提供更高效的文件管理方式。祝你玩得愉快！

---