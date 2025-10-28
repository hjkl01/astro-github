
---
title: nvim-cmp
---


# nvim-cmp

> GitHub 项目地址: https://github.com/hrsh7th/nvim-cmp

## 主要特性

- **异步补全**：支持多源异步补全，响应迅速。
- **高度可配置**：通过 Lua 配置文件可定制补全行为、显示格式、键位映射等。
- **多种补全源**：内置支持 `nvim_lsp`、`buffer`、`path`、`luasnip`、`cmp-nvim-lsp`、`cmp-vsnip` 等。
- **智能排位**：可自定义优先级、权重，灵活控制补全项排序。
- **可插拔**：可与 `nvim-lspconfig`、`luasnip`、`nvim-autopairs` 等插件无缝集成。
- **轻量高效**：核心代码约 500 行 Lua，运行占用资源极低。

## 功能概览

| 功能 | 说明 |
|------|------|
| 自动补全 | 当输入字符时自动弹出候选列表 |
| 智能提示 | 根据上下文显示 LSP 提示、文档、类型信息 |
| 关键字匹配 | 支持全局、局部、文件内、路径补全 |
| 代码片段 | 与 Snippet 插件配合使用，提供快速插入 |
| 排序与过滤 | 自定义排序规则，过滤无关项 |
| 键位映射 | `Tab/Shift-Tab` 换行、`Enter` 选中、`Ctrl-Space` 显示/隐藏 |
| 主题样式 | 支持多种主题，易于自定义 UI |

## 安装与使用

1. **安装插件**  
   使用插件管理器（如 `packer.nvim`）：

   ```lua
   use {
     'hrsh7th/nvim-cmp',
     requires = {
       'hrsh7th/cmp-nvim-lsp',   -- LSP source
       'hrsh7th/cmp-buffer',     -- Buffer source
       'hrsh7th/cmp-path',       -- Path source
       'saadparwaiz1/cmp_luasnip', -- Snippet source
     }
   }
   ```

2. **基本配置**  
   在 `init.lua` 或对应配置文件中添加：

   ```lua
   local cmp = require('cmp')

   cmp.setup({
     snippet = {
       expand = function(args)
         require('luasnip').lsp_expand(args.body)
       end,
     },
     mapping = {
       ['<Tab>'] = cmp.mapping.select_next_item(),
       ['<S-Tab>'] = cmp.mapping.select_prev_item(),
       ['<CR>'] = cmp.mapping.confirm({ select = true }),
       ['<C-Space>'] = cmp.mapping.complete(),
     },
     sources = {
       { name = 'nvim_lsp' },
       { name = 'luasnip' },
       { name = 'buffer' },
       { name = 'path' },
     },
     formatting = {
       format = function(entry, vim_item)
         local source_name = entry.source.name
         vim_item.menu = ' [' .. source_name .. ']'
         return vim_item
       end,
     },
   })
   ```

3. **与 LSP 配合**  
   确保已安装 `nvim-lspconfig` 并配置 LSP：

   ```lua
   require('lspconfig')['pyright'].setup({})
   ```

4. **使用 Snippets**  
   安装 `luasnip`，并在 `init.lua` 中添加：

   ```lua
   require('luasnip.loaders.from_vscode').lazy_load()
   ```

5. **自定义排序**  
   如需自定义排序逻辑，可在 `cmp.setup()` 中添加：

   ```lua
   sorting = {
     priority_weight = 2,
     comparators = {
       cmp.config.compare.offset,
       cmp.config.compare.exact,
       cmp.config.compare.score,
       cmp.config.compare.recently_used,
       cmp.config.compare.locality,
       cmp.config.compare.kind,
       cmp.config.compare.sort_text,
       cmp.config.compare.length,
       cmp.config.compare.order,
     },
   }
   ```

6. **主题与 UI**  
   可通过 `cmp.get_user_data()` 调整 `window` 选项：

   ```lua
   window = {
     completion = cmp.config.window.bordered(),
     documentation = cmp.config.window.bordered(),
   }
   ```

## 常见问题

- **补全列表不弹出**：检查 LSP 是否正常工作，确认 `cmp-nvim-lsp` 已安装。
- **Tab 键冲突**：如果 Tab 在插入模式已绑定其他功能，可在 `mapping` 中使用 `cmp.mapping.build()` 或重写 `Tab` 的行为。
- **性能下降**：关闭不需要的源或调整 `sorting` 的权重。

## 参考链接

- 官方仓库: https://github.com/hrsh7th/nvim-cmp
- 文档: https://github.com/hrsh7th/nvim-cmp/blob/master/README.md
- 示例配置: https://github.com/hrsh7th/nvim-cmp/blob/master/vim/README.md

---