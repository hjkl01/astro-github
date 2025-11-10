---
title: jellyfin-web
---


# Jellyfin Web

项目地址: https://github.com/jellyfin/jellyfin-web

## 主要特性
- **响应式界面**：支持桌面、平板与手机，适配不同分辨率。
- **多语言支持**：内置多语言资源，支持手动或自动切换语言。
- **主题定制**：提供多套主题，支持自定义配色与样式。
- **插件扩展**：可通过插件机制（如 Browse Plugin）扩展功能。
- **离线缓存**：支持离线缓存，提升播放体验。

## 功能
| 功能 | 说明 |
|------|------|
| **媒体浏览** | 按库、类型、收藏、最近播放等分类浏览 |
| **播放控制** | 支持本地文件、流媒体，享受全屏/窗口/电视模式 |
| **字幕与音轨** | 自动匹配字幕，支持自定义音轨 |
| **搜索与筛选** | 全站搜索、按收藏/评分过滤 |
| **用户管理** | 账号切换、权限管理 |
| **导出/分享** | 导出播放列表，分享给好友 |
| **高级设置** | 远程控制、磁贴插件、媒体服务器设置 |

## 用法
1. **克隆仓库**  
   ```bash
   git clone https://github.com/jellyfin/jellyfin-web.git
   ```
2. **安装依赖**  
   ```bash
   cd jellyfin-web
   npm install
   ```
3. **开发启动**  
   ```bash
   npm run dev
   ```
4. **生产构建**  
   ```bash
   npm run build
   ```
5. **部署**  
   将 `dist` 目录下的文件复制到支持静态文件托管的服务器（如 Nginx、Caddy 等）或直接在 Jellyfin 服务器的 `/jellyfin-web` 路径下提供。

## 参考文档
- 官方 Wiki: https://jellyfin.org/docs/
- 开发者指南: https://github.com/jellyfin/jellyfin-web/blob/master/CONTRIBUTING.md

---
