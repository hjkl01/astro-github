---
title: lf
---

# lf

**作者**: gokcehan  
**项目地址**: https://github.com/gokcehan/lf

## 项目介绍

`lf` 是一个用 Go 编写的终端文件管理器，受 `ranger` 文件管理器启发。它提供了快速、轻量级的文件浏览和管理体验。

## 主要功能

- **跨平台支持**: 支持 Linux、macOS、BSDs 和 Windows
- **单二进制无依赖**: 无需运行时依赖，静态二进制文件
- **高性能**: 快速启动，低内存占用
- **异步 IO**: 避免 UI 锁定
- **服务器/客户端架构**: 支持远程命令管理多个实例
- **可扩展性**: 通过 shell 命令扩展和配置
- **自定义键绑定**: 支持 vi 和 readline 默认绑定
- **其他特性**: 图标显示、预览、书签等

## 非功能特性

- 不支持标签或窗口（建议使用窗口管理器或终端多路复用器）
- 无内置分页器/编辑器（使用您选择的工具）
- 无内置文件操作命令（使用底层 shell 工具如 `mkdir`、`touch`、`chmod` 等）

## 安装

### 从源码构建

需要安装 [Go](https://go.dev/)。

**Unix 系统**:

```bash
env CGO_ENABLED=0 go install -ldflags="-s -w" github.com/gokcehan/lf@latest
```

**Windows (cmd)**:

```cmd
set CGO_ENABLED=0
go install -ldflags="-s -w" github.com/gokcehan/lf@latest
```

**Windows (PowerShell)**:

```powershell
$env:CGO_ENABLED = '0'
go install -ldflags="-s -w" github.com/gokcehan/lf@latest
```

### 预构建二进制

查看 [releases](https://github.com/gokcehan/lf/releases) 页面下载预构建二进制文件。

### 社区维护包

查看 [packages](https://github.com/gokcehan/lf/wiki/Packages) 获取社区维护的包。

## 使用方法

### 基本使用

安装后，在终端运行 `lf` 命令启动文件管理器，默认在当前目录启动。

### 命令行选项

运行 `lf -help` 查看所有命令行选项。

### 文档

运行 `lf -doc` 查看内置文档，或查看 [doc.md](https://github.com/gokcehan/lf/blob/master/doc.md)。

### 配置

查看 [etc](https://github.com/gokcehan/lf/tree/master/etc) 目录获取示例配置文件，包括 shell 集成、编辑器集成、颜色和图标配置。

### 集成

- [integrations](https://github.com/gokcehan/lf/wiki/Integrations): 与其他工具的集成
- [tips](https://github.com/gokcehan/lf/wiki/Tips): 使用技巧和示例

## 社区

- [Google Groups](https://groups.google.com/forum/#!forum/lf-fm)
- IRC: [#lf](https://web.libera.chat/#lf) (Libera.Chat)
- Matrix: [#lf:matrix.org](https://matrix.to/#/#lf:matrix.org)
