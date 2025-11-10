---
title: AiToEarn
---

# AiToEarn 项目

## 项目地址

https://github.com/yikart/AiToEarn

## 主要特性

AiToEarn 是一个企业级的 AI 内容营销平台，帮助创作者、品牌和企业使用 AI 自动化构建、分发和货币化内容。支持全球最受欢迎的平台。

支持的渠道：
Douyin, Xiaohongshu (Rednote), WeChat Channels, Kuaishou, Bilibili, WeChat Official Accounts,
TikTok, YouTube, Facebook, Instagram, Threads, Twitter (X), Pinterest

## 主要功能

### 1. 内容发布 — 一键多平台

- **分发到任何地方**：发布到全球最广泛的平台范围（Douyin, Kwai, WeChat Channels, WeChat Offical Account, Bilibili, Rednote, Facebook, Instagram, TikTok, LinkedIn, Threads, YouTube, Pinterest）。
- **智能导入**：导入历史内容以快速重新编辑和重新分发。
  - 示例：将您的 Xiaohongshu 帖子同步到 YouTube。

- **日历调度**：像日历一样规划和协调所有平台的内容。
- **统一仪表板**：在一个地方管理所有互动。
- **主动互动**：加入热门对话，与潜在客户联系。
- 将**被动操作**变成**主动流量增长**。

### 2. 内容热点 — 病毒灵感引擎

- **案例库**：探索如何创建获得 10,000+ 喜欢的帖子。
- **趋势雷达**：即时发现最新的病毒趋势，减少创作者焦虑。

### 3. 内容搜索 — 品牌和市场洞察

- **品牌监控**：实时跟踪关于您品牌的对话。
- **内容发现**：搜索帖子、话题和社区以进行有针对性的互动。

### 4. 评论搜索 — 精确用户挖掘

- **智能评论搜索**：检测高转化信号，如“链接请”或“如何购买”。
- **转化助推器**：即时回复，提高互动和销售。

### 5. 内容互动 — 增长引擎

- **统一仪表板**：在一个地方管理所有互动。
- **主动互动**：加入热门对话，与潜在客户联系。
- 将**被动操作**变成**主动流量增长**。

### 6. 内容分析 — 全漏斗数据

- **跨平台比较**：一个平台可能会阻止流量，但其他平台不会。
- **端到端监控**：跟踪性能并构建您的 1M+ 粉丝路径。

### 7. AI 内容创建 — 端到端助手

- **AI 文案**：自动生成标题、字幕和描述。
- **AI 评论**：主动互动，吸引流量。
- **图像和卡片生成器**：加速内容工作流程。
- **支持的 AI 视频模型**：Seedance, Kling, Hailuo, Veo, Medjourney, Sora, Pika, Runway。
- **支持的 AI 图像模型**：GPT, Flux。
- **下一步**：标签生成器、智能 DM、视频编辑、AI 头像、翻译以进行全球分发。

### 8. 内容市场 — 交易和货币化

- **创作者**：直接销售您的内容，快速找到买家。
- **品牌**：购买现成的、高质量的内容。
- **AI 驱动增长**：
  **让我们使用 AI 赚钱。让我们一起赚钱！**

## 用法

### 快速开始

| OS      | 下载                                                                                                                                                                                                            |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Android | [![下载 Android](https://img.shields.io/badge/APK-Android1.2.2-green?logo=android&logoColor=white)](https://aitoearn-download.s3.ap-southeast-1.amazonaws.com/aitoearn-download/1.2.2/Aitoearn-1.2.2.apk)       |
| Windows | [![下载 Windows](https://img.shields.io/badge/Setup-Windows1.2.2-blue?logo=windows&logoColor=white)](https://aitoearn-download.s3.ap-southeast-1.amazonaws.com/aitoearn-download/1.2.2/AiToEarnSetup-1.2.2.exe) |
| macOS   | [![下载 macOS](https://img.shields.io/badge/DMG-macOS1.2.2-black?logo=apple&logoColor=white)](https://aitoearn-download.s3.ap-southeast-1.amazonaws.com/aitoearn-download/1.2.2/AiToEarn+1.2.2.dmg)             |
| iOS     | **即将推出！**                                                                                                                                                                                                  |
| Web     | [在 Web 上使用](https://aitoearn.ai/en/accounts)                                                                                                                                                                |

[Google Play 下载](https://play.google.com/store/apps/details?id=com.yika.aitoearn.aitoearn_app)

### 开始 Web 项目

#### 1. 启动后端服务

```bash
cd project/aitoearn-monorepo
pnpm install
npx nx serve aitoearn-channel && npx nx serve aitoearn-server
```

#### 2. 启动前端 `aitoearn-web`

```bash
pnpm install
pnpm run dev
```

### 开始 Electron 项目

```sh
# 克隆仓库
git clone https://github.com/yikart/AttAiToEarn.git

# 进入目录
cd AttAiToEarn

# 安装依赖
npm i

# 编译 sqlite (better-sqlite3 需要 node-gyp, Python 必须本地安装)
npm run rebuild

# 开始开发
npm run dev
```

项目适合创作者和开发者使用，文档详见仓库的 README.md。
