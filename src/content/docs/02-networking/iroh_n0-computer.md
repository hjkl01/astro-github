
---
title: iroh
---

# Iroh

**项目地址**: [https://github.com/n0-computer/iroh](https://github.com/n0-computer/iroh)

## 主要特性

- **轻量级**：使用 Rust 编写，二进制体积小，启动速度快，适合嵌入式和边缘设备。
- **跨平台**：支持 Linux、macOS、Windows，及多种处理器架构（amd64、arm64、armv7 等）。
- **高并发**：采用异步 I/O（async/await），并发数可达数千，适合高吞吐量网络服务。
- **安全性**：默认开启 TLS/SSL，支持自签证书与证书链校验。
- **插件化**：内置插件系统，可通过插件扩展功能，插件均以可编译字段形式分发。
- **易于运维**：提供 `irohctl` 命令行工具，支持日志管理、配置热 reload、服务状态查询等。

## 核心功能

| 功能 | 说明 |
|------|------|
| **网络代理** | 支持 HTTP/HTTPS 和 SOCKS5 代理，支持透明代理与链路加密。 |
| **服务转发** | 动态配置服务端口，实现端口映射、负载均衡。 |
| **负载均衡** | 基于 IP 哈希或轮询算法实现简单的 L4 负载均衡。 |
| **访问控制** | 通过 ACL 与 JWT 结合进行细粒度访问控制。 |
| **监控集成** | 输出 Prometheus 格式指标，支持自定义 Pushgateway。 |
| **自动化脚本** | 提供脚本接口，可基于 Lua/VimScript 编写自定义业务逻辑。 |

## 安装与使用

### 安装方式

```bash
# 通过 cargo 安装（需要 Rust 1.64+）
cargo install iroh

# 或使用预编译二进制
curl -LO https://github.com/n0-computer/iroh/releases/latest/download/iroh-$(uname)-$(uname -m).tar.gz
tar -xf iroh-*.tar.gz
sudo mv iroh /usr/local/bin
```

### 快速上手

```bash
# 启动 Iroh 并监听本地 8080 端口，转发到远程服务器
iroh proxy --listen 0.0.0.0:8080 --remote example.com:443

# 推送服务端口到内网代理服务器
iroh service --publish 80 --to 0.0.0.0:8080

# 查看当前配置与状态
iroh status
```

### 配置文件

Iroh 支持 `iroh.yaml` 或 `iroh.json` 配置文件。示例（`iroh.yaml`）：

```yaml
listen: 0.0.0.0:8443
remote: example.com:443
protocol: https
tls:
  cert_file: /path/to/cert.pem
  key_file: /path/to/key.pem
logging:
  level: info
plugins:
  - name: auth
    config:
      type: jwt
      secret: "supersecret"
```

直接运行：

```bash
iroh run -c iroh.yaml
```

### 管理命令

| 命令 | 说明 |
|------|------|
| `irohctl status` | 显示当前运行实例状态 |
| `irohctl reload` | 热加载配置文件 |
| `irohctl logs --tail 100` | 查看最新日志 |
| `irohctl plugin list` | 列出已加载插件 |

### 运行示例（完整 pipeline）

1. **准备 TLS 证书**  
   ```bash
   mkcert example.com
   ```
2. **写入配置**  
   保存为 `iroh.yaml`。
3. **运行**  
   ```bash
   iroh run -c iroh.yaml
   ```
4. **验证**  
   在浏览器访问 `https://your.hostname:8443`，应该能通过 Iroh 成功代理到目标服务。

---

如果想了解更详细的功能、插件体系或性能调优，可参阅仓库中的 `docs/` 目录或贡献者指南。祝使用愉快！