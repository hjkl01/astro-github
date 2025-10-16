
---
title: zulip
---

# Zulip 项目概述

## 项目地址
[https://github.com/zulip/zulip](https://github.com/zulip/zulip)

## 主要特性
Zulip 是一个开源的团队协作和即时通讯平台，以其独特的“主题式”对话模式著称。该模式允许用户将消息组织成主题（topics），便于后续搜索和回顾讨论，避免传统聊天工具的线性混乱。主要特性包括：
- **主题组织**：每个对话线程以主题命名，支持嵌套回复，便于跟踪多线程讨论。
- **集成丰富**：支持与 GitHub、Jira、Slack 等工具的无缝集成，以及自定义机器人和 webhook。
- **搜索强大**：全文搜索功能支持消息、文件和用户，结合主题过滤，提高效率。
- **多平台支持**：跨设备兼容，包括 Web、桌面（Windows、macOS、Linux）和移动端（iOS、Android）应用。
- **安全性与隐私**：端到端加密选项、角色-based 访问控制（RBAC），以及自托管部署支持数据主权。
- **可扩展性**：基于 Python/Django 开发，支持大规模用户（数万用户），并提供 API 和插件系统。
- **开源协作**：完全开源（Apache 2.0 许可），社区驱动，易于自定义和贡献。

## 主要功能
Zulip 的核心功能聚焦于高效的团队沟通和协作：
- **即时消息与群聊**：支持一对一、私聊、频道（streams）和主题讨论。
- **文件共享与协作**：上传文件、Markdown 编辑、任务分配和提醒。
- **通知管理**：智能通知系统，可根据主题、用户或时间自定义，避免信息 overload。
- **视频/音频集成**：内置支持 Zoom、Jitsi 等会议工具的链接分享。
- **分析与报告**：管理员面板提供用户活跃度、消息统计等洞察。
- **国际化**：支持多语言界面，包括中文，并可自定义品牌。

## 用法指南
### 安装与部署
1. **自托管部署**（推荐用于企业）：
   - 克隆仓库：`git clone https://github.com/zulip/zulip.git`
   - 安装依赖：使用脚本 `./scripts/setup/install-node_modules.sh` 和 `pip install -r requirements.txt`。
   - 配置：编辑 `zulip/settings.py`，设置数据库（PostgreSQL）和 Redis。
   - 运行：`tools/provision` 初始化，然后 `supervisorctl start all` 启动服务。
   - 访问：通过浏览器打开 `http://your-server:9991`。

2. **云托管**：Zulip 提供官方云服务（zulip.com），免费试用后付费订阅。

### 日常使用
1. **注册与加入**：管理员邀请用户，或通过邀请链接加入组织。
2. **创建对话**：
   - 选择流（stream，如 #general），输入主题（如 “项目更新”），发送消息。
   - 回复时自动跟随主题，支持 @提及用户或 emoji 反应。
3. **搜索与导航**：
   - 使用左侧栏浏览流和主题，右上角搜索框输入关键词。
   - 移动端：下载 App，登录后同步所有对话。
4. **高级用法**：
   - 集成机器人：添加如 `/subscribe @bot` 命令。
   - API 使用：通过 REST API 发送消息或查询数据，例如 `curl -u user:pass https://your-zulip/api/v1/messages`。
   - 自定义：修改主题、设置通知偏好，或开发插件扩展功能。

Zulip 适合开发团队、开源社区或企业内部沟通，强调结构化和可搜索的对话体验。更多详情见官方文档：https://zulip.com/help/。