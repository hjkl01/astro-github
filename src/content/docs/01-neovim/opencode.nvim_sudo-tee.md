
---
title: opencode.nvim
---


# sudo-tee/opencode.nvim

**项目地址：**<https://github.com/sudo-tee/opencode.nvim>

## 主要特性

| # | 特性 | 说明 |
|---|-----|------|
| 1 | **快速打开文件** | 提供 `:OpenCode` 命令，可按路径或关键字快速定位并打开文件。 |
| 2 | **单窗口模式** | 打开文件后自动将编辑器切换为单文件视图，隐藏其它分割屏，保持工作区整洁。 |
| 3 | **自动恢复** | 在退出文件后可通过 `:CloseCode` 或 `Ctrl‑W q` 自动恢复之前的窗口布局。 |
| 4 | **多文件跳转** | 支持在已打开的文件间使用 `:NextCode` / `:PrevCode` 快速跳转。 |
| 5 | **可配置选项** | 提供全局选项 `opencode`，可自定义打开方式、窗口尺寸、快捷键。 |

## 功能概览

1. **打开代码文件**  
   ```vim
   :OpenCode <filepath>
   ```  
   或者在普通模式下按 `<leader>oc`（默认）快速打开文件。

2. **关闭代码文件**  
   ```vim
   :CloseCode
   ```  
   或者按 `Ctrl‑W q` 直接退出当前单文件视图。

3. **切换已打开文件**  
   ```vim
   :NextCode   " 切换到下一个已打开的文件
   :PrevCode   " 切换到上一个已打开的文件
   ```

4. **配置示例**（`init.lua` 里放置）  
   ```lua
   require('opencode').setup({
       split_width = 80,      -- 打开文件时切割屏的宽度
       hidden_win = true,     -- 自动隐藏多余窗口
       mappings = {          -- 自定义快捷键
           open   = "<leader>oc",
           close  = "<leader>oc",
       },
   })
   ```

5. **与已安装插件兼容**  
   - 可与 `telescope.nvim`、`fzf-lua` 等文件搜索插件一起使用，在搜索结果中直接按 `<CR>`  `:OpenCode`。

## 安装

使用 LuaRocks / Packer：

```lua
use { 'sudo-tee/opencode.nvim',
      config = function()
          require('opencode').setup()
      end }
```

## 贡献

欢迎提交 Issue 与 Pull Request，详细说明可参考仓库中的 `CONTRIBUTING.md` 文档。

``` 
```

