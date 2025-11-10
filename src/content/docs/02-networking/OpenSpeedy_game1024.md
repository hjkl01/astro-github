---
title: OpenSpeedy
---

# OpenSpeedy 项目

**项目地址:** [https://github.com/game1024/OpenSpeedy](https://github.com/game1024/OpenSpeedy)

## 主要特性
OpenSpeedy 是一个开源的网络加速工具，基于现代网络协议优化设计，主要特性包括：
- **高性能代理支持**：集成多种代理协议，如 V2Ray、Trojan 和 Shadowsocks，提供高效的流量转发和加密传输。
- **跨平台兼容**：支持 Windows、macOS、Linux 和 Android 等多种操作系统，便于在不同设备上部署。
- **轻量级设计**：核心模块体积小，资源占用低，适合低配置设备运行。
- **自定义配置**：支持 JSON 配置文件，允许用户灵活调整节点、路由规则和加密方式。
- **安全性增强**：内置 TLS 加密和伪装功能，防范 DPI（深度包检测），提升隐私保护。

## 主要功能
- **流量加速与代理**：实现科学上网，绕过网络限制，加速访问海外资源。
- **节点管理**：自动订阅节点列表，支持一键导入和切换多个服务器节点。
- **路由规则**：基于域名、IP 或端口的智能分流，支持全局代理或分应用代理。
- **监控与日志**：实时显示连接状态、流量统计和错误日志，便于调试和优化。
- **API 接口**：提供 RESTful API，用于外部集成或自动化管理。

## 用法
1. **安装**：
   - 从 GitHub Releases 下载对应平台的二进制文件。
   - 对于 Linux/macOS，使用 `git clone https://github.com/game1024/OpenSpeedy.git` 克隆仓库，然后运行 `make` 或 `./install.sh` 安装。

2. **配置**：
   - 编辑 `config.json` 文件，添加服务器节点信息，例如：
     ```
     {
       "inbounds": [{"port": 1080, "protocol": "socks"}],
       "outbounds": [{"protocol": "vless", "address": "your-server.com", "port": 443}]
     }
     ```
   - 支持订阅 URL 导入节点：运行 `./OpenSpeedy -subscribe url`。

3. **运行**：
   - 命令行启动：`./OpenSpeedy -config config.json`。
   - 设置系统代理：将 SOCKS/HTTP 代理指向本地端口（如 1080）。
   - GUI 版本：在界面中导入配置并点击“启动”。

4. **停止与更新**：
   - 停止：`Ctrl+C` 或关闭应用。
   - 更新：拉取最新代码 `git pull`，重新编译或下载新版本。

更多细节请参考项目 README.md 文件。