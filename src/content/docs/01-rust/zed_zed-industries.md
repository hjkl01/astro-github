
---
title: zed
---


# Zed 编辑器（zed-industries/zed）

> 项目地址：[https://github.com/zed-industries/zed](https://github.com/zed-industries/zed)

---

## 概述
Zed 是一个用 Rust 编写、支持多平台的现代化浏览器式代码编辑器。其核心设计理念是“轻量、可扩展、可协作”，通过插件化插件体系、内嵌终端、原生 WebView 等技术提供高性能的编辑体验。

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **跨平台** | 兼容 Windows、macOS、Linux，部分 Alpine 版本。 |
| **本地/远程文件** | 通过 Zed Server 与远程服务器直接联机，支持 SSH、Git 等协议。 |
| **分屏/选项卡** | 多标签页、水平/垂直拆分窗口，可随意拖拽。 |
| **内置终端** | 与编辑器共享环境，支持 Bash、PowerShell、WSL 等。 |
| **插件系统** | 提供一个插件接口（Plug-in API），可用 Rust 或 TypeScript 开发。 |
| **语法高亮 + 代码补全** | 基于 Language Server Protocol（LSP），支持多种语言。 |
| **原生 WebView** | 允许在编辑器内直接查看网页内容。 |
| **多人协作** | 基于 Zed Server 的实时协作功能（Beta）。 |

---

## 主要功能

1. **文件浏览器**  
   - 侧边栏支持目录树、图标化显示。  
   - 可以直接拖拽文件或文件夹打开。

2. **设置与主题**  
   - 全局设置面板：字体、缩进、插件、快捷键。  
   - 主题可通过插件进行更改，支持暗黑/亮色主题。

3. **编辑器**  
   - 行号、括号匹配、代码折叠。  
   - 多点编辑、记录重做、撤销。  
   - 搜索与替换支持正则。

4. **终端**  
   - 支持多终端实例，并可通过快捷键切换。  
   - 与项目根目录同步自动切换。

5. **插件管理**  
   - `zed` CLI 允许直接安装、更新插件。  
   - 插件目录位于 `~/.config/zed/plugins/`。  

6. **版本控制**  
   - 内置 Git、Mercurial、SVN。  
   - 提供提交、分支管理、冲突解决 UI。

7. **文档查看**  
   - 通过 `zed -d` 打开 Markdown / HTML 文档。  
   - 可在侧边栏预览。  

---

## 用法

### 1. 安装
```bash
# 通过 Cargo 安装
cargo install zed
```

> **提示**：如果没有 Cargo，请先安装 Rust 组件。  
> 也可以直接下载官方预编译包，地址见[Release 页面](https://github.com/zed-industries/zed/releases)。

### 2. 运行
在项目目录下执行：
```bash
zed .
```
- `.` 打开当前目录。  
- `zed 文件名` 打开单个文件。  

### 3. 基本快捷键
| 功能 | 快捷键（Windows/Linux） | 快捷键（macOS） |
|------|-------------------------|-----------------|
| 新建文件 | Ctrl+N | Cmd+N |
| 打开文件 | Ctrl+O | Cmd+O |
| 保存 | Ctrl+S | Cmd+S |
| 关闭标签 | Ctrl+W | Cmd+W |
| 侧边栏切换 | Ctrl+B | Cmd+B |
| 整行复制 | Ctrl+Shift+Alt+↑/↓ | Cmd+Shift+Option+↑/↓ |
| 行号面板 | Toggle | Toggle |
| 终端面板 | Ctrl+` | Cmd+` |

> 通过 `Ctrl+K Ctrl+S` 可查看完整快捷键列表。

### 4. 插件安装
```bash
# 安装官方插件
zed install <plugin-id>
# 例：安装 zed/lsp-injection
zed install zed/lsp-injection
```

### 5. 支持的语言
Zed 通过 LSP 识别多种语言：JavaScript/TypeScript、Python、Go、Rust、C、C++、Java、HTML/CSS、JSON 等。只需在对应语言相关配置中添加 LSP 服务器即可生效。

---

## 结语
Zed 旨在提供一种高效、可扩展且现代化的代码编辑体验。通过简洁的 UI、强大的本地/远程文件支持以及插件生态，能满足从日常编程到跨平台协作的多种工作场景。欢迎参与贡献，提交 Issue 与 PR 🚀

---