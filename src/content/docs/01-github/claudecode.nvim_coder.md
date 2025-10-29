
---
title: claudecode.nvim
---


# claudecode.nvim

**项目地址**  
<https://github.com/coder/claudecode.nvim>

---

## 主要特性

| 功能 | 描述 |
|------|------|
| ✅ 多编码解码 | 支持 Base64、Hex、Quoted-Printable、URL 编码、Gzip 等多种常见编码的解码 |
| 🔎 交互式解码 | 通过 Telescope / FZF 快速搜索要解码的区域或字符串 |
| 📁 快速预览 | 将解码结果在新 buffer、split 或 quickfix 列表中展示，支持滚动与跳转 |
| 🎛️ 可配置映射 | `g:claudecode_default_keymap` 可自定义触发命令的快捷键 |
| 🌐 CLI 集成 | 可以直接使用 `:ClaDecode` 等命令，在当前行、选区或光标所在位置解码 |
| 🧩 插件化扩展 | 通过 `claudecode#add_decoder()` 轻松添加自定义解码器 |
| 🔄 双向编码解码 | 同一插件内支持 `encode` 操作，命令 `:ClaEncode` |

---

## 常用命令

| 命令 | 用途 | 备注 |
|------|------|------|
| `:ClaDecode [encoding]` | 解码当前行 / 选区 | 如果不指定编码，会自动检测 |
| `:ClaEncode [encoding]` | 对当前行 / 选区进行编码 | 支持前述同类型编码 |
| `:ClaDecodeInteractive` | 交互式选择目标文本 | 需要 Telescope/FZF |
| `:ClaDecodeShow` | 在 quickfix 列表显示解码结果 | 直接跳转查看 |
| `:ClaReset` | 清空所有临时缓冲 | 释放内存 |

---

## 安装示例

```lua
-- packer.nvim
use {
  'coder/claudecode.nvim',
  config = function()
    require('claudecode').setup {
      -- 可选配置
      show_in_split = true,   -- 结果显示在 split 窗口
      keymap = {             -- 自定义映射
        decode = '<leader>cd',
        encode = '<leader>ce',
      },
    }
  end
}
```

---

## 配置示例

```lua
require('claudecode').setup({
  auto_detect = true,        -- 自动检测编码类型
  min_length = 5,            -- 结果最小长度阈值
  highlight = true,          -- 在结果窗口高亮显示
  encoders = {                -- 自定义编码器
    json = function(content)
      return vim.fn.json_encode(vim.fn.json_decode(content))
    end,
  },
  decoders = {                -- 自定义解码器
    json = function(content)
      return vim.fn.json_encode(vim.fn.json_decode(content))
    end,
  },
})
```

---

## 示例流程

1. **选中** 一段 Base64 编码的日志。
2. 输入 `:ClaDecode`（或 `<leader>cd` 触发快捷键）。
3. 结果在新窗口弹出，**双击** 行即可跳转查看原始文本。
4. 若需对结果再编码，可使用 `:ClaEncode gzip`。

---

**说明**  
本插件专注于快速解码与编码，支持多种类型，同时保持轻量且可配置。若遇到新的编码方式，只需在 `decoders` / `encoders` 中添加即可扩展。