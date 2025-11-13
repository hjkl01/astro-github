---
title: aliyundrive-webdav
---

# AliyunDrive WebDAV 项目

## 项目地址

[https://github.com/messense/aliyundrive-webdav](https://github.com/messense/aliyundrive-webdav)

## 主要特性

- **WebDAV 服务**：将阿里云盘转换为 WebDAV 服务，主要用于配合支持 WebDAV 协议的客户端如 Infuse、nPlayer 等在电视上观看云盘视频。
- **直接播放**：支持客户端直接从阿里云盘获取文件播放，不经过服务器中转。
- **上传支持**：支持上传文件，但受限于 WebDAV 协议不支持文件秒传，且上传功能测试不全面。
- **V2 版本**：基于阿里云盘开放平台接口实现，不再支持阿里云盘 Web 和 App 版本获取的 refresh token。
- **多种安装方式**：支持二进制下载、pip 安装、snap 安装、Docker 运行等。
- **跨平台**：支持 Windows、macOS、Linux 等系统，以及 OpenWrt 路由器。

## 用法

1. **安装**：
   - 从 [GitHub Releases](https://github.com/messense/aliyundrive-webdav/releases) 下载预先构建的二进制包。
   - 使用 pip：`pip install aliyundrive-webdav`。
   - 使用 snap：`sudo snap install aliyundrive-webdav`。
   - 使用 Docker：`docker run -d --name=aliyundrive-webdav --restart=unless-stopped -p 8080:8080 -v /etc/aliyundrive-webdav/:/etc/aliyundrive-webdav/ -e REFRESH_TOKEN='your refresh token' -e WEBDAV_AUTH_USER=admin -e WEBDAV_AUTH_PASSWORD=admin messense/aliyundrive-webdav`。
   - OpenWrt：下载对应架构的 ipk 文件，使用 opkg 安装。

2. **获取 refresh token**：
   - 通过在线工具：[https://messense-aliyundrive-webdav-backendrefresh-token-ucs0wn.streamlit.app/](https://messense-aliyundrive-webdav-backendrefresh-token-ucs0wn.streamlit.app/)。
   - 或命令行：`aliyundrive-webdav qr login` 扫码授权。

3. **运行**：
   - 命令行：`aliyundrive-webdav -r 'your_refresh_token'`。
   - Docker：如安装步骤中的命令。

4. **连接客户端**：
   - 在 WebDAV 客户端中输入服务器地址（如 `http://localhost:8080`），使用设置的用户名/密码连接。
   - 即可访问阿里云盘文件。
