
---
title: rod
---


# go-rod

> **项目地址**: https://github.com/go-rod/rod

## 简介
`go-rod` 是一个用 Go 编写的现代浏览器自动化框架，基于 Chrome DevTools Protocol（CDP）实现。它提供了易用、高效、支持并发的 API，适用于网页抓取、自动化测试、UI 交互等多种场景。

## 主要特性
- **零依赖**：不需要安装额外的浏览器驱动，直接使用 Chrome/Chromium。
- **简洁的链式 API**：支持链式调用，代码可读性高。
- **强大的等待机制**：内置 `Wait`, `WaitVisible`, `WaitNotVisible`, `WaitText` 等等待方法。
- **并发执行**：支持多实例/多页面并发操作，能够充分利用多核 CPU。
- **网络拦截与注入**：可以拦截请求、修改响应、注入脚本。
- **截图、PDF、PDF渲染**：内置截图、打印为 PDF 的支持。
- **页面事件监听**：支持页面加载、错误、请求等事件监听。
- **高级选择器**：支持 CSS, XPath, 文本内容等多种选择器。
- **可插拔**：通过插件机制扩展功能，例如 `rod/extend`。

## 核心功能
| 功能 | 描述 |
|------|------|
| `Browser` | 启动、关闭、管理浏览器实例 |
| `Page` | 打开 URL、刷新、跳转、执行脚本 |
| `Element` | 查找元素、点击、输入、拖拽、获取属性 |
| `Session` | 开启 DevTools Session 进行低级操作 |
| `Waiter` | 等待元素或条件满足 |
| `Intercept` | 请求拦截与响应修改 |
| `Keyboard/Mouse` | 模拟键盘与鼠标操作 |
| `Network` | 监控网络请求、设置代理 |
| `Screenshot/PDF` | 生成页面截图或 PDF 文件 |

## 快速上手

```go
package main

import (
    "github.com/go-rod/rod"
    "github.com/go-rod/rod/lib/launcher"
)

func main() {
    // 启动浏览器
    url := launcher.New().MustLaunch()
    browser := rod.New().ControlURL(url).Connect()

    // 打开页面
    page := browser.MustPage("https://example.com")

    // 等待页面加载完成
    page.MustWaitLoad()

    // 查找元素并点击
    page.MustElement("h1").MustClick()

    // 截图
    page.MustScreenshot("example.png")

    // 关闭浏览器
    browser.MustClose()
}
```

## 并发使用示例

```go
package main

import (
    "sync"

    "github.com/go-rod/rod"
)

func main() {
    browser := rod.New().MustConnect()
    var wg sync.WaitGroup

    urls := []string{
        "https://example.com",
        "https://golang.org",
        "https://github.com",
    }

    for _, u := range urls {
        wg.Add(1)
        go func(url string) {
            defer wg.Done()
            page := browser.MustPage(url)
            page.MustWaitLoad()
            // 处理页面...
            page.MustClose()
        }(u)
    }
    wg.Wait()
}
```

## 依赖

- Go 1.16 及以上
- Chrome/Chromium（`go-rod` 会自动下载对应版本，亦可自行指定）

## 贡献

项目欢迎 PR、issue 与建议，详细贡献指南请参见 `CONTRIBUTING.md`。

---

> **项目地址**: https://github.com/go-rod/rod
