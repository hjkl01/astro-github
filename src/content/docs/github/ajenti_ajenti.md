
---
title: ajenti
---

# Ajenti 项目

## 项目地址
[https://github.com/ajenti/ajenti](https://github.com/ajenti/ajenti)

## 主要特性
Ajenti 是一个开源的 Web-based 服务器管理面板，专为 Linux 系统设计。它提供现代化的用户界面，支持插件扩展，允许用户通过浏览器轻松管理服务器资源。核心特性包括：
- **模块化架构**：高度可扩展，支持数百个插件，用于管理不同服务和资源。
- **实时监控**：内置仪表盘显示 CPU、内存、磁盘使用率、网络流量等实时数据。
- **安全设计**：支持用户认证、SSL 加密和权限控制，确保服务器管理的安全性。
- **跨平台兼容**：主要针对 Debian、Ubuntu 等 Debian-based 系统，但可扩展到其他 Linux 发行版。
- **轻量级**：资源占用低，安装简单，不依赖复杂框架。

## 主要功能
Ajenti 提供全面的服务器管理功能，包括但不限于：
- **系统管理**：监控和控制文件系统、进程、用户账户和服务（如 Apache、Nginx、MySQL）。
- **插件生态**：内置插件支持 Web 服务器配置、数据库管理、防火墙规则、日志查看等。用户可安装社区插件扩展功能，如 Docker 管理或备份工具。
- **仪表盘自定义**：用户可自定义仪表盘布局，添加小部件显示特定指标。
- **远程访问**：通过 Web 界面实现 SSH-like 操作，支持文件编辑、终端访问和命令执行。
- **自动化任务**：集成 cron 作业管理和脚本执行，支持自动化维护。

## 用法
### 安装
1. **系统要求**：Python 2.7 或 3.x，适用于 Debian/Ubuntu 等系统。确保 root 权限。
2. **安装命令**（以 Ubuntu 为例）：
   ```
   wget -O - https://raw.github.com/Eugeny/ajenti/master/install.sh | sh
   ```
   这将自动下载并安装 Ajenti 及其依赖。
3. **启动服务**：安装后，Ajenti 默认监听 8000 端口。运行 `service ajenti restart` 启动服务。

### 使用步骤
1. **访问界面**：在浏览器中打开 `https://your-server-ip:8000`，使用默认凭据登录（用户名：admin，密码：admin）。立即更改密码以提高安全性。
2. **配置插件**：在左侧菜单选择“Plugins”，搜索并安装所需插件（如“File Manager”用于文件浏览）。
3. **管理服务器**：
   - 使用“Dashboard”查看概览。
   - 通过“Connections”管理 SSH 连接。
   - 在“Services”下启动/停止服务，如配置 Nginx 站点。
4. **扩展与自定义**：编辑 `/etc/ajenti/config.json` 文件自定义设置，或开发自定义插件（基于 Python）。
5. **卸载**：运行 `apt-get remove ajenti` 或使用安装脚本的反向操作。

Ajenti 适合系统管理员和开发者，用于简化服务器运维。更多细节请参考 GitHub 仓库的文档。