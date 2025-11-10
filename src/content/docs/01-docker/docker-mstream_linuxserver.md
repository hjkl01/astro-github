---
title: docker-mstream
---

# mStream Docker 项目

**项目地址:** [https://github.com/linuxserver/docker-mstream](https://github.com/linuxserver/docker-mstream)

## 主要特性
- **开源音乐流媒体服务器**: mStream 是一个轻量级的自托管音乐流媒体解决方案，支持跨设备同步和流式传输音乐库。
- **Docker 容器化部署**: 由 LinuxServer.io 维护，提供易于安装和管理的 Docker 镜像，支持多种架构（如 x86-64、ARM 等）。
- **多平台支持**: 兼容 Linux、macOS 和 Windows 主机，支持 Web 界面访问和移动 App 客户端。
- **高效资源使用**: 低内存占用，适合在 NAS、Raspberry Pi 或 VPS 上运行。
- **安全特性**: 支持 HTTPS 配置和用户认证，确保音乐库隐私。

## 主要功能
- **音乐库管理**: 自动扫描和索引本地音乐文件夹，支持 MP3、FLAC 等常见格式。
- **远程访问**: 通过 Web 界面或专用 App（如 Android/iOS）从任何设备流式传输音乐，无需上传到云端。
- **同步功能**: 支持设备间音乐同步，自动更新新添加的曲目。
- **播放列表支持**: 创建和管理播放列表，支持随机播放和跨设备共享。
- **扩展性**: 可集成外部存储（如 SMB/NFS），并支持插件扩展（如 Last.fm 集成）。

## 用法
1. **安装 Docker**: 确保主机已安装 Docker 和 Docker Compose。
2. **拉取镜像**: 使用命令 `docker pull lscr.io/linuxserver/mstream` 下载最新镜像。
3. **运行容器**: 通过 Docker Compose 或命令行启动，例如：
   ```
   docker run -d \
     --name=mstream \
     -e PUID=1000 \
     -e PGID=1000 \
     -p 3000:3000 \
     -v /path/to/music:/music \
     -v /path/to/config:/config \
     --restart unless-stopped \
     lscr.io/linuxserver/mstream
   ```
   - `-v /path/to/music:/music`: 挂载音乐文件夹。
   - `-v /path/to/config:/config`: 挂载配置文件目录。
   - `-p 3000:3000`: 暴露 Web 端口。
4. **访问界面**: 在浏览器中打开 `http://your-host-ip:3000`，设置用户名和密码后开始使用。
5. **配置**: 编辑容器内的 `server.ini` 文件调整设置，如启用 HTTPS 或更改端口。更多细节参考项目 README。