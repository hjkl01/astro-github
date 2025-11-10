---
title: docker-headless-vnc-container
---

# ConSol/docker-headless-vnc-container 项目描述

## 项目地址
[https://github.com/ConSol/docker-headless-vnc-container](https://github.com/ConSol/docker-headless-vnc-container)

## 主要特性
- **无头VNC容器**：提供基于Docker的无图形界面（headless）VNC服务器，支持远程桌面访问。
- **多桌面环境支持**：内置多种Linux桌面环境，如XFCE、KDE、GNOME等，用户可根据需求选择。
- **VNC协议兼容**：使用TigerVNC或TightVNC，支持标准VNC客户端连接，实现远程图形界面访问。
- **轻量级设计**：容器化部署，资源占用低，适合开发、测试和CI/CD环境。
- **安全性增强**：支持VNC密码认证、SSL/TLS加密（可选），并可配置防火墙规则。
- **跨平台兼容**：基于Debian/Ubuntu等基础镜像，支持x86_64和ARM架构。

## 主要功能
- **远程桌面访问**：允许用户通过VNC客户端（如VNC Viewer）从本地访问容器内的图形桌面，用于GUI应用运行。
- **应用部署**：适合运行需要图形界面的应用，如浏览器、IDE、图形编辑器等，在无头服务器上模拟桌面环境。
- **自定义配置**：支持环境变量自定义分辨率、深度、桌面环境和VNC端口，便于个性化设置。
- **无显示器模式**：在无物理显示器的服务器上运行，支持虚拟显示器（Xvfb）以实现headless操作。
- **集成工具**：内置novnc（Web-based VNC）支持浏览器直接访问，无需专用客户端。

## 用法
1. **拉取镜像**：
   ```
   docker pull consol/headless-vnc-ubuntu:20.04-xfce
   ```
   （替换为所需变体，如`kde`、`gnome`等）

2. **运行容器**：
   ```
   docker run -d \
     -p 5901:5901 \
     -p 6901:6901 \
     -e VNC_PW=password \
     --name my-vnc-container \
     consol/headless-vnc-ubuntu:20.04-xfce
   ```
   - `-p 5901:5901`：暴露VNC端口（默认5901）。
   - `-p 6901:6901`：暴露noVNC Web端口（浏览器访问http://localhost:6901）。
   - `-e VNC_PW=password`：设置VNC密码。

3. **连接访问**：
   - 使用VNC客户端连接`localhost:5901`，密码为设置的值。
   - 或通过浏览器访问`http://localhost:6901/vnc.html`进行noVNC连接。

4. **自定义选项**：
   - 设置分辨率：`-e VNC_RESOLUTION=1920x1080`。
   - 更改端口：`-p 自定义端口:5901`。
   - 持久化数据：添加`-v /host/path:/container/path`挂载卷。

更多细节请参考项目README。