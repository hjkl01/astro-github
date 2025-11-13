---
title: vaultwarden
---

# Vaultwarden 项目

**GitHub 项目地址:** [https://github.com/dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden)

## 主要特性
Vaultwarden 是一个开源的 Bitwarden 服务器实现，使用 Rust 语言编写，轻量级且高效。它兼容官方 Bitwarden 客户端，支持端到端加密，适用于个人或小型团队的密码管理。主要特性包括：
- **轻量级部署**：资源占用低，可在 Raspberry Pi 或 Docker 环境中轻松运行。
- **端到端加密**：所有数据使用 AES-256 加密，用户数据仅在客户端解密。
- **多平台支持**：兼容 Bitwarden 的所有客户端（浏览器扩展、移动 App、桌面 App）。
- **自托管**：完全开源，无需依赖官方服务器，数据隐私更高。
- **2FA 支持**：集成两因素认证，包括 TOTP 和 U2F。
- **附件存储**：支持安全存储文件附件。
- **组织与共享**：支持团队组织、密码共享和访问控制。
- **API 兼容**：提供完整的 REST API，便于集成和自动化。

## 主要功能
- **密码生成与存储**：自动生成强密码，安全存储用户名、密码、笔记等。
- **自动填充**：通过浏览器扩展实现表单自动填充。
- **同步与备份**：跨设备实时同步，支持导出/导入数据。
- **安全审计**：检查弱密码、数据泄露，并提供安全建议。
- **事件日志**：记录登录和访问事件，便于审计。
- **自定义配置**：支持自定义域名、SMTP 邮件服务器和邀请链接。

## 用法
1. **安装与部署**：
   - 使用 Docker 快速部署：运行命令 `docker run -d --name vaultwarden -v /vw-data/:/data/ -p 80:80 vaultwarden/server:latest`。
   - 或从源代码构建：克隆仓库后，使用 `cargo build --release` 编译，然后配置环境变量运行。

2. **配置**：
   - 编辑 `env` 文件设置数据库路径、域名、SIGNUPS_ALLOWED（是否允许注册）等。
   - 支持 SQLite（默认）或外部数据库如 PostgreSQL。

3. **使用客户端**：
   - 下载官方 Bitwarden App 或扩展，将服务器 URL 设置为你的 Vaultwarden 实例（如 `http://your-domain.com`）。
   - 创建账户，添加密码条目，即可同步使用。

4. **维护**：
   - 定期更新 Docker 镜像或二进制文件。
   - 使用 HTTPS（推荐通过反向代理如 Nginx）确保安全。
   - 备份 `/vw-data/` 目录以防止数据丢失。

更多详情请参考项目 README。