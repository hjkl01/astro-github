
---
title: chi
---


# Go-chi（chi）

**项目地址**: https://github.com/go-chi/chi

## 主要特性  
- 轻量级、零外部依赖  
- 高性能路由器（基于 Trie 结构）  
- 与中间件无缝集成，支持全局与路由组层级  
- 路由组与嵌套路由  
- URL 参数、查询字符串解析  
- 与 `net/http` 兼容，直接实现 `http.Handler`  

## 核心功能  

| 功能 | 说明 |
|------|------|
| 路由匹配 | 支持 `GET/POST/PUT/DELETE/...` 等 HTTP 方法 |
| 路由组 | `r.Route("/admin", func(r chi.Router) { ... })` 进行嵌套 |
| 参数解析 | `chi.URLParam(r, "id")` 获取路径参数 |
| 中间件 | `r.Use(middleware.Logger)` 及自定义中间件 |
| 路由树序列化 | `chi.RoutesToJSON(r)` 生成 JSON 描述 |
| 性能优化 | 内部 Trie + 路由剪枝，极速路由解析 |

## 使用方式  

```go
package main

import (
	"net/http"

	"github.com/go-chi/chi"
	"github.com/go-chi/chi/middleware"
)

func main() {
	r := chi.NewRouter()

	// 全局中间件
	r.Use(middleware.Logger)
	r.Use(middleware.Recover)

	// 单一路由
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello, chi!"))
	})

	// 路由组
	r.Route("/users", func(r chi.Router) {
		r.Get("/", listUsers)
		r.Post("/", createUser)
		r.Get("/{id}", getUser)
	})

	// 启动服务器
	http.ListenAndServe(":8080", r)
}

func listUsers(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("List users"))
}

func createUser(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Create user"))
}

func getUser(w http.ResponseWriter, r *http.Request) {
	id := chi.URLParam(r, "id")
	w.Write([]byte("User ID: " + id))
}
```

## 进一步阅读  
- 官方文档: https://go-chi.netlify.app/  
- 示例代码: https://github.com/go-chi/chi/tree/main/_examples  
