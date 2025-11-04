
---
title: cpp-httplib
---


# cpp-httplib

> 项目地址: https://github.com/yhirose/cpp-httplib

## 简介

cpp-httplib 是一个纯 C++11 的单文件 HTTP/HTTPS 客户端与服务器库。它不依赖任何第三方库，编译后仅为一个头文件 `httplib.h`，即可在任何支持 C++11 的编译环境中使用。

## 主要特性

| 功能 | 描述 |
|------|------|
| **单文件实现** | 仅需包含 `httplib.h` 即可使用，无需额外链接或安装。 |
| **跨平台** | 支持 Windows、Linux、macOS 等主流操作系统。 |
| **HTTP/HTTPS** | 同时支持 HTTP 和 HTTPS（通过 OpenSSL 或 LibreSSL）。 |
| **同步与异步** | 提供同步请求/响应和多线程/非阻塞服务器。 |
| **RESTful API** | 方便构建 RESTful 服务，支持路由、查询参数、请求体等。 |
| **文件上传/下载** | 支持 multipart/form-data 上传和二进制文件下载。 |
| **自定义头部** | 能够添加、获取、替换请求/响应头。 |
| **Cookie 管理** | 内置 Cookie 处理。 |
| **TLS 证书验证** | 可自定义证书链、禁用验证等。 |

## 安装与使用

### 1. 下载

```bash
git clone https://github.com/yhirose/cpp-httplib.git
```

或者直接下载 `httplib.h`。

### 2. 编译

```bash
g++ -std=c++11 -O2 -Wall -Wextra -o demo demo.cpp -lssl -lcrypto
```

> 如果不需要 HTTPS，只需去掉 `-lssl -lcrypto`。

### 3. 示例代码

#### HTTP 客户端

```cpp
#include "httplib.h"

int main() {
    httplib::Client cli("httpbin.org");

    // GET 请求
    auto res = cli.Get("/get?foo=bar");
    if (res && res->status == 200) {
        std::cout << res->body << std::endl;
    }

    // POST 请求
    res = cli.Post("/post",
                   "foo=bar&baz=qux",
                   "application/x-www-form-urlencoded");
    if (res && res->status == 200) {
        std::cout << res->body << std::endl;
    }

    return 0;
}
```

#### HTTPS 客户端

```cpp
#include "httplib.h"

int main() {
    // 需要 OpenSSL
    httplib::SSLClient cli("api.github.com");
    cli.set_ca_cert_path("/path/to/ca.pem"); // 可选，设置 CA 证书

    auto res = cli.Get("/repos/yhirose/cpp-httplib");
    if (res && res->status == 200) {
        std::cout << res->body << std::endl;
    }
    return 0;
}
```

#### 简单 HTTP 服务器

```cpp
#include "httplib.h"

int main() {
    httplib::Server svr;

    svr.Get("/", [](const httplib::Request&, httplib::Response& res) {
        res.set_content("Hello, world!", "text/plain");
    });

    svr.Get("/echo", [](const httplib::Request& req, httplib::Response& res) {
        res.set_content(req.body, "text/plain");
    });

    svr.listen("localhost", 8080);
    return 0;
}
```

#### HTTPS 服务器

```cpp
#include "httplib.h"

int main() {
    httplib::SSLServer svr("cert.pem", "key.pem");

    svr.Get("/", [](const httplib::Request&, httplib::Response& res) {
        res.set_content("Secure Hello!", "text/plain");
    });

    svr.listen("0.0.0.0", 8443);
    return 0;
}
```

### 4. 高级功能

- **路由**：`svr.Get("/api/v1/users/{id}", ...)`，支持路径参数。
- **中间件**：`svr.set_pre_routing_handler(...)`，在路由前执行自定义逻辑。
- **文件上传**：使用 `MultipartFormData` 解析。
- **Cookie**：`req.cookies` 与 `res.set_cookie`。

## 结语

cpp-httplib 以其轻量、易用、无依赖的特点，适合快速原型开发、嵌入式项目及需要自带 HTTP/HTTPS 功能的应用。  
