---
title: codecompanion.nvim
---

# codecompanion.nvim

> Description from GitHub: ✨ AI Coding, Vim Style

## 💜 赞助商

感谢以下人为他们的支持：

[unicell](https://github.com/unicell) [adam-e-trepanier](https://github.com/adam-e-trepanier) [jfgordon2](https://github.com/jfgordon2) [prettymuchbryce](https://github.com/prettymuchbryce) [pratyushmittal](https://github.com/pratyushmittal) [toupeira](https://github.com/toupeira) [JuanCrg90](https://github.com/JuanCrg90) [Alexander-Garcia](https://github.com/Alexander-Garcia) [LumenYoung](https://github.com/LumenYoung) [iamthebot](https://github.com/iamthebot) [serranomorante](https://github.com/serranomorante)

如果您喜欢 CodeCompanion 并在工作流程中使用它，请考虑 [赞助我](https://github.com/sponsors/olimorris)

## ✨ 特性

- 💬 Copilot Chat 遇见 Zed AI，在 Neovim 中
- 🔌 支持来自 Anthropic、Copilot、GitHub Models、DeepSeek、Gemini、Mistral AI、Novita、Ollama、OpenAI、Azure OpenAI、HuggingFace 和 xAI 的 LLM（或 [自带](https://codecompanion.olimorris.dev/extending/adapters.html)）
- 🤖 支持 [代理客户端协议](https://agentclientprotocol.com)，启用使用 Claude Code、Codex 和 Gemini CLI 等代理进行编码
- 🫶 用户贡献和支持的 [适配器](https://codecompanion.olimorris.dev/configuration/adapters#community-adapters)
- 🚀 [内联转换](https://codecompanion.olimorris.dev/usage/inline-assistant.html)、代码创建和重构
- 🎨 [变量](https://codecompanion.olimorris.dev/usage/chat-buffer/variables.html)、[斜杠命令](https://codecompanion.olimorris.dev/usage/chat-buffer/slash-commands.html)、[工具](https://codecompanion.olimorris.dev/usage/chat-buffer/tools.html) 和 [工作流](https://codecompanion.olimorris.dev/usage/workflows.html) 以改进 LLM 输出
- 🧠 支持像 CLAUDE.md、.cursor/rules 和您自己的自定义这样的 [记忆文件](https://codecompanion.olimorris.dev/usage/chat-buffer/memory.html)
- 🔮 本机 [超级差异](https://codecompanion.olimorris.dev/usage/chat-buffer/index.html#super-diff) 用于跟踪代理编辑
- ✨ 内置 [提示库](https://codecompanion.olimorris.dev/usage/action-palette.html) 用于常见任务，如 LSP 错误建议和代码解释
- 🏗️ 创建您自己的 [自定义提示](https://codecompanion.olimorris.dev/extending/prompts.html)、变量和斜杠命令
- 📚 同时打开 [多个聊天](https://codecompanion.olimorris.dev/usage/introduction.html#quickly-accessing-a-chat-buffer)
- 🎨 支持作为输入的 [视觉和图像](https://codecompanion.olimorris.dev/usage/chat-buffer/#images-vision)
- 💪 异步执行以实现快速性能

## 📸 实际操作

### [聊天缓冲区](https://github.com/user-attachments/assets/aa109f1d-0ec9-4f08-bd9a-df99da03b9a4)

### [工具 + 代理工作流](https://github.com/user-attachments/assets/362b7cfd-e794-4d9c-9a74-90d5e2a87a32)

### [内联助手](https://github.com/user-attachments/assets/dcddcb85-cba0-4017-9723-6e6b7f080fee)

## 🚀 开始使用

一切您需要知道的关于 CodeCompanion（安装、配置和使用）都在 [文档](https://codecompanion.olimorris.dev) 中。

## 🧰 故障排除

在提出 [问题](https://github.com/olimorris/codecompanion.nvim/issues) 之前，您可以采取一些步骤来排除问题：

**Checkhealth**

运行 `:checkhealth codecompanion` 并检查所有依赖项是否正确安装。还要注意日志文件路径。

**启用日志记录**

更新您的配置并打开调试日志记录：

```lua
-- lazy.nvim
{
  "olimorris/codecompanion.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-treesitter/nvim-treesitter",
  },
  opts = {
    -- NOTE: The log_level is in `opts.opts`
    opts = {
      log_level = "DEBUG", -- or "TRACE"
    },
  },
},

-- Other package managers
require("codecompanion").setup({
  opts = {
    log_level = "DEBUG", -- or "TRACE"
  }
})
```

并根据 checkhealth 命令中的位置检查日志文件。

**使用 `minimal.lua` 文件尝试**

大量在 Neovim 插件中提出的问题都是由于用户的配置造成的。这就是为什么我总是要求用户在提出问题时填写 `minimal.lua` 文件的原因。它可以排除您的配置是问题的原因，并允许我重现问题。

为此目的，我在存储库中包含了一个 [minimal.lua](https://github.com/olimorris/codecompanion.nvim/blob/main/minimal.lua) 文件供您测试。如果您遇到问题，只需复制文件，编辑它并使用 `nvim --clean -u minimal.lua` 运行 neovim。

## 🎁 贡献

我对贡献持开放态度，但它们将由我自行决定。欢迎在 PR 之前打开讨论，并请阅读 [CONTRIBUTING.md](/olimorris/codecompanion.nvim/blob/main/CONTRIBUTING.md) 指南。

## 👏 致谢

- [Steven Arcangeli](https://github.com/stevearc) 为他的天才创作聊天缓冲区和早期反馈
- [Wtf.nvim](https://github.com/piersolenski/wtf.nvim) 为 LSP 助手操作
- [CopilotChat.nvim](https://github.com/CopilotC-Nvim/CopilotChat.nvim) 为聊天缓冲区的渲染和可用性
- [Aerial.nvim](https://github.com/stevearc/aerial.nvim) 为符号斜杠命令启发的 Tree-sitter 解析
- [Saghen](https://github.com/Saghen) 为 [blink.cmp](https://github.com/Saghen/blink.cmp) 的精彩文档启发和对项目的持续 PR
- [Catwell](https://github.com/catwell) 为我用来堆栈代理和工具的 [队列](https://github.com/catwell/cw-lua/blob/master/deque/deque.lua) 启发
- [ravitemer](https://github.com/ravitemer) 为精彩的扩展 API
- [Davidyz](https://github.com/Davidyz) 为他的持续优秀贡献，使 CodeCompanion 继续发展
- [Conrad Irwin](https://github.com/conradirwin)、[Agus Zubiaga](https://github.com/agu-z) 和 Morgan Krey 从 [Zed Industries](https://github.com/zed-industries) 为实现 [ACP](https://agentclientprotocol.com) 的支持

## 关于

✨ AI Coding, Vim Style

[codecompanion.olimorris.dev](https://codecompanion.olimorris.dev 'https://codecompanion.olimorris.dev')

并根据 checkhealth 命令中的位置检查日志文件。

**使用 `minimal.lua` 文件尝试**

大量在 Neovim 插件中提出的问题都是由于用户的配置造成的。这就是为什么我总是要求用户在提出问题时填写 `minimal.lua` 文件的原因。它可以排除您的配置是问题的原因，并允许我重现问题。

为此目的，我在存储库中包含了一个 [minimal.lua](https://github.com/olimorris/codecompanion.nvim/blob/main/minimal.lua) 文件供您测试。如果您遇到问题，只需复制文件，编辑它并使用 `nvim --clean -u minimal.lua` 运行 neovim。

## 🎁 贡献

我对贡献持开放态度，但它们将由我自行决定。欢迎在 PR 之前打开讨论，并请阅读 [CONTRIBUTING.md](/olimorris/codecompanion.nvim/blob/main/CONTRIBUTING.md) 指南。

## 👏 致谢

- [Steven Arcangeli](https://github.com/stevearc) 为他的天才创作聊天缓冲区和早期反馈
- [Wtf.nvim](https://github.com/piersolenski/wtf.nvim) 为 LSP 助手操作
- [CopilotChat.nvim](https://github.com/CopilotC-Nvim/CopilotChat.nvim) 为聊天缓冲区的渲染和可用性
- [Aerial.nvim](https://github.com/stevearc/aerial.nvim) 为符号斜杠命令启发的 Tree-sitter 解析
- [Saghen](https://github.com/Saghen) 为 [blink.cmp](https://github.com/Saghen/blink.cmp) 的精彩文档启发和对项目的持续 PR
- [Catwell](https://github.com/catwell) 为我用来堆栈代理和工具的 [队列](https://github.com/catwell/cw-lua/blob/master/deque/deque.lua) 启发
- [ravitemer](https://github.com/ravitemer) 为精彩的扩展 API
- [Davidyz](https://github.com/Davidyz) 为他的持续优秀贡献，使 CodeCompanion 继续发展
- [Conrad Irwin](https://github.com/conradirwin)、[Agus Zubiaga](https://github.com/agu-z) 和 Morgan Krey 从 [Zed Industries](https://github.com/zed-industries) 为实现 [ACP](https://agentclientprotocol.com) 的支持

## 关于

✨ AI Coding, Vim Style

[codecompanion.olimorris.dev](https://codecompanion.olimorris.dev 'https://codecompanion.olimorris.dev')
