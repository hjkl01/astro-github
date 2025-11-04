
---
title: dust
---


# Dust (bootandy/dust)

> 项目地址：<https://github.com/bootandy/dust>

## 简介
Dust 是一个轻量级的命令行工具，旨在帮助开发者快速编写、执行与调试 HTTP 请求。它支持通过 YAML/JSON 配置文件描述请求，并提供了响应捕获、比较以及自动化测试等功能，是后端接口开发与测试的实用助手。

## 主要特性
| 特性 | 说明 |
|------|------|
| **请求描述文件** | 通过 YAML/JSON 格式编写请求，支持多种 HTTP 方法、Header、Body、Query 参数等。 |
| **命令行执行** | 一键执行配置文件中的请求，支持批量执行、并行执行。 |
| **响应捕获** | 自动将响应结果保存为 JSON，方便后续查看或做差异比较。 |
| **差异比较** | 对比两次请求的响应差异，支持格式化输出，帮助快速定位改动。 |
| **环境变量** | 支持在请求中使用环境变量，便于在不同环境下切换。 |
| **自动化测试** | 通过 `--test` 选项运行一组请求，并根据预期结果生成报告。 |
| **插件化** | 可通过自定义插件扩展请求处理逻辑，例如添加身份认证、日志拦截等。 |
| **跨平台** | 使用 Rust 编译，支持 Linux、macOS、Windows 等主流操作系统。 |

## 主要功能

1. **请求定义**  
   ```yaml
   request:
     method: POST
     url: https://api.example.com/v1/users
     headers:
       Content-Type: application/json
     body:
       name: "Alice"
       age: 30
   ```

2. **执行请求**  
   ```bash
   dust run user_create.yaml
   ```

3. **批量执行**  
   ```bash
   dust batch *.yaml
   ```

4. **响应比较**  
   ```bash
   dust diff user_create_1.json user_create_2.json
   ```

5. **环境变量**  
   ```yaml
   request:
     url: https://${env.API_HOST}/v1/users
   ```

   ```bash
   dust run --env API_HOST=api.example.com user_create.yaml
   ```

6. **自动化测试**  
   在请求文件中添加 `expect` 字段，Dust 会在测试模式下校验返回值。  
   ```yaml
   request: ...
   expect:
     status: 201
     body:
       id: !regex "^[0-9a-f]{24}$"
   ```

   ```bash
   dust test *.yaml
   ```

## 快速入门

### 安装

```bash
# 使用 Cargo 安装（推荐）
cargo install dust

# 或者直接下载预编译二进制文件
curl -L https://github.com/bootandy/dust/releases/latest/download/dust-linux-amd64.tar.gz | tar -xz
mv dust /usr/local/bin/
```

### 示例

```yaml
# 文件: example.yaml
request:
  method: GET
  url: https://httpbin.org/get
  headers:
    Accept: application/json
  params:
    foo: bar

# 运行
dust run example.yaml
```

### 查看帮助

```bash
dust --help
```

## 贡献

欢迎提交 Issue 与 Pull Request，详细贡献指南请参阅仓库的 `CONTRIBUTING.md`。

---

> 本文档摘自项目 README，已根据其功能进行概要整理，以供快速参考。若需更深入的使用细节，请查看官方文档或直接阅读源代码。
