---
title: RedisShake
---

# RedisShake 项目

**项目地址**: [https://github.com/alibaba/RedisShake](https://github.com/alibaba/RedisShake)

## 主要特性
RedisShake 是阿里巴巴开源的 Redis 数据处理工具，具有以下核心特性：
- **高效同步**：支持 Redis 到 Redis 的在线同步、离线同步和过滤同步，处理速度快，支持大流量数据迁移。
- **多协议兼容**：兼容 Redis 2.x 到 7.x 版本，支持单机、哨兵、集群模式，以及兼容 Redis 的数据库如 Tikv、TiDB 等。
- **数据过滤**：提供键过滤、正则表达式过滤、槽位过滤等功能，实现精确数据迁移。
- **高可用性**：支持断点续传、错误恢复机制，确保数据一致性和完整性。
- **轻量级**：纯 Go 语言实现，易于部署，无外部依赖。

## 主要功能
- **在线同步**：实时同步源 Redis 数据到目标 Redis，支持增量和全量同步。
- **离线同步**：通过 RDB/AOF 文件进行批量数据导入和导出。
- **数据过滤与转换**：根据规则过滤键值，支持类型转换（如 List 到 Set）。
- **监控与日志**：内置监控指标，支持 Prometheus 集成，提供详细日志输出。
- **扩展性**：可作为库集成到其他项目中，用于自定义数据处理。

## 用法
### 安装
1. 从 GitHub 下载最新 Release 版本，或使用 Go 构建：
   ```
   go install github.com/alibaba/RedisShake/cmd/redisshake@latest
   ```
2. 解压并确保可执行文件在 PATH 中。

### 基本用法
RedisShake 通过配置文件（TOML 格式）运行。创建 `config.toml` 文件，配置源和目标 Redis 信息。

示例配置文件（同步模式）：
```toml
[source]
type = "single"
address = "127.0.0.1:6379"
password = ""

[target]
type = "single"
address = "127.0.0.1:6380"
password = ""

mode = "sync"  # 模式：sync (在线同步), scan (离线同步), filter (过滤同步)
```

运行命令：
```
./redisshake -conf=config.toml
```

### 高级用法
- **过滤同步**：在配置文件中添加：
  ```
  filter = "key*"
  type_filter = ["string", "hash"]
  ```
- **集群模式**：将 `type` 设置为 `cluster`，并指定节点地址。
- **监控**：启用 `--metrics-addr=0.0.0.0:16379` 暴露指标。
- 更多选项参考官方文档：项目 README 或 `redisshake --help`。

详细文档和示例请查看项目仓库。