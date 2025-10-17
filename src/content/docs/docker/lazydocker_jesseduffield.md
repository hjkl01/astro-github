
---
title: lazydocker
---

# LazyDocker

**GitHub 项目地址:** [https://github.com/jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker)

## 主要特性

LazyDocker 是一个终端用户界面 (TUI) 工具，专为简化 Docker 和 Docker Compose 的管理而设计。它提供了一个直观的界面，让用户无需复杂命令即可监控和操作容器、镜像、卷、网络等 Docker 资源。主要特性包括：

- **实时监控**: 显示容器、镜像、卷和网络的实时状态，包括 CPU、内存和网络使用情况。
- **交互式界面**: 使用键盘快捷键导航，支持多面板视图（如容器列表、日志、统计等），无需鼠标。
- **Docker Compose 支持**: 轻松管理 Compose 项目，包括启动、停止和重建服务。
- **日志查看**: 实时查看容器日志，支持过滤和搜索。
- **资源管理**: 直接从界面中启动、停止、重启容器，查看和编辑 Compose 文件。
- **跨平台兼容**: 支持 Linux、macOS 和 Windows，支持通过 Homebrew、Scoop 等安装。
- **自定义配置**: 可配置主题、快捷键和行为，以适应用户偏好。
- **无依赖**: 纯 Go 语言编写，轻量级且易于安装。

## 主要功能

- **容器管理**: 列出所有容器，查看详情、日志、执行命令（如进入 shell）、调整资源限制。
- **镜像管理**: 浏览本地镜像，拉取新镜像，删除无用镜像。
- **卷和网络管理**: 查看和删除 Docker 卷、网络。
- **Compose 项目**: 加载 Docker Compose 文件，管理多容器应用栈，支持一键部署。
- **统计和指标**: 内置图表显示资源使用情况，帮助诊断性能问题。
- **事件监控**: 实时捕获 Docker 事件，如容器启动或停止。

## 用法

### 安装

1. **通过 Homebrew (macOS/Linux)**:
   ```
   brew install lazydocker
   ```

2. **通过 Scoop (Windows)**:
   ```
   scoop bucket add lazydocker https://github.com/jesseduffield/scoop-bucket
   scoop install lazydocker
   ```

3. **二进制下载**: 从 GitHub Releases 页面下载对应平台的二进制文件，并添加到 PATH。

4. **从源代码构建** (需要 Go 1.16+):
   ```
   git clone https://github.com/jesseduffield/lazydocker.git
   cd lazydocker
   make build
   ```

### 基本用法

1. **启动 LazyDocker**:
   ```
   lazydocker
   ```
   这将打开 TUI 界面，默认显示容器列表。

2. **导航界面**:
   - 使用 `Tab` 或 `Shift+Tab` 切换面板（容器、镜像、日志等）。
   - 使用箭头键上下移动，`Enter` 进入子视图。
   - 按 `?` 查看所有快捷键帮助。

3. **常用操作**:
   - **启动/停止容器**: 选择容器，按 `s` 启动，`d` 停止，`r` 重启。
   - **查看日志**: 选择容器，按 `l` 查看实时日志。
   - **进入容器**: 选择容器，按 `e` 执行命令（如 bash）。
   - **管理 Compose**: 在项目目录运行 `lazydocker`，它会自动检测 `docker-compose.yml` 文件。按 `Ctrl+R` 重建服务。
   - **退出**: 按 `q` 或 `Ctrl+C` 退出。

4. **配置**:
   - 创建 `~/.config/lazydocker/config.yml` 文件自定义设置，例如更改主题或默认视图。
   - 示例配置:
     ```yaml
     ui:
       theme: default
     ```

更多细节请参考项目文档或运行 `lazydocker --help`。LazyDocker 适合 Docker 初学者和高级用户，提升命令行工作效率。