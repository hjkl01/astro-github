
---
title: oh-my-posh
---


# oh-my-posh

**项目地址**: https://github.com/JanDeDobbeleer/oh-my-posh

## 概述
oh-my-posh 是一个跨平台的命令行提示词（prompt）生成器，专为 PowerShell、bash、zsh、fish 等 shell 设计。它利用 ANSI 颜色、Unicode 字符、Powerline 字体以及自定义模板来创建可视化、信息丰富且可高度定制的提示符。

## 主要特性
- **跨平台**：支持 Windows、macOS、Linux 的 PowerShell、bash、zsh、fish。
- **主题化**：提供数百个预设主题，支持自定义 JSON/INI/Go模板。
- **信息展示**：显示当前目录、Git 状态、虚拟环境、进程 ID、时间、天气、CPU/内存使用率等。
- **图形化元素**：支持 Powerline 字体、Unicode 字符、图标、徽标。
- **性能优化**：使用 Go 语言编译为二进制，启动速度快，资源占用低。
- **插件化**：通过 `oh-my-posh init` 命令动态加载脚本，支持插件扩展。

## 功能概览
| 功能 | 说明 |
|------|------|
| **Git 状态** | 显示分支、未提交更改、冲突、stash 等 |
| **目录层级** | 显示完整路径或缩略路径 |
| **虚拟环境** | 自动识别 Python、Node、Go 等虚拟环境 |
| **时间/日期** | 可自定义显示格式 |
| **系统信息** | CPU、内存、磁盘、网络状态 |
| **天气** | 集成天气 API，显示当前天气 |
| **自定义命令** | 允许用户添加自定义段落或脚本 |
| **多语言** | 支持多语言提示符布局 |

## 安装

### 1. 通过包管理器安装
- **Windows (PowerShell)**:
  ```powershell
  Install-Module oh-my-posh -Scope CurrentUser
  ```
- **macOS / Linux (bash/zsh)**:
  ```bash
  brew install jandedobbeleer/oh-my-posh/oh-my-posh
  ```

### 2. 手动下载
从 Releases 页面下载对应平台的二进制文件，放置于 PATH 中。

## 用法

### 初始化
在 shell 配置文件中添加如下行（示例为 PowerShell）:
```powershell
Import-Module oh-my-posh
Set-PoshPrompt -Theme Paradox
```
或使用快捷命令：
```powershell
oh-my-posh init pwsh --config Paradox | Invoke-Expression
```

### 切换主题
```bash
oh-my-posh set theme Paradox
```

### 创建自定义主题
1. 复制现有主题文件（`.json` 或 `.ini`）到 `~/.poshthemes`。
2. 编辑文件，修改颜色、段落或添加自定义脚本。
3. 在配置文件中引用自定义主题。

### 自定义段落示例
```json
{
  "type": "segment",
  "properties": {
    "style": "powerline",
    "foreground": "black",
    "background": "cyan",
    "prefix": " ",
    "suffix": " "
  },
  "functions": [
    {
      "name": "customTime",
      "command": "Get-Date -Format 'HH:mm:ss'"
    }
  ]
}
```

## 示例

```powershell
# PowerShell 示例
Import-Module oh-my-posh
Set-PoshPrompt -Theme Paradox
```

```bash
# bash 示例
eval "$(oh-my-posh init bash --config Paradox)"
```

## 文档与支持
- 官方文档: https://ohmyposh.dev/docs
- GitHub Issues: https://github.com/JanDeDobbeleer/oh-my-posh/issues
- 社区讨论: https://github.com/JanDeDobbeleer/oh-my-posh/discussions

---

> **提示**：使用 `oh-my-posh --help` 查看所有可用命令和参数。
