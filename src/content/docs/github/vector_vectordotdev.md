
---
title: vector
---

# Vector

> 项目地址: [https://github.com/vectordotdev/vector](https://github.com/vectordotdev/vector)

## 概述
Vector 是由 Vector.dev 开发的高性能、可扩展的日志、指标和事件收集与转发器。它能够从多种来源（文件、系统、应用程序等）收集数据，并将其发送到多种后端（Elasticsearch、Kafka、CloudWatch 等）进行存储、分析和监控。

## 主要特性
- **高吞吐量**：使用 Rust 编写，能够处理每秒数百万事件。
- **零拷贝**：避免不必要的数据复制，降低 CPU 与内存占用。
- **插件化架构**：支持输入、处理器、输出等插件，易于扩展。
- **事件路由**：基于字段匹配、正则、JSONPath 等多种规则路由事件。
- **动态配置**：支持热更新配置，无需重启即可变更规则。
- **安全**：支持 TLS、OAuth、Kerberos 等多种身份验证与加密方式。
- **可观测性**：内置指标与日志，支持 Prometheus、Grafana 等监控工具。
- **跨平台**：支持 Linux、macOS、Windows。

## 安装方式
```bash
# 通过官方 Docker 镜像
docker run -d --name vector \
  -p 8686:8686 \
  -v $(pwd)/config/vector.yaml:/etc/vector/vector.yaml \
  timberio/vector:latest

# 通过 Homebrew（macOS）
brew install timberio/vector

# 通过二进制包
curl -Lo vector.tar.gz https://github.com/vectordotdev/vector/releases/download/v0.36.0/vector-0.36.0-x86_64-linux.zip
tar -xzf vector.tar.gz
./vector
```

## 基本配置示例 (`vector.yaml`)
```yaml
sources:
  syslog:
    type: syslog
    address: 0.0.0.0:5140
    format: rfc5424

sinks:
  elasticsearch:
    type: elasticsearch
    inputs: [syslog]
    endpoint: https://elasticsearch.example.com:9200
    auth:
      username: elastic
      password: changeme
    index: "vector-{{ year }}-{{ month }}-{{ day }}"
```

## 用法
1. **启动 Vector**  
   ```bash
   vector -c vector.yaml
   ```
2. **查看日志**  
   Vector 会将自身日志输出到标准输出，或根据配置写入文件。
3. **热更新配置**  
   修改 `vector.yaml` 并触发 SIGHUP：
   ```bash
   pkill -SIGHUP vector
   ```
4. **监控**  
   Vector 通过 `metrics` sink 暴露 Prometheus 指标，访问 `http://localhost:8686/metrics`。

## 常用命令
- 查看版本：`vector --version`
- 检查配置合法性：`vector --config-check vector.yaml`
- 启动调试模式：`vector --debug -c vector.yaml`

## 参考文档
- 官方文档: https://vector.dev/docs
- 配置参考: https://vector.dev/docs/reference/configuration
- 插件列表: https://vector.dev/docs/reference/plugins

---