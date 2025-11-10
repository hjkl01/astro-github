---
title: mason.nvim
---

# mason.nvim

## 简介

mason.nvim 是一个便携式的 Neovim 包管理器，能够在任何运行 Neovim 的地方运行。它允许您轻松安装和管理外部编辑器工具，如 LSP 服务器、DAP 服务器、linters 和 formatters。

包默认安装在 Neovim 的数据目录中，可执行文件链接到单个 `bin/` 目录，mason.nvim 在设置期间会将其添加到 Neovim 的 PATH 中，从而实现从 Neovim 内置功能（LSP 客户端、shell、终端等）以及其他第三方插件的无缝访问。

## 功能

- **便携性**：在 Linux、macOS、Windows 等任何 Neovim 运行的环境中工作。
- **统一管理**：通过单一界面管理 LSP 服务器、DAP 服务器、linters 和 formatters。
- **自动 PATH 管理**：将安装的工具添加到 Neovim 的 PATH 中。
- **图形界面**：提供图形状态窗口来管理包。
- **并发安装**：支持同时安装多个包。
- **注册表支持**：使用 mason-registry 来获取可用包列表。

## 用法

### 安装

使用您的插件管理器安装 mason.nvim。例如，使用 lazy.nvim：

```lua
{
    "mason-org/mason.nvim",
    opts = {}
}
```

或者手动安装后，在您的 Neovim 配置中设置：

```lua
require("mason").setup()
```

### 命令

- `:Mason` - 打开图形状态窗口
- `:MasonUpdate` - 更新所有托管注册表
- `:MasonInstall <package> ...` - 安装/重新安装指定的包
- `:MasonUninstall <package> ...` - 卸载指定的包
- `:MasonUninstallAll` - 卸载所有包
- `:MasonLog` - 在新标签页窗口中打开 mason.nvim 日志文件

### 配置

您可以在 `setup()` 函数中配置行为。例如：

```lua
require("mason").setup({
    ui = {
        icons = {
            package_installed = "✓",
            package_pending = "➜",
            package_uninstalled = "✗"
        }
    }
})
```

### 要求

- Neovim >= 0.10.0
- Unix 系统：git, curl 或 wget, unzip, GNU tar, gzip
- Windows 系统：PowerShell 或 pwsh, git, GNU tar, 解压工具（如 7zip）

更多详细信息，请参考 `:help mason.nvim`。
