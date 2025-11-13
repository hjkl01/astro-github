---
title: dashy
---

# Dashy 项目

**GitHub 项目地址:** [https://github.com/Lissy93/dashy](https://github.com/Lissy93/dashy)

## 主要特性

🚀 为您构建的自托管个人仪表盘。包括状态检查、小部件、主题、图标包、UI 编辑器等等！

## 功能

🚀 为您构建的自托管个人仪表盘。包括状态检查、小部件、主题、图标包、UI 编辑器等等！

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
