
---
title: dozzle
---

# Dozzle 项目

## 项目地址
[GitHub 项目地址](https://github.com/amir20/dozzle)

## 主要特性
Dozzle 是一个轻量级的 Docker 日志查看器，基于 Web 界面设计，类似于 Docker 的实时日志输出工具。它具有以下主要特性：
- **实时日志流式传输**：支持实时查看容器日志，支持过滤和搜索功能。
- **简单易用**：无需复杂配置，即开即用，支持多用户访问和权限控制。
- **轻量级部署**：体积小巧，资源占用低，可作为 Docker 容器运行。
- **浏览器访问**：通过 Web 界面访问日志，无需 SSH 或命令行。
- **支持 Docker Compose**：无缝集成 Docker 环境，提供日志聚合视图。
- **开源免费**：基于 MIT 许可，社区活跃，支持自定义扩展。

## 主要功能
- **日志查看**：显示 Docker 容器的 stdout 和 stderr 输出，支持时间戳和颜色高亮。
- **容器管理**：列出所有运行中的容器，支持启动、停止和重启操作（需权限）。
- **搜索与过滤**：根据关键词、容器名称或标签过滤日志，支持导出日志文件。
- **多容器支持**：同时监控多个容器，提供全局日志视图。
- **安全特性**：支持基本认证和 HTTPS 配置，保护日志访问。
- **移动端友好**：响应式设计，适用于桌面和移动设备。

## 用法
### 安装与运行
1. **使用 Docker 运行**（推荐）：
   ```
   docker run -p 8080:8080 amir20/dozzle:latest
   ```
   访问 `http://localhost:8080` 查看日志。

2. **Docker Compose 示例**：
   在 `docker-compose.yml` 中添加：
   ```
   services:
     dozzle:
       image: amir20/dozzle:latest
       ports:
         - "8080:8080"
       volumes:
         - /var/run/docker.sock:/var/run/docker.sock
       restart: unless-stopped
   ```
   运行 `docker-compose up -d` 启动。

3. **配置选项**：
   - 通过环境变量自定义：如 `DOZZLE_KEY=your-secret` 设置认证密钥。
   - 挂载 Docker 套接字：确保 Dozzle 可以访问宿主机的 Docker API。
   - 支持 YAML 配置高级选项，如用户名/密码认证。

### 使用步骤
1. 启动 Dozzle 容器。
2. 在浏览器打开 Web 界面。
3. 选择要查看的容器，即可实时显示日志。
4. 使用搜索框过滤日志，或切换到不同容器。

更多详情请参考 [GitHub 项目文档](https://github.com/amir20/dozzle)。