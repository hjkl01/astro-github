---
title: coredns
---

# CoreDNS

CoreDNS 是一个用 Go 语言编写的快速、灵活的 DNS 服务器和转发器。它通过插件链的方式实现可定制的 DNS 功能，支持多种协议和集成，如 Kubernetes 和 etcd。

## 功能

- **插件化架构**：CoreDNS 通过插件链来处理 DNS 查询，每个插件可以执行特定的功能，如缓存、转发、重写等。
- **高性能**：设计用于高并发环境，支持 DNS over HTTPS (DoH)、DNS over TLS (DoT) 和 DNS over QUIC (DoQ)。
- **灵活配置**：使用 Corefile 配置文件，支持多种插件组合，实现自定义 DNS 行为。
- **集成支持**：与 Kubernetes、etcd 等系统集成，用于服务发现和负载均衡。
- **监控和日志**：内置插件支持 dnstap、pprof 等，用于监控和调试。

## 用法

### 安装

从 GitHub 克隆仓库并构建：

```bash
git clone https://github.com/coredns/coredns.git
cd coredns
go build -o coredns .
```

### 配置

CoreDNS 使用 Corefile 进行配置。以下是一个简单的例子：

```
.:53 {
    forward . 8.8.8.8 8.8.4.4
    log
}
```

这个配置将所有查询转发到 Google 的公共 DNS，并启用日志。

### 运行

运行 CoreDNS：

```bash
./coredns -conf /path/to/Corefile
```

### 插件示例

- **缓存插件**：添加缓存以提高性能。

```
. {
    cache 30
    forward . 8.8.8.8
}
```

- **重写插件**：重写查询名称。

```
. {
    rewrite name example.com example.org
    forward . 8.8.8.8
}
```

- **Kubernetes 插件**：用于 Kubernetes 服务发现。

```
cluster.local {
    kubernetes cluster.local
}
```

更多插件和配置选项请参考官方文档。
