---
title: koreader
---


# KOReader

*GitHub 地址*: https://github.com/koreader/koreader

## 项目概述
KOReader 是一款开源的、轻量级的电子书阅读器，专为电子墨水（e‑ink）设备设计。支持多种文档格式，内置丰富的阅读功能和高度可定制的 UI，广泛应用于 Kindle、Kobo 等硬件平台。

## 主要特性

| 特性 | 说明 |
|------|------|
| **多格式支持** | PDF, ePub, mHTML, MOBI, CBZ/CBR, TXT, RTF 等 |
| **高效排版** | 软渲染 PDF/CBZ，内置 ePub 排版器，支持行间距/字体自定义 |
| **阅读导航** | 目录/书签、搜索、批注（笔记、划线、下划线） |
| **阅读模式** | 夜间模式、日间模式、灰度模式、纸张背景、语音朗读 |
| **外部来源** | 支持内网/FTP、Google Drive、Dropbox、CTBox、SSH、WebDAV 等 |
| **插件/自定义** | Lua 脚本插件、定制 UI、定制触摸手势 |
| **系统集成** | 支持通过 ACL, JavaScript, PDF 的 JavaScript 等 |

## 安装与配置

1. **获取源码**  
   ```bash
   git clone https://github.com/koreader/koreader.git
   cd koreader
   ```

2. **编译**  
   KOReader 需要交叉编译工具链，示例（以 ARMv7 + Linux 为例）：
   ```bash
   sudo apt-get install build-essential git
   make
   ```
   编译完成后，`koreader` 可执行文件位于 `build/` 目录。

3. **部署到设备**  
   将 `koreader` 可执行文件复制到设备上 `/usr/local/bin/koreader` 或设备可执行目录。

4. **配置文件**  
   KOReader 读取 `koreader.cfg` 或 `config.lua`。示例：
   ```yaml
   # 配置文件示例
   library:
     location: /home/user/Library
   appearance:
     theme: dark
     font_size: 18
   ```

## 常用命令

| 命令 | 用法 |
|------|------|
| `koreader -u` | 开始更新库（扫描书籍目录） |
| `koreader -c config.lua` | 指定自定义 Lua 配置文件 |
| `koreader -p /dev/input/event0` | 指定使用特定的输入事件设备 |

## 使用体验

- 开放的接口允许用户通过 Lua 脚本扩展功能，如自动调整字体、自动下载封面、批量转换格式等。
- 支持多点触控手势，用户可通过滑动、长按自定义快捷操作。
- PDF 页面滚动流畅，支持扇形滚动、双页视图等。
- 内置书架同步功能，可与云服务联动自动更新书库。

> **Tip**：你可以在 `plugins/` 目录添加新插件，或者在 `config.lua` 中通过 `require` 加载已存在的 Lua 模块。

## 贡献

- Fork 本仓库，提交 PR 进行功能改进或 Bug 修复。
- 如需帮助，请查看 `README.md` 与 `CONTRIBUTING.md`，或在 Issues 区提交 bug/需求。

---
**项目地址**: https://github.com/koreader/koreader
