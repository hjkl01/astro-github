---
title: sqlx
---

## 项目简介

sqlx 是 Go 语言中 `database/sql` 库的通用扩展库。它为标准的数据库接口提供了额外的功能，使得数据库操作更加便捷和强大。sqlx 保持了底层接口不变，因此可以轻松集成现有的使用 `database/sql` 的代码库。

## 主要功能

- **数据映射**：支持将查询结果行数据映射到结构体（包括嵌入结构体）、映射（map）和切片（slice）。
- **命名参数**：支持命名参数，包括预准备语句（prepared statements）。
- **快速查询**：提供 `Get` 和 `Select` 方法，可以快速将查询结果转换为结构体或切片。

## 安装

使用以下命令安装 sqlx：

```bash
go get github.com/jmoiron/sqlx
```

## 使用示例

以下是一个简单的使用示例，展示了 sqlx 的基本功能：

```go
package main

import (
    "database/sql"
    "fmt"
    "log"

    _ "github.com/lib/pq"
    "github.com/jmoiron/sqlx"
)

var schema = `
CREATE TABLE person (
    first_name text,
    last_name text,
    email text
);
CREATE TABLE place (
    country text,
    city text NULL,
    telcode integer
)`

type Person struct {
    FirstName string `db:"first_name"`
    LastName  string `db:"last_name"`
    Email     string
}

type Place struct {
    Country string
    City    sql.NullString
    TelCode int
}

func main() {
    // 连接数据库
    db, err := sqlx.Connect("postgres", "user=foo dbname=bar sslmode=disable")
    if err != nil {
        log.Fatalln(err)
    }

    // 执行 schema
    db.MustExec(schema)

    // 插入数据
    tx := db.MustBegin()
    tx.MustExec("INSERT INTO person (first_name, last_name, email) VALUES ($1, $2, $3)", "Jason", "Moiron", "jmoiron@jmoiron.net")
    tx.MustExec("INSERT INTO person (first_name, last_name, email) VALUES ($1, $2, $3)", "John", "Doe", "johndoeDNE@gmail.net")
    tx.NamedExec("INSERT INTO person (first_name, last_name, email) VALUES (:first_name, :last_name, :email)", &Person{"Jane", "Citizen", "jane.citzen@example.com"})
    tx.Commit()

    // 查询数据到结构体切片
    people := []Person{}
    db.Select(&people, "SELECT * FROM person ORDER BY first_name ASC")

    // 查询单个结果
    jason := Person{}
    err = db.Get(&jason, "SELECT * FROM person WHERE first_name=$1", "Jason")

    // 处理 NULL 字段
    places := []Place{}
    err = db.Select(&places, "SELECT * FROM place ORDER BY telcode ASC")

    // 遍历行数据
    place := Place{}
    rows, err := db.Queryx("SELECT * FROM place")
    for rows.Next() {
        err := rows.StructScan(&place)
        if err != nil {
            log.Fatalln(err)
        }
        fmt.Printf("%#v\n", place)
    }

    // 命名查询
    _, err = db.NamedExec(`INSERT INTO person (first_name,last_name,email) VALUES (:first,:last,:email)`,
        map[string]interface{}{
            "first": "Bin",
            "last":  "Smuth",
            "email": "bensmith@allblacks.nz",
        })

    // 批量插入
    personStructs := []Person{
        {FirstName: "Ardie", LastName: "Savea", Email: "asavea@ab.co.nz"},
        {FirstName: "Sonny Bill", LastName: "Williams", Email: "sbw@ab.co.nz"},
        {FirstName: "Ngani", LastName: "Laumape", Email: "nlaumape@ab.co.nz"},
    }

    _, err = db.NamedExec(`INSERT INTO person (first_name, last_name, email)
        VALUES (:first_name, :last_name, :email)`, personStructs)
}
```

## 注意事项

- sqlx 与最新的两个 Go 版本兼容。
- 对于列名可能重复的查询，使用 `AS` 关键字为列指定别名，或手动使用 `rows.Scan` 扫描结果。
- 更多详细信息请参考 [官方文档](http://jmoiron.github.io/sqlx/)。
