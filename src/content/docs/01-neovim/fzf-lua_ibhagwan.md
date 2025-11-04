
---
title: fzf-lua
---

# fzf‑lua（ibhagwan）

- **项目地址**  
  <https://github.com/ibhagwan/fzf-lua>

---

## 主要特性

| 特色 | 说明 |
|------|------|
| **Neovim 原生 Lua 插件** | 通过 Lua 代码直接调用 fzf，避免了外部 shell 依赖。 |
| **多种 FZF 实例** | `files`, `live_grep`, `grep`, `buffers`, `commands`, `tags`, `help_tags`, `marks`, `sessions`, `registers`, `git_commits`, `git_branches` 等。 |
| **高度可配置** | 通过 `require('fzf-lua').setup { … }` 自定义键位、命令、预设等。 |
| **与 LSP 集成** | `lsp_document_symbols`, `lsp_workspace_symbols`, `lsp_code_actions`, `lsp_implementations` 等。 |
| **多终端模式** | 支持 `split`, `vsplit`, `topleft`, `topleft_split` 等多种打开方式。 |
| **易于扩展** | `custom` 选项允许用户自定义新的 FZF 入口。 |
| **高性能** | 采用 `fzf#run` 的方式，充分利用 `fzf` 的速度优势。 |

---

## 安装方式

```lua
-- 例：使用 packer.nvim
use {
  'ibhagwan/fzf-lua',
  requires = { 'nvim-tree/nvim-web-devicons' }, -- 可选
  config = function()
    require('fzf-lua').setup {
      -- 这里写自定义配置
    }
  end
}
```

---

## 基本用法

### 1. 打开文件

```vim
:lua require('fzf-lua').files()
```

或者使用快捷键（默认）  
`<Leader>pf`  → `files`

### 2. 代码搜索

```vim
:lua require('fzf-lua').live_grep()
```

快捷键 `<Leader>pg`

### 3. 切换缓冲区

```vim
:lua require('fzf-lua').buffers()
```

快捷键 `<Leader>pb`

### 4. LSP 相关

```vim
:lua require('fzf-lua').lsp_document_symbols()
```

快捷键 `<Leader>ps`

---

## 配置示例

```lua
require('fzf-lua').setup {
  winopts = {
    height = 0.5,
    width = 0.8,
    preview = true,
    border = 'rounded',
    preview_opts = {
      width = 0.6,
      height = 0.8,
    }
  },
  actions = {
    files = {
      split = 'vsp',
      vsplit = 'vsp',
      tab = 'tabedit',
    },
  },
  -- 自定义快捷键
  keybindings = {
    files = {
      ["<C-x>"] = "open_split",
      ["<C-v>"] = "open_vsplit",
    },
  },
  -- 自定义命令
  custom = {
    my_search = {
      cmd = function(opts)
        return 'rg --vimgrep -u .'
      end,
      key = "<Leader>ps",
      desc = "自定义 ripgrep",
    },
  },
}
```

---

## 快捷键对照（默认）

- **`<Leader>pf`** – 文件搜索  
- **`<Leader>pg`** – live grep  
- **`<Leader>pb`** – 缓冲区列表  
- **`<Leader>ps`** – LSP 文档符号  
- **`<Leader>pi`** – LSP 实现  
- **`<Leader>po`** – LSP 代码动作  
- **`<Leader>ph`** – 帮助标签  
- **`<Leader>pm`** – 标记列表  
- **`<Leader>pc`** – Git 提交历史  
- **`<Leader>pp`** – Git 分支

> 通过 `:lua require('fzf-lua').setup{}` 可自由修改或添加快捷键。

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