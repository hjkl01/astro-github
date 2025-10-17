
---
title: navidrome
---

# Navidrome 项目

**项目地址:** [https://github.com/navidrome/navidrome](https://github.com/navidrome/navidrome)

## 主要特性
Navidrome 是一个现代化的开源音乐服务器和流媒体应用，旨在为个人音乐库提供类似 Spotify 的流畅体验。它支持多种音频格式，并强调易用性和隐私保护。主要特性包括：
- **多用户支持**：允许多个用户创建个人账户，管理自己的播放列表和收藏。
- **Subsonic API 兼容**：无缝集成 Subsonic 客户端、Android/iOS 应用（如 DSub、Substreamer）和硬件设备（如 Roku、Sonos）。
- **多库管理**：支持管理多个音乐库，每个库可有独立的扫描设置和元数据处理。
- **高级扫描功能**：自动扫描音乐文件，支持嵌入式封面艺术、歌词和元数据标签（ID3v2 等）。
- **播放列表和推荐**：内置播放列表创建、共享功能，以及基于 Last.fm 的推荐集成。
- **跨平台支持**：运行于 Linux、macOS、Windows 和 Docker，支持 ARM 和 x86 架构。
- **隐私与自托管**：完全自托管，无需云服务，确保数据隐私。

## 主要功能
- **音乐流媒体**：通过 Web 界面或兼容客户端流式传输音乐，支持高品质音频（如 FLAC、MP3、AAC）。
- **Web 界面**：响应式设计，支持桌面和移动端，提供搜索、浏览艺术家/专辑/歌曲的功能。
- **元数据管理**：自动整理音乐库，支持自定义标签和封面艺术下载。
- **扩展性**：集成 Last.fm 进行 scrobbling（播放记录），支持插件和 API 扩展。
- **性能优化**：高效的数据库后端（SQLite 或 PostgreSQL），适合小型到中型音乐库（数千到数十万首歌曲）。

## 用法
1. **安装**：
   - 使用 Docker（推荐）：运行 `docker run -d --name=navidrome -p 4533:4533 -v /path/to/music:/music:ro -v /path/to/navidrome/data:/data deluan/navidrome:latest`。
   - 二进制安装：从 GitHub Releases 下载可执行文件，配置 `navidrome.toml` 文件，然后运行 `./navidrome`。
   - 详细安装指南见 [官方文档](https://www.navidrome.org/docs/installation/)。

2. **配置**：
   - 编辑配置文件 `navidrome.toml`，设置音乐库路径（`MusicFolder`）、数据库（`DBPath`）和端口（`Address`）。
   - 示例配置：
     ```
     MusicFolder = "/path/to/your/music"
     DataFolder = "/path/to/navidrome/data"
     Address = ":4533"
     ```

3. **启动和使用**：
   - 启动服务器后，访问 `http://your-server:4533` 创建管理员账户。
   - 上传或指向音乐文件夹，Navidrome 会自动扫描并索引文件。
   - 通过 Web 界面浏览和播放音乐，或使用 Subsonic 客户端连接（服务器 URL 为 `http://your-server:4533`）。
   - 管理用户：管理员可在 Web 界面添加用户，支持密码保护和权限设置。

更多细节请参考官方文档：https://www.navidrome.org/docs/