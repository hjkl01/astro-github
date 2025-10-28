
---
title: logdy-core
---

# Logdy Core 项目概述

## 项目地址
[https://github.com/logdyhq/logdy-core](https://github.com/logdyhq/logdy-core)

## 主要特性
Logdy Core 是一个开源的实时日志处理和传输工具，专为现代 DevOps 和监控环境设计。它支持高效的日志收集、解析、过滤和转发，具有以下核心特性：
- **实时日志流处理**：支持从多种来源（如文件、标准输入、TCP/UDP 等）实时捕获和处理日志数据。
- **多协议支持**：兼容 JSON、Syslog、GELF 等日志格式，并提供自定义解析器。
- **分布式传输**：通过 WebSocket、HTTP、Kafka 等协议实现日志的可靠传输和聚合。
- **轻量级架构**：基于 Rust 开发，性能高、资源占用低，适合容器化和微服务环境。
- **插件化扩展**：允许用户通过 Lua 脚本或自定义模块扩展功能，如数据转换、加密和警报。
- **监控集成**：内置仪表盘和 API 接口，便于与 Prometheus、Grafana 等工具集成。

## 主要功能
- **日志采集**：从本地文件、系统日志、网络流等来源收集日志，支持多路复用输入。
- **数据处理**：实时解析、过滤、丰富日志（如添加元数据、时间戳标准化），并处理异常数据。
- **日志转发**：将处理后的日志推送到 Elasticsearch、Loki、Splunk 等后端存储，或其他 Logdy 实例。
- **安全特性**：支持 TLS 加密、认证和访问控制，确保日志传输的安全性。
- **性能优化**：内置缓冲、压缩和批处理机制，处理高吞吐量日志流。
- **调试工具**：提供命令行界面（CLI）和 Web UI，用于测试配置和监控运行状态。

## 用法
### 安装
1. 通过 Cargo（Rust 包管理器）安装：
   ```
   cargo install logdy
   ```
2. 或从 GitHub Releases 下载预编译二进制文件，支持 Linux、macOS 和 Windows。

### 基本用法
Logdy 使用 YAML 或 TOML 配置文件定义管道（pipeline）。示例配置文件 `logdy.yaml`：
```yaml
input:
  - type: file
    path: /var/log/app.log
    format: json

filter:
  - type: grep
    pattern: "ERROR"

output:
  - type: stdout
  - type: elasticsearch
    host: localhost:9200
    index: logs
```

运行命令：
```
logdy --config logdy.yaml
```

### 高级用法
- **管道链式处理**：在配置文件中串联多个 filter 和 output 模块，例如：
  ```
  input -> parse_json -> filter_level=error -> output_elasticsearch
  ```
- **CLI 模式**：直接从命令行处理日志：
  ```
  logdy --input stdin --output websocket://hub.logdy.io --format json
  ```
- **Docker 部署**：使用官方 Docker 镜像：
  ```
  docker run -v /path/to/logs:/logs logdyhq/logdy --config /config/logdy.yaml
  ```
- **扩展脚本**：使用 Lua 编写自定义过滤器：
  ```lua
  function filter(record)
    if record.level == "debug" then
      return false  -- 过滤掉 debug 日志
    end
    return true
  end
  ```

更多细节请参考项目文档和示例配置。