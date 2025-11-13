---
title: golang/go
---

# Go Programming Language

## 功能

Go 是一种开源编程语言，旨在使构建简单、可靠和高效的软件变得容易。它由 Google 开发，具有静态类型、垃圾回收和并发支持等特性。Go 强调简洁性、性能和可读性，适用于网络编程、系统工具和大规模分布式系统。

## 用法

### 下载和安装

#### 二进制分发

官方二进制分发可在 [https://go.dev/dl/](https://go.dev/dl/) 获取。

下载二进制发布后，请访问 [https://go.dev/doc/install](https://go.dev/doc/install) 获取安装说明。

#### 从源码安装

如果您的操作系统和架构组合没有二进制分发，请访问 [https://go.dev/doc/install/source](https://go.dev/doc/install/source) 获取源码安装说明。

### 基本使用

安装 Go 后，您可以开始编写 Go 程序。创建一个简单的 "Hello, World!" 程序：

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

保存为 `main.go`，然后运行 `go run main.go`。

有关更多信息，请访问 [https://go.dev/](https://go.dev/)。
