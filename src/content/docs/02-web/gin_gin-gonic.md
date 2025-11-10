---
title: gin
---


# Gin - Go Web 框架

**项目地址**: https://github.com/gin-gonic/gin

## 主要特性
- **高性能**：通过高效的路由匹配与拆箱，吞吐量可达单机 go 原生 `net/http` 的 3 倍以上。
- **易用的路由**：支持层级路由、参数化路由、正则路由并与中间件轻松组合。
- **强大的中间件**：自带或自定义中间件可进行日志记录、错误处理、权限校验、CORS、压缩等功能。
- **请求绑定与验证**：`ShouldBindJSON`, `ShouldBindQuery`, `ShouldBindUri` 等实现对 JSON、XML、表单、查询字符串等的自动解析与验证。
- **渲染与模板**：内置支持 `HTML`, `JSON`, `XML`, `ProtoBuf` 四种响应格式；可绑定第三方模板引擎。
- **组与分组**：支持路由组（RouterGroup）以实现公共前缀、中间件复用、版本管理等。
- **错误处理**：统一的错误返回机制，方便自定义错误结构及状态码。
- **方便的测试**：提供 `gin.CreateTestContext` 可在单元测试中快速构造请求。

## 主要功能
| 功能 | 说明 |
|------|------|
| 路由 | 支持 GET/POST/PUT/DELETE/List 等 HTTP 方法，路由参数、命名路由、正则路由。 |
| 中间件 | 日志、中间件链、跨域、压缩、静态文件、GZIP、JWT、Session 等。 |
| 请求绑定 | 绑定结构体、验证标签、文件上传、表单与查询字符串。 |
| 响应渲染 | 返回 JSON、XML、ProtoBuf、HTML 或自定义数据。 |
| 组路由 | 通过 `RouterGroup` 对路由和中间件进行分组。 |
| 错误处理 | 统一返回错误码与 JSON 格式错误信息。 |
| 测试工具 | 便携的 `TestContext` 支持单元测试、集成测试。 |

## 快速开始

```go
package main

import (
    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default() // 含 Logger、Recovery 中间件

    // 路由组
    api := r.Group("/api")
    {
        api.GET("/ping", func(c *gin.Context) {
            c.JSON(200, gin.H{
                "message": "pong",
            })
        })
    }

    // POST 示例：接收并验证 JSON
    r.POST("/user", func(c *gin.Context) {
        var json struct {
            Name string `json:"name" binding:"required"`
            Age  int    `json:"age" binding:"gte=0"`
        }
        if err := c.ShouldBindJSON(&json); err != nil {
            c.JSON(400, gin.H{"error": err.Error()})
            return
        }
        c.JSON(200, gin.H{
            "status": "ok",
            "user":   json,
        })
    })

    r.Run(":8080") // 监听 8080 端口
}
```

1. **安装**  
```bash
go get -u github.com/gin-gonic/gin
```

2. **运行**  
```bash
go run main.go
```

浏览器访问 `http://localhost:8080/api/ping，返回 `{"message":"pong"}`。

## 文档与资源
- 官方文档: https://github.com/gin-gonic/gin
- 中文文档: https://github.com/gin-gonic/gin/wiki
- 示例项目: https://github.com/gin-gonic/example

---
以上即为 Gin 的主要特性、功能与使用方式的简要描述。祝开发愉快!
