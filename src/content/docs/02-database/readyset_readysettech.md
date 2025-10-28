
---
title: readyset
---

# ReadySet 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/readysettech/readyset)

## 主要特性
ReadySet 是一个开源的数据库加速器，旨在通过缓存和预计算机制显著提升数据库查询性能。其核心特性包括：
- **实时缓存**：自动缓存查询结果，支持低延迟响应，即使在高并发场景下也能保持性能。
- **SQL 解析与优化**：内置 SQL 解析器，能处理复杂查询，并优化执行路径以减少数据库负载。
- **分布式支持**：兼容 PostgreSQL 和 MySQL，支持分布式部署，适用于大规模应用。
- **零侵入性集成**：无需修改现有应用程序代码，即可作为数据库代理层插入。
- **监控与调试**：提供内置监控工具，用于跟踪缓存命中率、查询延迟和错误日志。

## 主要功能
- **查询加速**：对读密集型查询进行缓存，减少对后端数据库的直接访问，支持 TTL（生存时间）配置以确保数据新鲜度。
- **数据一致性**：通过变更数据捕获 (CDC) 机制监听数据库更新，自动失效和刷新缓存。
- **事务支持**：处理读写事务，确保 ACID 属性，同时优化读操作。
- **扩展性**：支持自定义缓存策略和插件扩展，适用于微服务架构。
- **安全性**：集成 TLS 加密和访问控制，保护数据传输。

## 用法
1. **安装**：
   - 通过 Docker 快速部署：`docker run -p 5432:5432 readysettech/readyset`（针对 PostgreSQL）。
   - 或从源代码构建：克隆仓库后，使用 Cargo（Rust 工具链）编译：`cargo build --release`。

2. **配置**：
   - 编辑配置文件（`readyset.toml`），指定上游数据库连接（如 `upstream = "postgres://user:pass@host:port/db"`）。
   - 配置缓存规则，例如针对特定表启用缓存：`[cache.table_name] ttl = "1h"`。

3. **运行与集成**：
   - 启动 ReadySet：`./readyset -c readyset.toml`。
   - 修改应用连接字符串，将数据库主机指向 ReadySet 实例（例如，从 `localhost:5432` 改为 ReadySet 的地址）。
   - 测试：执行 SQL 查询，观察性能提升（缓存命中率可通过 Web UI 或日志查看）。

4. **高级用法**：
   - 使用 CLI 工具管理：`readyset-cli query "SELECT * FROM users"` 来测试缓存。
   - 对于生产环境，结合 Kubernetes 部署以实现高可用。

更多细节请参考项目仓库的文档和示例。