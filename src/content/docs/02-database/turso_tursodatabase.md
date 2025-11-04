
---
title: turso
---

# Turso

## 项目地址
https://github.com/tursodatabase/turso

## 简介
Turso 是一个面向边缘计算的无服务器数据库，基于 SQLite 构建，提供高性能、低延迟、可弹性扩展的数据存储解决方案。它兼容 SQLite 的语法与生态，同时在全球 CDN 边缘节点自动部署，支持多租户、强一致性和安全的访问控制。

## 主要特性
- **无服务器 + 边缘部署**：数据库实例自动在全球 CDN 边缘节点上运行，几乎零延迟访问。
- **SQLite 兼容**：使用标准 SQLite 语法，迁移成本低，现有工具与库可直接使用。
- **安全与隔离**：每个数据库实例都有独立的 IAM 与 API Key，支持细粒度权限控制。
- **可扩展存储**：按需扩容存储空间，后台自动分片与复制。
- **多语言 SDK**：提供 Rust、JavaScript/TypeScript、Python 等客户端 SDK，易于集成。
- **事务与 ACID**：支持完整的 SQLite 事务语义，保证数据一致性。
- **实时同步**：通过 WebSocket 推送，支持实时订阅与推送更新。

## 功能
| 功能 | 描述 |
|------|------|
| 建表、查询 | 支持 `CREATE TABLE`, `SELECT`, `INSERT`, `UPDATE`, `DELETE` 等标准 SQL |
| 事务 | `BEGIN`, `COMMIT`, `ROLLBACK`，支持多语句事务 |
| 索引与全文搜索 | 支持 B-Tree 索引，SQLite FTS5 |
| 迁移 | CLI `turso migrate`，支持版本化迁移脚本 |
| 数据导入导出 | 支持 CSV、JSON 导入导出 |
| 监控 & 日志 | 提供查询日志、慢查询监控，支持 Grafana/Prometheus |
| 备份与恢复 | 自动化备份，支持点时间恢复 (PITR) |

## 用法

### 1. 安装 SDK（以 Rust 为例）
```bash
cargo add turso
```

### 2. 初始化客户端
```rust
use turso::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 通过环境变量或显式传入 API Key
    let api_key = std::env::var("TURSO_API_KEY")?;
    let endpoint = "https://YOUR_DB_HOST.turso.io";
    let client = Client::new(endpoint, api_key);

    // 创建表
    client.execute(
        r#"
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
        "#,
    ).await?;

    // 插入数据
    client.execute(
        r#"INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');"#,
    ).await?;

    // 查询数据
    let rows = client.query("SELECT id, name, email FROM users;").await?;
    for row in rows {
        let id: i64 = row.get("id");
        let name: String = row.get("name");
        let email: String = row.get("email");
        println!("{}: {} <{}>", id, name, email);
    }

    Ok(())
}
```

### 3. 使用命令行工具
```bash
# 安装 CLI
cargo install turso-cli

# 查看数据库信息
turso db list

# 运行迁移
turso migrate up

# 直接执行 SQL
turso sql "SELECT * FROM users;"
```

### 4. 在 JavaScript/TypeScript 中使用
```bash
npm install @tursodatabase/turso
```

```ts
import { Client } from '@tursodatabase/turso';

const client = new Client({
  url: 'https://YOUR_DB_HOST.turso.io',
  authToken: process.env.TURSO_API_KEY,
});

await client.execute(`
  CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
  );
`);

await client.execute(`INSERT INTO products (name, price) VALUES ('Book', 12.99);`);

const rows = await client.query('SELECT * FROM products;');
console.log(rows);
```

## 参考文档
- 官方文档: https://docs.turso.tech/
- SDK 参考: https://github.com/tursodatabase/turso/tree/main/sdk
- CLI 使用: https://github.com/tursodatabase/turso/blob/main/cli/README.md

---