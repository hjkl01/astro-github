
---
title: proxypin
---

# Proxypin 项目

**项目地址：** [https://github.com/wanghongenpin/proxypin](https://github.com/wanghongenpin/proxypin)

## 主要特性
Proxypin 是一个开源的代理工具项目，专注于提供高效的代理管理和网络流量转发功能。主要特性包括：
- **多协议支持**：兼容 HTTP、HTTPS、SOCKS4/SOCKS5 等常见代理协议，支持自定义协议扩展。
- **高性能转发**：基于高效的异步 I/O 实现，低延迟代理转发，适用于高并发场景。
- **负载均衡**：内置负载均衡机制，可自动分配流量到多个上游代理服务器，提高稳定性和可用性。
- **安全加密**：支持 TLS/SSL 加密传输，保护数据隐私；可选的身份验证机制防止未授权访问。
- **配置灵活**：通过 YAML 或 JSON 配置文件管理，支持热重载无需重启服务。
- **监控与日志**：集成实时监控仪表盘和详细日志记录，便于调试和性能分析。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 系统，易于部署。

## 主要功能
- **代理服务器搭建**：快速部署本地或远程代理服务器，实现网络流量中转。
- **规则路由**：基于域名、IP 或路径的智能路由规则，支持分流和黑白名单。
- **隧道模式**：提供 SSH 隧道或 VPN-like 的隧道功能，用于安全访问受限网络。
- **API 接口**：RESTful API 支持动态管理代理节点、查询状态等。
- **插件扩展**：模块化设计，支持用户自定义插件，如流量统计或过滤器。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/wanghongenpin/proxypin.git`
   - 进入目录：`cd proxypin`
   - 安装依赖（以 Go 为例）：`go mod download`
   - 构建：`go build -o proxypin`

2. **配置**：
   - 编辑 `config.yaml` 文件，例如：
     ```
     server:
       listen: ":8080"
       upstreams:
         - url: "socks5://example.com:1080"
           weight: 1
     rules:
       - domain: "*.example.com"
         proxy: "upstream1"
     ```
   - 支持命令行参数覆盖配置：`./proxypin -config config.yaml -port 8080`

3. **运行**：
   - 启动服务：`./proxypin`
   - 测试代理：使用浏览器或 curl 设置代理为 `127.0.0.1:8080`，访问目标网站。
   - 停止：Ctrl+C 或发送 SIGTERM 信号。

4. **高级用法**：
   - 部署到 Docker：使用提供的 Dockerfile 构建镜像，运行 `docker run -p 8080:8080 proxypin`。
   - 监控：访问 `http://localhost:8080/metrics` 查看指标。
   - 更多细节请参考项目 README 和示例配置。