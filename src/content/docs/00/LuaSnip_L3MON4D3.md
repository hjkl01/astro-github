---
title: LuaSnip
---

# LuaSnip

## 项目简介

LuaSnip 是一个为 Neovim 编写的 Snippet 引擎，使用 Lua 语言开发。它提供了强大的代码片段功能，支持多种类型的片段定义和扩展。

## 主要功能

- **Tabstops**: 支持多位置跳转和编辑
- **文本转换**: 使用 Lua 函数进行文本变换
- **条件扩展**: 根据上下文条件扩展片段
- **嵌套片段**: 支持定义嵌套的代码片段
- **文件类型特定片段**: 为不同文件类型提供专门的片段
- **选择节点**: 在片段中提供多个选项选择
- **动态片段创建**: 运行时动态生成片段
- **正则触发**: 使用正则表达式触发片段
- **自动触发片段**: 无需手动触发即可自动扩展
- **后缀片段**: 轻松创建后缀样式的片段
- **高性能**: 快速的片段处理
- **LSP 样式片段解析**: 支持直接在 Lua 中解析 LSP 样式的片段，或作为 VSCode 包或 SnipMate 片段集合
- **与补全插件集成**: 支持与 nvim-compe 或 nvim-cmp 集成扩展 LSP 片段（需要 cmp_luasnip）
- **片段历史**: 可以跳转回旧的片段
- **Treesitter 文件类型解析**: 使用 Treesitter 在光标位置解析文件类型

## 安装要求

