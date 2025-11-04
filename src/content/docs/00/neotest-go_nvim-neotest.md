
---
title: neotest-go
---

# neotest-go – Go 测试集成插件

**GitHub 项目地址**  
<https://github.com/nvim-neotest/neotest-go>

## 项目概述  
neotest-go 是 Neovim 生态中专为 Go 语言设计的 Neotest 适配器。通过 Neotest 的统一接口，它能在 Neovim 内部直接跑、调试、查看 Go 单元测试，并支持多种测试框架与工具链。

## 主要特性

- **原生 Go 测试支持**  
  - 直接执行 `go test`，支持常用标志（如 `-v`、`-race`、`-count` 等）。  
  - 自动识别当前文件或目录下的测试文件（`*_test.go`）。

- **多框架兼容**  
  - 原生 Go 测试。  
  - `ginkgo` 框架。  
  - 通过插件配置可扩展到其它测试工具。

- **高效的测试运行模式**  
  - 单文件 / 单 test / 目录 / 整个项目。  
  - 按需重新运行（改动后只跑 affected tests）。  
  - 断点式运行：`--run` 选项可指定测试匹配。

- **Results & UI 集成**  
  - 与 Neotest UI 完全集成：测试运行状态、节点树、结果列表、详细错误堆栈。  
  - 可在 `quickfix` 或 `location list` 里直接跳转到失败的测试代码位置。  
  - 支持覆盖率信息（通过 `-coverprofile` 生成后在 Neotest UI 中展示）。

- **调试集成**  
  - 在 Neovim 内部通过 DAP 调试 Go 测试，支持设置断点、查看变量、单步执行。  
  - 通过 `:NeotestDebug` 或快捷键启动。

- **插件化扩展**  
  - 仅依赖 Neotest，无需额外依赖。  
  - 可通过 config 选项自定义 `cmd`, `env`, `runner`, `skipFiles` 等。

## 基本用法

1. **安装**  
   ```lua
   use { {'neovim/nvim-lspconfig'}, {'nvim-telescope/telescope.nvim'}, {'nvim-neotest/neotest'}, {'nvim-neotest/neotest-go'} }
   ```

2. **Neotest 配置**  
   ```lua
   require('neotest').setup({
     adapters = {
       require('neotest-go')({
         -- 可自定义参数
         cmd = function()
           return {'go', 'test', '-v'}
         end,
         -- 支持 ginkgo
         -- path = { 'ginkgo', 'test', '-focus', '.*' }
       })
     }
   })
   ```

3. **运行命令**  
   - 运行当前文件所有测试：`<leader>nt` 或 `:NeotestRun`  
   - 运行选中区段)：`<leader>nr`  
   - 停止所有测试：`<leader>ns` 或 `:NeotestStop`  
   - 查看最近测试结果：`<leader>ntq` 或 `:NeotestSummary`

4. **调试**  
   ```lua
   vim.keymap.set('n', '<leader>nd', require('neotest').run.run { strategy = 'dap' })
   ```

5. **查看覆盖率**  
   - 在 Neotest UI 打开 `c`（coverage），即可查看当前文件/目录的覆盖率。

6. **快速跳转**  
   - `gt`：跳转到 next failure
   - `gT`：跳转到 previous failure

## 高级配置示例

```lua
require('neotest').setup({
  adapters = {
    require('neotest-go')({
      -- 自定义命令行
      cmd = function(opts)
        local parts = {'go', 'test', '-v', '-count=1'}
        if opts.focus then
          table.insert(parts, '-run')
          table.insert(parts, opts.focus)
        end
        return parts
      end,
      -- 过滤掉无意义的文件
      skipFiles = function(filename)
        return filename:match('%.gen%.go$')
      end,
      env = {
        GOFLAGS = '-mod=vendor'
      }
    })
  }
})
```

> **提示**：neotest-go 与 Neotest 的所有 UI 与命令保持一致，所有快捷键与命令可在 `:h neotest` 里查看。

> **注意**：若要在远程终端或 CI 环境下使用，需要保证 `go` 命令在 `PATH` 内。

---

**结束**