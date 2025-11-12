---
title: serverless-dns
---

# serverless-dns

serverless-dns 是一个基于 RethinkDNS 的无服务器 DNS 解析器，具有类似 Pi-Hole 的内容拦截功能。它支持 DNS-over-HTTPS (DoH) 和 DNS-over-TLS (DoT) 协议，可以部署到多个无服务器平台上。

## 主要特性

- **无服务器架构**：支持 Cloudflare Workers、Deno Deploy、Fastly Compute@Edge 和 Fly.io
- **内容拦截**：内置 190+ 个拦截列表，可阻止广告、恶意软件等
- **多协议支持**：同时支持 DoH 和 DoT 协议
- **高性能**：服务器端处理时间 0-2ms，端到端延迟 10-30ms
- **免费部署**：各平台的免费层级足以覆盖 10-20 台设备的 DNS 流量

## 支持的平台

| 平台                | 部署难度 | 运行时        | 服务器位置 |
| ------------------- | -------- | ------------- | ---------- |
| Cloudflare Workers  | 简单     | V8 Isolates   | 280+       |
| Deno Deploy         | 中等     | Deno Isolates | 30+        |
| Fastly Compute@Edge | 简单     | Fastly JS     | 80+        |
| Fly.io              | 困难     | Node MicroVM  | 30+        |

## 快速部署

### Cloudflare Workers（推荐）

最简单的部署方式，一键部署：

[![Deploy to Cloudflare Workers](https://deploy.workers.cloudflare.com/?url=https://github.com/serverless-dns/serverless-dns)](https://deploy.workers.cloudflare.com/?url=https://github.com/serverless-dns/serverless-dns)

### Fastly Compute@Edge

[![Deploy to Fastly](https://deploy.edgecompute.app/deploy)](https://deploy.edgecompute.app/deploy)

## 开发环境设置

### 前置要求

- Node.js 22+ 或 Deno 2+
- Git

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/serverless-dns/serverless-dns.git
cd serverless-dns

# 安装依赖
npm install

# 本地运行（Node.js）
./run n

# 本地运行（Deno）
./run d
```

### 平台特定运行

```bash
# Cloudflare Workers
./run w

# Fastly Compute@Edge
./run f
```

## 配置说明

### 环境变量配置

主要配置文件：

- Cloudflare Workers: `wrangler.toml`
- Fastly: `fastly.toml`
- 通用配置: `src/core/env.js`

### 拦截列表设置

部署完成后，访问 `https://<your-domain>.tld/configure` 来配置拦截列表，界面类似于 RethinkDNS 的配置页面。

### 认证设置

支持基于 bearer token 的认证：

1. **DoH 认证**：在 blockstamp 末尾添加消息密钥

   ```
   1:1:4AIggAABEGAgAA:<msg-key>
   ```

2. **DoT 认证**：在 SNI 域名中添加消息密钥
   ```
   1-4abcbaaaaeigaiaa-<msg-key>
   ```

## 日志和分析

支持通过 Cloudflare Logpush 上传日志：

```bash
# 设置 Logpush 作业
CF_ACCOUNT_ID=<account-id>
CF_API_KEY=<api-key>
R2_BUCKET=<bucket-name>
# ... 其他配置
```

## 架构说明

### 请求流程

1. 客户端 ↔ 服务器入口点 ↔ `doh.js` ↔ `plugin.js`
2. `plugin.js` 流程：`user-op.js` → `cache-resolver.js` → `cc.js` → `resolver.js`

### 缓存机制

- Node.js 和 Deno：使用 `@serverless-dns/lfu-cache`
- Cloudflare Workers：结合 Cache Web API 和进程内 LFU 缓存

### 拦截列表

- 使用压缩的简洁基数树（Succinct Radix Trie）
- 包含约 1300 万条目（截至 2023 年 1 月）
- 每周更新一次

## 生产环境部署

### Cloudflare Workers

```bash
npm run build
npx wrangler publish [-e <env-name>]
```

### Fastly Compute@Edge

```bash
fastly compute publish
```

### Fly.io

```bash
npm run build:fly
flyctl deploy --dockerfile node.Dockerfile --config <fly.toml>
```

## 许可证

本项目采用 MPL-2.0 许可证。

## 相关链接

- [项目主页](https://github.com/serverless-dns/serverless-dns)
- [RethinkDNS 配置](https://rethinkdns.com/configure)
- [拦截列表仓库](https://github.com/serverless-dns/blocklists)
- [文档](https://docs.rethinkdns.com/dns/open-source)
