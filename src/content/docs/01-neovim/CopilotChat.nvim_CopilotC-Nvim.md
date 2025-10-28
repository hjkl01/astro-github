
---
title: CopilotChat.nvim
---

# CopilotChat.nvim（CopilotC-Nvim）  
> 访问地址: <https://github.com/CopilotC-Nvim/CopilotChat.nvim>

## 概述  
CopilotChat.nvim 是一个将 GitHub Copilot Chat 与 Neovim 深度集成的插件。它在 Neovim 内部提供 Chat 界面，支持：

- 代码生成与改写  
- 代码解释与对话  
- 上下文感知（自动注入文件内容、光标上下文）  
- 输出代码直接插入编辑器或打开新缓冲区  
- 语法高亮和格式化（User 或 LSP 支持）  
- 可配置的执行方式（Normal/Insert 模式）

---

## 安装

使用 **packer.nvim**（示例）：

```lua
use {
  'CopilotC-Nvim/CopilotChat.nvim',
  requires = { 'nvim-lua/plenary.nvim', 'nvim-telescope/telescope.nvim' }, -- 可选
  config = function()
    require('CopilotChat').setup {
      -- 你可以在此添加自己的配置
    }
  end
}
```

> 其他插件管理器：`lazy.nvim`、`vim-plug`、`dein` 等，只需把仓库地址添加到插件列表即可。

---

## 基础使用

### 打开 Chat 窗口  
```vim
:CopilotChatOpen
```
或者使用快捷键（如果你在 `setup` 中定义了映射）：

```vim
nnoremap <leader>ss <Cmd>CopilotChatOpen<CR>
```

### 与 Copilot Chat 对话  

- **输入**：在 chat 窗口中键入提示，然后 <kbd>Enter</kbd>  
- **回复**：插件调用 Chat API，返回代码或解释  
- **执行**：默认打开新缓冲区；使用 `:CopilotChatInsert` 可以直接插入光标位置（Normal / Insert 模式）  

### 执行模式  
```lua
require('CopilotChat').setup {
  default_action = 'open', -- 'open', 'insert'
  -- 其它选项...
}
```

---

## 命令

| 命令 | 说明 |
|------|------|
| `:CopilotChatOpen` | 打开 Chat 窗口 |
| `:CopilotChatInsert` | 将结果插入光标位置 |
| `:CopilotChatToggle` | 打开/关闭 Chat 窗口 |
| `:CopilotChatClear` | 清空聊天记录 |
| `:CopilotChatClose` | 关闭 Chat 窗口 |

---

## 配置示例

```lua
require('CopilotChat').setup {
  default_action = 'insert',              -- 默认直接插入
  open_width = 80,                         -- Chat 窗口宽度
  open_height = 20,                        -- Chat 窗口高度
  plugins = { openai = { key = 'YOUR_OPENAI_KEY' } },  -- 认证信息
  instructions = { 'GitHub Copilot Chat' }, -- 插件提示
  providers = { 'openai' },                 -- 选用的后端服务
}
```

---

## 快捷键（可选）

```lua
local map = vim.keymap.set
map('n', '<leader>cc', require('CopilotChat').open,  { desc = 'Copilot Chat 打开' })
map('n', '<leader>ci', require('CopilotChat').insert, { desc = 'Copilot Chat 插入' })
map('n', '<leader>cl', require('CopilotChat').clear,  { desc = 'Copilot Chat 清空' })
```

---

## 运行环境

- Neovim ≥ 0.8  
- Lua 5.1+  
- 网络访问 GitHub Chat 服务（需网络代理/免墙）  
- `vimplug`/`packer`/`lazy` 等插件管理器

---

## 常见问题

| 问题 | 解决办法 |
|------|--------|
| API 请求超时 | 检查网络代理或 VPN，确认 `OPENAI_API_KEY` 正确配置 |
| 语法高亮不生效 | 确认 `telescope.nvim` 或其他 LSP 已配置；在 `setup` 或 `require('CopilotChat').open` 前加载插件 |
| 插件冲突 | 关闭其他 `Chat`/`AI` 插件的映射，或在 `setup` 中做冲突检测 |

---

## 许可证

MIT

---

> 以上便是 CopilotChat.nvim 的核心特性与使用方法。详细信息请参阅官方仓库的 README 与 Wiki。