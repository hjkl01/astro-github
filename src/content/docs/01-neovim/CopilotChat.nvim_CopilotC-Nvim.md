---
title: CopilotChat.nvim
---


# CopilotChat.nvim

> GitHub 地址: [https://github.com/CopilotC-Nvim/CopilotChat.nvim](https://github.com/CopilotC-Nvim/CopilotChat.nvim)

## 主要特性

- **AI 辅助聊天**：集成 GitHub Copilot，支持在 Neovim 内直接与 AI 对话。
- **多语言支持**：可对多种编程语言的代码进行提问、分析和生成。
- **上下文感知**：自动捕获当前编辑器的上下文（光标所在位置、文件内容等），让 AI 更准确地回答。
- **交互式对话窗口**：使用浮动窗口或分屏显示聊天记录，支持滚动、复制、清空等操作。
- **自定义提示**：允许用户自定义提示词或模型参数，以满足不同场景需求。
- **快捷键映射**：提供一组默认快捷键，方便快速打开/关闭聊天窗口、发送消息等。

## 功能概览

| 功能 | 说明 |
|------|------|
| `CopilotChat.Chat()` | 打开聊天窗口，开始与 AI 对话 |
| `CopilotChat.Send()` | 发送消息给 AI，返回回答 |
| `CopilotChat.Clear()` | 清空聊天记录 |
| `CopilotChat.SetContext()` | 手动设置或更新上下文 |
| `CopilotChat.Config()` | 配置插件选项（如窗口位置、模型参数等） |

## 用法

### 1. 安装

```lua
-- 使用 packer.nvim
use {
  'CopilotC-Nvim/CopilotChat.nvim',
  requires = { { 'nvim-lua/plenary.nvim' } },
  config = function()
    require('CopilotChat').setup {}
  end
}
```

### 2. 基本使用

```vim
" 打开聊天窗口
:CopilotChat

" 在聊天窗口中输入问题后按 Enter 发送
```

### 3. 快捷键（默认）

| 快捷键 | 操作 |
|--------|------|
| `<leader>cc` | 打开/关闭聊天窗口 |
| `<leader>cs` | 发送当前选区内容给 AI |
| `<leader>cr` | 清空聊天历史 |
| `<leader>ct` | 切换到文本模式 / 代码模式 |

> 你可以在 `init.lua` 或 `init.vim` 中自定义快捷键，例如：

```lua
vim.api.nvim_set_keymap('n', '<leader>cp', ':CopilotChat<CR>', { noremap = true, silent = true })
```

### 4. 配置示例

```lua
require('CopilotChat').setup {
  -- 窗口设置
  popup = true,           -- 使用浮动窗口
  width = 0.8,            -- 宽度占比
  height = 0.6,           -- 高度占比
  -- AI 参数
  model = "gpt-4o-mini",
  temperature = 0.7,
  -- 其他自定义选项
  prompt = {
    system = "You are a helpful coding assistant."
  }
}
```

### 5. 高级用法

- **上下文注入**：使用 `:CopilotChat.SetContext` 手动注入自定义上下文，例如文件头或项目说明。
- **多分区聊天**：在同一窗口中同时进行多条对话，使用 `:CopilotChat.NewChat` 创建新会话。
- **日志导出**：使用 `:CopilotChat.Export` 将聊天记录导出为 Markdown 或纯文本。

## 贡献

如果你想改进插件，欢迎提交 Issue 或 Pull Request。请遵循官方贡献指南。

--- 

> **Tip**：在使用过程中若遇到 API 调用失败或响应慢，检查网络连接或 GitHub Copilot 的配额限制。
