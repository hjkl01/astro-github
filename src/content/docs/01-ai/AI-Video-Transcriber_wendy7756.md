---
title: AI-Video-Transcriber
---

# AI-Video-Transcriber (wendy7756)

> **项目地址**：<https://github.com/wendy7756/AI-Video-Transcriber>

## 简介

AI-Video-Transcriber 是一款基于 AI 的视频转写和摘要工具，支持 YouTube、Tiktok、Bilibili 等 30+ 视频平台。使用 Faster-Whisper 进行高精度语音转文本，AI 文本优化、多种语言摘要、实时进度跟踪等功能。支持移动设备，易于使用。

## 主要特性

| 功能            | 说明                                             |
| --------------- | ------------------------------------------------ |
| **多平台支持**  | 支持 YouTube、Tiktok、Bilibili 等 30+ 平台       |
| **智能转写**    | 使用 Faster-Whisper 进行高精度语音转文本         |
| **AI 文本优化** | 自动修正错别字、句子补全、智能分段               |
| **多语言摘要**  | 生成多种语言的智能摘要                           |
| **实时进度**    | 实时进度跟踪和状态更新                           |
| **条件翻译**    | 当摘要语言与转写语言不同时，自动使用 GPT-4o 翻译 |
| **移动友好**    | 完美支持移动设备                                 |

## 安装与依赖

### 前置条件

- Python 3.8+
- FFmpeg
- OpenAI API Key（可选，用于 AI 摘要功能）

### 自动安装

```bash
git clone https://github.com/wendy7756/AI-Video-Transcriber.git
cd AI-Video-Transcriber
chmod +x install.sh
./install.sh
```

### Docker 安装

```bash
git clone https://github.com/wendy7756/AI-Video-Transcriber.git
cd AI-Video-Transcriber
cp .env.example .env
# 编辑 .env 文件，设置 OPENAI_API_KEY
docker-compose up -d
```

### 手动安装

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key_here"
```

## 使用方法

### 启动服务

```bash
python3 start.py
```

打开浏览器访问 `http://localhost:8000`。

### 使用指南

1. 输入视频 URL（YouTube、Bilibili 等）
2. 选择摘要语言
3. 点击开始处理
4. 监控实时进度
5. 查看优化转写文本和智能摘要
6. 下载 Markdown 格式文件

## 技术架构

- **后端**：FastAPI、yt-dlp、Faster-Whisper、OpenAI API
- **前端**：HTML5 + CSS3 + JavaScript

## 支持语言

- 转写：支持 100+ 语言
- 摘要：英语、中文、日语、韩语、西班牙语、法语、德语等

## 常见问题

- **转写慢**：选择较小 Whisper 模型以提高速度
- **平台支持**：所有 yt-dlp 支持的平台
- **AI 功能不可用**：需要 OpenAI API Key

## 贡献

欢迎提交 Issue 和 Pull Request。
