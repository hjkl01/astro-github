
---
title: aliyundrive-webdav
---

# AliyunDrive WebDAV 项目

## 项目地址
[https://github.com/messense/aliyundrive-webdav](https://github.com/messense/aliyundrive-webdav)

## 主要特性
- **WebDAV 协议支持**：将阿里云盘转换为 WebDAV 服务，允许通过标准 WebDAV 客户端访问和管理文件。
- **多用户支持**：支持多个阿里云盘账号登录，实现文件共享和多盘管理。
- **文件同步与传输**：支持上传、下载、删除、移动等文件操作，兼容主流文件管理工具。
- **安全认证**：使用阿里云盘的 OAuth 授权机制，确保数据安全。
- **轻量级部署**：基于 Rust 开发，性能高效，支持 Docker 容器化部署。
- **跨平台兼容**：可在 Windows、macOS、Linux 等系统上运行，支持各种 WebDAV 客户端如 Cyberduck、WinSCP 等。

## 主要功能
- **文件浏览与管理**：通过 WebDAV 协议浏览阿里云盘目录、预览文件。
- **实时同步**：支持双向文件同步，自动处理文件变更。
- **分享与协作**：可将阿里云盘文件映射为网络驱动器，便于团队协作。
- **API 集成**：提供 RESTful API 接口，便于与其他应用集成。
- **日志与监控**：内置日志记录和错误处理，便于调试和维护。

## 用法
1. **安装**：
   - 使用 Cargo（Rust 包管理器）安装：`cargo install aliyundrive-webdav`。
   - 或使用 Docker：`docker pull messense/aliyundrive-webdav`。

2. **配置**：
   - 获取阿里云盘 Refresh Token：访问 [阿里云盘开放平台](https://openapi.aliyundrive.com/)，通过 OAuth 流程获取 token。
   - 创建配置文件（如 `config.toml`），设置 token 和 WebDAV 端口，例如：
     ```
     [server]
     host = "0.0.0.0"
     port = 8080

     [aliyundrive]
     refresh_token = "your_refresh_token"
     ```

3. **运行**：
   - 命令行启动：`aliyundrive-webdav --config config.toml`。
   - Docker 运行：`docker run -d -p 8080:8080 -v /path/to/config:/config messense/aliyundrive-webdav`。

4. **连接客户端**：
   - 在 WebDAV 客户端中输入服务器地址（如 `http://localhost:8080`），使用用户名/密码（可选，根据配置）连接。
   - 即可像本地驱动器一样管理阿里云盘文件。