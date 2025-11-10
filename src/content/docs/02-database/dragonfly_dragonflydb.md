---
title: dragonfly
---

# Dragonfly 项目

**项目地址:** [https://github.com/dragonflydb/dragonfly](https://github.com/dragonflydb/dragonfly)

## 主要特性
Dragonfly 是一个现代化的高性能内存数据库，旨在作为 Redis 的高吞吐量替代品。它采用 C++ 实现，支持多线程架构，能够在单实例中处理数百万 QPS（每秒查询数），并提供极低的延迟。主要特性包括：
- **高性能与可扩展性**：利用多核 CPU 优化，支持水平扩展，吞吐量比 Redis 高 25 倍以上，同时保持微秒级延迟。
- **Redis 兼容性**：完全兼容 Redis API 和协议，支持 RESP（REdis Serialization Protocol），无需修改现有客户端代码即可迁移。
- **内存效率**：先进的内存管理机制，减少碎片化，支持大容量数据集（TB 级），并提供高效的键值存储、列表、哈希、集合等数据结构。
- **持久化与高可用**：内置 AOF（Append Only File）持久化，支持快照备份；集成 Raft 共识算法实现分布式高可用集群。
- **多租户支持**：通过命名空间隔离多用户环境，适用于云原生场景。
- **其他亮点**：支持 Lua 脚本、事务、Pub/Sub 发布订阅，以及模块化扩展（如搜索、图数据库）。

## 主要功能
Dragonfly 的核心功能聚焦于内存数据库操作，覆盖 Redis 的绝大部分场景：
- **数据结构支持**：键值对（String）、列表（List）、哈希（Hash）、集合（Set）、有序集合（Sorted Set）、位图（Bitmap）、HyperLogLog 等。
- **高级功能**：事务（MULTI/EXEC）、Lua 脚本执行、流（Streams）、地理空间索引（Geo）、模块加载（如 RediSearch 用于全文搜索）。
- **集群与复制**：主从复制、哨兵模式、自动分片，支持多主多从架构，确保数据一致性和容错。
- **监控与管理**：集成 Prometheus 指标暴露、INFO 命令查询状态、CONFIG 配置动态调整。
- **安全特性**：支持 ACL（访问控制列表）、TLS 加密、密码认证，适用于生产环境。

## 用法
### 安装
1. **从源代码构建**（推荐 Linux/macOS）：
   - 克隆仓库：`git clone https://github.com/dragonflydb/dragonfly.git`
   - 安装依赖：CMake 3.13+、GCC 9+ 或 Clang。
   - 构建：`cd dragonfly && mkdir build && cd build && cmake .. && make -j$(nproc)`
   - 运行：`./src/dragonfly --port=6379 --requirepass=yourpassword`

2. **Docker 安装**（快速启动）：
   - 拉取镜像：`docker pull docker.dragonflydb.io/dragonflydb/dragonfly`
   - 运行容器：`docker run -p 6379:6379 dragonflydb/dragonfly`
   - 带持久化：`docker run -v /path/to/data:/data -p 6379:6379 dragonflydb/dragonfly --dir=/data`

3. **预编译二进制**：从 GitHub Releases 下载适用于 Linux/x86_64 的二进制文件，直接执行。

### 基本用法
Dragonfly 使用与 Redis 相同的命令行接口。使用 `redis-cli` 或任何 Redis 客户端连接（默认端口 6379）。

- **连接**：`redis-cli -h localhost -p 6379 -a yourpassword`
- **基本命令示例**：
  - 设置键值：`SET key value`
  - 获取值：`GET key`
  - 列表操作：`LPUSH mylist item1 item2`、`LRANGE mylist 0 -1`
  - 哈希操作：`HSET user:1 name "Alice" age 30`、`HGETALL user:1`
  - 事务：`MULTI`、`SET foo bar`、`EXEC`
- **集群模式**：使用 `--cluster_mode=yes` 启动，支持 `CLUSTER CREATE` 等命令配置节点。
- **配置**：通过命令行参数或 `dragonfly.conf` 文件调整，如 `--maxmemory=4gb` 限制内存使用。
- **迁移**：直接替换 Redis 服务器地址，现有应用无需改动；使用 `redis-check-aof` 工具导入 AOF 文件。

更多细节请参考官方文档：[Dragonfly 文档](https://www.dragonflydb.io/docs)。