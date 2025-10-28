
---
title: BaiduPCS-Go
---

# BaiduPCS-Go 项目

**GitHub 项目地址:** [https://github.com/qjfoidnh/BaiduPCS-Go](https://github.com/qjfoidnh/BaiduPCS-Go)

## 主要特性
BaiduPCS-Go 是一个用 Go 语言实现的百度网盘命令行客户端，支持跨平台运行（Windows、macOS、Linux）。它提供高效的文件管理和传输功能，模拟百度PCS API 接口，实现与百度网盘的无缝交互。主要特性包括：
- **高性能传输**：支持多线程下载和上传，速度可达网盘上限。
- **跨平台支持**：无需安装额外依赖，直接编译运行。
- **命令行友好**：简单易用的 CLI 接口，支持脚本自动化。
- **安全认证**：使用百度账号登录，避免浏览器操作。
- **文件管理**：支持本地与网盘间的同步、搜索和批量操作。

## 主要功能
- **登录与认证**：通过百度账号登录，获取访问令牌。
- **文件上传/下载**：支持单文件、多文件和目录的上传下载，支持断点续传。
- **文件管理**：列出目录、创建文件夹、重命名、删除文件/目录。
- **搜索功能**：在网盘中搜索文件，支持关键词和路径过滤。
- **配额查询**：查看网盘使用空间和剩余容量。
- **元数据操作**：获取文件信息、修改分享链接等。

## 用法
1. **安装**：
   - 下载预编译二进制文件从 GitHub Releases，或使用 Go 安装：`go install github.com/qjfoidnh/BaiduPCS-Go@latest`。
   - 确保 Go 环境已安装（可选）。

2. **登录**：
   ```
   ./baidupcs-go login
   ```
   打开浏览器扫描二维码或输入验证码完成授权。

3. **基本命令示例**：
   - 列出网盘根目录：`./baidupcs-go ls /`
   - 下载文件：`./baidupcs-go download /path/to/remote/file local/path`
   - 上传文件：`./baidupcs-go upload local/file /path/to/remote/dir`
   - 搜索文件：`./baidupcs-go search keyword`
   - 查询配额：`./baidupcs-go quota`

详细用法请参考项目 README.md 中的完整文档。支持 `-h` 或 `--help` 查看命令帮助。