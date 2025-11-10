---
title: hertzbeat
---

# HertzBeat 项目介绍

## 项目地址
[GitHub 项目地址](https://github.com/dromara/hertzbeat/blob/master/README_CN.md)

## 主要特性
HertzBeat 是一个开源的时间序列监控告警系统，基于 Spring Boot 开发，支持实时采集、存储和展示监控数据。主要特性包括：
- **多维监控支持**：内置 200+ 种监控模板，覆盖云原生、数据库、网络设备、中间件、OS 等多种监控场景。
- **插件化设计**：采用 YAML 配置驱动的插件式架构，便于扩展和自定义监控指标。
- **高性能存储**：支持 InfluxDB、Prometheus 等时序数据库，高效处理海量数据。
- **告警机制**：集成多种告警渠道，如邮件、钉钉、企业微信、Webhook 等，支持阈值告警和异常检测。
- **可视化仪表盘**：提供 Grafana 集成和内置 Web UI，支持自定义图表和仪表盘。
- **易部署**：支持 Docker 一键部署，低资源占用，适合中小型企业使用。
- **开源社区**：基于 Apache 2.0 许可，活跃社区维护，兼容 Prometheus 生态。

## 主要功能
- **监控采集**：通过 Yml 模板定义指标采集规则，支持 JMX、SNMP、HTTP、SSH 等协议采集数据。
- **数据存储与查询**：集成时序数据库，实现数据持久化和高效查询。
- **监控管理**：支持监控主机/服务的添加、编辑、删除，以及标签和分组管理。
- **告警配置**：设置监控阈值、告警规则和通知渠道，实现自动化告警。
- **报告与分析**：生成监控报告，支持历史数据回溯和趋势分析。
- **API 接口**：提供 RESTful API，便于集成到其他系统中。
- **安全性**：内置用户认证、角色权限控制，支持 HTTPS 和数据加密。

## 用法
### 1. 环境准备
- Java 环境：JDK 8+。
- 数据库：可选 InfluxDB 或 Prometheus（默认内置 H2 数据库用于测试）。
- 网络：确保监控目标可访问。

### 2. 快速部署
- **Docker 部署**（推荐）：
  ```
  docker run -d -p 1157:1157 -p 1158:1158 --name hertzbeat dromara/hertzbeat
  ```
  访问 Web UI：http://localhost:1157，初始用户名/密码：admin/hertzbeat。

- **源码部署**：
  1. 克隆仓库：`git clone https://github.com/dromara/hertzbeat.git`。
  2. 进入目录：`cd hertzbeat`。
  3. 构建：`mvn clean package -DskipTests`。
  4. 运行：`java -jar hertzbeat-web/target/hertzbeat-web.jar`。
  访问：http://localhost:1157。

### 3. 使用步骤
- **登录系统**：使用默认账号登录 Web 界面。
- **添加监控**：
  1. 进入“监控管理” > “新增监控”。
  2. 选择监控类型（如 Ping、HTTP、MySQL 等）。
  3. 配置目标主机、端口、认证信息。
  4. 应用模板或自定义 Yml 配置。
  5. 保存并测试采集。
- **配置告警**：
  1. 在监控详情中设置阈值规则（如 CPU > 80%）。
  2. 添加告警通知（如邮件服务器配置）。
  3. 启用告警，系统将自动触发通知。
- **查看数据**：
  - 在“监控列表”查看实时状态和图表。
  - 使用“仪表盘”自定义视图。
  - 通过 API 查询数据：`/api/v1/metrics/query?metric=xxx`。
- **扩展插件**：
  - 编辑 `hertzbeat-collector/src/main/resources/metric.yml` 添加自定义模板。
  - 重启服务生效。

### 4. 高级用法
- **集成 Grafana**：配置数据源为 HertzBeat 的 Prometheus 端点（:1158）。
- **集群部署**：使用 Docker Compose 或 Kubernetes，支持多实例高可用。
- **API 文档**：访问 Web UI 的 API 页面或 Swagger 接口。
- **常见问题**：参考官方文档 troubleshooting 部分，常见如端口冲突或数据库连接失败。

更多详情请参考项目 README。