---
title: StreamCap
---

# StreamCap

StreamCap 是一个基于FFmpeg和StreamGet的多平台直播流录制客户端，覆盖 40+ 国内外主流直播平台，支持批量录制、循环监控、定时监控和自动转码等功能。

## ✨功能特性

- **多端支持**：支持Windows/MacOS/Web运行
- **循环监控**：实时监控直播间状态，开播即录。
- **定时任务**：根据设定时间范围检查直播间状态。
- **多种输出格式**：支持 ts、flv、mkv、mov、mp4、mp3、m4a 等格式。
- **自动转码**：录制完成后自动转码为 mp4 格式。
- **消息推送**：支持直播状态推送，及时获取开播通知。

## 🛠️快速开始

### 1. 运行预构建的程序

访问 [StreamCap Releases](https://github.com/ihmily/StreamCap/releases/latest) 页面，根据自身系统下载对应的最新版本压缩包。

- **Windows 用户**：下载 `StreamCap.zip` 文件，解压后运行 `StreamCap.exe`。
- **macOS 用户**：下载 `StreamCap.dmg` 文件，按照提示完成安装，即可在启动台找到应用并运行。

### 2. 从源代码运行

确保已安装 **Python 3.10** 或更高版本。

1. **克隆项目代码**：

   ```
   git clone https://github.com/ihmily/StreamCap.git
   cd StreamCap
   ```

2. **安装依赖**：

   ```
   # 安装核心依赖
   pip install -i https://pypi.org/simple streamget

   # 桌面端
   pip install -r requirements.txt

   # Web端
   pip install -r requirements-web.txt
   ```

3. **配置运行环境**：

   将.env.example示例配置文件复制一份并将文件重命名为.env

   ```
   cp .env.example .env
   ```

4. **运行程序**：

   在Windows和macOS上默认以桌面程序的方式运行，使用以下命令启动程序：

   ```
   python main.py
   ```

   Linux请使用web方式运行，修改 `.env` 文件，将 `PLATFORM` 的值改为 `web`，即可以Web方式运行。

   或者无需修改配置文件，直接使用以下命令启动

   ```
   python main.py --web
   ```

   启动成功后，通过 `http://127.0.0.1:6006` 访问。更多配置请参考 [Web运行指南](https://github.com/ihmily/StreamCap/wiki/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97#web-%E7%AB%AF%E8%BF%90%E8%A1%8C)

   如果程序提示缺少 FFmpeg，请访问 FFmpeg 官方下载页面[Download FFmpeg](https://ffmpeg.org/download.html)，下载预编译的 FFmpeg 可执行文件，并配置环境变量。

## 🐋容器运行

本机无需Python环境运行，在运行命令之前，请确保您的机器上安装了 [Docker](https://docs.docker.com/get-docker/) 和 [Docker Compose](https://docs.docker.com/compose/install/)

1. **快速启动**

   最简单方法是使用`docker compose`运行，进入项目根目录后，只需简单执行以下命令(确保已经存在`.env`文件)：

   ```
   docker compose up
   ```

   可选 `-d` 在后台运行。注意容器内时区问题，默认使用的是 `Asia/Shanghai` ，如需修改可以在.env文件配置。

2. **停止容器实例**

   ```
   docker compose stop
   ```

3. **构建镜像(可选)**

   Docker仓库中的镜像的代码版本不一定是最新的，如有需要运行本仓库主分支最新代码，可以本地自定义构建

   ```
   docker build -t streamcap .
   ```

## 😺已支持平台

**国内平台（30+）**：抖音、快手、虎牙、斗鱼、B站、小红书、YY、映客、Acfun、Blued、京东、淘宝...

**海外平台（10+）**：TikTok、Twitch、PandTV、Soop、Twitcasting、CHZZK、Shopee、Youtube、LiveMe、Flextv(TTingLive)、Popkontv、Bigo...

更多示例地址请参考项目README。
