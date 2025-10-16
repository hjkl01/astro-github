
---
title: diving
---

# Diving 项目

## 项目地址
[https://github.com/vicanso/diving](https://github.com/vicanso/diving)

## 主要特性
- **高性能代理服务**：基于Go语言开发，支持HTTP、HTTPS和SOCKS5代理协议，提供高效的网络代理功能。
- **负载均衡**：内置负载均衡机制，支持多种算法（如轮询、随机），可将流量分发到多个后端服务器。
- **健康检查**：自动检测后端服务器健康状态，支持HTTP、TCP等多种检查方式，确保流量仅路由到可用服务器。
- **配置灵活**：使用YAML或JSON格式配置文件，支持热加载配置变更，无需重启服务。
- **监控与日志**：集成Prometheus指标暴露，便于监控代理性能；支持详细日志记录，便于调试和审计。
- **安全性**：支持TLS加密、认证机制（如Basic Auth），防止未授权访问。
- **轻量级设计**：无外部依赖，易于部署和扩展，支持Docker容器化。

## 主要功能
- **代理转发**：将客户端请求转发到上游服务器，支持透明代理和自定义路由规则。
- **反向代理**：作为反向代理服务器，处理Web应用流量，支持路径重写、头部修改和压缩。
- **流量控制**：实现限速、限流和连接池管理，防止资源滥用。
- **故障转移**：当后端服务器故障时，自动切换到备用服务器，确保服务高可用。
- **API支持**：提供RESTful API接口，用于动态管理代理配置和查询状态。

## 用法
1. **安装**：
   - 下载预编译二进制文件，或使用Go构建：`go install github.com/vicanso/diving/cmd/diving@latest`。
   - 对于Docker：`docker pull vicanso/diving`。

2. **配置**：
   - 创建配置文件`config.yaml`，示例：
     ```
     listen: ":8080"
     upstreams:
       - name: backend1
         url: "http://127.0.0.1:3000"
         healthCheck: "/health"
     ```
   - 支持命令行参数覆盖配置，如`diving -c config.yaml -l :8080`。

3. **运行**：
   - 启动服务：`diving`（默认使用config.yaml）。
   - 访问代理：通过`http://localhost:8080`发送请求，将被转发到上游。

4. **高级用法**：
   - 热加载：发送SIGHUP信号`kill -HUP <pid>`重新加载配置。
   - 监控：访问`/metrics`端点暴露Prometheus指标。
   - 更多细节参考项目README和示例配置。