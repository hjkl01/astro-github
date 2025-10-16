
---
title: dbmate
---

# dbmate 项目概述

**GitHub 项目地址：** [https://github.com/amacneil/dbmate](https://github.com/amacneil/dbmate)

## 主要特性
dbmate 是一个轻量级的数据库迁移工具，专为 Go 语言开发，支持 PostgreSQL、MySQL 和 SQLite 等常见数据库。它类似于 Ruby on Rails 的 ActiveRecord 迁移系统，但更简单且独立于框架。主要特性包括：
- **简单易用**：通过命令行界面（CLI）管理数据库迁移脚本，无需复杂的配置。
- **跨数据库支持**：兼容 PostgreSQL、MySQL 和 SQLite，迁移脚本使用标准 SQL 编写。
- **版本控制**：自动跟踪迁移历史，确保数据库 schema 的可重现性和团队协作。
- **幂等性**：支持迁移的回滚（rollback），便于开发和测试。
- **Go 集成**：作为 Go 库使用时，可嵌入到应用程序中，实现自动化迁移。
- **轻量级**：无外部依赖，体积小，适合小型项目或微服务。

## 主要功能
- **创建迁移**：生成新的迁移文件（up 和 down SQL 脚本），用于定义数据库变更。
- **应用迁移**：执行未应用的迁移，更新数据库 schema。
- **回滚迁移**：撤销最近的迁移，恢复数据库状态。
- **状态检查**：查看当前迁移状态和历史记录。
- **新数据库初始化**：为新环境创建数据库并应用所有迁移。
- **集成支持**：可作为 CLI 工具或 Go 包在代码中调用，支持 CI/CD 管道。

## 用法
dbmate 的用法主要通过命令行操作。首先，确保安装 dbmate（Go 用户可通过 `go install` 获取）。基本用法如下：

### 1. 安装
```bash
go install github.com/amacneil/dbmate@latest
```

### 2. 配置
设置数据库连接字符串环境变量，例如：
```bash
export DATABASE_URL="postgres://user:pass@localhost/dbname?sslmode=disable"
```

### 3. 创建迁移
```bash
dbmate new create_users_table
```
这会生成一个时间戳命名的迁移文件，包含 `up.sql` 和 `down.sql` 部分。例如：
- `up.sql`：`CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(255));`
- `down.sql`：`DROP TABLE users;`

### 4. 应用迁移
```bash
dbmate up
```
应用所有未执行的迁移。

### 5. 回滚迁移
```bash
dbmate down
```
回滚最近一次迁移。或指定步数：`dbmate down 2`。

### 6. 查看状态
```bash
dbmate status
```
显示迁移历史和待应用迁移。

### 7. 其他命令
- `dbmate new <name>`：创建新迁移。
- `dbmate up <version>`：应用到特定版本。
- `dbmate drop`：删除数据库（谨慎使用）。

在 Go 代码中使用时，可导入包并调用 `dbmate.New()` 初始化迁移管理器。更多细节请参考项目 README。