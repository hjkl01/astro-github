---
title: PeerBanHelper
---

# PeerBanHelper 项目

**GitHub 项目地址**: [https://github.com/PBH-BTN/PeerBanHelper](https://github.com/PBH-BTN/PeerBanHelper)

## 主要特性
PeerBanHelper 是一个开源工具，专为 BTN (BroadcastTheNet) 社区设计，主要用于帮助用户管理 BT 下载中的 Peer 封禁（Peer Ban）问题。其核心特性包括：
- **自动化检测与处理**：自动扫描和识别潜在的 Peer 封禁事件，支持实时监控下载进度。
- **集成 BT 客户端**：兼容 qBittorrent、Transmission 等流行 BT 客户端，提供插件式集成或脚本支持。
- **数据可视化**：生成封禁报告和统计图表，帮助用户分析封禁原因（如 IP 泄露或协议违规）。
- **隐私保护**：强调用户隐私，不收集个人信息，支持本地运行以避免数据外泄。
- **跨平台支持**：适用于 Windows、macOS 和 Linux 系统，通过 Python 脚本实现。

## 主要功能
- **Peer 封禁检测**：监控 torrent 下载中的 Peer 连接，检测异常封禁信号，并自动隔离问题 Peer。
- **日志分析**：解析 BT 客户端日志文件，提取封禁相关信息，并输出易读的报告。
- **自动修复建议**：基于检测结果，提供 VPN 配置、端口转发或客户端设置的优化建议。
- **批量处理**：支持同时处理多个 torrent 文件，提高效率。
- **自定义规则**：用户可定义封禁过滤规则，例如忽略特定 IP 范围或协议类型。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/PBH-BTN/PeerBanHelper.git`
   - 安装依赖：进入项目目录，运行 `pip install -r requirements.txt`（需要 Python 3.6+）。

2. **配置**：
   - 编辑 `config.yaml` 文件，设置 BT 客户端路径、监控目录和 VPN 接口。
   - 示例配置：
     ```
     client_path: /path/to/qbittorrent
     watch_dir: /downloads
     vpn_interface: tun0
     ```

3. **运行**：
   - 命令行启动：`python main.py --watch`（监控模式）。
   - 分析日志：`python analyzer.py --log /path/to/logfile.log`。
   - 生成报告：运行后，报告将保存在 `output/` 目录下。

4. **注意事项**：
   - 确保 BT 客户端启用日志记录。
   - 项目仅供学习和个人使用，遵守 BTN 社区规则。
   - 如遇问题，参考仓库的 README.md 或 issues 页面。