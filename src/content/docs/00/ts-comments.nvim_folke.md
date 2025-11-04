
---
title: ts-comments.nvim
---


# ts-comments.nvim

- **GitHub 地址**: https://github.com/folke/ts-comments.nvim

## 主要特性

| 特性 | 说明 |
|------|------|
| **TreeSitter 上下文感知** | 根据光标所在的语法节点自动决定使用行注释、块注释或行内注释。 |
| **多语言支持** | 内置多种语言的注释符号映射，支持 `lua`、`python`、`javascript`、`c`、`cpp`、`rust` 等。 |
| **行/块/行内注释** | 可以在单行、选中范围或行尾添加注释。 |
| **可自定义注释符** | 通过 `comment_char` 或 `language_map` 进行自定义。 |
| **默认快捷键** | `gc`（切换注释）/ `gb`（块注释）/ `gn`（行内注释）。 |
| **Neovim 0.9+** | 依赖最新的 TreeSitter API。 |
| **与 nvim-treesitter 集成** | 需要先安装并启用对应语言的 TreeSitter。 |

## 功能概览

- **一键注释/取消注释**：`<leader>gc` 或 `gc` 在可注释节点上自动切换。  
- **块注释**：`<leader>gb` 或 `gb` 在选中范围内插入块注释。  
- **行内注释**：`<leader>gn` 或 `gn` 在当前行尾添加注释。  
- **自定义注释规则**：通过 `only_active_nodes` 限制仅对可注释节点生效。  
- **语言映射**：支持根据文件类型自动切换注释符号。  

## 安装

### packer.nvim

```lua
use {
  'folke/ts-comments.nvim',
  config = function()
    require('ts-comments').setup()
  end
}
```

### lazy.nvim

```lua
{
  'folke/ts-comments.nvim',
  config = function()
    require('ts-comments').setup()
  end
}
```

## 基本用法

| 快捷键 | 操作 |
|--------|------|
| `<leader>gc` | 切换注释（行或块） |
| `<leader>gb` | 块注释（选中范围） |
| `<leader>gn` | 行内注释（行尾） |

> **提示**：在 Visual 模式下使用同样的快捷键即可批量注释。

## 配置示例

```lua
require('ts-comments').setup({
  -- 默认快捷键，可自行修改
  keymaps = {
    toggle = '<leader>gc',
    block  = '<leader>gb',
    line   = '<leader>gn',
  },
  -- 仅对可注释节点生效
  only_active_nodes = true,
  -- 自定义注释符
  comment_char = '#',
  -- 语言到注释符的映射（可覆盖默认）
  language_map = {
    python   = '#',
    lua      = '--',
    javascript = '//',
    rust     = '//',
    c        = '//',
    cpp      = '//',
    sql      = '--',
  },
})
```

> 通过 `only_active_nodes = true` 可以避免在函数体外部误注释。

## 高级用法

- **在 Lua 中手动调用**  
  ```lua
  require('ts-comments').toggle()   -- 切换注释
  require('ts-comments').block()    -- 块注释
  require('ts-comments').line()     -- 行内注释
  ```

- **自定义注释范围**  
  在 `setup` 中添加 `node_types = { 'function', 'class' }`，仅对这些节点类型进行注释。

- **兼容 Telescope/Harpoon**  
  直接调用上述 Lua 函数即可将注释功能集成到自定义 Telescope 入口或 Harpoon 组。

## 兼容性

- **Neovim 0.9+**（TreeSitter API）  
- **nvim-treesitter**（已集成）  
- 需要安装对应语言的 TreeSitter 语法高亮插件（如 `treesitter#ensure_installed` 列表中包含目标语言）。

## 常见问题

| 问题 | 解决方案 |
|------|-----------|
| 插件不生效 | 确认 Neovim 版本 >= 0.9，已安装 `nvim-treesitter` 并启用对应语言。 |
| 注释符号错误 | 在 `language_map` 中手动指定正确的注释符号。 |
| 快捷键冲突 | 在 `keymaps` 中改写为你喜欢的键位。 |

## 贡献

> 请参考 [CONTRIBUTING.md](https://github.com/folke/ts-comments.nvim/blob/master/CONTRIBUTING.md)。

## 许可证

MIT

---  

> 以上内容已保存至 `src/content/docs/00/ts-comments.nvim_folke.md`。