- Neovim >= 0.7 (需要 extmarks 支持)
- 可选：`jsregexp` 用于 `lsp-snippet-transformations`（安装提示请参考[文档](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#transformations)）

## 安装方法

使用你喜欢的插件管理器安装，例如：

### Packer

```lua
use({
    "L3MON4D3/LuaSnip",
    -- 跟随最新发布版本
    tag = "v2.*", -- 将 <CurrentMajor> 替换为最新发布的主要版本号
    -- 可选：安装 jsregexp
    run = "make install_jsregexp"
})
```

### Lazy

```lua
{
    "L3MON4D3/LuaSnip",
    -- 跟随最新发布版本
    version = "v2.*", -- 将 <CurrentMajor> 替换为最新发布的主要版本号
    -- 可选：安装 jsregexp
    build = "make install_jsregexp"
}
```

### Vim-plug

```vim
" 跟随最新发布版本并安装 jsregexp
Plug 'L3MON4D3/LuaSnip', {'tag': 'v2.*', 'do': 'make install_jsregexp'} " 将 <CurrentMajor> 替换为最新发布的主要版本号
```

注意：在 Windows 上，你需要 C 编译器和 `make` 来安装 `jsregexp`。如果编译器不是 `gcc`、`clang` 或 `zig`，需要在构建命令中明确指定 `CC` 变量：`make install_jsregexp CC=your_compiler_program`。确保 `%GIT%/bin` 目录已添加到 `$PATH` 中，以便 `make` 可以使用 `%GIT%/bin/sh.exe`。

## 按键映射设置

### Vim Script 示例

使用 `<Tab>` 进行前进/扩展片段，`<Shift-Tab>` 后退，`<Ctrl-E>` 在 `choiceNode` 中更改当前选择：

```vim
" 按 <Tab> 扩展或跳转到片段中。这些也可以分别映射
" 通过 <Plug>luasnip-expand-snippet 和 <Plug>luasnip-jump-next
imap <silent><expr> <Tab> luasnip#expand_or_jumpable() ? '<Plug>luasnip-expand-or-jump' : '<Tab>'
" -1 用于向后跳转
inoremap <silent> <S-Tab> <cmd>lua require'luasnip'.jump(-1)<Cr>
snoremap <silent> <Tab> <cmd>lua require('luasnip').jump(1)<Cr>
snoremap <silent> <S-Tab> <cmd>lua require('luasnip').jump(-1)<Cr>
" 用于在 choiceNodes 中更改选择（基本设置中不是必需的）
imap <silent><expr> <C-E> luasnip#choice_active() ? '<Plug>luasnip-next-choice' : '<C-E>'
smap <silent><expr> <C-E> luasnip#choice_active() ? '<Plug>luasnip-next-choice' : '<C-E>'
```

### Lua 示例

使用不同的按键：`<Ctrl-K>` 扩展，`<Ctrl-L>` 前进跳转，`<Ctrl-J>` 后退跳转，`<Ctrl-E>` 更改活动选择。

```lua
local ls = require("luasnip")

vim.keymap.set({"i"}, "<C-K>", function() ls.expand() end, {silent = true})
vim.keymap.set({"i", "s"}, "<C-L>", function() ls.jump( 1) end, {silent = true})
vim.keymap.set({"i", "s"}, "<C-J>", function() ls.jump(-1) end, {silent = true})

vim.keymap.set({"i", "s"}, "<C-E>", function()
    if ls.choice_active() then
        ls.change_choice(1)
    end
end, {silent = true})
```

`nvim-cmp` 的 wiki 也包含了[设置超级 Tab 式映射的示例](https://github.com/hrsh7th/nvim-cmp/wiki/Example-mappings#luasnip)。

## 添加片段

检查[文档](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#loaders)以获取加载器的通用说明及其好处。以下列表仅作为简短概述。

### VS Code 样式

要使用现有 VS Code 样式片段（例如来自 [rafamadriz/friendly-snippets](https://github.com/rafamadriz/friendly-snippets)），只需安装插件，然后在 Neovim 配置中添加：

```lua
require("luasnip.loaders.from_vscode").lazy_load()
```

LuaSnip 将在启动时加载插件中包含的片段。你也可以通过将自定义片段目录的路径传递给加载函数来轻松**加载自己的自定义 VSCode 样式片段**：

```lua
-- 从 path/of/your/nvim/config/my-cool-snippets 加载片段
require("luasnip.loaders.from_vscode").lazy_load({ paths = { "./my-cool-snippets" } })
```

> 注意：片段目录中必须有 `package.json` 文件。示例请参见 [friendly-snippets](https://github.com/rafamadriz/friendly-snippets/blob/main/package.json)。

有关 VS Code 加载器的更多信息，请查看[示例](https://github.com/L3MON4D3/LuaSnip/blob/b5a72f1fbde545be101fcd10b70bcd51ea4367de/Examples/snippets.lua#L501)或[文档](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#loaders)。

### SnipMate 样式

与 VS Code 包非常相似；安装提供片段的插件并调用加载函数：

```lua
require("luasnip.loaders.from_snipmate").lazy_load()
```

SnipMate 格式非常简单，因此添加**自定义片段**只需要几个步骤：

- 在 `init.vim` 旁边（或 `runtimepath` 中的任何其他位置）添加一个名为 `snippets` 的目录
- 在该目录中，创建名为 `<filetype>.snippets` 的文件，并在其中为给定文件类型添加片段（灵感来源：[honza/vim-snippets](https://github.com/honza/vim-snippets/tree/master/snippets)）

```snippets
# comment
snippet <trigger> <description>
<snippet-body>
snippet if C-style if
if ($1)
    $0
```

同样，有一些[示例](https://github.com/L3MON4D3/LuaSnip/blob/b5a72f1fbde545be101fcd10b70bcd51ea4367de/Examples/snippets.lua#L517)和[文档](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#snipmate)。

### Lua

通过调用 `require("luasnip").add_snippets(filetype, snippets)` 添加片段。此示例可以在[此处](https://github.com/L3MON4D3/LuaSnip/blob/master/Examples/snippets.lua#L190)找到。

这也可以通过使用[Lua 加载器](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#lua)以更清洁的方式完成，并获得使用加载器带来的所有好处。

还有一个收集各种语言片段的仓库：[molleweide/LuaSnip-snippets.nvim](https://github.com/molleweide/LuaSnip-snippets.nvim)

## 文档和资源

### 入门指南

你有两个主要选择：使用 SnipMate/VS Code 片段（更容易）或用 Lua 编写片段（更复杂但功能更丰富）。以下是为任一情况入门的建议：

- **SnipMate 或 VS Code 片段**：如果你只想编写/加载 SnipMate 或 VS Code 片段并忽略 Lua 片段（如果你还不需 Lua 片段的更复杂功能，这绝对是推荐的），请查看 `DOC.md` 中关于加载 [VS Code](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#vscode) 或 [SnipMate](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#snipmate) 包的部分。其中，SnipMate 绝对是编写片段的更舒适方式。
- **Lua 片段**：我们建议首先观看或阅读下面“新用户资源”部分中的入门指南之一。熟悉基础知识后，你应该查看以下重要 LuaSnip 功能列表：
  - [`config`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#config-options)：值得注意：`region_check_events` 用于跳转到光标不再位于其中的片段末尾，`delete_check_events` 用于清理已删除文本的片段，以及 `enable_autosnippets` 以启用自动片段扩展。
  - [`extras`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#extras)：此模块包含许多使编写片段显著更容易的函数；`fmt` 和 `lambda` 特别有用。
  - [`lua-loader`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#lua)：加载片段的一种非常有用的方式，比调用 `add_snippets` 更舒适。也支持热重载（限于同一 Neovim 实例中缓冲区中的编辑文件）和[跳转到为当前缓冲区提供片段的文件](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#edit_snippets)。
  - 高级节点：[`functionNode`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#functionnode)、[`dynamicNode`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#dynamicnode)、[`choiceNode`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#choicenode) 和 [`restoreNode`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#restorenode)。与其在文档中阅读它们，前三个在 TJ DeVries 的[这个视频](https://www.youtube.com/watch?v=KtQZRAkgLqo)中解释得很好。

### 官方文档和示例

注意：与其立即阅读官方文档，你可能想查看下面的“新用户资源”部分，因为文档更像是参考手册而不是新用户的教程。

- [`DOC.md`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md) 是主要文档——它概述了如何编写片段，解释了每个 LuaSnip 节点的作用和用例，展示了如何从 Lua、VS Code 和 SnipMate 格式加载片段，并涵盖了可用的 LuaSnip API。
- `:help luasnip.txt` 是 `DOC.md` 的纯文本版本，可通过 Neovim 的 `:help` 功能使用。
- 文件 [`Examples/snippets.lua`](https://github.com/L3MON4D3/LuaSnip/blob/master/Examples/snippets.lua) 包含许多用 Lua 编写的示例片段——我们强烈推荐在使用 LuaSnip 的高级功能之前查看（或更好，`:luafile`）这些示例片段。
- [Wiki](https://github.com/L3MON4D3/LuaSnip/wiki) 包含一些有用的 LuaSnip 扩展以及一些高级片段和配置的示例。
- 配置也在 [`DOC.md`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#config-options) 中有文档。

【中文版】中文版 DOC 在[此处](https://zjp-cn.github.io/neovim0.6-blogs/nvim/luasnip/doc1.html)。

### 新用户资源

以下是一些网络上的 LuaSnip 视频和教程：

- [入门](https://www.youtube.com/watch?v=Dn800rlPIho) 和 [高级](https://www.youtube.com/watch?v=KtQZRAkgLqo) YouTube 视频，由 TJ DeVries 制作。不幸的是，自这些视频录制以来 LuaSnip 发生了一些破坏性更改：
  - 现在通过 [`ls.add_snippets`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#adding-snippets) 添加片段，而不是使用 `ls.snippets = {}`
- [@ejmastnak](https://github.com/ejmastnak) 制作的[用 Lua 编写片段指南](https://www.ejmastnak.com/tutorials/vim-latex/luasnip/)，带有 LaTeX 主题的 GIF 和真实示例
- [@evesdropper](https://github.com/evesdropper) 制作的 [LuaSnip 指南集合](https://evesdropper.dev/files/luasnip)，其中大部分也在 LaTeX 上下文中
- Ziontee113 制作的[针对初学者的入门 LuaSnip 视频教程](https://www.youtube.com/watch?v=ub0REXjhpmk)

受 [vsnip.vim](https://github.com/hrsh7th/vim-vsnip/) 启发
