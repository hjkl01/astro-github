
---
title: geoip
---


# geoip - Loyalsoldier

**项目地址**: <https://github.com/Loyalsoldier/geoip>

## 主要特性

- **自动更新 GeoIP 数据**  
  通过 MiniPay 与 MaxMind 订阅的付费数据库以及免费 GeoLite2 数据库，定期拉取最新 IP 地理位置信息。

- **多种格式输出**  
  - `MMDB`（MaxMind Binary）  
  - `CSV`（通用文本）  
  - `IP-CIDR`（符合 Clash、surge 等网络代理工具的列表）

- **多版本兼容**  
  支持 GeoIP2 Country、City、ISP 等不同级别的数据库。

- **轻量化 Docker 镜像**  
  提供 `ghcr.io/lyft/geoip:latest`（或自建镜像），可直接部署在容器化环境中。

## 核心功能

1. **数据库合并**  
   将付费版与免费版的数据合并，消除冲突，提升完整度。

2. **数据清洗**  
   自动剔除无效 IP 或缺失信息，保证最终数据库质量。

3. **定时任务**  
   支持通过 Cron 触发自动更新，或手动执行 `update.sh`。

4. **代理工具集成**  
   直接生成专为 Clash、Surge、Shadowsocks、V2Ray 等工具准备的 IP 列表。

## 用法示例

### 1. 下载并更新数据库

```bash
# 拉取源码
git clone https://github.com/Loyalsoldier/geoip.git
cd geoip

# 运行更新脚本（需要 Python3、pip、maxminddb-cpp）
./update.sh
```

> **提示**：首次运行会尝试下载 MaxMind 的免费 GeoLite2 数据；若已注册 MaxMind API 账号，可以在 `.env` 文件中配置 `MAXMIND_LICENSE_KEY`。

### 2. Docker 部署

```bash
docker pull ghcr.io/lyft/geoip:latest

# 运行容器，默认会在 /data 里生成数据库文件
docker run -d --name geoip \
  -v $(pwd)/data:/data \
  ghcr.io/lyft/geoip:latest
```

容器启动后会自动执行更新，可配合 `cron` 或宿主机定时任务实现持续更新。

### 3. 生成 Clash/Surge 的 IP 列表

```bash
# 生成 CSV 并转换为 IP-CIDR 列表
./generate.sh --format csv --output data/geoip.csv
./clip2cidr.sh data/geoip.csv > data/geoip.conf
```

将 `geoip.conf` 配置到所使用的代理工具中即可。

## 目录结构

```
geoip/
├─ data/          # 存放生成的数据库文件
├─ scripts/       # 更新、合并、转换脚本
├─ .env.example   # 环境变量配置示例
├─ Dockerfile
└─ README.md
```

## 开源许可证

MIT

---

> 需要关注项目最新更新，请关注 GitHub 上的 Releases 与 Issues 页面。祝您使用愉快！