---
title: neotest-go
---

# neotest-go

## 功能介绍

neotest-go 是为 [Neotest](https://github.com/rcarriga/neotest) 框架提供 Go 语言适配器的插件。Neotest 是一个用于 Neovim 的测试框架，支持多种编程语言的测试运行和结果展示。该插件允许在 Neovim 中直接运行 Go 测试，并提供丰富的测试结果可视化功能。

主要功能包括：

- 运行单个测试函数
- 运行整个测试文件
- 运行目录下的所有测试
- 运行整个测试套件
- 支持 testify 等测试框架的错误消息格式化
- 可配置额外参数传递给 `go test` 命令

## 安装

使用 packer 安装：

```lua
use({
  "nvim-neotest/neotest",
  requires = {
    "nvim-neotest/neotest-go",
    -- 其他测试适配器
  },
  config = function()
    -- 获取 neotest 命名空间
    local neotest_ns = vim.api.nvim_create_namespace("neotest")
    vim.diagnostic.config({
      virtual_text = {
        format = function(diagnostic)
          local message =
            diagnostic.message:gsub("\n", " "):gsub("\t", " "):gsub("%s+", " "):gsub("^%s+", "")
          return message
        end,
      },
    }, neotest_ns)
    require("neotest").setup({
      -- neotest 配置
      adapters = {
        require("neotest-go"),
      },
    })
  end,
})
```

可选配置参数：

```lua
require("neotest").setup({
  adapters = {
    require("neotest-go")({
      experimental = {
        test_table = true,
      },
      args = { "-count=1", "-timeout=60s" },
      recursive_run = true  -- 递归运行测试
    })
  }
})
```

## 用法

注意：所有 `require('neotest').run.run` 调用可以映射到 Neovim 命令中。

### 测试单个函数

将光标悬停在测试函数上，运行：

```lua
require('neotest').run.run()
```

注意：使用 testify 的测试方法无法单独运行，因为 `go test` 无法使用 `-run` 标志单独运行这些测试。

### 测试文件

运行当前文件的测试：

```lua
require('neotest').run.run(vim.fn.expand('%'))
```

### 测试目录

运行指定目录下的测试：

```lua
require('neotest').run.run("path/to/directory")
```

### 测试套件

运行整个测试套件：

```lua
require('neotest').run.run(vim.fn.getcwd())
```

### 额外参数

为 `go test` 命令添加额外参数：

```lua
require('neotest').run.run({path, extra_args = {"-race"}})
```
