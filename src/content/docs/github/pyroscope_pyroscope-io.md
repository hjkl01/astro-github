
---
title: pyroscope
---

# Pyroscope 项目

## 项目地址
[GitHub 项目地址](https://github.com/pyroscope-io/pyroscope)

## 主要特性
Pyroscope 是一个开源的持续性能剖析（Continuous Profiling）平台，专为现代应用程序设计。它支持多种编程语言（如 Go、Python、Java、Ruby 等），能够实时收集和分析 CPU、内存等资源的性能数据。主要特性包括：
- **实时剖析**：无需停止应用程序，即可进行低开销的性能剖析，支持采样模式以最小化对生产环境的干扰。
- **多语言支持**：内置对多种语言和运行时的支持，包括 Go 的 pprof、Python 的 py-spy 等。
- **可视化界面**：提供 Web UI，用于浏览火焰图（Flame Graphs），帮助开发者直观识别热点代码和瓶颈。
- **分布式部署**：支持 Kubernetes、Docker 等环境，可作为服务运行，集成 Prometheus 等监控工具。
- **数据存储与查询**：使用高效的存储后端（如 ClickHouse 或本地文件），支持历史数据查询和比较。
- **API 和 SDK**：提供 REST API 和客户端库，便于集成到 CI/CD 管道或现有监控系统中。
- **开源与社区驱动**：完全开源，活跃社区贡献，支持自定义扩展。

## 主要功能
- **性能监控**：捕获应用程序的调用栈样本，生成火焰图以可视化代码执行路径和资源消耗。
- **热点检测**：自动识别 CPU 或内存使用率高的函数和模块，支持差分分析（比较不同版本或时间点的性能）。
- **警报与通知**：集成警报系统，当性能指标超过阈值时发送通知。
- **数据导出**：支持将剖析数据导出为 JSON、Pprof 等格式，便于进一步分析。
- **集成能力**：与 Grafana、Datadog 等工具集成，实现全面的 Observability（可观测性）栈。

## 用法
### 安装与部署
1. **使用 Docker 快速启动**：
   ```
   docker run -p 4040:4040 -v pyroscope-data:/var/lib/pyroscope pyroscope/pyroscope:latest server
   ```
   访问 `http://localhost:4040` 查看 Web UI。

2. **从源代码构建**：
   - 克隆仓库：`git clone https://github.com/pyroscope-io/pyroscope.git`
   - 安装依赖：`make deps`
   - 构建：`make build`
   - 运行服务器：`./pyroscope server`

3. **Kubernetes 部署**：使用 Helm Chart 安装，支持 Helm 仓库中的官方 chart。

### 使用示例
1. **上传剖析数据**：
   - 对于 Go 应用，使用 Pyroscope Go 代理：
     ```go
     import "github.com/pyroscope-io/pyroscope/pkg/agent/profiler"
     profiler.Start(profiler.Config{ServerAddress: "http://pyroscope:4040", ProfileTypes: []profiler.ProfileType{profiler.CPU}})
     ```
   - 命令行上传：`pyroscope upload cpu --from pprof.pb.gz --to http://pyroscope:4040`

2. **在 Web UI 中查看**：
   - 导航到应用名称，选择时间范围，查看火焰图。
   - 查询示例：`/applications?query=app.cpu`

3. **集成到 CI/CD**：
   - 在构建管道中运行剖析命令，并上传结果到 Pyroscope 服务器，用于回归测试性能变化。

更多详细用法，请参考官方文档：https://pyroscope.io/docs/