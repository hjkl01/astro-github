---
title: Telegraf
---

# Telegraf

## 功能

Telegraf 是一个用于收集、处理、聚合和写入指标、日志和其他任意数据的代理。

- 提供超过300个插件的综合套件，涵盖系统监控、云服务和消息传递等广泛功能。
- 允许集成用户定义的代码来高效收集、转换和传输数据。
- 编译成独立的静态二进制文件，没有外部依赖，确保简化的部署过程。
- 使用TOML进行配置，提供用户友好且明确的设置体验。
- 由超过1200名贡献者的多元化社区开发。

插件类别包括：

- **设备**：OPC UA, Modbus
- **日志**：File, Tail, Directory Monitor
- **消息传递**：AMQP, Kafka, MQTT
- **监控**：OpenTelemetry, Prometheus
- **网络**：Cisco TelemetryMDT, gNMI
- **系统监控**：CPU, Memory, Disk, Network, SMART, Docker, Nvidia SMI 等。
- **通用**：Exec, HTTP, HTTP Listener, SNMP, SQL
- **Windows**：Event Log, Management Instrumentation, Performance Counters

## 用法

用户定义一个TOML配置文件，其中包含他们希望使用的插件和设置，然后将该配置传递给Telegraf。Telegraf代理然后在每个间隔从输入收集数据，并在每个刷新间隔将数据发送到输出。

### 基本步骤

1. **安装Telegraf**：参考[安装指南](https://github.com/influxdata/telegraf/blob/master/docs/INSTALL_GUIDE.md)，支持二进制构建、Docker镜像、RPM & DEB包等。
2. **创建配置文件**：使用TOML格式定义输入插件（收集数据）、处理器插件（处理数据）、聚合器插件（聚合数据）和输出插件（写入数据）。
3. **运行Telegraf**：使用命令 `telegraf --config <config_file>` 启动代理。

更多详情请参考[快速开始指南](https://github.com/influxdata/telegraf/blob/master/docs/QUICK_START.md)和[配置文档](https://github.com/influxdata/telegraf/blob/master/docs/CONFIGURATION.md)。
