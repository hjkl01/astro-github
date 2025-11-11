---
title: neotest
---

# Neotest

Neotest 是一个用于在 NeoVim 中与测试交互的可扩展框架。它允许用户运行、调试和查看测试结果，支持多种测试运行器。

## 功能

- **测试运行**：运行最近的测试、当前文件或整个测试套件。
- **调试支持**：与 nvim-dap 集成，支持调试测试。
- **输出显示**：提供输出窗口、摘要窗口和诊断消息。
- **状态指示**：在代码中显示测试状态符号。
- **可扩展性**：支持多种适配器，用于不同语言和测试框架。

## 用法

### 安装

Neotest 需要以下依赖：

- [nvim-nio](https://github.com/nvim-neotest/nvim-nio)
- [plenary.nvim](https://github.com/nvim-lua/plenary.nvim)
- [nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter)
- [FixCursorHold.nvim](https://github.com/antoinemadec/FixCursorHold.nvim)（推荐）

使用包管理器安装，例如 lazy.nvim：

```lua
{
  "nvim-neotest/neotest",
  dependencies = {
    "nvim-neotest/nvim-nio",
    "nvim-lua/plenary.nvim",
    "antoinemadec/FixCursorHold.nvim",
    "nvim-treesitter/nvim-treesitter"
  }
}
```

还需要安装适配器，例如 neotest-python 用于 Python 测试。

### 配置

在 init.lua 中配置：

```lua
require("neotest").setup({
  adapters = {
    require("neotest-python")({
      dap = { justMyCode = false },
    }),
    require("neotest-plenary"),
  },
})
```

### 基本用法

- 运行最近的测试：`require("neotest").run.run()`
- 运行当前文件：`require("neotest").run.run(vim.fn.expand("%"))`
- 调试最近的测试：`require("neotest").run.run({strategy = "dap"})`
- 停止测试：`require("neotest").run.stop()`
- 附加到测试：`require("neotest").run.attach()`

### 消费者

- **输出窗口**：显示测试输出。
- **摘要窗口**：显示测试套件结构。
- **诊断消息**：在代码中显示错误。
- **状态符号**：显示测试状态。

### 支持的运行器

Neotest 支持多种测试运行器，包括 pytest、jest、rspec 等，通过相应的适配器。

更多详情请参考 [Neotest GitHub](https://github.com/nvim-neotest/neotest)。
