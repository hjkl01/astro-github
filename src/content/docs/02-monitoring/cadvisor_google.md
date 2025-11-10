---
title: cadvisor
---

# cAdvisor 项目

**GitHub 项目地址：** [https://github.com/google/cadvisor](https://github.com/google/cadvisor)

## 主要特性
cAdvisor（Container Advisor）是一个开源工具，由 Google 开发，用于监控和管理容器化环境。它专注于实时收集和分析容器资源使用情况，支持 Docker 和其他容器运行时。主要特性包括：
- **实时资源监控**：跟踪容器的 CPU、内存、网络 I/O 和文件系统使用率，提供详细的性能指标。
- **容器发现**：自动发现并监控主机上的所有容器，无需手动配置。
- **历史数据存储**：支持将监控数据存储到后端如 InfluxDB、Prometheus 等，实现长期趋势分析。
- **轻量级设计**：作为独立二进制文件运行，低资源占用，易于集成到 Kubernetes 或其他容器编排系统中。
- **多平台支持**：兼容 Linux、Windows 和 macOS，支持多种容器引擎。
- **安全性**：提供细粒度的访问控制和数据导出选项，确保监控数据的隐私。

## 主要功能
- **资源利用率分析**：实时显示容器的 CPU、内存、磁盘和网络指标，帮助识别性能瓶颈。
- **事件日志记录**：捕获容器生命周期事件，如启动、停止和重启。
- **指标导出**：通过 HTTP API 或标准输出导出数据，便于与其他监控系统集成（如 Prometheus、Grafana）。
- **自定义配置**：支持配置文件调整监控范围、采样频率和输出格式。
- **集成 Kubernetes**：常用于 Kubernetes 集群中，作为节点级监控代理，提供容器级洞察。

## 用法
1. **安装**：
   - 下载预编译二进制文件或从源代码构建：`go install github.com/google/cadvisor@latest`。
   - 对于 Docker 用户：`docker run --volume=/:/rootfs:ro --volume=/var/run:/var/run:rw --volume=/sys:/sys:ro --volume=/var/lib/docker/:/var/lib/docker:ro --publish=8080:8080 --detach=true --name=cadvisor --privileged google/cadvisor:latest`。

2. **运行**：
   - 基本启动：`./cadvisor`（默认监听 8080 端口）。
   - 指定存储后端：`./cadvisor --store_influxdb_host=localhost:8086 --store_influxdb_db=mydb`。
   - 在 Kubernetes 中部署：使用 DaemonSet YAML 文件部署到每个节点。

3. **访问监控数据**：
   - 通过 Web UI：打开浏览器访问 `http://localhost:8080` 查看仪表板。
   - 查询 API：使用 `curl http://localhost:8080/metrics` 获取 Prometheus 格式指标。
   - 集成 Grafana：配置 Prometheus 抓取 cAdvisor 端点，实现可视化仪表板。

更多详情请参考官方文档：[https://github.com/google/cadvisor/blob/master/README.md](https://github.com/google/cadvisor/blob/master/README.md)。