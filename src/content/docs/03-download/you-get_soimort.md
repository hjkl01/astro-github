---
title: you-get
---

# you-get 项目

**GitHub项目地址:** [https://github.com/soimort/you-get](https://github.com/soimort/you-get)

## 主要特性
you-get 是一个轻量级的命令行视频下载工具，支持从多个视频网站提取和下载视频。它基于 Python 开发，具有跨平台兼容性（Windows、macOS、Linux），无需复杂的依赖安装。主要特性包括：
- **多平台支持**：兼容 YouTube、Bilibili、Vimeo、TED、Instagram 等数百个国内外视频网站。
- **高质量下载**：自动检测并下载最高质量的视频和音频，支持格式转换（如 MP4、FLV）。
- **简单高效**：命令行界面，体积小巧，无需图形界面，适合脚本自动化。
- **插件式扩展**：易于添加新网站支持，通过 YAML 配置自定义提取规则。
- **安全可靠**：开源项目，MIT 许可，社区维护活跃，避免了浏览器插件的隐私风险。

## 主要功能
- **视频提取与下载**：从指定 URL 下载视频，支持单视频、播放列表或频道批量下载。
- **格式选择**：用户可指定视频分辨率、格式（如高清、标清）或仅下载音频。
- **字幕支持**：自动下载嵌入式字幕或独立字幕文件。
- **代理与 cookie 支持**：可配置代理服务器绕过地域限制，并使用 cookie 访问登录内容。
- **输出自定义**：支持自定义输出文件名、目录，并集成 FFmpeg 进行视频合并和转换。
- **错误处理**：内置重试机制和详细日志输出，便于调试。

## 用法
1. **安装**：
   - 使用 pip 安装：`pip install you-get`（推荐 Python 3.6+）。
   - 或从源代码克隆：`git clone https://github.com/soimort/you-get.git`，然后 `cd you-get` 并运行 `python setup.py install`。

2. **基本用法**：
   - 下载单个视频：`you-get https://www.youtube.com/watch?v=VIDEO_ID`
   - 下载播放列表：`you-get https://www.bilibili.com/video/BV1xx411c7mu/`
   - 指定格式：`you-get -f bestvideo+bestaudio https://example.com/video`
   - 输出到指定目录：`you-get -o /path/to/output https://url`
   - 仅下载音频：`you-get --format=m4a https://url`
   - 查看可用格式：`you-get --info https://url`

3. **高级选项**：
   - 使用代理：`you-get --http-proxy http://proxy:port https://url`
   - 帮助命令：`you-get --help` 查看完整选项。
   - 集成 FFmpeg：确保系统安装 FFmpeg 以支持高级格式转换。

更多详情请参考项目 README 和 Wiki。