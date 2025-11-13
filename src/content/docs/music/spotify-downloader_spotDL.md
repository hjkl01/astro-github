---
title: spotify-downloader
---


# SpotDL – Spotify Downloader

项目地址: https://github.com/spotDL/spotify-downloader

## 主要特性
- **从 Spotify 下载单曲、专辑、播放列表**  
  直接使用 Spotify 链接或搜索词进行下载
- **自动回退到 YouTube**  
  当 Spotify 无法找到对应音频时，自动在 YouTube 上搜索并下载
- **多种音频格式支持**  
  支持 `mp3`, `aac`, `flac`, `m4a`, `wav` 等格式，并可自定义比特率
- **高质量下载**  
  支持 `high`、`medium`、`low` 质量选项，默认下载最高可用质量
- **完整元数据填充**  
  自动写入 `artist`, `album`, `title`, `track number`, `date`, `cover art` 等标签
- **可自定义输出路径与文件名**  
  使用模板指定文件夹结构和文件命名规则
- **多线程下载**  
  支持并发下载，显著提升批量下载速度
- **轻量级 CLI**  
  通过命令行完成所有操作，使用 Python 脚本，跨平台兼容

## 安装方法
```bash
pip install spotdl
```

> 需要 `ffmpeg`（或 `avconv`）和 `youtube_dl`（或 `yt_dlp`）已安装在系统路径。

## 基本用法

### 1. 下载单首歌曲
```bash
spotdl "https://open.spotify.com/track/xxxxxxxxxxxx"
```

### 2. 搜索并下载歌曲
```bash
spotdl "干杯 by 周杰伦"
```

### 3. 下载专辑、播放列表
```bash
spotdl "https://open.spotify.com/album/xxxxxxxxxxxx"
spotdl "https://open.spotify.com/playlist/xxxxxxxxxxxx"
```

### 4. 指定输出文件夹与文件名模板
```bash
spotdl "https://open.spotify.com/track/xxxxxxxxxxxx" -o "./Music/%artist%/%album%/%tracknumber% - %title%.mp3"
```

### 5. 仅仅下载音频（不包含封面）
```bash
spotdl "https://open.spotify.com/track/xxxxxxxxxxxx" --reset --quiet
```

### 6. 使用高质量下载
```bash
spotdl "https://open.spotify.com/track/xxxxxxxxxxxx" --quality high
```

### 7. 可自定义的 ffmpeg 转码参数
```bash
spotdl "https://open.spotify.com/track/xxxxxxxxxxxx" --ffmpeg-lvl 320k
```

## 常用命令行选项
- `-a, --album-cover`：下载专辑封面
- `-c, --compression`：设置 ffmpeg 比特率（如 `320k`）
- `-q, --quality`：设置下载质量（`low` / `medium` / `high`）
- `-o, --output`：自定义输出路径与文件名模板
- `--verbose`：显示详细日志
- `--quiet`：最小化输出
- `--filename-format`：自定义文件名格式（`track`, `title` 等）
- `--max-time`：限制单个下载时长

## 进阶使用

### 下载整个 Spotify 教学组（示例）
```bash
cat playlists.txt | while read url; do spotdl "$url"; done
```

> `playlists.txt` 每行记录一个 Spotify 播放列表/专辑链接。

### 自动化脚本
```python
from spotdl import Spotdl

spotdl = Spotdl()
spotdl.download("https://open.spotify.com/track/xxxxxxxxxxxx")
```

> 支持在 Python 脚本中直接调用，方便集成。

## 常见问题
- **下载失败**：检查 `ffmpeg` 是否已正确安装，或使用 `--ffmpeg-flags "-strict -2"` 解决兼容性问题。  
- **无法识别搜索词**：使用完整歌曲名 + 艺人名，例如 `"Shape of You - Ed Sheeran"`。  
- **多线程下载卡顿**：减小 `-t` 参数，例如 `-t 4`。

> 详细信息请参阅官方文档与 `spotdl --help`。

