---
title: Bifrost
---

# Bifrost 项目

**GitHub 项目地址:** [https://github.com/brokercap/Bifrost](https://github.com/brokercap/Bifrost)

## 主要特性
Bifrost 是一个基于 Go 语言开发的数据库代理工具（Proxy），主要针对 MySQL 数据库，提供高可用性、数据同步和负载均衡等功能。它支持多种数据库操作的代理和分发，适用于大规模分布式数据库环境。核心特性包括：
- **高性能代理**：支持 MySQL 协议的代理转发，减少数据库连接开销。
- **数据同步**：实现 MySQL 到其他数据库（如 TiDB、MySQL 等）的实时同步，支持 binlog 解析和事件订阅。
- **负载均衡**：自动分发查询到后端多个数据库节点，支持读写分离。
- **插件化扩展**：模块化设计，便于自定义插件，如过滤器、监控等。
- **高可用性**：支持主从复制、故障转移和监控告警。
- **多协议支持**：兼容 MySQL 5.6+ 版本，并扩展到其他兼容协议。

## 主要功能
- **Binlog 解析与订阅**：捕获 MySQL binlog 日志，实现数据变更的实时订阅和分发，支持 DDL 和 DML 操作。
- **数据迁移与同步**：从源 MySQL 数据库同步数据到目标数据库，支持全量和增量同步。
- **SQL 路由与过滤**：根据规则路由 SQL 查询，支持黑白名单过滤和 SQL 解析优化。
- **监控与告警**：内置 Prometheus 指标暴露和日志监控，便于运维管理。
- **配置管理**：通过 YAML 或配置文件管理节点、规则和插件，支持动态加载。
- **安全特性**：支持 SSL 加密、用户认证和访问控制。

## 用法
### 安装
1. **下载源码**：从 GitHub 克隆仓库 `git clone https://github.com/brokercap/Bifrost.git`。
2. **构建**：使用 Go 环境构建 `go build -o bifrost`。
3. **二进制安装**：直接下载预编译的二进制文件，解压后运行。

### 基本配置
- 编辑 `conf/bifrost.conf` 文件，配置源数据库连接（如 MySQL URI）和目标节点。
- 示例配置：
  ```
  [mysql]
  addr = 127.0.0.1:3306
  user = root
  password = password
  ```

### 启动与使用
1. **启动 Bifrost**：运行 `./bifrost -c conf/bifrost.conf`。
2. **配置同步任务**：使用 Web 管理界面（默认端口 21000）或命令行添加同步规则，例如订阅 binlog 并指定目标数据库。
3. **示例用法**：
   - 同步数据：`bifrost-cli create canal to_mysql -source mysql://user:pass@host:port -target mysql://target_user:pass@target_host:port`。
   - 监控：访问 `http://localhost:21000` 查看仪表盘。
4. **停止**：使用 `Ctrl+C` 或发送 SIGTERM 信号。
5. **高级用法**：集成插件如自定义过滤器，通过 API 接口管理任务，支持 Docker 部署。

更多细节请参考项目 README 和文档。