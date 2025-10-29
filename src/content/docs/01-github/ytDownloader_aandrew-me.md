
---
title: ytDownloader
---

# ytDownloader（aandrew‑me）  
GitHub 项目地址: <https://github.com/aandrew-me/ytDownloader>  

## 项目简介  
`ytDownloader` 是一个轻量级的命令行工具，用于从 **YouTube** 下载视频或音频。它提供了多种选择，支持下载指定清晰度、格式以及将音频单独提取为 MP3。项目基于 Python，使用 `pytube` 进行 YouTube 解析、`ffmpeg` 进行格式转换，使用方便，依赖少。

## 主要特性  
- **下载视频或音频**：一次即可完成，支持多种格式（MP4、MP3 等）。  
- **自定义清晰度**：按分辨率或文件大小挑选最适合的流。  
- **指定输出目录**：自动创建文件夹，方便管理。  
- **批量下载**：支持从文本文件或命令行直接提供多个 URL。  
- **简易命令行接口**：直观易用，已实现常用参数。  
- **跨平台**：Linux / macOS / Windows 均可运行。  

## 安装方法  
```bash
# 方式 1：直接克隆仓库
git clone https://github.com/aandrew-me/ytDownloader.git
cd ytDownloader
pip install -r requirements.txt
python setup.py install

# 方式 2：使用 pip 直接安装（需先安装 ffmpeg）
pip install git+https://github.com/aandrew-me/ytDownloader.git
```

> **依赖**  
> - Python 3.8+  
> - `pytube`（已在 requirements.txt 自动安装）  
> - `ffmpeg`（需系统自行安装，并加入 PATH）  

## 用法

```bash
# 基本用法
ytDownloader -u <YouTube_URL>

# 指定清晰度（例：720p）
ytDownloader -u <YouTube_URL> -r 720

# 只下载音频并转为 MP3
ytDownloader -u <YouTube_URL> -a

# 指定输出目录
ytDownloader -u <YouTube_URL> -o ./downloads

# 批量下载（urls.txt 每行一个 URL）
ytDownloader -l urls.txt

# 查看帮助
ytDownloader -h
```

### 参数说明

| 参数 | 作用 |
|------|------|
| `-u, --url` | 要下载的 YouTube 视频链接（必填） |
| `-o, --output` | 输出目录（默认当前目录） |
| `-r, --resolution` | 目标清晰度（如 1080、720、480） |
| `-a, --audio` | 仅下载音频并转换为 MP3 |
| `-l, --list` | 指定包含多条 URL 的文本文件 |
| `-h, --help` | 显示帮助信息 |

## 示例

```bash
# 下载 1080p 视频到 ./videos
ytDownloader -u https://www.youtube.com/watch?v=dQw4w9WgXcQ -r 1080 -o ./videos

# 仅保存音频为 MP3
ytDownloader -u https://www.youtube.com/watch?v=dQw4w9WgXcQ -a

# 批量下载
cat urls.txt | ytDownloader -l -o ./batch
```

---

> **提示**  
> - 如遇到加密流或下载失败，尝试更新 `pytube` 版本：`pip install --upgrade pytube`。  
> - 对于较大视频，建议在 `-o` 选项后给出完整路径以避免权限或磁盘空间问题。  

---