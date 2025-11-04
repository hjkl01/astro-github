
---
title: Telegram-Media-Downloader
---


# Telegram Media Downloader（Neet-Nestor 版）

- **项目地址**: https://github.com/Neet-Nestor/Telegram-Media-Downloader

## 主要特性

| 编号 | 功能 | 说明 |
|------|------|------|
| 1 | **多账号支持** | 同时管理多个 Telegram 账号/会话，避免单个账号频繁请求导致被限流。 |
| 2 | **多来源下载** | 支持从频道、群组、私聊以及机器人拉取媒体。 |
| 3 | **媒体类型过滤** | 可按文件扩展名、MIME 类型、文件大小、上传时间等条件筛选。 |
| 4 | **批量下载** | 一键下载选定聊天或频道内全部符合条件的媒体。 |
| 5 | **自动重试 & 限速** | 内置重试机制，支持自定义下载速率，避免网络拥堵。 |
| 6 | **保存到多端** | 支持本地磁盘或云存储（如 Dropbox、Google Drive）同步。 |
| 7 | **命令行工具** | 通过 CLI 进行快速操作，支持配置文件和命令行参数混合使用。 |
| 8 | **日志与统计** | 提供下载进度、错误日志、总文件数及占用空间等统计信息。 |
| 9 | **可定制脚本** | 通过插件/脚本方式扩展下载逻辑，满足特殊业务需求。 |

## 功能说明

- **初始化会话**：使用 `api_id`、`api_hash` 与 `phone_number` 生成并保存会话文件。  
- **配置文件**：`config.yaml` 里可以统一管理所有账号、下载路径、过滤条件、重试次数、速率限制等。  
- **下载命令**：  
  ```bash
  python main.py --config config.yaml
  ```  
  或者单独指定参数：  
  ```bash
  python main.py --chat "TelegramChannelName" --type photo --min-size 1M
  ```  
- **日志**：下载日志默认输出到 `logs/download.log`，支持 `--log-level DEBUG/INFO/ERROR`。  
- **插件**：在 `plugins/` 目录下放置自定义脚本，项目会自动加载并执行。  

## 用法示例

1. **克隆仓库**  
   ```bash
   git clone https://github.com/Neet-Nestor/Telegram-Media-Downloader.git
   cd Telegram-Media-Downloader
   ```

2. **安装依赖**  
   ```bash
   pip install -r requirements.txt
   ```

3. **配置文件**  
   ```yaml
   # config.yaml
   accounts:
     - api_id: 123456
       api_hash: "abcdef1234567890"
       phone: "+1234567890"
       session_name: "my_account"
   download:
     path: "./downloads"
     filter:
       types: ["photo", "video", "document"]
       min_size: "500K"
       max_size: "50M"
       date_from: "2023-01-01"
   ```

4. **启动下载**  
   ```bash
   python main.py --config config.yaml
   ```

5. **单聊/频道下载**  
   ```bash
   python main.py --chat "@channel_name" --type video
   ```

6. **查看帮助**  
   ```bash
   python main.py --help
   ```

## 重要提示

- 请先在 Telegram 端开启 **两步验证** 并获取 `api_id`/`api_hash`。  
- 频繁、大量下载可能导致账号被限流或封禁，建议合理设置 `download.rate_limit`。  
- 本项目仅用于学习与合法用途，严禁用于侵犯他人版权或隐私。

---

**文件路径**: `src/content/docs/00/Telegram-Media-Downloader_Neet-Nestor.md`
