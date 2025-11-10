---
title: Trendradar
---

# TrendRadar

## 项目简介

🎯 TrendRadar 是一个新闻热点聚合与AI分析工具，帮助用户告别信息过载，通过AI理解热点新闻。项目由 sansan0 开发，目前在GitHub上拥有5k星标。

## 核心功能

### 全网热点聚合

- 支持监控35个主流平台，包括：
  - 知乎、抖音、B站
  - 华尔街见闻、财联社
  - 微博、今日头条、澎湃新闻等
- 默认监控11个平台，可自定义添加更多平台

### 智能推送策略

支持三种推送模式：

- **当日汇总 (daily)**：定时推送当日所有匹配新闻
- **当前榜单 (current)**：定时推送当前热点榜单
- **增量监控 (incremental)**：仅推送新增热点内容

### 精准内容筛选

- 支持关键词配置：普通词、必须词(+)、过滤词(!)
- 词组化管理，独立统计不同主题热点
- 个性化热点算法：排名权重60%、频次权重30%、热度权重10%

### 多渠道实时推送

支持多种推送渠道：

- 企业微信、飞书、钉钉
- Telegram、邮件、ntfy
- 支持时间窗口控制，避免非工作时间打扰

### AI智能分析 (v3.0.0新增)

- 基于MCP协议的AI对话分析系统
- 13种分析工具：趋势追踪、情感分析、相似检索等
- 支持Cherry Studio、Claude Desktop、Cursor等多客户端

### 零技术门槛部署

- GitHub一键Fork部署
- Docker容器化运行
- 网页版报告自动生成

## 快速开始

### 1. Fork项目

访问 [https://github.com/sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) 并Fork到自己的GitHub账户。

### 2. 配置推送渠道

在Fork后的仓库中设置GitHub Secrets，选择需要的推送平台：

- **企业微信**：设置 `WEWORK_WEBHOOK_URL`
- **飞书**：设置 `FEISHU_WEBHOOK_URL`
- **钉钉**：设置 `DINGTALK_WEBHOOK_URL`
- **Telegram**：设置 `TELEGRAM_BOT_TOKEN` 和 `TELEGRAM_CHAT_ID`
- **邮件**：设置 `EMAIL_FROM`、`EMAIL_PASSWORD`、`EMAIL_TO` 等
- **ntfy**：设置 `NTFY_TOPIC` 等

### 3. 配置关键词

在 `config/frequency_words.txt` 中设置监控关键词：

```
AI
ChatGPT
+技术
!广告
```

### 4. 手动测试

进入Actions页面，运行"Hot News Crawler"工作流测试推送效果。

## Docker部署

### 快速部署

```bash
docker run -d --name trend-radar \
  -v ./config:/app/config:ro \
  -v ./output:/app/output \
  -e WEWORK_WEBHOOK_URL="your_webhook" \
  wantcat/trendradar:latest
```

### 使用docker-compose

```bash
# 下载配置文件
wget https://raw.githubusercontent.com/sansan0/TrendRadar/master/config/config.yaml -P config/
wget https://raw.githubusercontent.com/sansan0/TrendRadar/master/config/frequency_words.txt -P config/

# 启动服务
docker-compose pull
docker-compose up -d
```

## AI分析部署

### 1. 启动HTTP服务

```bash
# Windows
start-http.bat

# Mac/Linux
./start-http.sh
```

### 2. 配置AI客户端

以Cherry Studio为例，添加MCP服务器：

- URL: `http://localhost:3333/mcp`
- 开始使用自然语言查询："分析今天的AI热点趋势"

## 配置说明

### 关键词语法

- **普通词**：`AI` (包含即可)
- **必须词**：`+技术` (必须同时包含)
- **过滤词**：`!广告` (排除包含的新闻)

### 推送模式配置

在 `config/config.yaml` 中设置：

```yaml
mode: daily # daily/current/incremental
push_window:
  enabled: true
  start_time: '09:00'
  end_time: '18:00'
```

## 适用场景

- **投资者**：监控财经热点，及时把握市场动态
- **自媒体人**：追踪行业趋势，发现内容灵感
- **企业公关**：舆情监控，品牌声誉管理
- **普通用户**：个性化新闻推送，告别信息过载

## 项目特点

- 🚀 30秒网页部署，1分钟手机通知
- 🤖 AI深度分析，无需编程基础
- 📊 多平台聚合，自定义热点算法
- 🔄 自动定时更新，支持多种推送渠道
- 🐳 Docker一键部署，开箱即用

## 许可证

GPL-3.0 License
