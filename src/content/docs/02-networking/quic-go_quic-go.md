
---
title: quic-go
---

# quic-go

**GitHub**: [https://github.com/quic-go/quic-go](https://github.com/quic-go/quic-go)

## 概述
quic-go 是一个完全用 Go 编写的 QUIC 协议实现，支持 HTTP/ 与 QUIC 直接通信。它兼容 Google 的 QUIC 规范，提供稳定的传输层功能，适用于需要低延迟、高效网络传输的应用。

## 主要特性
- **原生 Go 实现**：不依赖任何 C 代码，易于构建与发布。
- **支持 QUIC 1.0（IETF）**：实现了 IETF QUIC 协议规范，兼容多种服务器与客户端。
- **HTTP/3 集成**：内置 QUIC‑HTTP/3 支持，方便快速搭建 HTTP/3 服务。
- **多路复用**：单连接支持多请求，降低拥塞与延迟。
- **快速连接恢复**：使用迁移与恢复机制提升网络掉线恢复速度。
- **TLS 1.3 集成**：使用标准 TLS 1.3 加密，兼容现代浏览器。
- **可裁剪性**：可通过 go build tags 配置启用或禁用功能模块。
- **跨平台**：支持 Linux、Windows、macOS、aix、freebsd、openbsd 等平台。

## 关键功能
| 模块 | 说明 |
|------|------|
| `quic-go` | QUIC 连接、控制、包解析、重传等核心功能 |
| `quic-go/http3` | HTTP/3 框架，提供服务器、客户端实现 |
| `quic-go/examples` | 各种使用示例：server、client、proxy、proxy_over_quic 等 |
| `transport` | 提供基于 `net.Conn` 的 QUIC 流接口 |
| `logging` | 内置日志记录，支持不同日志级别 |
| `crypto` | TLS 1.3 与 QUIC 密钥生成、密钥演变 |

## 用法

### 安装
```bash
go get -u github.com/quic-go/quic-go
```

### 开启 HTTP/3 服务器
```go
package main

import (
    "log"
    "net"
    "net/url"

    "github.com/quic-go/quic-go/http3"
)

func main() {
    uri := "https://localhost:8443"
    serverAddress, err := url.Parse(uri)
    if err != nil {
        log.Fatal(err)
    }

    srv := http3.Server{
        ListenAddr:     serverAddress.Host,
        Cert:           []byte(certPEM),           // PEM 格式 cert
        Key:            []byte(keyPEM),            // PEM 格式 key
        Handlers:       http.NewServeMux(),       // 用于处理 http3 请求
        HandlersForwardRef: true,                  // 允许 for 请求
    }

    log.Fatal(srv.ListenAndServe())
}
```

### QUIC 客户端连接
```go
package main

import (
    "fmt"
    "os"

    "github.com/quic-go/quic-go"
)

func main() {
    session, err := quic.DialAddr("localhost:8443",
        &tls.Config{InsecureSkipVerify: true},
        &quic.Config{})
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }

    stream, err := session.OpenStreamSync()
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }

    _, err = stream.Write([]byte("Hello QUIC!"))
    if err != nil {
        fmt.Println(err)
    }
}
```

### 纯 QUIC 示例（无 HTTP/3）
```go
// server.go
package main

import (
    "crypto/tls"
    "log"

    "github.com/quic-go/quic-go"
)

func main() {
    tlsConf := &tls.Config{InsecureSkipVerify: true}
    quicConf := &quic.Config{HandshakeTimeout: 10 * time.Second}

    listener, err := quic.ListenAddr("localhost:4242", tlsConf, quicConf)
    if err != nil {
        log.Fatal(err)
    }

    for {
        session, err := listener.Accept()
        if err != nil {
            log.Print(err)
            continue
        }
        go handleConn(session)
    }
}

func handleConn(session quic.Session) {
    // 处理传输流
}
```

## 贡献
- Fork → Review → Pull Request
- 关注 `ISSUES` 与 `PRs`，确保符合协议规范

---

**项目地址**: https://github.com/quic-go/quic-go  
使用 `git clone https://github.com/quic-go/quic-go.git` 获取源码。