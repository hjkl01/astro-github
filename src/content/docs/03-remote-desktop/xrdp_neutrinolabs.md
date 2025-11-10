---
title: xrdp
---

# xrdp 项目

## 项目地址
[GitHub 项目地址](https://github.com/neutrinolabs/xrdp)

## 主要特性
xrdp 是一个开源的远程桌面协议 (RDP) 服务器实现，旨在为 Linux 和其他类 Unix 系统提供 RDP 连接支持。其主要特性包括：
- **跨平台兼容性**：支持 Windows、macOS 和 Linux 客户端通过 RDP 协议连接到 Linux 服务器。
- **多会话支持**：允许多个用户同时连接，支持会话管理和断开重连。
- **模块化设计**：集成 X11、Xvnc 等后端，支持多种图形界面（如 Xorg、Wayland）。
- **安全性**：支持 TLS 加密、证书验证和 PAM 认证集成，提高连接安全性。
- **轻量级**：资源占用低，适合服务器环境部署。
- **开源免费**：基于 GNU GPL 许可，社区维护活跃。

## 主要功能
xrdp 的核心功能聚焦于远程桌面访问：
- **RDP 服务器**：实现 RDP 协议栈，允许客户端使用 Microsoft RDP、FreeRDP 或 rdesktop 等工具连接。
- **会话管理**：自动启动用户桌面环境（如 GNOME、KDE、XFCE），支持音视频重定向和剪贴板共享。
- **认证与授权**：集成系统用户认证，支持密码、证书和多因素认证。
- **性能优化**：支持压缩、缓存和远程打印功能，优化网络传输。
- **扩展性**：可与 xorgxrdp 模块结合，提供原生 X11 支持；兼容 VNC 后端作为备选。

## 用法
### 安装
1. **依赖安装**（以 Ubuntu/Debian 为例）：
   ```
   sudo apt update
   sudo apt install build-essential autoconf libtool intltool pkg-config nasm xserver-xorg-dev libssl-dev libpam0g-dev libxrdp-dev
   ```
   对于其他发行版，使用相应包管理器安装依赖。

2. **从源代码编译安装**：
   ```
   git clone https://github.com/neutrinolabs/xrdp.git
   cd xrdp
   ./bootstrap
   ./configure --enable-pixman --enable-vchannels --enable-fuse
   make
   sudo make install
   ```

3. **安装 xorgxrdp（推荐，用于 X11 支持）**：
   ```
   git clone https://github.com/neutrinolabs/xorgxrdp.git
   cd xorgxrdp
   ./bootstrap
   ./configure
   make
   sudo make install
   ```

### 配置与启动
1. **编辑配置文件**：
   - 主配置文件：`/etc/xrdp/xrdp.ini`（端口默认 3389，可修改）。
   - 用户级：`~/.xrdp.ini`。
   示例配置端口和加密：
   ```
   [globals]
   port=3389
   security_layer=tls
   ```

2. **启动服务**：
   ```
   sudo systemctl enable xrdp
   sudo systemctl start xrdp
   ```
   或手动启动：`sudo /etc/init.d/xrdp start`。

3. **连接**：
   - 使用 Windows 的“远程桌面连接”工具，输入服务器 IP 和端口（默认 3389）。
   - Linux/macOS：使用 Remmina 或 FreeRDP 客户端，例如 `xfreerdp /v:server_ip:3389 /u:username /p:password`。
   - 首次连接需输入系统用户名和密码。

### 注意事项
- 确保防火墙允许 3389 端口：`sudo ufw allow 3389/tcp`。
- 对于 SELinux 系统，可能需调整策略。
- 调试日志：`/var/log/xrdp.log` 和 `/var/log/xrdp-sesman.log`。
- 更多详情参考项目 README 和官方文档。