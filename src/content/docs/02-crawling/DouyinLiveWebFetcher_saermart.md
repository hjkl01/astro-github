---
title: DouyinLiveWebFetcher
---

# 抖音直播间网页版弹幕数据抓取

**项目地址：** [https://github.com/saermart/DouyinLiveWebFetcher](https://github.com/saermart/DouyinLiveWebFetcher)

## 主要特性

- **抖音弹幕抓取**：专门用于抓取抖音直播间网页版的弹幕数据，支持实时获取进场消息、聊天消息、礼物消息、点赞消息等。
- **2025最新版本**：持续更新以适应抖音接口变化，包含最新的signature和a_bogus参数处理。
- **Python实现**：基于Python开发，支持WebSocket连接获取实时数据。
- **开源免费**：AGPL-3.0许可，仅用于学习研究交流。
- **多环境支持**：支持Windows、macOS、Linux，Python 3.7+，Node.js v18.2.0。

## 主要功能

- **弹幕数据抓取**：实时抓取直播间弹幕，包括用户进场、聊天、礼物、点赞、粉丝团等消息。
- **观看人数统计**：获取当前观看人数和累计观看人数。
- **数据输出**：将抓取的数据输出到控制台，支持自定义处理。
- **Protobuf支持**：使用Protobuf解析抖音的二进制数据包。
- **签名生成**：内置JS代码生成必要的签名参数（signature、a_bogus）。

## 用法

1. **环境准备**：
   - 安装Python 3.7+ 和 Node.js v18.2.0。
   - 安装protoc（libprotoc 25.1）。
   - 克隆仓库：
     ```
     git clone https://github.com/saermart/DouyinLiveWebFetcher.git
     cd DouyinLiveWebFetcher
     ```
   - 安装依赖：
     ```
     pip install -r requirements.txt
     ```

2. **运行**：
   - 执行主程序：
     ```
     python main.py
     ```
   - 输入抖音直播间网页URL，程序将自动提取房间ID并开始抓取弹幕。

3. **数据查看**：
   - 弹幕数据实时输出到控制台，包括用户昵称、性别、消息内容等。

注意：仅用于学习研究交流，严禁用于商业谋利、破坏系统或盗取个人信息。遵守抖音平台使用条款。
