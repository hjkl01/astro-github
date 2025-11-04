
---
title: nvim-dap
---


# nvim-dap (mfussenegger)

项目地址: <https://github.com/mfussenegger/nvim-dap>

---

## 主要特性

- **DAP（调试适配协议）**：使用 VS Code 的 DAP 协议，支持多种语言的调试。
- **多语言支持**：通过安装对应的适配器（如 `codelldb`, `vscode-node-debug2` 等）即可调试 Go, Python, C/C++, JavaScript/TypeScript, Rust 等。
- **嵌入式 UI**：内置 `nvim-dap-ui` 用于快速查看调用栈、变量、断点、日志等信息。
- **可配置快捷键**：支持自定义键绑定便捷地执行调试操作（开始/继续/停止/单步等）。
- **序列化配置**：所有调试配置均以 Lua 表形式存储，易于版本控制和共享。
- **命令行友好**：提供 `:lua require'dap'.continue()` 等命令，可直接在 Vim 命令行调用。

---

## 功能说明

| 功能 | 说明 |
|------|------|
| **启动调试会话** 通过 `dap.run` 或 `dap.continue` 启动。 |
| **单步调试** | `dap.step_into`, `dap.step_over`, `dap.step_out`. |
| **断点管理** | `dap.set_breakpoint`, `dap.clear_breakpoints`, `dap.set_breakpoint{condition="..."}`. |
| **变量监视** | `dap.ui.widgets.variables` 可查看当前作用域下所有变量。 |
| **日志输出** | `dap.listeners.after.event_initialized["dapui_config"] = function() require("dapui").open() end` 自动打开 UI。 |
| **配置堆栈** | `dap.set_log_level("TRACE")` 开启调试日志，帮助定位问题。 |
| **终端交互** | `dapui.controls.term` 直接在 Neovim 内部打开调试终端。 |

---

## 用法示例

### 1. 安装

```lua
-- packer.nvim
use {
  'mfussenegger/nvim-dap',
  requires = { 'rcarriga/nvim-dap-ui', 'theHamsta/nvim-dap-virtual-text' }
}
```

### 2. 基本配置（Lua）

```lua
local dap = require('dap')
local dapui = require('dapui')

-- 打开 UI
dapui.setup()

-- 自动在调试会话开始时打开 UI
dap.listeners.after.event_initialized["dapui_config"] = function()
  dapui.open()
end

-- 自动在调试会话结束时关闭 UI
dap.listeners.before.event_terminated["dapui_config"] = function()
  dapui.close()
end

-- Keybindings
vim.api.nvim_set_keymap('n', '<F5>', "<cmd>lua require'dap'.continue()<CR>", { noremap = true })
vim.api.nvim_set_keymap('n', '<F10>', "<cmd>lua require'dap'.step_over()<CR>", { noremap = true })
vim.api.nvim_set_keymap('n', '<F11>', "<cmd>lua require'dap'.step_into()<CR>", { noremap = true })
vim.api.nvim_set_keymap('n', '<F12>', "<cmd>lua require'dap'.step_out()<CR>", { noremap = true })
vim.api.nvim_set_keymap('n', '<Leader>b', "<cmd>lua require'dap'.toggle_breakpoint()<CR>", { noremap = true })
```

### 3. 语言适配器示例（Python）

```lua
dap.adapters.python = {
  type = 'executable';
  command = 'python3'; -- 如果你使用的是 pyright
  args = { '-m', 'debugpy.adapter' };
}

dap.configurations.python = {
  {
    type = 'python';
    request = 'launch';
    name = "Launchfile";
    program = "${file}";
    pythonPath = function()
      return '/usr/bin/python3'
    end;
  },
}
```

> 你可以根据需要替换 `pythonPath` 或使用虚拟环境。

### 4. 断点快捷键

```lua
-- 设置断点并跳转到对应行
vim.api.nvim_set_keymap('n', '<Leader>db', "<cmd>lua require'dap'.toggle_breakpoint()<CR>", { noremap = true })
```

---

## 小结

- `nvim-dap` 是一个使用 VS Code 的 DAP 协议的 Neovim 调试插件。
- 通过插件集成调试适配器，可在 Neovim 内实现 **程序调试、单步、断点、变量查看、终端交互** 等完整调试体验。
- 跟随 `require'dap'` 的 Lua API 进行配置，可自由定制启动方式、UI、快捷键。  

--- 

以上为项目的核心功能与使用示例，供你快速上手 `nvim-dap` 并在 Neovim 中体验完整调试流程。祝调试愉快！
