---
title: xiaomusic
---

# xiaomusic

xiaomusic 是一个用于小爱音箱播放音乐的项目，使用 yt-dlp 下载音乐，支持语音口令控制播放。

## 功能

- **无限听歌**：通过 yt-dlp 下载音乐，支持多种音乐源。
- **语音控制**：支持语音口令，如“播放歌曲+歌名”、“上一首”、“下一首”、“单曲循环”、“全部循环”、“随机播放”、“关机”等。
- **设备支持**：支持多种小爱音箱型号，包括 L06A、L07A、S12、LX5A 等。
- **音乐格式**：支持 mp3、flac、wav、ape、ogg、m4a 等格式。
- **网络歌单**：支持配置 JSON 格式的歌单，支持电台和歌曲。
- **收藏功能**：支持加入和取消收藏歌曲。
- **搜索播放**：支持搜索关键词播放歌曲。
- **本地播放**：支持播放本地歌曲文件。

## 用法

### Docker 运行（推荐）

最简配置运行：

```bash
docker run -p 58090:8090 -e XIAOMUSIC_PUBLIC_PORT=58090 -v /xiaomusic_music:/app/music -v /xiaomusic_conf:/app/conf hanxi/xiaomusic
```

国内用户：

```bash
docker run -p 58090:8090 -e XIAOMUSIC_PUBLIC_PORT=58090 -v /xiaomusic_music:/app/music -v /xiaomusic_conf:/app/conf docker.hanxi.cc/hanxi/xiaomusic
```

Docker Compose 配置：

```yaml
services:
  xiaomusic:
    image: hanxi/xiaomusic
    container_name: xiaomusic
    restart: unless-stopped
    ports:
      - 58090:8090
    environment:
      XIAOMUSIC_PUBLIC_PORT: 58090
    volumes:
      - /xiaomusic_music:/app/music
      - /xiaomusic_conf:/app/conf
```

启动后，访问 http://NAS_IP:58090 配置参数。

### pip 安装运行

```bash
pip install -U xiaomusic
xiaomusic --config config.json
```

配置文件参考 `config-example.json`。

### 开发环境运行

```bash
pdm run xiaomusic.py
```

## 注意事项

- 初次安装遇到问题请查阅 [FAQ](https://github.com/hanxi/xiaomusic/issues/99)。
- 建议开启密码登录以确保安全。
- 支持的设备型号详见项目文档。
