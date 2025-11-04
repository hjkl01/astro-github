
---
title: codecompanion.nvim
---


# codecompanion.nvim（olimorris）

> GitHub 项目地址：<https://github.com/olimorris/codecompanion.nvim>

## 简介
`codecompanion.nvim` 是一个 Neovim 插件，利用 OpenAI 或兼容的 LLM（如 Claude、Gemini 等）为开发者提供 AI 辅助功能。它将对话式 AI 与 Neovim 无缝集成，支持代码补全、解释、重构、文档生成等多种场景。

---

## 主要特性

| 功能 | 说明 |
|------|------|
| **AI 代码补全** | 在编辑器中实时生成代码片段，支持多语言（JavaScript、Python、Rust、Go 等）。 |
| **代码解释** | 选中代码块后，自动生成中文或英文的注释/说明。 |
| **重构与优化** | 自动重构函数、提取变量、改写复杂逻辑。 |
| **文档生成** | 根据函数签名或文件内容生成 Markdown / Docstrings。 |
| **多模式交互** | 支持 *Chat*、*Explain*、*Refactor*、*Doc* 等四种模式。 |
| **可配置 AI 提供商** | 支持 OpenAI、Claude、Gemini、Ollama 等，并可自定义模型与超参数。 |
| **快捷键 & 命令** | 通过 `:CodeCompanion` 及自定义快捷键触发对应功能。 |
| **高可配置性** | 通过 Lua 表自定义提示词、输出格式、缓存策略等。 |
| **安全与隐私** | 所有文本都可在本地处理（Ollama），或通过可控的 API 调用。 |

---

## 安装

```lua
-- 使用 packer.nvim
use {
  'olimorris/codecompanion.nvim',
  requires = { 'nvim-lua/plenary.nvim', 'nvim-telescope/telescope.nvim' }, -- 根据需要
  config = function()
    require('codecompanion').setup({
      -- 默认配置示例
      api_key      = os.getenv('OPENAI_API_KEY'),  -- 或其他 LLM 的 API key
      model        = 'gpt-4o-mini',               -- 可选: 'gpt-4o', 'claude-3-5-sonnet', 'gemini-pro' 等
      -- 提示词模板
      prompts = {
        explain = "请用简洁的中文解释以下代码：\n\n{code}",
        refactor = "请优化并重构以下代码，保持相同功能：\n\n{code}",
        doc = "为以下函数生成 Markdown 文档，包含参数、返回值和示例：\n\n{code}",
        chat = "你是一个代码助手，帮助我解决编程问题。"
      },
      -- 其它可选选项
      timeout = 120000,          -- ms
      debug   = false,
    })
  end
}
```

> **提示**  
> - 你可以在 `init.lua` 或 `plugins.lua` 中配置 `api_key`，如果使用本地模型（如 Ollama），请将 `model` 设置为 `llama3` 并在 `api_base` 指定本地地址。  
> - 如果你想在终端中使用 `telescope.nvim` 进行代码搜索，也可以将 `telescope` 选项打开。

---

## 用法

### 1. 交互式聊天

```vim
:CodeCompanionChat
```

- 打开一个浮窗，输入问题，按 `Enter` 发送。  
- 支持多轮对话，返回历史会自动保存在浮窗中。  
- `Esc` 退出浮窗。

### 2. 代码解释

```vim
:CodeCompanionExplain
```

- 选中一段代码后执行（可在 Visual 模式下）。  
- 在当前缓冲区下方插入中文注释。  
- 也可使用 `:CodeCompanionExplain!` 直接在浮窗中查看。

### 3. 代码重构

```vim
:CodeCompanionRefactor
```

- 选中一段代码后执行，插件会返回重构后的代码并替换原段。  
- 通过 `:CodeCompanionRefactor!` 在浮窗中预览。

### 4. 文档生成

```vim
:CodeCompanionDoc
```

- 对当前函数或文件生成 Markdown 文档，插入到当前缓冲区。  
- 使用 `:CodeCompanionDoc!` 在浮窗中查看。

### 5. 快捷键

| 快捷键 | 功能 |
|-------|------|
| `<leader>cc` | 打开聊天浮窗 |
| `<leader>ce` | 解释选中代码 |
| `<leader>cr` | 重构选中代码 |
| `<leader>cd` | 生成文档 |

> **自定义**  
> 在 `setup` 时可以修改 `keymaps` 表来自定义快捷键。

---

## 配置示例

```lua
require('codecompanion').setup({
  api_key = os.getenv('OPENAI_API_KEY'),
  model   = 'gpt-4o-mini',
  prompts = {
    explain = "请用简洁的中文解释以下代码，包含关键步骤：\n\n{code}",
    refactor = "请优化并重构以下代码，保持相同功能，使用更现代的语法：\n\n{code}",
    doc = "为以下函数生成 Markdown 文档，包含参数、返回值、示例代码：\n\n{code}",
    chat = "你是一个经验丰富的编程助手，帮助我解决编程难题。"
  },
  -- 本地模型示例
  -- model = 'llama3',
  -- api_base = 'http://localhost:11434/v1',
  keymaps = {
    chat  = "<leader>cc",
    explain = "<leader>ce",
    refactor = "<leader>cr",
    doc = "<leader>cd"
  },
  debug = false,
})
```

---

## 进阶使用

- **自定义模板**：在 `prompts` 中添加新的模式，例如 `summarize`，并在命令中使用 `:CodeCompanionSummarize`。  
- **多语言支持**：在 `prompts.explain` 中使用 `{lang}` 变量，插件会自动填充当前缓冲区语言。  
- **输出到浮窗**：所有命令默认输出到普通编辑区；在 `setup` 中设置 `floating = true` 可强制使用浮窗。  
- **缓存与重用**：插件会缓存最近的对话历史，`<C-r>` 可以在聊天浮窗中重用上一条消息。  

---

## 常见问题

| 问题 | 解决方案 |
|------|-----------|
| **API Key 不工作** | 确认 `api_key` 正确设置，且网络可访问 OpenAI。 |
| **模型返回错误** | 检查 `model` 名称是否正确，或尝试切换至 `gpt-4o-mini`。 |
| **浮窗不可见** | 关闭 `floating` 或检查 Neovim 版本，需 0.10+。 |
| **本地模型不可用** | 确认 `api_base` 与 Ollama 端口一致，且已启动服务。 |

---

## 贡献

欢迎 Fork、Issue 与 Pull Request！  
- 需遵守 `LICENSE`（MIT）。  
- 代码风格使用 `luacheck` 与 `stylua`。  
- 测试请使用 `busted` 或 `nvim-treesitter`。

---

## 参考

- 官方文档：<https://github.com/olimorris/codecompanion.nvim>  
- 相关 LLM API：OpenAI, Claude, Gemini, Ollama

``` 
