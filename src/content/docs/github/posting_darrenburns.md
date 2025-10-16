
---
title: posting
---

# Posting 项目

## 项目地址
[GitHub 项目地址](https://github.com/darrenburns/posting)

## 主要特性
- **社交媒体自动化发布**：支持一键将内容发布到多个社交平台，如 Twitter、LinkedIn 和 Mastodon。
- **内容调度**：允许用户预设发布时间，实现定时发布功能。
- **多格式支持**：兼容文本、图片和链接等多种内容类型。
- **API 集成**：基于 OAuth 认证的安全连接，避免手动输入凭证。
- **开源与可扩展**：使用 Python 开发，易于自定义和扩展插件。

## 主要功能
- **平台管理**：轻松添加或移除支持的社交平台账户。
- **内容编辑器**：内置简单编辑器，支持 Markdown 预览和格式化。
- **批量处理**：一次性上传多个帖子，并设置不同的发布策略。
- **日志与监控**：记录发布历史，提供成功/失败通知和错误调试。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 系统运行。

## 用法
1. **安装**：克隆仓库 `git clone https://github.com/darrenburns/posting.git`，然后运行 `pip install -r requirements.txt`。
2. **配置**：编辑 `config.yaml` 文件，输入你的社交平台 API 密钥和账户信息。
3. **运行**：使用命令 `python main.py` 启动应用，导入内容并选择发布选项。
4. **调度帖子**：在界面中设置发布时间，保存后系统会自动执行。
5. **高级用法**：通过 CLI 模式运行 `python posting.py --post "你的内容" --platforms twitter,linkedin`，快速发布。