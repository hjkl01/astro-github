
---
title: lapce
---


# Lapce

**项目地址:** https://github.com/lapce/lapce

Lapce 是一款基于 Rust Language 开发、使用 Flutter 框架构建的轻量级、跨平台代码编辑器。它兼具现代界面与强大的编辑功能，专为提高开发效率而设计。

## 主要特性

- **高性能渲染**：使用 Flutter 的绘制引擎，保证流畅的 UI 响应和占用低资源。
- **多语言语法高亮**：支持 60+ 语言的高亮与智能提示。
- **语言服务器协议（LSP）**：原生集成 LSP，提供代码补全、跳转、诊断等智能功能。可通过配置自动安装与管理对应语言服务器。
- **内置终端**：一键打开与代码目录同步的终端，支持多标签。
- **文件资源管理**：侧边栏文件树、面板搜索、批量重命名等文件操作工具。
- **多标签 & 代码折叠**：支持无限标签页与代码段折叠，便于大型项目浏览。
- **插件生态**：通过内置插件市场可下载安装主题、主题色、插件等，支持自定义插件。
- **主题 & 主题色**：默认暗色与亮色主题，支持第三方主题。
- **键盘快捷键 & 配置**：支持全局键盘快捷键设置，提供可视化配置面板。
- **跨平台**：支持 Windows、macOS、Linux 发行版。

## 快速上手

### 1. 安装

#### 官方发行版

- **Windows/Mac/Linux**  
  访问 Releases 页面下载对应平台的二进制压缩包，解压后运行即可。

#### 源码构建（需要 Rust 1.70+）

```bash
git clone https://github.com/lapce/lapce.git
cd lapce
cargo build --release
```

构建完成后，执行生成的可执行文件：`./target/release/lapce`。

### 2. 打开项目

```bash
lapce /path/to/your/project
```

或在 UI 右上角选择 **Open Folder**。

### 3. 基本使用

| 功能 | 快捷键 | 说明 |
|------|--------|------|
| 新建窗口 | `Ctrl+Shift+N` | 打开独立窗口 |
| 新建标签 | `Ctrl+T` | 新建空白文件 |
| 切换标签 | `Ctrl+Tab` | 切换到下一个标签 |
| 跳转到定义 | `F12` | 在 LSP 支持的文件中跳转 |
| 终端 | `Ctrl+` | 打开/切换终端面板 |
| 搜索文件 | `Ctrl+P` | 快捷打开文件 |
| 代码搜索 | `Ctrl+Shift+F` | 全局搜索文本 |
| 侧边栏 | `Ctrl+B` | 切换侧边栏可视化 |
| 主题切换 | `Ctrl+K Ctrl+T` | 切换主题 |

### 4. 配置与插件

- **settings.json**：位于 `~/.config/lapce/settings.json`。可手动编辑主题、颜色、快捷键等。
- **插件管理**：在 `Extensions` 面板搜索并安装所需插件。插件可以自定义脚本、添加新功能。

```json
{
  "editor.fontSize": 14,
  "workbench.colorTheme": "Lapce Dark",
  "lapce.lsp.use_dap": true
}
```

### 5. 运行与调试

Lapce 支持 DAP（Debug Adapter Protocol），在 `Launch.json` 配置项中设置断点、运行参数后即可调试：
```json
{
  "name": "Launch",
  "type": "cppdbg",
  "request": "launch",
  "program": "${workspaceFolder}/main",
  "args": [],
  "stopAtEntry": false,
  "cwd": "${workspaceFolder}"
}
```

---

> **快速提示**  
> - 使用 `Ctrl+Shift+F` 可以在所有文件中进行文本搜索。  
> - 插件 `lapce-git` 为 Git 提供了丰富的 UI，支持提交、分支切换、冲突解决等。  
> - 通过 `Ctrl+P` 后跟 `>` 可以快速打开命令面板，执行任意 Lapce 命令。  

> 进一步支持与社区贡献请查看官方仓库（issues, PRs）。  

---  
> **Base Features**  
> - Minimalist editor with strong focus on Rust-based speed and Flutter UI.  
> - Build on LSP for language features, with extensible plugin ecosystem akin to VS Code plus less overhead.  

> **How to contribute**  
> - Fork → clone → `cargo build --release`  
> - Submit PR to `main` branch with descriptive commit messages.
