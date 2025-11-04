
---
title: return-youtube-dislike
---

# return-youtube-dislike

> 项目地址: https://github.com/Anarios/return-youtube-dislike

## 项目简介

`return-youtube-dislike` 是一个开源项目，用于恢复 YouTube 视频的“喜欢/不喜欢”计数。它通过向 YouTube 的服务器发送请求，获取并返回视频的喜欢数和不喜欢数，从而解决了 YouTube 在某些地区显示“已删除”或“隐藏”不喜欢计数的问题。

## 主要特性

- **跨平台支持**：可在 Windows、macOS、Linux 等多种操作系统上使用。
- **轻量级**：依赖最少，使用 Python 3.7+，不需要额外的数据库或后端服务。
- **易于使用**：提供命令行界面（CLI）和 RESTful API 两种访问方式。
- **高可用性**：通过多线程和重试机制，保证请求稳定性。
- **数据缓存**：可选本地缓存，减少对 YouTube 服务器的请求频率。
- **可扩展性**：支持自定义请求头、代理、API 路径等。

## 功能说明

| 功能 | 描述 |
|------|------|
| 获取喜欢/不喜欢计数 | 输入视频 ID 或 URL，即可返回对应视频的喜欢数与不喜欢数。 |
| RESTful API | 通过 `GET /v1/dislike?url={video_url}` 获取数据，支持 `X-API-KEY` 认证。 |
| CLI 工具 | `python dislike.py https://youtu.be/VIDEO_ID` 直接在终端查询。 |
| 缓存机制 | 默认缓存 24 小时，避免频繁请求同一视频。 |
| 代理支持 | 通过环境变量或命令行参数配置 HTTP/HTTPS 代理。 |
| 自定义头部 | 可添加自定义 HTTP 头部，适配不同网络环境。 |
| 错误处理 | 统一错误码与信息，便于调试。 |

## 用法

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 通过 CLI 查询

```bash
python dislike.py https://youtu.be/dQw4w9WgXcQ
```

输出示例：

```
视频 ID: dQw4w9WgXcQ
喜欢: 120,000
不喜欢: 3,000
```

### 3. 通过 RESTful API

```bash
curl -X GET "http://localhost:5000/v1/dislike?url=https://youtu.be/dQw4w9WgXcQ" -H "X-API-KEY: your_api_key"
```

返回 JSON：

```json
{
  "video_id": "dQw4w9WgXcQ",
  "likes": 120000,
  "dislikes": 3000,
  "status": "success"
}
```

### 4. 代理与自定义头部

```bash
export HTTP_PROXY="http://proxy.example.com:8080"
export HTTPS_PROXY="https://proxy.example.com:8080"

python dislike.py https://youtu.be/dQw4w9WgXcQ --header "User-Agent: CustomAgent/1.0"
```

### 5. 缓存使用

默认缓存有效期为 24 小时，若需修改：

```bash
python dislike.py https://youtu.be/dQw4w9WgXcQ --cache-time 7200  # 2 小时
```

## 贡献

欢迎提交 Issue 与 Pull Request，详细信息请参阅项目根目录下的 `CONTRIBUTING.md`。

---