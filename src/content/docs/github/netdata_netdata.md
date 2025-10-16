
---
title: netdata
---

# Netdata 项目

## 项目地址
[https://github.com/netdata/netdata](https://github.com/netdata/netdata)

## 主要特性
Netdata 是一个开源的实时性能监控和故障诊断工具，具有以下核心特性：
- **实时监控**：提供亚秒级分辨率的监控数据，支持数百种指标的实时采集和可视化，无需外部依赖。
- **零配置安装**：简单易用，支持一键安装（例如通过 curl 命令），自动发现和监控系统资源。
- **分布式架构**：支持单节点和多节点部署，可通过代理模式扩展到大规模环境。
- **高性能**：使用高效的 C 语言实现，低 CPU 和内存占用，即使在资源受限的设备上也能运行。
- **警报系统**：内置智能警报机制，支持自定义阈值和通知渠道（如 email、Slack、PagerDuty）。
- **开源与社区驱动**：完全开源（GPLv3 许可），活跃社区贡献，支持插件扩展。

## 主要功能
Netdata 的功能覆盖系统和应用的全面监控，包括：
- **系统监控**：CPU、内存、磁盘 I/O、网络流量、进程等系统级指标。
- **应用监控**：支持数据库（如 MySQL、PostgreSQL）、Web 服务器（如 Nginx、Apache）、容器（如 Docker、Kubernetes）等。
- **可视化仪表板**：交互式 Web 界面，提供图表、热图和拓扑视图，便于快速诊断问题。
- **数据收集**：内置数百个收集器（collectors），可监控硬件传感器、云服务（如 AWS、Azure）和自定义指标。
- **历史数据存储**：支持本地或远程存储历史数据，便于趋势分析和报告生成。
- **集成与 API**：RESTful API 支持与其他工具集成，如 Grafana、Prometheus；支持导出到外部系统。

## 用法
### 安装
1. **一键安装（Linux/macOS）**：
   ```
   bash <(curl -Ss https://my-netdata.io/kickstart.sh)
   ```
   这将自动下载、编译并启动 Netdata。安装后，默认在 http://localhost:19999 访问 Web 界面。

2. **Docker 安装**：
   ```
   docker run -d --name=netdata -p 19999:19999 -v netdata:/etc/netdata -v netdatalib:/var/lib/netdata -v netdatacache:/var/cache/netdata -v /etc/passwd:/host/etc/passwd:ro -v /etc/group:/host/etc/group:ro --restart unless-stopped --cap-add SYS_PTRACE -v /proc:/host/proc:ro -v /sys:/host/sys:ro -v /etc/os-release:/host/etc/os-release:ro netdata/netdata
   ```

3. **从源代码构建**：
   克隆仓库后，使用 `./netdata-installer.sh` 脚本安装。

### 基本用法
- **访问界面**：安装后，打开浏览器访问 `http://<your-ip>:19999`，即可查看实时仪表板。
- **配置**：编辑 `/etc/netdata/netdata.conf` 文件自定义监控项、警报阈值或端口。
- **添加警报**：在配置文件中设置阈值，例如监控 CPU 使用率超过 80% 时发送通知。
- **扩展监控**：通过插件目录（`/usr/libexec/netdata/plugins.d/`）添加自定义收集器。
- **导出数据**：使用 API 如 `http://localhost:19999/api/v1/data?chart=cpu&after=-100` 获取 JSON 数据。

更多细节请参考官方文档：https://learn.netdata.cloud/