
---
title: canary
---


# Canary（OpenTibia 服务器监控工具）

> 项目地址: <https://github.com/opentibiabr/canary>

---

## 一、项目概览

Canary 是一个基于 Python 的轻量级监控工具，专为 **OpenTibia** 服务器设计。通过定时检查服务器状态、玩家数量、CPU/内存/磁盘使用率等指标，并将结果推送到 Discord 频道，帮助管理员及时发现并处理服务器故障。

---

## 二、主要特性

| 特性 | 说明 |
|------|------|
| **服务器状态监控** | 定时 ping 服务器，判断是否在线。 |
| **玩家统计** | 获取当前在线玩家人数，支持自定义阈值告警。 |
| **系统资源监控** | 监测 CPU、内存、磁盘占用率并可配置报警阈值。 |
| **Discord 通知** | 通过 Webhook 或 Bot Token 发送告警消息，支持自定义消息模板。 |
| **周期配置** | 通过 `config.yaml` 或环境变量自定义检查间隔、告警阈值。 |
| **日志与持续运行** | 记录监控日志，支持 Docker 容器化部署。 |
| **多平台兼容** | 只需 Python 3.8+，可在 Windows、Linux、macOS 上运行。 |

---

## 三、功能细节

1. **健康检查**  
   - 发送 TCP ping，检测端口是否开放。  
   - 若服务器在指定时间内未响应，触发“服务器宕机”告警。

2. **玩家统计**  
   - 调用 OpenTibia 的 `players.php` 接口获取当前玩家列表。  
   - 支持设置“玩家数阈值”告警，例如玩家少于 `5` 时提醒。

3. **系统资源监控**  
   - 利用 `psutil` 获取 CPU、内存、磁盘使用率。  
   - 设定阈值后，当占用率超过阈值时发送告警。

4. **Discord 通知**  
   - 通过 Webhook URL 或 Bot Token 发送 RichEmbed 消息。  
   - 消息可自定义标题、颜色、字段等。

5. **配置文件**  
   ```yaml
   # config.yaml
   server:
     host: "tibia.example.com"
     port: 7171
     check_interval: 60      # 秒
   thresholds:
     player_count: 5
     cpu: 80                # 百分比
     memory: 80
     disk: 90
   discord:
     webhook_url: "https://discord.com/api/webhooks/..."
     bot_token: null
   log_level: "INFO"
   ```

---

## 四、使用方法

### 1. 环境准备

```bash
# 安装 Python 3.8+
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 配置

- 复制 `config.yaml.example` 为 `config.yaml` 并根据需要修改。
- 在 Discord 创建 Webhook 或 Bot，获取 `WEBHOOK_URL` 或 `BOT_TOKEN`。

### 3. 运行

```bash
# 直接运行
python canary/main.py

# 或使用 Docker
docker build -t opentibiabr/canary .
docker run -d --name canary \
  -v $(pwd)/config.yaml:/app/config.yaml \
  opentibiabr/canary
```

### 4. 日志与监控

- 日志默认输出到 `logs/canary.log`。  
- 可通过监控平台（如 Grafana）集成 Prometheus，获取更细粒度的指标。

---

## 五、常见问题

| 问题 | 解决方案 |
|------|----------|
| 服务器无法访问 | 检查 `host` 与 `port` 是否正确，防火墙是否允许外部访问。 |
| Discord 消息不发送 | 确认 `webhook_url` 或 `bot_token` 正确无误，且 Discord 服务器允许机器人发送消息。 |
| 资源监控误报 | 调整 `thresholds` 配置，或检查服务器负载是否正常。 |

---

> 该项目仅供学习与实验之用，若用于生产环境请自行评估与安全测试。祝使用愉快!