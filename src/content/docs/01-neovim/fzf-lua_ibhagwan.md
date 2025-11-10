---
title: fzf-lua
---
---

## 常见命令

```vim
:lua require('fzf-lua').files({ cwd = vim.fn.getcwd() })   -- 以当前工作目录为根
:lua require('fzf-lua').grep({ pattern = 'TODO' })          -- 全局搜索 TODO
:lua require('fzf-lua').git_commits({})                    -- 查看 Git 提交
:lua require('fzf-lua').registers()                        -- 注册表查看
```

---
## 结语
fzf‑lua 是一个功能丰富、可高度自定义的 Neovim fuzzy finder 插件，借助 fzf 的强大性能与 Neovim 的 Lua API，提供了从文件搜索、代码查找、 LSP 操作到 Git 操作等多种实用工具。通过简单的配置即可满足日常开发需求。