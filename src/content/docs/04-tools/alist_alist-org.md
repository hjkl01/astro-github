---
title: alist
---

# AList 项目

## 项目地址
[https://github.com/alist-org/alist](https://github.com/alist-org/alist)

## 主要特性
AList 是一个开源的文件列表程序，支持多种存储服务，提供统一的 Web 界面访问和管理。它的主要特性包括：
- **多存储支持**：兼容阿里云盘、天翼云盘、OneDrive、Google Drive、Dropbox 等 50+ 种存储服务，以及本地存储、FTP 等。
- **统一访问**：通过单一入口访问所有存储，无需多个账号登录。
- **WebDAV 支持**：可作为 WebDAV 服务器使用，与支持 WebDAV 的客户端（如文件管理器）集成。
- **元数据管理**：支持文件预览、缩略图生成、搜索和标签管理。
- **安全性**：内置用户认证、权限控制、HTTPS 支持和访问日志。
- **跨平台**：支持 Linux、Windows、macOS 和 Docker 部署，轻量级且易扩展。
- **开源免费**：基于 Go 语言开发，MIT 许可，社区活跃。

## 主要功能
- **文件管理**：上传、下载、删除、重命名、移动文件，支持批量操作。
- **存储挂载**：动态添加和管理多个存储后端，支持虚拟文件系统（VFS）。
- **媒体预览**：集成视频、音频、图片、文档等预览功能，支持在线播放。
- **API 接口**：提供 RESTful API，便于第三方集成和自动化脚本。
- **策略与规则**：自定义访问策略、限速、缓存机制。
- **扩展插件**：支持 Aria2 下载、OnlyOffice 在线编辑等插件集成。

## 用法
1. **安装**：
   - 下载最新二进制文件从 GitHub Releases，或使用 Docker：`docker run -d --restart=unless-stopped -v /etc/alist:/opt/alist/data -p 5244:5244 --name="alist" xhofe/alist:latest`。
   - 运行 `./alist server` 启动服务，默认监听 5244 端口。

2. **初始配置**：
   - 首次访问 `http://localhost:5244`，设置管理员账号和密码。
   - 在 Web 界面进入“存储”页面，添加存储（如阿里云盘：输入账号、密码、刷新令牌）。

3. **使用**：
   - 通过 Web 界面浏览和管理文件，支持拖拽上传。
   - 分享文件：生成链接，支持密码保护和过期时间。
   - 作为 WebDAV 使用：在客户端（如 Windows 资源管理器）连接 `http://your-ip:5244/dav`，使用 Web 界面账号登录。
   - 高级用法：编辑 `conf.json` 配置参数，或通过 API 调用（如 `/api/fs/list` 获取文件列表）。

更多详情参考官方文档：https://alist.nn.ci/