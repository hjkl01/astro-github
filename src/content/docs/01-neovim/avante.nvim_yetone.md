---
title: avante.nvim
---


# avante.nvim（yetone）

**项目地址**：<https://github.com/yetone/avante.nvim>

## 概述
avante.nvim 是一个面向 Neovim 的 AI 编码助手，融合了 OpenAI / Anthropic / GPT 等模型，支持代码补全、对话式问答、语法纠错、生成代码片段文件多轮交互。其核心目标是让开发者在 Vim 环境中轻松调用 AI，提升编码效率。

## 主要特性
| 特性 | 简述 |
|------|------|
| **聊天窗口** | 在 Neovim 内部打开独立 chat 窗口，支持即时对话与上下文记忆。 |
| **代码补全** | 对选区或光标所在位置进行 AI 自动补全，支持多行多种语法。 |
| **智能重构** | 自动改写、提取函数、重命名变量等，帮助快速重构。 |
| **错误修复** | 识别语法/逻辑错误并提供修改建议。 |
| **多语言支持** | 支持多种编程语言的语义解析与补全。 |
| **自定义 Prompt** | 通过配置文件或命令行自定义 Prompt，满足不同场景需求。 |
| **安全性** | 所有交互都通过本地网络请求完成，外部数据交互可通过代理或 API Token 控制。 |
| **触发快捷键** | 预设快捷键可快速输入、发送请求或打开聊天窗口，亦支持自定义。 |
| **插件化扩展** | 通过 `hooks` 和 `custom_commands` 轻松扩展功能，支持第三方插件集成。 |

## 安装方式
```vim
" packer.nvim
use {
  'yetone/avante.nvim',
  requires = { 'nvim-lua/plenary.nvim', 'nvim-telescope/telescope.nvim' },
}

" lazy.nvim
{ 'yetone/avante.nvim',
  dependencies = { 'nvim-lua/plenary.nvim', 'nvim-telescope/telescope.nvim' } }
```

## 基本配置（Lua）
```lua
require('avante').setup({
  api_key      = vim.env.OPENAI_API_KEY,   -- 你的 API Key，或在此直接写入字符串
  api_base     = nil,                       -- 如使用自建模型可填入 base URL
  model        = 'gpt-4o-mini',             -- 你想使用的模型
  timeout      = 30,                        -- 请求超时（s）
  prompt_prefix = '[Avante]',               -- Prompt 前缀
  automask     = true,                      -- 自动屏蔽敏感信息
  default_context = '在此编写代码',           -- 默认上下文
  -- 你可以添加自定义 клавиш或 hooks
})
```

## 关键命令与快捷键
| 命令 | 操作 | 快捷键（默认） |
||------|----------------|
| `:AvanteChat` | 打开聊天窗口 | `Ctrl-Alt-C` |
| `:AvanteComplete` | 对选区/光标进行 AI 补全 | `Ctrl-Alt-S` |
| `:AvanteFix` | 识别并修复错误 | `Ctrl-Alt-F` |
| `:AvanteExtract` | 将光标所在代码块提炼为函数 | `Ctrl-Alt-E` |
| `:AvanteClearChat` | 清空聊天历史 | `Ctrl-Alt-L` |

> 以上快捷键可在 `setup()` 中自定义，例如：
```lua
  keymaps = {
    chat      = 'gC',
    complete  = 'gS',
    fix       = 'gF',
    extract   = 'gE',
    clear_chat = 'gL',
  }
```

## 使用示例
1. **打开聊天**  
   `:AvanteChat` → 在弹出的窗口中输入问题，例如 `如何在 Lua 中实现闭包？` → AI 给出回答并附带代码示例。

2. **补全代码**  
   在 `main.lua` 文件中输入 `function fibonacci(n) `，并执行 `:AvanteComplete`（或快捷键）→ 自动补全完整实现。

3. **错误修复**  
   选中错误行后 `:AvanteFix` → AI 给出修复建议，直接一键替换。

4. **提炼函数**  
   代码块闪光后执行 `:AvanteExtract` → AI 将其提炼为可复用函数，并返回给编辑器。

## 高级用法
- **多轮对话上下文**：聊天窗口默认存储会话历史，可使用 `:AvanteClearChat` 清空或 `:AvanteLoop` 持续对话。
- **自定义 Prompt**：在 `~/.config/nvim/lua/avante.lua` 中即可修改 `prompt` 模板，支持占位符 `${snip}`、`${context}` 等。
- **插件集成**：可在 Telescope 或 LSP 配置中添加 `Avante` 作为后端分析器，例如在 `symbols` 或 `code_actions` 中绑定。
- **代理与身份认证**：若你在公司网络内，可在 `setup()` 中设置 `http_proxy` 与 `no_proxy`，或者仅通过自定义 `request_handler` 函数来处理。

## 常见问题
- **Key 长度限制**：如果 `api_key` 为较长字符串，可放置在 `init.lua` 中 `vim.env.OPENAI_API_KEY` 或使用 `env` 文件 (.env)。
- **网络错误**：请检查防火墙或代理配置，或在 `setup()` 中设置 `timeout`。
- **模型不支持**：改用 `model = 'gpt-3.5-turbo'` 或下载本地模型。

---  
**注意**：使用此插件前请确保你已获取合法的 API Key，并在使用过程中遵守平台的条款与规定。祝编码愉快 🚀
