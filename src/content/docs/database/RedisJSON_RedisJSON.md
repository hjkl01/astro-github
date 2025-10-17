
---
title: RedisJSON
---

# RedisJSON 项目

## 项目地址
[https://github.com/RedisJSON/RedisJSON](https://github.com/RedisJSON/RedisJSON)

## 主要特性
RedisJSON 是一个 Redis 模块，它允许用户以 JSON 格式存储、检索和操作数据。主要特性包括：
- **JSON 数据类型支持**：RedisJSON 引入了 JSON 类型的数据结构，支持原生 JSON 操作，而无需将 JSON 字符串作为字符串类型存储。
- **高效查询和索引**：支持在 JSON 文档中进行路径-based 查询、索引和搜索，提高数据检索性能。
- **原子操作**：提供原子级的 JSON 更新、合并和修改操作，确保数据一致性。
- **兼容 Redis 生态**：无缝集成 Redis 的现有功能，如复制、持久化和集群支持。
- **性能优化**：利用 Redis 的内存存储优势，实现低延迟的 JSON 操作，适用于高性能应用场景。

## 主要功能
- **存储和检索**：使用 `JSON.SET` 命令将 JSON 数据存储到 Redis 中，使用 `JSON.GET` 检索指定路径的 JSON 值。
- **修改和更新**：支持 `JSON.SET`、`JSON.DEL`、`JSON.MERGE` 等命令，实现对 JSON 对象的精确修改。
- **查询和遍历**：通过 `JSON.NUMINCRBY`、`JSON.STRAPPEND` 等命令处理数值和字符串操作；支持数组和对象的遍历。
- **调试和工具**：提供 `JSON.DEBUG` 命令用于内存和性能调试。
- **扩展性**：与 Redis Stack 集成，支持与其他模块如 RediSearch 的组合使用，实现复杂查询。

## 用法示例
安装 RedisJSON 后（通过 Redis Stack 或手动编译），在 Redis CLI 中使用以下命令：

1. **设置 JSON 数据**：
   ```
   JSON.SET mydoc . '{"name": "John", "age": 30, "city": "New York"}'
   ```

2. **获取 JSON 值**：
   ```
   JSON.GET mydoc .name
   # 输出: "John"
   ```

3. **更新 JSON**：
   ```
   JSON.SET mydoc .age 31
   ```

4. **删除路径**：
   ```
   JSON.DEL mydoc .city
   ```

5. **合并 JSON**：
   ```
   JSON.MERGE mydoc . '{"hobbies": ["reading", "sports"]}'
   ```

详细用法请参考官方文档：https://oss.redislabs.com/redisjson/。