---
title: dashy
---

# Dashy 项目

**GitHub 项目地址:** [https://github.com/Lissy93/dashy](https://github.com/Lissy93/dashy)

## 主要特性
Dashy 是一个现代化的、完全可开源的仪表盘工具，用于快速访问和管理您的自托管服务、书签和应用程序。它采用 YAML 配置驱动的设计，支持高度自定义化，界面简洁美观。主要特性包括：
- **响应式设计**：适配桌面、平板和移动设备，支持暗黑模式和多种主题。
- **高度可配置**：通过 YAML 文件定义仪表盘布局、图标和服务链接，支持动态更新。
- **自托管友好**：轻量级部署，支持 Docker、Node.js 等多种方式，无需复杂依赖。
- **集成扩展**：内置搜索功能、状态监控（如 Uptime Kuma 集成）、多语言支持（包括中文）。
- **安全与隐私**：本地运行，不依赖第三方服务，支持认证和 HTTPS。
- **社区驱动**：活跃的开源社区，提供大量预设配置和插件。

## 功能
Dashy 的核心功能围绕仪表盘管理展开：
- **服务聚合**：将各种工具（如 Docker、Plex、Home Assistant 等）集中到一个页面，便于导航。
- **书签管理**：支持分组、标签和图标自定义，类似于个人化的启动页。
- **实时监控**：集成服务健康检查、CPU/内存使用率显示。
- **API 支持**：提供 REST API 用于自动化配置和数据导入。
- **多用户支持**：可配置多个仪表盘视图，适合团队或家庭使用。
- **扩展性**：支持自定义 CSS、JavaScript 和插件，允许添加天气、新闻等小部件。

## 用法
### 1. 安装
- **Docker 方式**（推荐）：
  ```
  docker run -d \
    --name dashy \
    -p 8080:80 \
    -v /path/to/your/conf.yml:/app/public/conf.yml \
    lissy93/dashy:latest
  ```
  访问 `http://localhost:8080`。

- **Node.js 方式**：
  ```
  git clone https://github.com/Lissy93/dashy.git
  cd dashy
  npm install
  npm run build  # 构建
  npm run start  # 启动开发服务器
  ```

### 2. 配置
- 编辑 `conf.yml` 文件（示例在仓库中）：
  ```yaml
  pageInfo:
    title: 我的仪表盘
  sections:
    - name: 服务
      items:
        - title: 示例服务
          url: https://example.com
          icon: favicon
  ```
- 重启应用后，配置自动加载。支持从 GitHub 或本地文件同步配置。

### 3. 高级用法
- **自定义主题**：在 `conf.yml` 中添加 `appConfig: theme: dark`。
- **部署到云**：使用 Vercel 或 Netlify 免费部署静态版本。
- **监控集成**：在配置中添加 `statusPage` 字段链接到外部监控工具。
- 更多细节请参考仓库的 [文档](https://dashy.to/docs)。

Dashy 适合自托管爱好者和开发者，用于简化日常工具访问。