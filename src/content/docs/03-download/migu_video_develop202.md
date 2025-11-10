---
title: migu
---


# Migu Video Downloader – develop202 版

**项目地址**: [https://github.com/develop202/migu_video](https://github.com/develop202/migu_video)

## 主要特性

- **批量下载**：支持一次性下载视频列表、单个剧集或大片资源。
- **多格式支持**：自动判断并下载最佳清晰的MP4或M3U8文件。
- **字幕提取**：可选下载对应的SRT字幕文件，方便后期编辑。
- **进度可视化**：命令行下实时显示下载进度与速度。
- **错误重试**：出现网络中断时自动重试，保证下载完整。
- **日志记录**：下载完成后生成详细日志，方便排查问题。

## 功能概览

1. **视频单文件下载**  
   通过视频 ID、URL 或标题直接下载单个视频。

2. **列表批量下载**  
   从提供的播放列表文件（TXT、JSON）中读取 ID，批量下载全部内容。

3. **指定清晰度**  
   可通过命令行参数选择 480p / 720p / 1080p / 4K 等清晰度。

4. **字幕同步**  
   自动识别并下载对应语言的字幕文件，支持多语言切换。

5. **断点续传**  
   对已下载部分采用断点续传功能，避免重复下载。

## 用法

```bash
# 安装依赖
pip install -r requirements.txt

# 直接下载单个视频
python migu_video.py --url "https://www.migu.cn/video/12345/" --quality 1080p

# 批量下载，输入文件包含视频 ID 或完整 URL
python migu_video.py --list path/to/list.txt --quality 720p --subtitle

# 指定输出目录
python migu_video.py --url "https://..." --output /path/to/save

# 仅下载字幕
python migu_video.py --url "https://..." --subtitle-only
```

> *请确保已安装 `ffmpeg`，以支持 M3U8 的合并转码。*

## 常见问题

- **下载失败**：请检查网络，或手动切换清晰度重试。
- **缺少字幕**：部分视频不提供字幕，日志会提示缺失。
- **日志文件**：下载完成后会在 `logs/` 目录生成 `download.log`。

> 如需贡献或反馈，请提交 Pull Request 或 Issue。

---
**键点总结**
- 轻松批量下载 Migu 视频  
- 多清晰度 & 自动字幕  
- 断点续传 & 进度显示  
- 简单易用的命令行接口
