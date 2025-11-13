---
title: BaiduPCS-Go
---

# BaiduPCS-Go 项目

**GitHub 项目地址:** [https://github.com/qjfoidnh/BaiduPCS-Go](https://github.com/qjfoidnh/BaiduPCS-Go)

## 主要特性

BaiduPCS-Go 是一个用 Go 语言实现的百度网盘命令行客户端，支持跨平台运行（Windows、macOS、Linux）。它提供高效的文件管理和传输功能，模拟百度PCS API 接口，实现与百度网盘的无缝交互。主要特性包括：

- **高性能传输**：支持多线程下载和上传，速度可达网盘上限。
- **跨平台支持**：无需安装额外依赖，直接编译运行。
- **命令行友好**：简单易用的 CLI 接口，支持脚本自动化，支持通配符匹配路径和 Tab 自动补齐命令和路径。
- **安全认证**：使用百度账号登录，避免浏览器操作。
- **文件管理**：支持本地与网盘间的同步、搜索和批量操作。
- **转存功能**：支持转存其他用户分享的文件，支持带密码的分享链接。
- **离线下载**：支持http/https/ftp/电驴/磁力链协议。
- **回收站管理**：支持回收站文件的列出、还原和删除。

## 主要功能

- **登录与认证**：通过百度账号登录，获取访问令牌，支持多用户切换。
- **文件上传/下载**：支持单文件、多文件和目录的上传下载，支持断点续传（下载）和分片上传（上传，不支持断点续传），支持秒传检测和同名文件策略配置。
- **文件管理**：列出目录、创建文件夹、重命名、删除文件/目录，拷贝、移动文件/目录。
- **搜索功能**：在网盘中搜索文件，支持关键词和路径过滤。
- **配额查询**：查看网盘使用空间和剩余容量。
- **元数据操作**：获取文件信息、修改分享链接等。
- **转存功能**：转存分享链接里的文件到指定目录。
- **分享管理**：设置分享文件/目录、列出已分享、取消分享。
- **离线下载**：添加、查询、取消、删除离线下载任务。
- **回收站**：列出回收站文件、还原、删除回收站文件。

## 用法

1. **安装**：
   - 下载预编译二进制文件从 GitHub Releases，或使用 Go 安装：`go install github.com/qjfoidnh/BaiduPCS-Go@latest`。
   - 确保 Go 环境已安装（可选）。

2. **登录**：

   ```
   ./baidupcs-go login
   ```

   支持多种登录方式，包括扫描二维码、输入验证码、BDUSS+STOKEN、Cookies。

3. **基本命令示例**：
   - 列出网盘根目录：`./baidupcs-go ls /`
   - 下载文件：`./baidupcs-go download /path/to/remote/file`
   - 上传文件：`./baidupcs-go upload local/file /path/to/remote/dir`
   - 搜索文件：`./baidupcs-go search keyword`
   - 查询配额：`./baidupcs-go quota`
   - 转存文件：`./baidupcs-go transfer <分享链接> <提取码>`
   - 离线下载：`./baidupcs-go offlinedl add -path=/ <资源地址>`

详细用法请参考项目 README.md 中的完整文档。支持 `-h` 或 `--help` 查看命令帮助。
