
---
title: docker-webtop
---

# LinuxServer.io Webtop 项目

## 项目地址
[https://github.com/linuxserver/docker-webtop](https://github.com/linuxserver/docker-webtop)

## 主要特性
- **基于 Docker 的 Web 桌面环境**：提供了一个完整的 Linux 桌面体验，通过 Web 浏览器访问，支持多种桌面环境如 XFCE、KDE、MATE 等。
- **跨平台兼容性**：无需安装本地软件，只需浏览器即可访问，支持 Windows、macOS、Linux 和移动设备。
- **容器化部署**：利用 Docker 容器技术，易于部署和管理，支持 ARM 和 x86 架构。
- **自定义选项**：支持多种 Linux 发行版（如 Ubuntu、Debian、Fedora）和桌面主题，允许用户自定义分辨率、键盘布局等。
- **安全性与隔离**：每个实例独立运行，提供安全的沙箱环境，适合开发、测试或远程访问。

## 主要功能
- **Web 界面访问**：通过浏览器登录，获得完整的桌面界面，包括文件管理器、终端、浏览器和办公软件。
- **文件共享与持久化**：支持挂载主机目录，实现数据持久化和与主机文件的共享。
- **VNC/RDP 支持**：内置 VNC 服务器，支持远程桌面协议（RDP），便于远程控制。
- **多用户支持**：可配置多用户环境，适用于团队协作或教育场景。
- **资源管理**：容器化设计允许轻松调整 CPU、内存和存储资源，优化性能。

## 用法
1. **安装 Docker**：确保系统已安装 Docker 和 Docker Compose。
2. **拉取镜像**：使用命令 `docker pull lscr.io/linuxserver/webtop:latest`（替换 `latest` 为特定标签，如 `ubuntu-xfce`）。
3. **运行容器**：示例命令：
   ```
   docker run -d \
     --name=webtop \
     -e PUID=1000 \
     -e PGID=1000 \
     -e TZ=Asia/Shanghai \
     -e PASSWORD=yourpassword \
     -p 3000:3000 \
     -v /path/to/config:/config \
     --shm-size="1gb" \
     --restart unless-stopped \
     lscr.io/linuxserver/webtop:ubuntu-xfce
   ```
   - `PUID/PGID`：设置用户/组 ID。
   - `PASSWORD`：设置登录密码。
   - `-v`：挂载配置目录以持久化数据。
4. **访问界面**：在浏览器中打开 `http://your-host-ip:3000`，输入密码登录桌面。
5. **高级配置**：参考 GitHub 仓库的 README，调整环境变量如 `RESOLUTION=1920x1080` 或 `KEYBOARD=zh` 以自定义设置。使用 Docker Compose 文件简化多容器部署。