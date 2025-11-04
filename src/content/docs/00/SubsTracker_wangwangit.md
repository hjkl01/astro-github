
---
title: SubsTracker
---

# SubsTracker (by wangwangit)

> GitHub 地址: https://github.com/wangwangit/SubsTracker

## 📌 项目简介
SubsTracker 是一款轻量级的字幕追踪与下载工具，专为个人影音库自动管理设计。它支持监控本地或网络媒体目录，智能匹配并下载对应的字幕文件，保持字幕时序一致，提升观影体验。

---

## ✨ 主要特性

| 功能 | 说明 |
|------|------|
| **文件监控** | 监视指定路径（支持本地硬盘、NAS、uTorrent 等）、实时检测新增影片/剧集文件。 |
| **多源字幕搜索** | 自动调用 OpenSubtitles、Subscene、yts-subs.com 等多家字幕站点，支持多种语言。 |
| **精准匹配** | 采用 MD5、IMDb、剧集/集数解析等多维度匹配算法，确保字幕与原文件匹配度高。 |
| **批量自动下载** | 识别匹配的字幕后，自动下载、解压并放置到与媒体文件同级或指定子文件夹。 |
| **定期更新** | 能够周期性检查已有字幕，若有新版本可自动更新。 |
| **日志与通知** | 完整的操作日志与邮件/Telegram 通知插件，便于排错与远程监控。 |
| **可扩展插件** | 通过配置文件实现自定义搜索策略、下载源、分离逻辑等，插件体系灵活。 |
| **CLI & 后台服务** | 支持从命令行启动，亦可在 Docker/系统服务中运行，便于部署。 |

---

## 🚀 用法

### 1. 安装依赖

```bash
git clone https://github.com/wangwangit/SubsTracker.git
cd SubsTracker
pip install -r requirements.txt  # 或使用 poetry / pipenv
```

> **运行环境**：Python 3.10+，建议使用 virtualenv 或 conda。

### 2. 配置文件

默认配置文件 `config.yaml` 位于项目根目录，可根据需要自行修改：

```yaml
# 监控目录
watch_dirs:
  - /media/movies
  - /media/series

# 字幕源
sources:
  - name: OpenSubtitles
    key: YOUR_OSS_TOKEN   # 若需 API key 请在此填写
  - name: Subscene

# 匹配规则
match:
  languages: [zh-CN, en]
  quality: high

# 下载路径
download_path: shared/subtitles

# 日志设置
logging:
  level: INFO
  file: subs_tracker.log

# 通知
notify:
  telegram:
    token: YOUR_BOT_TOKEN
    chat_id: YOUR_CHAT_ID
```

### 3. 运行

```bash
# 直接启动
python subs_tracker.py

# 或作为后台服务（Linux）
nohup python subs_tracker.py > subs.out 2>&1 &
```

> 运行后，它会持续监控 `watch_dirs` 下的文件，新文件添加后立即启动匹配与下载流程。

### 4. 常用命令行参数

```bash
python subs_tracker.py --help
```

> 典型参数涵盖：
> - `--config PATH`：自定义配置文件
> - `--dry-run`：仅模拟匹配，不下载
> - `--once`：只执行一次扫描，退出

### 5. Docker 部署（推荐）

```yaml
# docker-compose.yml 示例
services:
  subs_tracker:
    image: wangwangit/substracker:latest
    volumes:
      - /media/movies:/media/movies
      - /media/series:/media/series
      - /mnt/subtitles:/mnt/subtitles
      - ./config.yaml:/app/config.yaml
    environment:
      - TZ=Asia/Shanghai
```

```bash
docker compose up -d
```

---

## 🔧 常见问题

| 问题 | 解决方案 |
|------|-----------|
| **字幕匹配不到** | 确认文件名格式符合标准（如 `xxx.2024.1080p.mkv`），或在配置中开启 `ignore_sensitive`。 |
| **下载速度慢** | 检查网络代理，或调整 `sources` 顺序。 |
| **日志文件被占用** | 关机后使用 `lsof -i :PORT` 检查进程，或修改日志文件名。 |

---

## 📦 贡献 & 反馈

如遇 bug 或功能建议，欢迎提交 issue 或 pull request。详细开发者文档请参阅项目根目录的 `docs/` 目录。

---

> 祝使用愉快 🚀

---