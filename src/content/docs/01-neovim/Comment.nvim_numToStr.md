---
title: Comment.nvim
---

## 功能介绍

Comment.nvim 是一个智能且强大的 Neovim 注释插件，支持 Treesitter、点重复、左右/上下移动、钩子等功能。它提供了行注释（`//`）和块注释（`/* */`）的支持，能够处理多种语言和文件类型。

### 主要特性

- **Treesitter 支持**：利用 Treesitter 计算注释字符串，支持多语言嵌入。
- **点重复**：支持 `.` 重复操作，如 `gcc`、`gbc` 等。
- **计数支持**：支持 `[count]gcc` 和 `[count]gbc` 等计数操作。
- **移动支持**：支持左右（`gcw`、`gc$`）和上下（`gc2j`、`gc4k`）移动。
- **文本对象**：可与文本对象结合使用，如 `gci{`、`gbat`。
- **钩子**：支持预钩子和后钩子函数。
- **忽略行**：可忽略特定行，支持 Lua 正则表达式。

## 用法

### 安装

使用 lazy.nvim：

```lua
{
    'numToStr/Comment.nvim',
    opts = {
        -- 添加选项
    }
}
```

使用 packer.nvim：

```lua
use {
    'numToStr/Comment.nvim',
    config = function()
        require('Comment').setup()
    end
}
```

使用 vim-plug：

```vim
Plug 'numToStr/Comment.nvim'

" 在 plug#end() 后
lua require('Comment').setup()
```

### 设置

调用 `setup()` 方法创建默认映射：

```lua
require('Comment').setup()
```

可选配置：

```lua
require('Comment').setup({
    padding = true,  -- 注释与行之间添加空格
    sticky = true,   -- 光标保持位置
    ignore = nil,    -- 忽略的行
    toggler = {
        line = 'gcc',  -- 行注释切换
        block = 'gbc', -- 块注释切换
    },
    opleader = {
        line = 'gc',
        block = 'gb',
    },
    extra = {
        above = 'gcO',  -- 在上方添加注释
        below = 'gco',  -- 在下方添加注释
        eol = 'gcA',    -- 在行尾添加注释
    },
    mappings = {
        basic = true,
        extra = true,
    },
    pre_hook = nil,
    post_hook = nil,
})
```

### 基本映射

- **NORMAL 模式**：
  - `gcc`：切换当前行行注释
  - `gbc`：切换当前行块注释
  - `[count]gcc`：切换指定行数行注释
  - `[count]gbc`：切换指定行数块注释
  - `gc[count]{motion}`：使用行注释切换区域
  - `gb[count]{motion}`：使用块注释切换区域

- **VISUAL 模式**：
  - `gc`：使用行注释切换区域
  - `gb`：使用块注释切换区域

### 额外映射

- `gco`：在下一行插入注释并进入插入模式
- `gcO`：在上一行插入注释并进入插入模式
- `gcA`：在当前行尾插入注释并进入插入模式

### 示例

- `gcw`：从光标位置切换到下一个单词
- `gc$`：从光标位置切换到行尾
- `gc5j`：切换光标后5行
- `gcip`：切换段落内
- `gbaf`：切换函数周围（需 LSP/Treesitter 支持）

### Treesitter 集成

插件原生支持 Treesitter，可用于计算多语言的注释字符串。对于高级用例，可与 `nvim-ts-context-commentstring` 集成：

```lua
pre_hook = require('ts_context_commentstring.integrations.comment_nvim').create_pre_hook(),
```

### 钩子

- `pre_hook`：在注释前调用，可返回自定义注释字符串。
- `post_hook`：在注释后调用。

### 忽略行

使用 `ignore` 选项忽略特定行：

```lua
ignore = '^$',  -- 忽略空行
```

或使用函数：

```lua
ignore = function()
    if vim.bo.filetype == 'lua' then
        return '^$'
    end
end,
```

### 文件类型支持

对于不支持的文件类型，可设置 `commentstring` 或使用插件接口：

```lua
local ft = require('Comment.ft')
ft.set('yaml', '#%s')
ft.javascript = {'//%s', '/*%s*/'}
```
