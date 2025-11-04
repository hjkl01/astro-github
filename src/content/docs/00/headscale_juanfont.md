
---
title: headscale
---

# headscale - `juanfont/headscale`

> 项目地址: https://github.com/juanfont/headscale

## 项目概述
`headscale` 是一个开源的 Tailscale 控制服务器实现，基于 WireGuard。它允许用户在私有网络中快速构建安全、加密的 VPN 网络，支持多平台（Linux、macOS、Windows）以及多种部署方式。

## 主要
- **Tailscale 兼**：完全兼容官方 Tailscale 客户端，支持相同的认证、授权和网络管理。
- **自托管**：无需依赖 Tailscale 官方服务，可在自己的服务器或云主机部署。
- **简易配置**：采用单个 YAML 文件 (`headscale.yaml`) 进行配置；使用 `sqlite` 或 `postgres` 存储后端。
- **自动 NAT 穿透**：通过 WireGuard 暗网让节点实现直接互联，无需手动配置端口映射。
- **多用户管理**：支持用户、组织、实例、ACL 等层级权限模型。
- **多种身份验证方式**：支持 OAuth（Google、GitHub）、密码、硬件密钥（YubiKey）、简单的令牌等。
- **负载均衡**：可配置多台 `headscale` 节点，实现高可用和负载均衡。
- **日志与监控**：支持 JSON 日志、Prometheus 指标导出，易于集成监控系统。

## 快速使用

1. **获取源码**

   ```bash
   git clone https://github.com/juanfont/headscale
   cd headscale
   ```

2. **编译**

   ```bash
   make
   ```

3. **配置文件**

   创建 `headscale.yaml`（示例）：

   ```yaml
   listen_addr: ":8080"
   storage_type: "sqlite"
   sqlite_database_path: "headscale.db"
   base_url: "https://your.headscale.domain"
   trusted_proxies: []
   ```

4. **启动**

   ```bash
   ./headscale start
   ```

5. **生成访问令牌**

   在管理界面或 CLI 生成访问令牌，配合 Tailscale 客户端使用 `sudo tailscale up --authkey <TOKEN> --hostname <YOUR_HOSTNAME>`。

6. **配置客户端**

   ```bash
   sudo tailscale up \
       --auth-key <YOUR_AUTH_KEY> \
       --hostname <NAME> \
       --backend-service <YOUR_HEADSCALE_SERVICE> \
       --advertise-routes 10.0.0.0/24
   ```

7. **管理与监控**

   - 访问 HTTPS 控制面板（`https://your.headscale.domain`）查看节点状态、配置 ACL、查看日志。
   - 可将日志输出到 Prometheus，利用 Grafana 进行可视化。

## 常见命令

```bash
# 启动服务（后台）
./headscale start

# 停止服务
./headscale stop

# 生成服务器配置文件示例
./headscale generate-config

# 查看版本
./headscale version
```

## 许可证
MIT 许可证 – 详见项目根目录下的 `LICENSE` 文件。