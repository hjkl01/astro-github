---
title: squirrel
---

# Squirrel

Squirrel 是一个用于 Go 语言的流畅 SQL 生成器。它不是一个 ORM，而是帮助你从可组合部分构建 SQL 查询。

## 功能

- 支持流畅的 SQL 查询构建，包括 SELECT、INSERT、UPDATE、DELETE 等操作。
- 支持条件查询、JOIN、WHERE 子句等。
- 支持占位符格式，包括问号和美元符号（适用于 PostgreSQL）。
- 可以直接执行查询或生成 SQL 字符串和参数。
- 支持语句缓存以提高性能。

## 用法

### 安装

```bash
go get github.com/Masterminds/squirrel
```

### 基本示例

```go
import sq "github.com/Masterminds/squirrel"

// 构建 SELECT 查询
users := sq.Select("*").From("users").Join("emails USING (email_id)")
active := users.Where(sq.Eq{"deleted_at": nil})
sql, args, err := active.ToSql()
// sql == "SELECT * FROM users JOIN emails USING (email_id) WHERE deleted_at IS NULL"

// 构建 INSERT 查询
sql, args, err := sq.Insert("users").Columns("name", "age").
    Values("moe", 13).Values("larry", sq.Expr("? + 5", 12)).
    ToSql()
// sql == "INSERT INTO users (name,age) VALUES (?,?),(?,? + 5)"

// 直接执行查询
stooges := users.Where(sq.Eq{"username": []string{"moe", "larry", "curly", "shemp"}})
three_stooges := stooges.Limit(3)
rows, err := three_stooges.RunWith(db).Query()
```

### 条件查询

```go
if len(q) > 0 {
    users = users.Where("name LIKE ?", fmt.Sprintf("%%%s%%", q))
}
```

### PostgreSQL 支持

```go
psql := sq.StatementBuilder.PlaceholderFormat(sq.Dollar)
sql, _, _ := psql.Select("*").From("elephants").Where("name IN (?,?)", "Dumbo", "Verna").ToSql()
// sql == "SELECT * FROM elephants WHERE name IN ($1,$2)"
```

### 返回插入 ID

```go
query := sq.Insert("nodes").
    Columns("uuid", "type", "data").
    Values(node.Uuid, node.Type, node.Data).
    Suffix("RETURNING \"id\"").
    RunWith(m.db).
    PlaceholderFormat(sq.Dollar)

query.QueryRow().Scan(&node.id)
```

## 注意事项

- Squirrel 不是 ORM，它专注于 SQL 生成。
- 对于更复杂的应用，可以结合 structable 等库使用。
- 测试用例是文档的一部分，可以参考更多高级用法。
