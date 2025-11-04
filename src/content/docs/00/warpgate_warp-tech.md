
---
title: warpgate
---

以下为可直接保存至 `src/content/docs/00/warpgate_warp-tech.md` 的 Markdown 内容：

```markdown
# Warpgate（WarpTech）

## 项目地址
[https://github.com/warp-tech/warpgate](https://github.com/warp-tech/warpgate)

## 主要特性  
| 关键特性 | 简介 |
| --- | --- |
| **基于 Cloudflare WARP** | 利用 Cloudflare WARP 网络实现高性能、低延迟的 VPN 通道。 |
| **轻量级 Gateway** | 只需一条命令即可启动，资源占用极低，适合 Docker 容器部署。 |
| **多租户支持** | 通过配置文件或环境变量对不同用户/客户端进行分配和隔离。 |
| **自定义路由** | 提供可编辑的路由策略，支持 CIDR、子域、协议等多维度路由决策。 |
| **Web 状态面板** | 内置 HTTP 接口，可实时展示状态、日志、流量统计，支持 Grafana/Prometheus 采集。 |
| **DNS 解析拦截** | 自动拦截 DNS 请求，支持自定义 DNS 服务器与域名过滤列表。 |
| **安全加固** | TLS 加密、IP 白名单、访问令牌等机制，保证数据传输安全。 |
| **跨平台** | 支持 Linux、BSD、macOS（通过 Docker 或直接 binary）等平台。 |

## 核心功能  
1. **WARP Tunnel 创建**  
   - 自动使用 Cloudflare 账号或 API Token 初始化 WARP tunnel。  
2. **本地代理/隧道**  
   - 监听指定端口，将客户端流量通过 WARP tunnel 转发至目标服务器。  
3. **网络策略管理**  
   - 基于配置文件制定 `whitelist`、`blacklist`、`split-tunneling` 等多种策略。  
4. **日志与监控**  
   - 支持标准日志输出、JSON 日志格式、以及 Prometheus 导出。  
5. **健康检查**  
   - 通过 `/health` 或 `/metrics` 接口提供健康状态，方便集成 CI/CD、Kubernetes liveness probes。  

## 使用方法  

### 1. Docker 安装（推荐）
```bash
docker run -d \
  --name warpgate \
  -p 0.0.0.0:8080:8080 \        # Web 面板 & 健康检查端口
  -p 0.0.0.0:8443:8443 \        # 可选：TLS 代理端口
  -v /path/to/config:/app/config \
  --restart unless-stopped \
  warp-tech/warpgate:latest
```
> `config.yaml` 示例：  
> ```yaml
> warp_token: "YOUR_WARP_API_TOKEN"
> listen_address: "0.0.0.0"
> listen_port: 8080
> routes:
>   - cidr: "0.0.0.0/0"
>     next_hop: "warp"
> ```

### 2. 直接 Binary 安装
```bash
# 下载
wget https://github.com/warp-tech/warpgate/releases/download/vX.Y.Z/warpgate-linux-amd64.tar.gz
tar -xzf warpgate-linux-amd64.tar.gz
cd warpgate-linux-amd64

# 运行
./warpgate --config /path/to/config.yaml
```

### 3. 运行参数
| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `--config` | string | `./config.yaml` | 配置文件路径 |
| `--metrics-addr` | string | `0.0.0.0:9100` | Prometheus metrics 输出地址 |
| `--log-level` | string | `info` | 日志级别（debug, info, warn, error） |
| `--bind-addr` | string | `0.0.0.0` | 监听地址 |
| `--bind-port` | int | `8080` | 监听端口 |

### 4. 常见命令行示例
```bash
# 开启调试日志
./warpgate --log-level debug

# 指定分离路由
./warpgate --config custom.yaml

# 启用 TLS
./warpgate --tls-cert /etc/ssl/cert.pem --tls-key /etc/ssl/key.pem
```

## 配置示例

```yaml
# config.yaml
warp_token: "YOUR_WARP_API_TOKEN"
listen:
  address: "0.0.0.0"
  port: 8080
tls:
  cert: "/etc/ssl/cert.pem"
  key: "/etc/ssl/key.pem"
routes:
  - cidr: "10.0.0.0/8"
    type: "warp"          # 通过 WARP
  - cidr: "172.16.0.0/12"
    type: "direct"        # 直连
  - cidr: "0.0.0.0/0"
    type: "warp"          # 默认走 WARP
dns:
  server: "1.1.1.1"
  blocklist:
    - "ads.example.com"
    - "tracker.example.org"
```

## 常见问题

| 问题 | 解答 |
| --- | --- |
| **如何获取 Cloudflare WARP API Token？** | 登录 Cloudflare Dashboard → "My Profile" → "API Tokens" → 创建自定义 Token 并勾选 `Warp` 权限。 |
| **启动后出现连接失败？** | 检查 `warp_token` 是否正确，确认网络可访问 Cloudflare。 |
| **如何查看实时流量？** | 访问 `http://<host>:8080/metrics` 或 `http://<host>:8080/health`。 |

---  

**License**：MIT  
**Author**：WarpTech
