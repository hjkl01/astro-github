---
title: nvim-colorizer.lua
---

## 功能介绍

`nvim-colorizer.lua` 是一个高性能的 Neovim 颜色高亮插件，用于在代码中实时高亮颜色值。它没有外部依赖，完全用 Lua 编写，支持多种颜色格式，包括：

- #RGB 和 #RRGGBB 十六进制颜色代码
- 颜色名称（如 Blue、Red 等）
- CSS 函数如 rgb()、rgba()、hsl()、hsla()
- 可选的 #RRGGBBAA 透明度支持

插件强调速度和性能，能够实时更新高亮，而不会影响编辑体验。支持前景色和背景色两种显示模式。

## 用法

### 安装

使用插件管理器安装，例如：

```vim
Plug 'norcalli/nvim-colorizer.lua'
```

### 基本设置

在 Neovim 配置中添加：

```lua
require'colorizer'.setup()
```

这将为所有文件类型启用颜色高亮。

### 自定义配置

可以为特定文件类型设置选项：

```lua
require'colorizer'.setup({
  'css',
  'javascript',
  html = {
    mode = 'foreground'
  }
})
```

支持的选项包括：

- `RGB`: 启用 #RGB 格式
- `RRGGBB`: 启用 #RRGGBB 格式
- `names`: 启用颜色名称
- `RRGGBBAA`: 启用透明度格式
- `rgb_fn`: 启用 CSS rgb() 函数
- `hsl_fn`: 启用 CSS hsl() 函数
- `css`: 启用所有 CSS 功能
- `mode`: 显示模式 ('foreground' 或 'background')

### 命令

- `:ColorizerAttachToBuffer` - 为当前缓冲区启用高亮
- `:ColorizerDetachFromBuffer` - 停止当前缓冲区高亮
- `:ColorizerReloadAllBuffers` - 重新加载所有缓冲区设置
- `:ColorizerToggle` - 切换当前缓冲区高亮

### 注意事项

- 需要 Neovim >= 0.4.0 和 `set termguicolors`
- 对于无文件类型的缓冲区，需要手动运行 `:ColorizerAttachToBuffer`
