
---
title: nginx-ui
---

# nginx-ui 项目

## 项目地址
[https://github.com/schenkd/nginx-ui](https://github.com/schenkd/nginx-ui)

## 主要特性
nginx-ui 是一个基于 Web 的 Nginx 配置界面工具，主要特性包括：
- **图形化配置管理**：提供直观的 Web 界面来编辑和可视化 Nginx 配置，而无需直接修改配置文件。
- **实时预览和验证**：支持配置变更的实时预览和语法验证，帮助用户避免配置错误。
- **模块支持**：集成 Nginx 的常见模块，如反向代理、负载均衡、SSL/TLS 配置等。
- **简单部署**：易于安装和运行，支持 Docker 等容器化部署。
- **开源免费**：基于开源许可，用户可以自由修改和扩展。

## 主要功能
- **配置编辑**：通过拖拽或表单方式编辑 Nginx 的 server、location、upstream 等块。
- **监控与日志**：集成 Nginx 日志查看和基本性能监控功能。
- **备份与恢复**：自动备份配置变更，支持一键恢复。
- **模板支持**：提供预设模板，用于快速搭建常见场景如静态文件服务或 API 代理。
- **多站点管理**：同时管理多个 Nginx 站点配置。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/schenkd/nginx-ui.git`
   - 进入目录：`cd nginx-ui`
   - 安装依赖（如果需要）：根据 README，使用 npm 或 yarn 安装前端依赖。
   - 运行：使用 `npm start` 或 Docker 命令启动服务，例如 `docker run -p 8080:8080 schenkd/nginx-ui`。

2. **访问界面**：
   - 在浏览器打开 `http://localhost:8080`（默认端口）。
   - 连接到 Nginx 配置目录，通常需指定 Nginx 的 conf.d 路径。

3. **基本操作**：
   - 登录后，选择站点添加或编辑配置。
   - 使用左侧菜单导航到不同模块（如 Servers > Locations）。
   - 保存变更后，工具会自动重载 Nginx（需配置权限）。
   - 查看日志或测试配置以验证生效。

详细用法请参考项目 README 文件。