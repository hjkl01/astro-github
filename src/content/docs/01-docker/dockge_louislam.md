---
title: dockge
---

# Dockge 项目

**GitHub 项目地址:** [https://github.com/louislam/dockge](https://github.com/louislam/dockge)

## 主要特性
Dockge 是一个轻量级的 Docker 容器管理工具，专为简化 Docker Compose 项目的管理和监控而设计。其核心特性包括：
- **可视化界面**：通过 Web 界面轻松管理 Docker Compose 文件，无需命令行操作。
- **实时监控**：实时显示容器状态、日志和资源使用情况，支持一键启动、停止、重启和更新容器。
- **栈（Stack）管理**：支持多个 Docker Compose 项目（称为栈）的组织和切换，便于管理复杂环境。
- **文件同步**：自动同步 Docker Compose 文件的变化，并支持 Git 集成以实现版本控制。
- **轻量高效**：基于 Node.js 构建，资源占用低，易于部署在 Raspberry Pi 等低功耗设备上。
- **安全性**：内置基本认证，支持 HTTPS，并限制对 Docker API 的访问权限。
- **跨平台支持**：兼容 Linux、Windows 和 macOS 等平台。

## 主要功能
- **容器生命周期管理**：创建、启动、停止、删除和更新 Docker 容器。
- **日志查看**：实时查看容器日志，支持搜索和过滤。
- **资源监控**：监控 CPU、内存和网络使用，支持警报通知。
- **Compose 文件编辑**：内置编辑器修改 Docker Compose 文件，并自动应用变更。
- **备份与恢复**：支持栈的导出和导入，便于迁移或备份。
- **插件扩展**：可通过自定义脚本扩展功能，如集成外部工具。

## 用法
1. **安装**：
   - 确保系统已安装 Docker 和 Docker Compose。
   - 使用 Docker 运行 Dockge：  
     ```
     docker run -d \
       --name dockge \
       --restart always \
       -p 5001:5001 \
       -v /var/run/docker.sock:/var/run/docker.sock \
       -v /opt/stacks:/opt/stacks \
       -v /opt/dockge:/app/config \
       louislam/dockge:1
     ```
     （`/opt/stacks` 为存放 Compose 文件的目录，可自定义。）

2. **访问界面**：
   - 在浏览器中打开 `http://你的服务器IP:5001`，设置管理员账户。

3. **添加栈**：
   - 点击“添加栈”，选择本地目录或 Git 仓库，上传或拉取 Docker Compose 文件。
   - Dockge 会自动解析并显示容器列表。

4. **管理容器**：
   - 在栈页面，选择容器进行启动/停止/重启。
   - 查看日志或编辑 Compose 文件后，点击“更新”应用变更。

5. **高级用法**：
   - 配置 HTTPS：使用反向代理如 Nginx 或 Traefik。
   - 集成 Git：为栈启用 Git 拉取，实现自动更新。
   - 更多细节参考项目 README。

Dockge 适合个人开发者或小型团队管理 Docker 环境，安装简单，使用直观。