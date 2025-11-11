---
title: copyparty
---

# copyparty

## 项目简介

copyparty 是一个便携式文件服务器，提供加速的可恢复上传、去重、WebDAV、FTP、TFTP、zeroconf、媒体索引器、缩略图等功能，所有功能集成在一个文件中，无需依赖。

## 主要功能

- **服务器要求**：仅需 Python 2 或 3，所有依赖可选。
- **支持协议**：
  - HTTP
  - WebDAV
  - FTP
  - TFTP
  - SMB/CIFS
- **客户端支持**：
  - Android 应用
  - iOS Shortcuts
- **上传功能**：
  - 基本 multipart 上传，支持 IE6
  - up2k：JS 驱动，可恢复、多线程上传，无文件大小限制
  - 拖拽文件夹上传
  - 文件名随机化
  - 只写文件夹
  - 上传撤销/删除
  - 自毁上传（指定服务器端或客户端）
  - 上传时下载（几乎像点对点）
  - 内容匹配去重
- **下载功能**：
  - 浏览器中下载单个文件
  - 将文件夹下载为 ZIP 或 TAR 文件
  - FUSE 客户端（只读）
- **浏览器界面**：
  - 导航面板（目录树侧边栏）
  - 文件管理器（剪切/粘贴、重命名、删除）
  - 音频播放器（支持几乎所有音频格式，包括 OS 媒体控件和 Opus/MP3 转码）
  - 图像画廊与 WebM 播放器
  - 文本文件浏览器（带语法高亮，支持实时流式传输日志文件）
  - Markdown 查看器和编辑器
  - 多语言 UI（英语、挪威语、中文等）
  - SPA（上传时浏览）
- **服务器索引**：
  - 按内容定位文件
  - 按名称/路径/日期/大小搜索
  - 按 MP3 标签等搜索
- **客户端支持**：
  - 文件夹同步（单向）
  - 挂载为驱动器
- **其他**：
  - 跨平台（Windows、Linux、MacOS、Android、iOS、FreeBSD 等）
  - 零配置（Zeroconf / mDNS / SSDP）
  - 事件钩子 / 脚本运行器
  - 反向代理支持
  - Prometheus 指标

## 快速开始

1. 下载并运行 [copyparty-sfx.py](https://github.com/9001/copyparty/releases/latest/download/copyparty-sfx.py)：

   ```bash
   python copyparty-sfx.py
   ```

   这将在当前文件夹中启动服务器，提供读写访问。

2. 启用可选功能：
   - 缩略图、媒体索引、音频转码：安装 `python3-pil ffmpeg`（Alpine/Debian 等）或 `Pillow ffmpeg`（Windows）。

3. 基本用法：
   - 访问 `http://127.0.0.1:3923` 以浏览和上传文件。
   - 拖拽文件到浏览器上传。
   - 使用 `-v /path/to/folder::r` 设置只读文件夹。
   - 使用 `-a username:password` 添加账户。

## 配置示例

- 允许任何人上传到当前文件夹：

  ```bash
  python copyparty-sfx.py
  ```

- 设置账户和权限：

  ```bash
  python copyparty-sfx.py -a user:pass -v /music:/music:r,user
  ```

- 启用索引和搜索：
  ```bash
  python copyparty-sfx.py -e2dsa -e2ts
  ```

## 更多信息

- 项目主页：[https://github.com/9001/copyparty](https://github.com/9001/copyparty)
- 演示服务器：[https://a.ocv.me/pub/demo/](https://a.ocv.me/pub/demo/)
- 完整文档：[README.md](https://github.com/9001/copyparty/blob/hovudstraum/README.md)
