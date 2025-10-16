
---
title: DouyinLiveWebFetcher
---

# DouyinLiveWebFetcher 项目

## 项目地址
[GitHub 项目地址](https://github.com/saermart/DouyinLiveWebFetcher)

## 主要特性
- **实时直播数据抓取**：支持从抖音直播间实时获取视频流、弹幕、礼物等数据，通过WebSocket和HTTP接口实现高效数据传输。
- **Web界面支持**：提供简易的Web前端，用户可以通过浏览器访问和监控直播内容，无需复杂配置。
- **多平台兼容**：基于Node.js开发，支持Windows、macOS和Linux系统运行，易于部署。
- **数据持久化**：可选将抓取的数据保存为JSON或CSV格式，便于后续分析和存储。
- **轻量级设计**：代码结构简洁，依赖少，适合个人开发者或小型项目使用。

## 主要功能
- **直播间监控**：输入抖音直播间ID或URL，即可开始抓取直播视频流和互动数据。
- **弹幕实时显示**：捕获并实时展示直播间的弹幕消息，支持过滤和关键词搜索。
- **礼物与互动追踪**：记录观众送出的礼物、点赞和分享等互动事件，提供统计汇总。
- **API接口**：内置RESTful API，允许外部程序调用抓取数据，实现自动化集成。
- **错误处理与日志**：内置日志系统，记录抓取过程中的异常和调试信息，确保稳定运行。

## 用法
1. **环境准备**：
   - 安装Node.js（版本 >= 14.0）。
   - 克隆仓库：`git clone https://github.com/saermart/DouyinLiveWebFetcher.git`。
   - 进入项目目录：`cd DouyinLiveWebFetcher`。
   - 安装依赖：`npm install`。

2. **配置**：
   - 编辑`config.json`文件，设置抖音直播间ID、代理（如需绕过限制）和输出路径。

3. **运行**：
   - 启动服务器：`npm start`。
   - 通过浏览器访问`http://localhost:3000`，输入直播间信息开始抓取。
   - 使用命令行模式：`node fetcher.js --roomId=你的直播间ID`。

4. **停止与数据导出**：
   - 按Ctrl+C停止抓取。
   - 数据自动保存至`output/`目录，可自定义路径。

注意：使用时需遵守抖音平台的使用条款，避免滥用导致账号封禁。项目仅供学习和研究目的。