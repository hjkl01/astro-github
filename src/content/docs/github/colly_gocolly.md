
---
title: colly
---

# Colly 项目

**GitHub 项目地址:** [https://github.com/gocolly/colly](https://github.com/gocolly/colly)

## 主要特性
Colly 是一个用 Go 语言编写的快速且优雅的网络爬虫框架。它支持并发爬取、自定义请求、缓存管理以及插件扩展。主要特性包括：
- **高性能并发**：内置支持高并发请求处理，适合大规模数据采集。
- **简洁 API**：提供直观的接口，如 `Collector`、`Request` 和 `Response`，易于上手。
- **内置缓存和去重**：自动处理重复请求和响应缓存，避免无效爬取。
- **插件支持**：可扩展 HTML/CSS 选择器、代理、Cookie 管理等功能。
- **异步和同步模式**：支持阻塞式和非阻塞式爬取，灵活适应不同场景。
- **跨平台兼容**：纯 Go 实现，无外部依赖，适用于 Linux、Windows 和 macOS。

## 主要功能
Colly 的核心功能聚焦于 Web 数据提取和自动化爬取：
- **页面爬取**：从 URL 获取 HTML、JSON 或其他内容，支持 GET/POST 等 HTTP 方法。
- **数据解析**：集成 GoQuery（类似于 jQuery），用于选择和提取 DOM 元素中的数据，如文本、链接、图片。
- **链接跟踪**：自动发现并跟随页面中的超链接，实现深度爬取。
- **自定义处理**：允许在请求前/后添加钩子函数，进行数据清洗、存储或错误处理。
- **限速与反爬虫**：内置延迟控制、User-Agent 随机化和代理支持，规避网站反爬机制。
- **存储集成**：易于与数据库（如 SQLite、MongoDB）或文件系统结合，持久化爬取结果。

## 用法示例
安装 Colly：
```bash
go get -u github.com/gocolly/colly/v2
```

基本用法（爬取示例网站并提取标题）：
```go
package main

import (
    "fmt"
    "github.com/gocolly/colly/v2"
)

func main() {
    c := colly.NewCollector()

    // 注册回调函数：当访问页面时提取标题
    c.OnHTML("h1", func(e *colly.HTMLElement) {
        fmt.Println("标题:", e.Text)
    })

    // 访问 URL
    c.Visit("https://example.com")

    // 跟踪所有链接
    c.OnHTML("a[href]", func(e *colly.HTMLElement) {
        link := e.Attr("href")
        fmt.Println("发现链接:", link)
        c.Visit(e.Request.AbsoluteURL(link))
    })
}
```

运行后，Colly 会并发访问页面，提取并打印标题和链接。该框架适合构建 RSS 订阅器、价格监控或数据聚合工具。更多高级用法请参考官方文档。