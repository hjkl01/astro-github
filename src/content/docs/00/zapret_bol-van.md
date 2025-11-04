
---
title: zapret
---

# Zapret – Telegram 过滤与黑名单机器人

**GitHub 项目地址**: <https://github.com/bol-van/zapret>

---

## 主要特性

- **自动黑名单**：根据预设规则自动拦截和删除垃圾/恶意信息。  
- **手动黑名单**：管理员可通过 `/ban`、`/unban` 等指令手动添加/移除号码/关键词。  
- **多渠道支持**：可在群组、频道或私聊中使用，支持 1:1 机器人与多方聊天。  
- **日志与审计**：所有拦截事件自动记录到 SQLite/PG/Redis，可通过 `/stats` 查看历史。  
- **Webhook/Long Polling**：支持两种连接模式，适配不同部署环境。  
- **可扩展插件**：核心代码模块化，易于添加自定义过滤器或第三方 API。  
- **多语言/本地化**：默认支持中文与俄文，其他语言可自行扩展。  

## 功能说明

| 指令 | 说明 |
|------|------|
| `/start` | 启动机器人，获取简易帮助 |
| `/help` | 查看完整指令列表 |
| `/ban <号码/关键词>` | 添加到黑名单（管理员权限） |
| `/unban <号码/关键词>` | 移除黑名单 |
| `/list` | 列出当前黑名单 |
| `/stats` | 查看拦截统计（管理员权限） |
| `/config` | 查看或修改机器人配置（管理员权限） |

> **管理员权限**：通过 `config.yaml` 或环境变量设置 `ADMIN_IDS`，仅这些 ID 可执行管理指令。

## 用法

### 1. 环境准备

```bash
# 克隆仓库
git clone https://github.com/bol-van/zapret.git
cd zapret

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置文件

复制示例配置并填写：

```bash
cp config.yaml.sample config.yaml
```

- `TOKEN` – 你的 Telegram Bot Token  
- `ADMIN_IDS` – 管理员 Telegram ID 列表  
- `DB_URL` – 数据库连接字符串（默认 SQLite）  
- `MODE` – `webhook` 或 `polling`  

### 3. 运行

#### 长轮询方式

```bash
python main.py
```

#### Webhook（推荐 Docker 部署）

```bash
docker build -t zapret .
docker run -e TOKEN=YOUR_TOKEN -e ADMIN_IDS=123456,789012 -e DB_URL=sqlite:///zapret.db -p 8443:8443 zapret
```

> 在 Webhook 模式下，请先在 BotFather 设置 `https://<your-domain>/webhook`，并在 `config.yaml` 中配置 `WEBHOOK_URL`。

### 4. 日志与监控

- 日志文件默认存储在 `logs/` 目录。  
- 可以使用 `systemd` 或 `supervisord` 进行进程管理。  
- 若使用 Docker，日志可通过 `docker logs` 查看。

## 贡献

如需改进或新增功能，欢迎提交 PR。请参考 `CONTRIBUTING.md`。

---