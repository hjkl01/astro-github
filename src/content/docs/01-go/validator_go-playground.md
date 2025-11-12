---
title: validator
---

# go-playground/validator 简介

## 描述

`go-playground/validator` 是一个 Go 语言包，用于基于标签对结构体和单个字段进行值验证。它提供了强大的验证功能，支持多种数据类型和自定义验证规则。

## 主要特性

- **跨字段和跨结构体验证**：通过验证标签或自定义验证器实现。
- **多维数据验证**：支持切片、数组和映射的深入验证，包括映射键和值的验证。
- **类型处理**：自动确定接口的底层类型进行验证。
- **自定义字段类型**：支持如 SQL 驱动 Valuer 的自定义类型。
- **别名验证标签**：允许将多个验证映射到一个标签，便于结构体定义。
- **自定义字段名称提取**：例如提取 JSON 名称用于错误信息。
- **国际化错误消息**：支持可定制的 i18n 感知错误消息。
- **Gin 框架默认验证器**：支持 Gin 框架的升级和覆盖。

## 安装

使用 `go get` 安装：

```bash
go get github.com/go-playground/validator/v10
```

然后在代码中导入：

```go
import "github.com/go-playground/validator/v10"
```

## 基本使用示例

初始化验证器并验证结构体：

```go
package main

import (
    "fmt"
    "github.com/go-playground/validator/v10"
)

type User struct {
    Name  string `validate:"required,min=2,max=100"`
    Email string `validate:"required,email"`
    Age   int    `validate:"gte=0,lte=130"`
}

func main() {
    validate := validator.New()

    user := User{
        Name:  "John",
        Email: "john@example.com",
        Age:   25,
    }

    err := validate.Struct(user)
    if err != nil {
        // 处理验证错误
        validationErrors := err.(validator.ValidationErrors)
        for _, fieldError := range validationErrors {
            fmt.Printf("Field: %s, Tag: %s\n", fieldError.Field(), fieldError.Tag())
        }
    } else {
        fmt.Println("验证通过")
    }
}
```

更多示例和详细文档请参考 [GoDoc](https://pkg.go.dev/github.com/go-playground/validator/v10)。
