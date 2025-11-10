---
title: rod
---

# Rod

## 项目介绍

Rod 是一个基于 Chrome DevTools Protocol 的高水平驱动程序，专为 Web 自动化和爬取而设计。它适用于高级和低级使用，高级开发者可以使用低级包和函数轻松定制或构建自己的 Rod 版本。

## 功能特性

- **链式上下文设计**：直观地超时或取消长时间运行的任务
- **自动等待元素就绪**：确保元素在操作前准备好
- **调试友好**：自动输入跟踪、远程监控无头浏览器
- **线程安全**：所有操作都是线程安全的
- **自动查找或下载浏览器**：简化设置过程
- **高级助手**：如 WaitStable、WaitRequestIdle、HijackRequests、WaitDownload 等
- **两步 WaitEvent 设计**：永不错过事件
- **正确处理嵌套 iframe 或影子 DOM**
- **无僵尸浏览器进程**：崩溃后自动清理
- **100% 测试覆盖率**：通过 CI 强制执行

## 用法示例

### 基本用法

```go
package main

import (
    "github.com/go-rod/rod"
)

func main() {
    // 启动浏览器
    browser := rod.New().MustConnect()

    // 创建新页面
    page := browser.MustPage("https://example.com")

    // 查找元素并点击
    page.MustElement("a").MustClick()

    // 获取页面标题
    title := page.MustEval("() => document.title").String()
    println(title)
}
```

### 等待元素

```go
// 等待元素出现
el := page.MustElement("input[name='q']")

// 输入文本
el.MustInput("rod")

// 提交表单
page.MustElement("form").MustSubmit()
```

### 截图

```go
// 截取页面截图
page.MustScreenshot("screenshot.png")
```

更多详细示例，请查看 [examples_test.go](https://github.com/go-rod/rod/blob/main/examples_test.go) 文件和 [examples](https://github.com/go-rod/rod/tree/main/lib/examples) 文件夹。

## 文档和资源

- [官方文档](https://go-rod.github.io/)
- [API 参考](https://pkg.go.dev/github.com/go-rod/rod)
- [FAQ](https://go-rod.github.io/#/faq/README)
- [中文 API 文档](https://pkg.go.dev/github.com/go-rod/go-rod-chinese)
