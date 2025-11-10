---
title: yt-dlp
---

# yt-dlp 项目

## 项目地址
[GitHub 项目地址](https://github.com/yt-dlp/yt-dlp)

## 主要特性
yt-dlp 是一个功能强大的命令行工具，用于从 YouTube 和数千个其他视频/音频网站下载媒体内容。它是 youtube-dl 的一个活跃分支，提供了更新的支持、更好的兼容性和增强的功能。主要特性包括：
- **广泛的网站支持**：支持 YouTube、Vimeo、Bilibili、Twitter、TikTok 等 1000+ 个网站。
- **格式选择**：支持下载视频、音频、字幕，并选择最佳质量或特定格式（如 MP4、MP3）。
- **高级选项**：包括下载播放列表、频道、字幕翻译、元数据嵌入、速度限制等。
- **跨平台兼容**：适用于 Windows、macOS、Linux，支持 Python 3.7+。
- **插件和扩展**：可通过外部插件扩展功能，并有内置的更新机制。
- **隐私与安全性**：不收集用户数据，支持代理和 cookie 导入以绕过限制。

## 主要功能
- **下载媒体**：从单个视频到整个播放列表或频道批量下载。
- **格式转换**：自动合并视频和音频流，或转换为指定格式。
- **字幕处理**：下载嵌入式或外部字幕，支持自动翻译（通过 Google Translate 等）。
- **元数据提取**：获取视频标题、描述、缩略图等信息，并嵌入到文件中。
- **速度与限制控制**：设置下载速度上限、并发下载、跳过已下载文件。
- **错误处理**：自动重试失败下载，支持调试模式诊断问题。
- **自定义配置**：通过配置文件（yt-dlp.conf）或命令行参数自定义行为。

## 用法
yt-dlp 通过命令行使用。首先，确保安装 Python 和 yt-dlp（推荐使用 pip：`pip install -U yt-dlp`）。

### 基本用法
- 下载单个视频：  
  `yt-dlp https://www.youtube.com/watch?v=VIDEO_ID`

- 下载最佳质量视频：  
  `yt-dlp -f best https://example.com/video`

- 下载音频（MP3 格式）：  
  `yt-dlp -x --audio-format mp3 https://example.com/video`

- 下载播放列表：  
  `yt-dlp https://www.youtube.com/playlist?list=PLAYLIST_ID`

### 高级用法
- 下载字幕：  
  `yt-dlp --write-subs --sub-lang en,zh https://example.com/video`

- 限制下载速度：  
  `yt-dlp -r 500K https://example.com/video`（500 KB/s）

- 使用配置文件：  
  创建 `yt-dlp.conf` 文件，添加选项如 `--embed-thumbnail`，然后运行 `yt-dlp URL`。

- 更新工具：  
  `yt-dlp -U`

更多详细用法请参考官方文档：https://github.com/yt-dlp/yt-dlp/wiki。