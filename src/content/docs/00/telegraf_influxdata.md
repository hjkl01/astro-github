
---
title: telegraf
---


# Telegraf

> GitHub: https://github.com/influxdata/telegraf

## 项目简介
Telegraf 是 InfluxData 生态系统的一部分，专为收集、处理并将指标数据发送到 InfluxDB、Prometheus 等后端而设计的插件化代理。

## 主要特性
- **插件化架构**：支持输入、处理和输出插件，插件可独立安装与升级。
- **高性能**：使用 Go 语言实现，低内存占用、低延迟。
- **跨平台**：兼容 Linux、Windows、macOS、FreeBSD、Solaris 等系统。
- **多种数据源**：内置插件可收集系统指标、Docker、Kubernetes、Redis、MySQL 等多种来源的数据。
- **动态配置**：支持通过 `telegraf.conf` 文件实时修改配置，无需重启。
- **自定义函数**：可通过 `aggregator`、`filter` 等插件自定义数据处理逻辑。

## 功能概览
| 类别 | 说明 |
|------|------|
| **输入插件** | 采集本机或远程主机的系统、服务、应用指标（如 CPU、内存、磁盘、网络、进程、容器等）。 |
| **处理插件** | 对数据进行聚合、过滤、转换、标记、阈值检测等处理。 |
| **输出插件** | 将处理后的数据写入 InfluxDB、Prometheus Pushgateway、OpenTSDB、Kafka、MQTT、Graphite、HTTP、文件等。 |
| **插件扩展** | 通过 `plugin` 机制可自行开发插件，支持 Go 原生编译或通过插件目录加载。 |

## 用法示例

```bash
# 安装 Telegraf
brew install telegraf         # macOS
sudo apt-get install telegraf # Ubuntu

# 生成默认配置文件
telegraf config > telegraf.conf

# 启动 Telegraf
telegraf --config telegraf.conf

# 通过 systemd 管理
sudo systemctl enable telegraf
sudo systemctl start telegraf
```

1. **编辑 `telegraf.conf`**  
   - 在 `[[inputs.cpu]]`、`[[outputs.influxdb]]` 等段落中启用或禁用插件。  
   - 配置输出目标（InfluxDB 端点、认证信息等）。

2. **动态重载**  
   ```bash
   telegraf --config telegraf.conf --config-directory /etc/telegraf/telegraf.d
   ```

3. **插件开发**  
   - 在 `plugins/inputs/`、`plugins/outputs/` 等目录添加自定义插件，编译后放至 `telegraf.d`，Telegraf 自动加载。

## 常见命令

| 命令 | 作用 |
|------|------|
| `telegraf --help` | 查看帮助信息 |
| `telegraf --version` | 查看版本 |
| `telegraf config` | 生成默认配置 |
| `telegraf --config <file>` | 指定配置文件启动 |
| `telegraf --config-directory <dir>` | 监听配置目录并热重载 |

---

> 以上内容为 Telegraf 项目的核心特性、功能及使用方法的简要中文说明。若需更详细信息，请参阅官方文档或项目仓库。