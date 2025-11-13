---
title: chi
---

# Go-chi（chi）

**项目地址**: https://github.com/go-chi/chi

## 安装

```bash
go get -u github.com/go-chi/chi/v5
```

## 主要特性

- **轻量级** - cloc'd 在 ~1000 LOC 用于 chi 路由器
- **快速** - 是的，见基准测试
- **100% 兼容 net/http** - 使用生态系统中的任何 http 或中间件包，只要它也兼容 `net/http`
- **专为模块化/可组合 API 设计** - 中间件、内联中间件、路由组和子路由器挂载
- **上下文控制** - 基于 Go 1.7 中引入的新 `context` 包，用于跨处理程序链的信号、取消和请求范围值
- **健壮** - 在 Pressly、Cloudflare、Heroku、99Designs 和许多其他公司生产中
- **文档生成** - `docgen` 从您的源代码自动生成路由文档到 JSON 或 Markdown
- **Go.mod 支持** - 从 v5 开始，go.mod 支持
- **无外部依赖** - 纯 Go stdlib + net/http

## 核心功能

| 功能         | 说明                                                     |
| ------------ | -------------------------------------------------------- |
| 路由匹配     | 支持 `GET/POST/PUT/DELETE/...` 等 HTTP 方法              |
| 路由组       | `r.Route("/admin", func(r chi.Router) { ... })` 进行嵌套 |
| 参数解析     | `chi.URLParam(r, "id")` 获取路径参数                     |
| 中间件       | `r.Use(middleware.Logger)` 及自定义中间件                |
| 路由树序列化 | `chi.RoutesToJSON(r)` 生成 JSON 描述                     |
| 性能优化     | 内部 Trie + 路由剪枝，极速路由解析                       |

## 使用方式

```go
package main

import (
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

func main() {
	r := chi.NewRouter()

	// 一个好的基础中间件堆栈
	r.Use(middleware.RequestID)
	r.Use(middleware.RealIP)
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)

	// 设置请求上下文的超时值 (ctx)，该值将向 ctx.Done() 发出信号
	// 请求已超时，进一步处理应停止。
	r.Use(middleware.Timeout(60 * time.Second))

	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("hi"))
	})

	// "articles" 资源的 RESTy 路由
	r.Route("/articles", func(r chi.Router) {
		r.With(paginate).Get("/", listArticles)                           // GET /articles
		r.With(paginate).Get("/{month}-{day}-{year}", listArticlesByDate) // GET /articles/01-16-2017

		r.Post("/", createArticle)                                        // POST /articles
		r.Get("/search", searchArticles)                                  // GET /articles/search

		// Regexp url 参数:
		r.Get("/{articleSlug:[a-z-]+}", getArticleBySlug)                // GET /articles/home-is-toronto

		// 子路由器:
		r.Route("/{articleID}", func(r chi.Router) {
			r.Use(ArticleCtx)
			r.Get("/", getArticle)                                        // GET /articles/123
			r.Put("/", updateArticle)                                     // PUT /articles/123
			r.Delete("/", deleteArticle)                                  // DELETE /articles/123
		})
	})

	// 挂载管理员子路由器
	r.Mount("/admin", adminRouter())

	http.ListenAndServe(":3333", r)
}

func ArticleCtx(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		articleID := chi.URLParam(r, "articleID")
		article, err := dbGetArticle(articleID)
		if err != nil {
			http.Error(w, http.StatusText(404), 404)
			return
		}
		ctx := context.WithValue(r.Context(), "article", article)
		next.ServeHTTP(w, r.WithContext(ctx))
	})
}

func getArticle(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	article, ok := ctx.Value("article").(*Article)
	if !ok {
		http.Error(w, http.StatusText(422), 422)
		return
	}
	w.Write([]byte(fmt.Sprintf("title:%s", article.Title)))
}

// 一个完全独立的管理员路由器
func adminRouter() http.Handler {
	r := chi.NewRouter()
	r.Use(AdminOnly)
	r.Get("/", adminIndex)
	r.Get("/accounts", adminListAccounts)
	return r
}

func AdminOnly(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		ctx := r.Context()
		perm, ok := ctx.Value("acl.permission").(YourPermissionType)
		if !ok || !perm.IsAdmin() {
			http.Error(w, http.StatusText(403), 403)
			return
		}
		next.ServeHTTP(w, r)
	})
}
```

## 进一步阅读

- 官方文档: https://go-chi.io/
- 示例代码: https://github.com/go-chi/chi/tree/master/_examples
