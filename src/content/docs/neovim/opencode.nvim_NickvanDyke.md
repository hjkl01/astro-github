---
title: opencode.nvim
---

# opencode.nvim

opencode.nvim 是一个 Neovim 插件，用于将 opencode AI 助手集成到 Neovim 中，简化编辑器感知的研究、审查和请求。

## 功能

- 自动连接到在 Neovim 当前工作目录中运行的任何 opencode，或提供集成的实例。
- 支持输入提示，包括补全、高亮和正常模式支持。
- 从库中选择提示，并定义自己的提示。
- 注入相关的编辑器上下文（缓冲区、光标、选择、诊断等）。
- 使用命令控制 opencode。
- 响应 opencode 的权限请求。
- 实时重新加载 opencode 编辑的缓冲区。
- 通过状态行组件监控 opencode 的状态。
- 将 opencode 的服务器发送事件作为自动命令转发以进行自动化。
- 提供合理的默认设置，具有完善的文档和灵活的配置以及 API，以适应您的工作流程。

## 安装和设置

### 使用 lazy.nvim

在您的 Neovim 配置中添加以下内容：

```lua
{
  "NickvanDyke/opencode.nvim",
  dependencies = {
    -- 推荐用于 ask() 和 select()。
    -- snacks 提供程序需要。
    { "folke/snacks.nvim", opts = { input = {}, picker = {}, terminal = {} } },
  },
  config = function()
    ---@type opencode.Opts
    vim.g.opencode_opts = {
      -- 您的配置，如果有的话 — 请参阅 lua/opencode/config.lua，或 "goto definition"。
    }

    -- 为 opts.events.reload 所需。
    vim.o.autoread = true

    -- 推荐/示例键映射。
    vim.keymap.set({ "n", "x" }, "<C-a>", function() require("opencode").ask("@this: ", { submit = true }) end, { desc = "Ask opencode" })
    vim.keymap.set({ "n", "x" }, "<C-x>", function() require("opencode").select() end,                          { desc = "Execute opencode action…" })
    vim.keymap.set({ "n", "x" },    "ga", function() require("opencode").prompt("@this") end,                   { desc = "Add to opencode" })
    vim.keymap.set({ "n", "t" }, "<C-.>", function() require("opencode").toggle() end,                          { desc = "Toggle opencode" })
    vim.keymap.set("n",        "<S-C-u>", function() require("opencode").command("session.half.page.up") end,   { desc = "opencode half page up" })
    vim.keymap.set("n",        "<S-C-d>", function() require("opencode").command("session.half.page.down") end, { desc = "opencode half page down" })
    -- 如果您坚持使用上述有意见的 "<C-a>" 和 "<C-x>"，您可能需要这些 — 否则考虑 "<leader>o"。
    vim.keymap.set('n', '+', '<C-a>', { desc = 'Increment', noremap = true })
    vim.keymap.set('n', '-', '<C-x>', { desc = 'Decrement', noremap = true })
  end,
}
```

### 使用 nixvim

在您的 nixvim 配置中添加：

```nix
programs.nixvim = {
  extraPlugins = [
    pkgs.vimPlugins.opencode-nvim
  ];
};
```

## 配置

