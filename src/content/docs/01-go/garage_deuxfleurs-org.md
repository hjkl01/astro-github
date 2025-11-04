
---
title: garage
---

# Garage – deuxfleurs-org/garage

[Project on GitHub](https://github.com/deuxfleurs-org/garage)

## 概述  
Garage 是一个轻量级的车库管理与诊断框架，提供统一的数据采集、存储与可视化接口，支持多种传感器协议（CAN、OBD‑II、MQTT 等）以及插件化扩展。

## 主要功能  

- **多协议支持**：内置 CAN、OBD‑II、UART、I²C 等总线驱动，可通过插件添加新协议。  
- **实时数据采集**：从车辆系统实时读取信息，可写入文件、InfluxDB、PostgreSQL、Redis 等后端。  
- **统一 API**：REST/​WebSocket 接口提供车辆状态查询、命令下发和实时推送。  
- **插件系统**：插件可实现自定义解析器、过滤器、告警规则，使用 YAML 或 TypeScript 定义。  
- **CLI 工具**：`garage-cli` 支持设备扫描、协议识别、调试日志打印等操作。  
- **Dashboard**：基于 Grafana 的仪表盘模板，直接部署即可查看实时车况。  

## 使用方法  

```bash
# 克隆仓库
git clone https://github.com/deuxfleurs-org/garage.git
cd garage

# 安装依赖
npm ci

# 配置文件示例 config.yaml
# 参考 docs/config.md

# 启动服务
npm run start

# 访问 API
curl http://localhost:8080/api/vehicle/status
```

### 插件添加步骤  
1. 在 `plugins/` 目录下创建插件文件，例如 `plugins/custom.plugin.ts`。  
2. 在 `config.yaml` 的 `plugins` 节点添加路径。  
3. 重启服务即可生效。  

## 配置示例  

```yaml
server:
  host: 0.0.0.0
  port: 8080

database:
  type: influxdb
  url: http://localhost:8086
  bucket: garage

plugins:
  - ./plugins/custom.plugin.ts
```

## 贡献  
请先阅读 `CONTRIBUTING.md`，提 issue 或 PR。项目使用 TypeScript 编写，保持 lint 通过即可提交。