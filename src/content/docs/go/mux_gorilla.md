---
title: mux
---

# gorilla/mux

## 项目简介

`gorilla/mux` 是一个强大的 HTTP 路由器和 URL 匹配器，用于构建 Go web 服务器。它实现了 `http.Handler` 接口，与标准 `http.ServeMux` 兼容。

## 主要功能

- **请求匹配**：基于 URL 主机、路径、路径前缀、方案、头部和查询值、HTTP 方法或自定义匹配器匹配请求。
- **变量支持**：URL 主机、路径和查询值可以包含变量，支持可选的正则表达式。
- **URL 构建**：注册的 URL 可以被构建或"反转"，帮助维护资源引用。
- **子路由器**：路由可以用作子路由器，嵌套路由仅在父路由匹配时测试，用于定义共享公共条件的路由组，并优化请求匹配。
- **中间件支持**：支持添加中间件，按添加顺序执行。
- **CORS 处理**：提供 `CORSMethodMiddleware` 来简化 CORS 请求处理。
- **静态文件服务**：轻松服务静态文件。
- **单页应用支持**：支持服务单页应用（如 React、Vue 等）。
- **优雅关闭**：支持 Go 1.8+ 的优雅服务器关闭。
- **路由遍历**：可以使用 `Walk` 函数遍历所有注册的路由。

## 安装

使用 Go 工具链安装：

```bash
go get -u github.com/gorilla/mux
```

## 基本用法

### 注册路由

```go
func main() {
    r := mux.NewRouter()
    r.HandleFunc("/", HomeHandler)
    r.HandleFunc("/products", ProductsHandler)
    r.HandleFunc("/articles", ArticlesHandler)
    http.Handle("/", r)
}
```

### 路径变量

```go
r := mux.NewRouter()
r.HandleFunc("/products/{key}", ProductHandler)
r.HandleFunc("/articles/{category}/", ArticlesCategoryHandler)
r.HandleFunc("/articles/{category}/{id:[0-9]+}", ArticleHandler)
```

获取变量：

```go
func ArticlesCategoryHandler(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    w.WriteHeader(http.StatusOK)
    fmt.Fprintf(w, "Category: %v\n", vars["category"])
}
```

### 匹配条件

```go
r := mux.NewRouter()
// 仅匹配特定域名
r.Host("www.example.com")
// 匹配动态子域名
r.Host("{subdomain:[a-z]+}.example.com")
// 路径前缀
r.PathPrefix("/products/")
// HTTP 方法
r.Methods("GET", "POST")
// 方案
r.Schemes("https")
// 头部
r.Headers("X-Requested-With", "XMLHttpRequest")
// 查询值
r.Queries("key", "value")
// 自定义匹配器
r.MatcherFunc(func(r *http.Request, rm *RouteMatch) bool {
    return r.ProtoMajor == 0
})
```

### 子路由器

```go
r := mux.NewRouter()
s := r.Host("www.example.com").Subrouter()
s.HandleFunc("/products/", ProductsHandler)
s.HandleFunc("/products/{key}", ProductHandler)
s.HandleFunc("/articles/{category}/{id:[0-9]+}", ArticleHandler)
```

### 静态文件服务

```go
r.PathPrefix("/static/").Handler(http.StripPrefix("/static/", http.FileServer(http.Dir(dir))))
```

### 中间件

```go
func loggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        log.Println(r.RequestURI)
        next.ServeHTTP(w, r)
    })
}

r := mux.NewRouter()
r.HandleFunc("/", handler)
r.Use(loggingMiddleware)
```

### URL 构建

```go
r := mux.NewRouter()
r.HandleFunc("/articles/{category}/{id:[0-9]+}", ArticleHandler).Name("article")

url, err := r.Get("article").URL("category", "technology", "id", "42")
// 结果: "/articles/technology/42"
```

## 许可证

BSD 3-Clause 许可证。