opencode.nvim 提供丰富的默认体验 — 请参阅所有可用选项及其默认值 [lua/opencode/config.lua](https://github.com/NickvanDyke/opencode.nvim/blob/main/lua/opencode/config.lua)。

### 上下文

opencode.nvim 在提示中替换占位符为相应的上下文：

| 占位符         | 上下文                         |
| -------------- | ------------------------------ |
| `@this`        | 如果有视觉选择，否则为光标位置 |
| `@buffer`      | 当前缓冲区                     |
| `@buffers`     | 打开的缓冲区                   |
| `@visible`     | 可见文本                       |
| `@diagnostics` | 当前缓冲区诊断                 |
| `@quickfix`    | 快速修复列表                   |
| `@diff`        | Git 差异                       |
| `@grapple`     | grapple.nvim 标签              |

### 提示

选择或引用提示来审查、解释和改进您的代码：

| 名称          | 提示                                       |
| ------------- | ------------------------------------------ |
| `diagnostics` | 解释 `@diagnostics`                        |
| `diff`        | 审查以下 git 差异的正确性和可读性：`@diff` |
| `document`    | 为 `@this` 添加文档注释                    |
| `explain`     | 解释 `@this` 及其上下文                    |
| `fix`         | 修复 `@diagnostics`                        |
| `optimize`    | 为性能和可读性优化 `@this`                 |
| `review`      | 审查 `@this` 的正确性和可读性              |
| `test`        | 为 `@this` 添加测试                        |

### 提供程序

您可以手动在 Neovim 的 CWD 中运行 opencode，opencode.nvim 会找到它！

如果 opencode.nvim 找不到现有的 opencode，它会使用配置的提供程序（基于可用性默认）为您管理一个。

#### snacks.terminal

```lua
vim.g.opencode_opts = {
  provider = {
    enabled = "snacks",
    snacks = {
      -- ...
    }
  }
}
```

#### kitty

```lua
vim.g.opencode_opts = {
  provider = {
    enabled = "kitty",
    kitty = {
      -- ...
    }
  }
}
```

kitty 提供程序需要通过套接字启用远程控制。

#### wezterm

```lua
vim.g.opencode_opts = {
  provider = {
    enabled = "wezterm",
    -- 这些是 wezterm 设置的默认值
    wezterm = {
      direction = "bottom", -- left/right/top/bottom
      top_level = false,
      percent = 50,
    }
  }
}
```

#### tmux

```lua
vim.g.opencode_opts = {
  provider = {
    enabled = "tmux",
    tmux = {
      -- ...
    }
  }
}
```

#### 自定义

集成您的自定义方法以方便使用！

```lua
vim.g.opencode_opts = {
  provider = {
    toggle = function(self)
      -- ...
    end,
    start = function(self)
      -- ...
    end,
    stop = function(self)
      -- ...
    end,
    show = function(self)
      -- ...
    end
  }
}
```

## 用法

### Ask — `require("opencode").ask()`

输入 opencode 的提示。

- 按 `<Up>` 浏览最近的询问。
- 高亮和补全上下文和 opencode 子代理。
  - 按 `<Tab>` 触发内置补全。
  - 当使用 `snacks.input` 和 `blink.cmp` 时注册 `opts.ask.blink_cmp_sources`。

### Select — `require("opencode").select()`

从所有 opencode.nvim 功能中选择。

- 从 opencode 获取自定义命令。
- 当使用 `snacks.picker` 时高亮和预览项目。

### Prompt — `require("opencode").prompt()` | `:[range]OpencodePrompt`

提示 opencode。

- 解析对配置提示的命名引用。
- 注入配置的上下文。
- opencode 将解释对文件或子代理的 `@` 引用。

### Command — `require("opencode").command()`

命令 opencode：

| 命令                     | 描述                           |
| ------------------------ | ------------------------------ |
| `session.list`           | 列出会话                       |
| `session.new`            | 开始新会话                     |
| `session.share`          | 分享当前会话                   |
| `session.interrupt`      | 中断当前会话                   |
| `session.compact`        | 压缩当前会话（减少上下文大小） |
| `session.page.up`        | 向上滚动消息一页               |
| `session.page.down`      | 向下滚动消息一页               |
| `session.half.page.up`   | 向上滚动消息半页               |
| `session.half.page.down` | 向下滚动消息半页               |
| `session.first`          | 跳转到会话中的第一条消息       |
| `session.last`           | 跳转到会话中的最后一条消息     |
| `session.undo`           | 撤销当前会话中的最后操作       |
| `session.redo`           | 重做最后撤销的操作             |
| `prompt.submit`          | 提交 TUI 输入                  |
| `prompt.clear`           | 清除 TUI 输入                  |
| `agent.cycle`            | 循环选择的代理                 |

## 事件

opencode.nvim 将 opencode 的服务器发送事件作为 `OpencodeEvent` 自动命令转发：

```lua
-- 处理 opencode 事件
vim.api.nvim_create_autocmd("User", {
  pattern = "OpencodeEvent:*", -- 可选过滤事件类型
  callback = function(args)
    ---@type opencode.cli.client.Event
    local event = args.data.event
    ---@type number
    local port = args.data.port

    -- 查看可用的事件类型及其属性
    vim.notify(vim.inspect(event))
    -- 做一些有用的事情
    if event.type == "session.idle" then
      vim.notify("opencode 完成响应")
    end
  end,
})
```

### 编辑

当 opencode 编辑文件时，opencode.nvim 自动重新加载相应的缓冲区。

### 权限

当 opencode 请求权限时，opencode.nvim 等待空闲以询问您批准或拒绝它。

### 状态行

#### lualine

```lua
require("lualine").setup({
  sections = {
    lualine_z = {
      {
        require("opencode").statusline,
      },
    }
  }
})
```

## 致谢

- 受 [nvim-aider](https://github.com/GeorgesAlkhouri/nvim-aider)、[neopencode.nvim](https://github.com/loukotal/neopencode.nvim) 和 [sidekick.nvim](https://github.com/folke/sidekick.nvim) 启发。
- 使用 opencode 的 TUI 以简化 — 请参阅 [sudo-tee/opencode.nvim](https://github.com/sudo-tee/opencode.nvim) 以获取 Neovim 前端。
- [mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server) 可能更适合您，但它缺乏定制，并且工具调用缓慢且不可靠。
