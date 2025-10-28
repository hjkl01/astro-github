
---
title: loggie
---

# Loggie 项目

**GitHub 项目地址:** [https://github.com/loggie-io/loggie](https://github.com/loggie-io/loggie)

## 主要特性

Loggie 是一个轻量级、高性能的数据采集和处理框架，专为云原生环境设计。主要特性包括：

- **高性能管道处理**：支持高效的数据采集、转换和转发，使用 Go 语言实现，适用于大规模日志和事件数据。
- **云原生支持**：无缝集成 Kubernetes、Docker 等容器化环境，支持动态配置和自动发现。
- **插件化架构**：模块化设计，提供丰富的输入（Sources）、处理（Processors）和输出（Sinks）插件，便于扩展和自定义。
- **数据转换与过滤**：内置多种处理器，支持日志解析、过滤、聚合、路由等操作，提高数据质量。
- **可靠性与容错**：内置重试机制、缓冲区管理和错误处理，确保数据不丢失。
- **监控与可观测性**：集成 Prometheus 和其他监控工具，提供详细的指标和日志，便于运维。
- **轻量级部署**：二进制部署，无需外部依赖，资源占用低，适合边缘计算和微服务场景。

## 主要功能

Loggie 的核心功能围绕数据管道构建，涵盖从采集到输出的全流程：

- **数据采集**：支持多种来源，如文件、Syslog、Kafka、HTTP 等，实时捕获日志和指标。
- **数据处理**：通过处理器进行解析（JSON、Grok 等）、过滤（条件匹配）、增强（添加元数据）和转换（格式化）。
- **数据路由与输出**：支持多路输出到 Elasticsearch、Kafka、Loki、HTTP 等目标，支持负载均衡和备份。
- **配置管理**：使用 YAML 配置，支持热加载和 Kubernetes ConfigMap 集成。
- **安全特性**：支持 TLS 加密、认证和访问控制，确保数据传输安全。
- **扩展性**：用户可开发自定义插件，适应特定业务需求。

## 用法

### 安装

1. **二进制下载**：从 GitHub Releases 下载最新版本的 Loggie 二进制文件。
   ```bash
   wget https://github.com/loggie-io/loggie/releases/download/vX.Y.Z/loggie_linux_amd64.tar.gz
   tar -xzf loggie_linux_amd64.tar.gz
   sudo mv loggie /usr/local/bin/
   ```

2. **Docker 部署**：
   ```bash
   docker pull loggieio/loggie:latest
   docker run -d --name loggie -p 8080:8080 loggieio/loggie:latest
   ```

3. **Kubernetes 部署**：使用 Helm Chart 或 YAML  manifests 部署，支持 DaemonSet 模式采集节点日志。

### 配置与运行

Loggie 使用 `loggie.yaml` 配置文件定义管道。基本结构如下：

```yaml
loggie:
  version: v1.0.0
  pipelines:
    - name: default
      sources:
        - type: file
          name: file-source
          paths: ["/var/log/*.log"]
      processors:
        - type: jsonParser
          name: json-parser
      sinks:
        - type: es
          name: es-sink
          hosts: ["http://elasticsearch:9200"]
          index: loggie-%{+yyyy.MM.dd}
```

- **运行命令**：
  ```bash
  loggie -c loggie.yaml
  ```

- **验证**：访问 HTTP 端点 `http://localhost:8080/metrics` 查看指标，或使用 `loggie --help` 查看更多选项。

### 示例用法

1. **简单日志采集**：配置文件源采集 `/var/log/app.log`，解析 JSON 并输出到 Kafka。
2. **Kubernetes 日志**：部署为 DaemonSet，采集 Pod 日志并路由到中央日志系统。
3. **自定义插件**：参考文档编写 Go 插件，实现特定过滤逻辑。

更多详情请参考 [官方文档](https://github.com/loggie-io/loggie/blob/main/README_cn.md)。