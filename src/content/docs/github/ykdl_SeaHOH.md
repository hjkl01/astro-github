
---
title: ykdl
---

# ykdl 项目

## 项目地址
[GitHub 项目地址](https://github.com/SeaHOH/ykdl)

## 主要特性
- **支持多种视频平台**：ykdl 是一个开源的视频下载工具，支持 YouTube、Bilibili、Youku、iQiyi、Tencent Video 等国内外主流视频网站，以及 Twitter、Instagram 等社交媒体平台的视频下载。
- **高效下载**：基于 Python 开发，支持多线程下载、格式选择（如 MP4、FLV）和分辨率自定义，提高下载速度和灵活性。
- **轻量级设计**：无需复杂安装，通过命令行操作，适合开发者、脚本自动化和批量下载任务。
- **开源免费**：采用 MIT 许可，社区维护，支持插件扩展，允许用户自定义添加新网站支持。
- **跨平台兼容**：在 Windows、macOS 和 Linux 上运行良好，无需额外依赖过多库。

## 主要功能
- **视频下载**：从指定 URL 下载单个视频或整个播放列表，支持字幕下载和元数据提取。
- **格式转换**：自动检测并下载最佳质量，支持 DASH 和 HLS 流媒体协议。
- **批量处理**：通过配置文件或脚本实现批量 URL 下载，适用于爬虫或自动化任务。
- **代理支持**：内置代理配置，绕过地域限制下载海外视频。
- **错误处理**：智能重试机制和日志记录，确保下载过程稳定。

## 用法
1. **安装**：
   - 确保 Python 3.6+ 已安装。
   - 使用 pip 安装：`pip install ykdl`。
   - 或者从 GitHub 克隆仓库：`git clone https://github.com/SeaHOH/ykdl.git`，然后 `cd ykdl` 并运行 `pip install -e .`。

2. **基本下载**：
   - 命令行使用：`ykdl <URL>`，例如 `ykdl https://www.bilibili.com/video/BV1xx411c7mu`。
   - 下载到指定目录：`ykdl -o /path/to/output <URL>`。

3. **高级选项**：
   - 指定格式：`ykdl -f bestvideo+bestaudio <URL>`（使用 ffmpeg 合并）。
   - 下载播放列表：`ykdl -P playlist <URL>`。
   - 启用代理：`ykdl --http-proxy http://proxy:port <URL>`。
   - 查看帮助：`ykdl --help` 以获取完整参数列表。

注意：下载前请遵守各平台的版权政策，并确保安装 ffmpeg 以支持高级功能。