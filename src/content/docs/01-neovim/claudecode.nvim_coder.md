
---
title: claudecode.nvim
---


# claudecode.nvim

**GitHub 地址**: https://github.com/coder/claudecode.nvim

## 简介
`claudecode.nvim` 是一款 Neovim 插件，专为 Claude AI（Anthropic）提供集成。它允许你在编辑器内直接向 Claude 发送代码片段或文本，获取 AI 生成的回复，并可通过流式输出实时查看结果。

## 主要特性
- **发送文本/代码到 Claude**：选中文本后一键提交，获取 AI 回复。  
- **多模型支持**：可配置使用不同的 Claude 模型（`claude-3-haiku-20240307`、`claude-3-5-sonnet-20240620` 等）。  
- **流式输出**：支持 `stream` 模式，AI 生成的内容会实时显示。  
- **交互式聊天**：开启聊天窗口，进行多轮对话。  
- **快捷键绑定**：默认键位可自定义，快速触发发送或聊天。  
- **可配置**：通过 `setup` 函数自定义 API Key、模型、温度、最大 token 等参数。  
- **保存历史**：聊天记录可保存在本地，便于后续查看。  
- **代码片段建议**：在编写代码时可获取 AI 的补全建议。  

## 快速使用

### 1. 安装  
```lua
-- packer.nvim 示例
use {
  'coder/claudecode.nvim',
  config = function()
    require('claudecode').setup({
      api_key = os.getenv('CLAUDE_API_KEY'),  -- 或直接写字符串
      model = 'claude-3-5-sonnet-20240620',
      temperature = 0.7,
      max_tokens = 1024,
      stream = true,
    })
  end
}
```

### 2. 配置环境变量  
```bash
export CLAUDE_API_KEY="your_api_key_here"
```

### 3. 常用命令  
| 命令 | 功能 |
|------|------|
| `:ClaudeSend` | 发送当前选中文本到 Claude，显示回复 |
| `:ClaudeChat` | 打开交互式聊天窗口 |
| `:ClaudeClearChat` | 清空聊天记录 |
| `:ClaudeSetModel <model>` | 切换使用的模型 |
| `:ClaudeSetTemperature <value>` | 调整温度参数 |

### 4. 快捷键（默认）  
- `<leader>c`：发送选中文本  
- `<leader>ch`：开启聊天窗口  

> 你可以在 `keymaps.lua` 或 `init.lua` 自定义快捷键，例如：
```lua
vim.api.nvim_set_keymap('n', '<leader>cs', ':ClaudeSend<CR>', { noremap = true, silent = true })
```

## 进一步阅读  
请参考插件根目录下的 `README.md` 获取更详细的配置选项和高级用法。