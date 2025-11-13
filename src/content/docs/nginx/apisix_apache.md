---
title: apisix
---

# APISIX

> **GitHub 项目地址**  
> https://github.com/apache/apisix

## 简介

Apache APISIX 是一款轻量、高性能、可插拔的云原生 API 网关。它基于 Nginx/Stream Server 与 Lua 开发，支持动态配置、流量控制、边缘缓存、服务治理等功能，面向微服务架构、服务网格与边缘计算场景。

## 主要特性

- **All platforms**: Cloud-Native, Platform agnostic, No vendor lock-in, APISIX API Gateway can run from bare-metal to Kubernetes.
- **Multi protocols**: TCP/UDP Proxy, Dubbo Proxy, MQTT Proxy, gRPC proxy, gRPC Web Proxy, gRPC transcoding, Proxy Websocket, Proxy Protocol, HTTP(S) Forward Proxy, SSL, HTTP/3 with QUIC.
- **Full Dynamic**: Hot Updates And Hot Plugins, Proxy Rewrite, Response Rewrite, Dynamic Load Balancing, Health Checks, Circuit-Breaker, Proxy Mirror, Traffic Split.
- **Fine-grained routing**: Supports full path matching and prefix matching, Support all Nginx built-in variables as conditions for routing, Support various operators as judgment conditions for routing, IPv6, Support TTL, Support priority, Support Batch Http Requests, Support filtering route by GraphQL attributes.
- **Security**: Rich authentication & authorization support (key-auth, JWT, basic-auth, wolf-rbac, casbin, keycloak, casdoor), IP Whitelist/Blacklist, Referer Whitelist/Blacklist, IdP, Limit-req, Limit-count, Limit-concurrency, Anti-ReDoS, CORS, URI Blocker, Request Validator, CSRF.
- **OPS friendly**: Zipkin tracing, Open source APM (Apache SkyWalking), Works with external service discovery (etcd, Consul, Consul_kv, Nacos, Eureka, Zookeeper), Monitoring And Metrics (Prometheus), Clustering, High availability, Dashboard, Version Control, CLI, Standalone, Global Rule, High performance, Fault Injection, REST Admin API, External Loggers (HTTP Logger, TCP Logger, Kafka Logger, UDP Logger, RocketMQ Logger, SkyWalking Logger, Alibaba Cloud Logging(SLS), Google Cloud Logging, Splunk HEC Logging, File Logger, SolarWinds Loggly Logging, TencentCloud CLS), ClickHouse, Elasticsearch, Datadog, Helm charts, HashiCorp Vault.
- **Highly scalable**: Custom plugins, Plugin can be written in Java/Go/Python, Custom load balancing algorithms, Custom routing.
- **Multi-Language support**: Apache APISIX is a multi-language gateway for plugin development and provides support via RPC and Wasm.
- **Serverless**: Lua functions, AWS Lambda, Azure Functions, Apache OpenWhisk.

## 主要功能

APISIX API Gateway provides rich traffic management features such as load balancing, dynamic upstream, canary release, circuit breaking, authentication, observability, and more.

APISIX can serve as an AI Gateway through its flexible plugin system, providing AI proxying, load balancing for LLMs, retries and fallbacks, token-based rate limiting, and robust security to ensure the efficiency and reliability of AI agents. APISIX also provides the mcp-bridge plugin to seamlessly convert stdio-based MCP servers to scalable HTTP SSE services.

## 快速上手

1. Installation: Please refer to [install documentation](https://apisix.apache.org/docs/apisix/installation-guide/).

2. Getting started: The getting started guide is a great way to learn the basics of APISIX. Just follow the steps in [Getting Started](https://apisix.apache.org/docs/apisix/getting-started/).

3. Admin API: Apache APISIX provides [REST Admin API](https://apisix.apache.org/docs/apisix/admin-api.md) to dynamically control the Apache APISIX cluster.

4. Plugin development: You can refer to [plugin development guide](https://apisix.apache.org/docs/apisix/plugin-develop.md), and sample plugin `example-plugin`'s code implementation. Reading [plugin concept](https://apisix.apache.org/docs/apisix/terminology/plugin.md) would help you learn more about the plugin.

## 代码目录结构概览

```
apisix/
├─ api/        # 管理 API
├─ conf/       # 默认配置文件
├─ core/       # 核心功能实现
├─ plugins/    # 插件 ui/         # Web 控制台
├─ docs/       # 文档
└─ etcd/       # etcd 配置与资源
```

## 社区与支持

- **邮件列表**：apisix-dev@apache.org
- **钉钉/Slack**：Apache APISIX 官方讨论组
- **官网**：https://apisix.apache.org
- **技术博客**：httpsapisix.apache.org/blog

以上即为 Apache APISIX 的核心特性、功能与基本使用方法。祝你使用愉快！
