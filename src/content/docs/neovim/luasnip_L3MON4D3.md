---
title: LuaSnip
---

# LuaSnip

https://github.com/L3MON4D3/LuaSnip

> Description from GitHub: Snippet Engine for Neovim written in Lua.

## Installation

Use with your plugin manager:

```lua
use({
    "L3MON4D3/LuaSnip",
    -- 跟随最新发布版本
    tag = "v2.*", -- 将 <CurrentMajor> 替换为最新发布的主要版本号
    -- 可选：安装 jsregexp
    run = "make install_jsregexp"
})
```

Or:

```lua
{
    "L3MON4D3/LuaSnip",
    -- 跟随最新发布版本
    version = "v2.*", -- 将 <CurrentMajor> 替换为最新发布的主要版本号
    -- 可选：安装 jsregexp
    build = "make install_jsregexp"
}
```

For Vim:

跟随最新发布版本并安装 jsregexp.

## Notes

jsregexp is used for ECMAScript regex in LSP snippet transformations. Without it, transformations fall back to simple copies.
