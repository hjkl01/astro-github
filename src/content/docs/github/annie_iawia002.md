
---
title: annie
---

# Annie 项目

## 项目地址
[https://github.com/iawia002/annie](https://github.com/iawia002/annie)

## 主要特性
Annie 是一个开源的下载器，支持从多个视频网站下载资源，具有以下主要特性：
- **多平台支持**：兼容 Windows、macOS 和 Linux 系统。
- **高效下载**：支持多线程下载，提高速度和稳定性。
- **格式灵活**：可选择下载视频、音频或字幕，支持多种分辨率和格式。
- **轻量级**：体积小巧，无需复杂安装，纯命令行工具。
- **开源免费**：基于 Go 语言开发，MIT 许可，社区活跃。

## 主要功能
- **视频下载**：支持 Bilibili、YouTube、Twitter、Instagram、Vimeo 等数百个国内外网站。
- **批量处理**：可下载播放列表、频道或指定范围的视频。
- **信息提取**：获取视频元数据，如标题、时长、封面等。
- **代理支持**：内置代理配置，适用于网络受限环境。
- **自定义输出**：指定输出路径、文件名格式，并支持合并视频和音频流。

## 用法
Annie 通过命令行操作，使用简单。以下是基本用法示例（需先下载并安装 Annie 二进制文件）：

### 安装
- 从 GitHub Releases 下载对应平台的二进制文件。
- Linux/macOS：`chmod +x annie` 后添加至 PATH。
- Windows：直接运行 .exe 文件。

### 基本下载
```bash
# 下载单个视频
annie "https://www.bilibili.com/video/BV1xx411c7mu"

# 下载并指定分辨率（例如 1080p）
annie -r 1080 "https://www.youtube.com/watch?v=VIDEO_ID"

# 下载音频（MP3 格式）
annie -f mp3 "https://www.youtube.com/watch?v=VIDEO_ID"

# 批量下载播放列表
annie "https://www.bilibili.com/video/BV1xx411c7mu?list=PLAYLIST_ID"
```

### 高级选项
- **输出目录**：`annie -o /path/to/output URL`
- **文件名格式**：`annie -s "%title_%id" URL`（自定义标题和 ID）
- **代理设置**：`annie -p http://proxy:port URL`
- **帮助**：`annie -h` 查看完整参数。

更多详情请参考项目 README。