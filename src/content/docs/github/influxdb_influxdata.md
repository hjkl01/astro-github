---
title: influxdb
---


# InfluxDB（InfluxData）

> 项目地址: <https://github.com/influxdata/influxdb>

## 一、项目概述  
InfluxDB 是一款专为时序数据（Time‑Series Data）设计的高性能数据库。它支持海量数据写入、即时查询、持久化存储，并提供多种查询语言与 RESTful API，适用于监控、物联网、实时分析等场景。

## 二、主要特性  

| 特性 | 说明 |
|------|------|
| **高吞吐量写入** | 采用列式存储 + 预分配内存，支持每秒百万条写入 |
| **高效查询** | 内置 InfluxQL（SQL 语法）和 Flux（功能更强的查询语言） |
| **数据保留与压缩** | Retention Policies、Shard Groups、Continuous Queries、Downsampling |
| **多时区 & 时序聚合** | 支持时区转换、窗口聚合、滑动窗口、离散聚合等 |
| **多协议写入** | Line Protocol（文本）、TCP、UDP、HTTP、InfluxDB Client Libraries |
| **持久化 & 复制** | 内置 WAL、磁盘压缩、TSM (Time‑Series Merge) 存储引擎 |
| **集成生态** | Telegraf（收集器）、Chronograf（UI）、Kapacitor（流程引擎） |
| **安全 & 权限** | 用户认证、基于角色的访问控制 (RBAC) |
| **可扩展** | 轻量级集群模式、水平扩展（Clustered） |

## 三、核心功能  

1. **写入（Write）**  
   - 通过 Line Protocol 或 HTTP API 写入单条或批量时序点。  
   - 示例（Line Protocol）:  
     ```text
     temperature,location=room1 value=23.5 1633024800000000000
     ```

2. **查询（Query）**  
   - **InfluxQL**（类似 SQL）:  
     ```sql
     SELECT mean("value") FROM "temperature" WHERE time > now() - 1h GROUP BY time(10m)
     ```
   - **Flux**（更灵活）:  
     ```javascript
     from(bucket:"sensors")
       |> range(start: -1h)
       |> filter(fn: (r) => r._measurement == "temperature")
       |> aggregateWindow(every: 10m, fn: mean)
     ```

3. **数据保留与压缩**  
   - 设置 Retention Policy（保留周期）和 Continuous Query（持续查询）实现自动 downsampling。  
   - 通过 TSM 存储引擎实现磁盘压缩。

4. **集成与扩展**  
   - **Telegraf**：插件化收集器，支持多种数据源。  
   - **Chronograf**：Web UI，提供可视化查询、仪表盘。  
   - **Kapacitor**：实时流处理与告警。

5. **安全**  
   - 支持 OAuth、JWT、基本认证。  
   - RBAC：细粒度权限控制。

## 四、使用步骤（示例）  

1. **安装**  
   ```bash
   # 通过二进制包
   wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.7.0-linux-amd64.tar.gz
   tar xzf influxdb2-2.7.0-linux-amd64.tar.gz
   cd influxdb2-2.7.0-linux-amd64
   ./influxd
   ```

2. **写入数据**  
   ```bash
   curl -i -XPOST http://localhost:8086/api/v2/write?org=myorg&bucket=mybucket&precision=ns \
     --data-binary 'temperature,location=room1 value=23.5 1633024800000000000'
   ```

3. **查询数据**  
   ```bash
   curl -G http://localhost:8086/api/v2/query \
     --data-urlencode "q=from(bucket:\"mybucket\") |> range(start: -1h)" \
     -H "Authorization: Token <YOUR_TOKEN>"
   ```

4. **可视化**  
   - 访问 `http://localhost:9090`（Chronograf）创建仪表盘。  
   - 或使用 Grafana 插件 `InfluxDB` 进行展示。

## 五、常见命令行工具  

| 工具 | 用途 |
|------|------|
| `influx` | InfluxDB 交互式 CLI（InfluxQL） |
| `influx` | `influx v1` 兼容模式 |
| `influx` | `influx v2` 兼容模式（Flux） |
| `telegraf` | 数据采集 |
| `kapacitor` | 流处理、告警 |

## 六、总结  
InfluxDB 以其针对时序数据的高效存储与查询能力，成为监控、物联网、实时分析等领域的首选数据库。通过丰富的生态插件和简洁的 API，开发者可以快速构建从数据采集到可视化的完整链路。

> 项目地址: <https://github.com/influxdata/influxdb>
