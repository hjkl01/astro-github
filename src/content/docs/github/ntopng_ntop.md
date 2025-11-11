---
title: ntopng
---


# ntopng - 网络流量分析工具

> **项目地址**: https://github.com/ntop/ntopng

## 一、项目概述
ntopng 是一款开源的网络流量分析与监控平台，提供实时流量可视化、统计分析、告警与历史数据查询等功能。其核心工作是将网络数据包转化为可解析的流量信息（Flow），并通过 Web UI 或 API 供管理员查看、分析和报警。

## 二、主要特性
| 特色 | 说明 |
|------|------|
| **实时流量监控** | 通过采集网卡流量，实时生成流量统计（带宽、协议、IP、端口等） |
| **多协议深度解析** | 支持 TCP/UDP/ICMP、HTTP、DNS、TLS、SSH、MySQL、PostgreSQL 等协议 |
| **流量图表与仪表盘** | 内置丰富的图表（柱状图、饼图、折线图）和自定义仪表盘 |
| **告警与事件** | 基于阈值或规则的告警，支持邮件、Webhook、SNMP Trap 等通知方式 |
| **插件与扩展** | 通过插件机制支持自定义协议解析、外部集成（Grafana、InfluxDB、ElasticSearch 等） |
| **多租户与访问控制** | 支持多用户、角色权限，隔离各租户视图 |
| **API & CLI** | RESTful API、命令行工具，便于自动化管理与脚本调用 |
| **历史数据存储** | 持久化存储流量信息，支持长时间查询和报告生成 |
| **跨平台** | 可在 Linux、FreeBSD、MacOS、Windows 上编译运行 |

## 三、核心功能
1. **流量采集**  
   - 通过 libpcap / nfqueue 等方式抓取网络包。  
   - 支持多网卡、VLAN、bonding 等网络环境。

2. **流量解析**  
   - 将包转换为 Flow，提取源/目的 IP、端口、协议、字节数、时间戳等。  
   - 对协议进行深度检测，提取 HTTP URI、DNS 查询、TLS 主机名等上下层信息。

3. **数据存储**  
   - 默认使用 SQLite（轻量级）或 InfluxDB、PostgreSQL、MySQL 等后端。  
   - 支持分区、压缩与归档。

4. **可视化界面**  
   - Web UI（HTML/JavaScript）提供仪表盘、流量表格、地图、热力图等。  
   - 通过 CSS/JS 可定制主题与布局。

5. **告警与报告**  
   - 基于阈值（如带宽 > 80%）或自定义表达式触发告警。  
   - 可生成 PDF、CSV 报告，支持导出为 JSON/XML。

6. **多租户与安全**  
   - RBAC（角色/权限）系统，支持 LDAP、OAuth2。  
   - TLS/HTTPS 加密传输，支持证书管理。

## 四、使用方法

### 1. 环境准备
```bash
# 安装依赖（Ubuntu 示例）
sudo apt-get update
sudo apt-get install -y build-essential cmake libpcap-dev libssl-dev libboost-all-dev \
  libreadline-dev libjsoncpp-dev libsqlite3-dev libcurl4-openssl-dev
```

### 2. 克隆代码 & 编译
```bash
git clone https://github.com/ntop/ntopng.git
cd ntopng
mkdir build && cd build
cmake .. -DNTOPNG_WEBUI=ON -DNTOPNG_WITH_PCAP=ON
make -j$(nproc)
sudo make install
```

### 3. 配置
- **主配置文件**: `/etc/ntopng/ntopng.conf`  
  示例内容：
  ```ini
  -i eth0          # 监听接口
  -w 3000          # Web UI 端口
  -f "capture.pcap"  # pcap 文件（可选）
  -s sqlite:///var/lib/ntopng/ntopng.db  # SQLite 存储
  -p 3000          # 监听端口
  -T 0            # 不使用代理
  ```
- **用户密码**:
  ```bash
  sudo ntopng --create-admin-password
  ```

### 4. 运行
```bash
sudo ntopng
```
访问 `http://localhost:3000` （或配置的 IP + 端口）登录。

### 5. 常用命令行参数
| 参数 | 说明 |
|------|------|
| `-i` | 指定监听网卡 |
| `-p` | 监听端口 |
| `-w` | Web UI 端口 |
| `-s` | 数据库连接字符串 |
| `-F` | 开启流量抓包 |
| `--help` | 显示帮助信息 |

### 6. API 使用示例（curl）
```bash
# 获取流量统计
curl -u admin:password "http://localhost:3000/api/flows?from=1620000000&to=1620003600"
```

## 五、学习资源
- 官方文档: https://www.ntop.org/guides/ntopng/
- 示例配置: https://github.com/ntop/ntopng/tree/master/etc
- 社区支持: https://github.com/ntop/ntopng/discussions

---
> **提示**：在生产环境中建议使用 HTTPS、LDAP 或 OAuth 进行身份认证，并开启告警通知以实时监控网络安全。
