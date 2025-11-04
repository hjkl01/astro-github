
---
title: ai-gateway
---


# Envoy AI Gateway

**项目地址**：<https://github.com/envoyproxy/ai-gateway>

## 项目简介
Envoy AI Gateway 是一个基于 Envoy 的 AI 请求网关，旨在帮助用户安全、高效地将前端请求路由到大语言模型（LLM），并对请求/响应进行智能转换、监控与安全过滤。它提供了可插拔的请求处理器、动态配置与高可靠性的一站式服务。

## 主要特性
- **多模型支持**：内置对 OpenAI、Amazon Bedrock、Azure OpenAI、HuggingFace 等主流 LLM 的代理与转发能力。
- **请求 & 响应转换**：可根据业务需求自定义请求体映射、参数补全、后缀附加等操作，实现与目标模型的无缝对接。
- **安全与合规**：内置 OpenAI Moderation、内容过滤、速率限制、API Key/Token 校验等安全功能，满足合规需求。
- **动态配置**：通过 Envoy 的 xDS API 或 YAML 配置文件，实时更新路由、插件、策略等，零停机升级。
- **可观测性**：默认收集 Prometheus 指标，支持 OpenTracing、Jaeger 等分布式追踪；日志可直接输出到 stdout 或配置的日志后端。
- **可扩展插件**：提供丰富的过滤器接口，支持自定义插件编写（Go/Python/C++ 等），满足特殊业务场景。
- **高性能部署**：利用 Envoy 的高性能、低延迟特性，实现大并发下的高吞吐网络层服务。

## 关键功能模块
| 模块 | 说明 |
|------|------|
| **Routing** | 基于 VirtualService 与 VirtualRoute 的路由匹配，实现模型多租户与流量分配。 |
| **Transforms** | `RequestTransform` 与 `ResponseTransform`，可对请求/响应进行 JSON 结构改造、字段替换、密钥注入等。 |
| **Security** | `AuthFilter`、`RateLimitFilter`、`ContentModerationFilter` 等，合规与安全保障。 |
| **Observability** | `MetricsFilter`、`TracingFilter` 结合 Envoy 原生插件，自动生成指标与链路追踪。 |
| **Dynamic Config** | `Envoy Gateway` 的 xDS 控制平面，支持热部署的动态路由与插件配置。 |
| **Extensibility** | SDK 和插件模板，支持 Python/Go/C++ 自定义业务扩展。 |

## 快速上手

1. **克隆仓库**  
   ```bash
   git clone https://github.com/envoyproxy/ai-gateway.git
   cd ai-gateway
   ```

2. **准备 Envoy 配置**  
   - 参照 `config/envoy.yaml` 或 `config/envoy-gateway.yaml` 进行适配。  
   - 修改 `static_cluster` 或 `dynamic_cluster`，指向目标 AI 服务端点。  
   - 根据需要在 YAML 中添加 `request_transform`, `response_transform`, `auth_filter`, `rate_limit` 等配置。  

3. **运行 Docker Compose（示例）**  
   ```bash
   docker compose up -d
   ```  
   Docker Compose 会启动 Envoy、Prometheus、Grafana、Jaeger 等监控组件，方便快速验证功能。

4. **访问 Gateway**  
   - 通过 `http://localhost:10000/api/chat`（或自定义路径）发送请求，Envoy 将自动路由、转换并返回 LLM 响应。  
   - 检查 Prometheus 指标，或在 Grafana 仪表盘查看实时监控。

5. **动态更新配置**  
   - 修改配置文件后，直接 reload Envoy：  
     ```bash
     docker exec envoy-envoyproxy envoy --service-node <node-id> --service-cluster <cluster-id> --config-yaml <path-to-config>
     ```  
   - 或使用 Envoy xDS 控制台 push 新配置。

## 参考文档
- [官方文档](https://github.com/envoyproxy/ai-gateway/blob/main/README.md)  
- [示例配置](https://github.com/envoyproxy/ai-gateway/tree/main/config)  
- [插件开发教程](https://github.com/envoyproxy/ai-gateway/blob/main/docs/extensions.md)

---
