---
title: yazi.nvim
---


# yazi.nvim - Neovim 插件集成 Yazi 文件管理器

**项目地址**  
[https://github.com/mikavilpas/yazi.nvim](https://github.com/mikavilpas/yazi.nvim)

## 概述
yazi.nvim 是一个专为 Neovim 设计的插件，它将可配置的文件管理器 Yazi 与 Neovim 无缝集成。通过插件可以在 Neovim 内部直接浏览文件、执行常见文件系统操作、预览文件内容，并保持编辑器状态与文件系统同步。

## 主要特性
| 功能 | 说明 |
|------|------|
| **一键打开 Yazi** | 在 Neovim 内启动完整的 Yazi UI，支持常见 Vim/Emacs 风格组合键。 |
| **文件/目录快速切换** | 通过 `<c-j> / <c-k>` 或 `hjkl` 在文件列表中移动，支持多层目录导航。 |
| **内置预览** | 选中文件时可即时预览（如图片、markdown 等），预览栏可持久化。 |
| **编辑器交互** | 直接在当前分屏或新窗口打开选中文件，支持 `Ctrl+o`（新窗口）及 `Enter`（覆盖）。 |
| **同步操作** | 复制、移动、删除等文件系统操作会实时刷新 Neovim 的缓冲区，保持 UI 一致。 |
| **可定制快捷键** | 提供默认映射，可在 `setup` 时通过 `keymaps` 字典自定义。 |
| **多终端会话** | 同一个 Yazi 进程可在不同 Neovim 窗口共享，避免重复启动。 |
| **命令插件** | 通过 Vim 命令与 Lua API 访问 Yazi，支持自定义脚本与插件扩展。 |

## 安装方式

> 推荐使用 packer.nvim 或 lazy.nvim 等插件管理器。

### packer.nvim

```lua
use {
  "mikavilpas/yazi.nvim",
  requires = { "rktjmp/lush.nvim" },  -- 如果需要 UI 主题
  config = function()
    require('yazi').setup()
  end
}
```

### lazy.nvim

```lua
{
  "mikavilpas/yazi.nvim",
  dependencies = { "rktjmp/lush.nvim" },
  config = true  -- 自动调用 require('yazi').setup()
}
```

> **注意**：Yazi 必须在系统 PATH 中可用，或者在插件配置中指定 `yazi_path`。

## 基本用法

| 按键/命令 | 功能 | 说明 |
|------------|------|------|
| `<leader>y`（或 `:Yazi`） | 打开 Yazi | 在当前窗口启动 Yazi 宽屏模式。 |
| `Enter` | 打开文件/目录 | 在分屏内打开目录或当前文件。 |
| `Ctrl+o` | 选中文件在新窗口打开 | 保持原窗口不变。 |
| `d` | 删除 | 删除选中文件，支持确认。 |
| `r` | 重命名 | 触发重命名交互。 |
| `p` | 复制 | 复制选中文件到剪贴板。 |
| `x` | 剪切 | 剪切选中文件到剪贴板。 |
| `v` | 预览 | 在右侧窗口预览选中文件。 |
| `q` | 关闭 Yazi | 退出 Yazi 并回到 Neovim。 |

## Lua API 使用示例

```lua
local yazi = require('yazi')

-- 以自定义宽度打开 Yazi
yazi.open({
  width = 120,
  height = 25,
  preview = true,
})

-- 在顶部行预览文件
yazi.open_in_split({
  vertical = true,
  preview = true,
})
```

## 配置示例

```lua
require('yazi').setup({
  -- Yazi 可执行文件路径(可选，如果已在 PATH 中则不必设置)
  yazi_path = "yazi",

  -- 预览选项
  preview = {
    -- 是否在选中文件时自动预览
    auto = true,
    -- 预览窗口高度 (行数)
    height = 12,
  },

  -- 缩进、箭头等 UI 自定义
  keymaps = {
    next = "<c-j>",
    prev = "<c-k>",
    exec = "<cr>",
    preview = "p",
  },

  -- 行内显示模式(如 previewer, split 等)
  mode = "split",
})
```

> 参考完整选项请查看 `lua/yazi/init.lua` 或官方 README。

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| Yazi 未启动 | 确认 `yazi` 可执行文件已安装，并且已加入 PATH，或在 `setup` 中指定 `yazi_path`。 |
| 打开文件无响应 | 检查是否在 `keymaps` 中冲突，或在 `:Yazi` 前加 `:silent`。 |
| 预览无法显示图片 | 需要安装 `ueberzug`（Linux）或 `w3m-img`（macOS）等支持库。 |

## 贡献与交流

- Issues：如果遇到 bug 或想讨论功能，可在 GitHub Issues 页面提出。
- PR：直接 Fork 并提交 Pull Request，遵循插件的代码风格即可。
- 社区：可在 Neovim 的 Discord/Telegram 群聊中讨论与使用体验。

---
**代码仓库**  
[https://github.com/mikavilpas/yazi.nvim](https://github.com/mikavilpas/yazi.nvim)
