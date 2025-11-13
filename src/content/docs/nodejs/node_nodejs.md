---
title: node
---


# Node.js

> 项目地址: <https://github.com/nodejs/node>

Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行时，主要用于构建可扩展的网络应用程序。它实现了异步、事件驱动的 I/O，适合高并发、实时、数据密集型的应用场景。

## 主要特性

- **事件驱动 I/O**  
  通过事件循环（Event Loop）实现非阻塞 I/O，最大化资源利用率。

- **单线程多并发**  
  采用单线程模型，借助 libuv 库实现多线程 I/O。

- **模块化**  
  内置模块（fs, http, https, crypto 等）与 npm 生态的第三方模块无缝集成。

- **跨平台**  
  支持 Windows、macOS、Linux、BSD 等多种操作系统。

- **高性能**  
  V8 引擎对 JavaScript 进行即时编译（JIT），性能优异。

- **丰富的生态系统**  
  npm 提供数万个开源模块，几乎可以满足任何项目需求。

## 核心功能

| 功能 | 说明 |
|------|------|
| **HTTP/HTTPS 服务器** | 可快速搭建 RESTful API、WebSocket、GraphQL 等服务。 |
| **文件系统操作** | 提供同步/异步文件读写、目录操作等 API。 |
| **网络套接字** | 支持 TCP/UDP、Unix socket、原生 TLS/SSL。 |
| **子进程管理** | fork、spawn、exec 等 API，用于多进程编程。 |
| **事件与流** | EventEmitter、Readable/Writable/Transform Streams。 |
| **模块加载** | CommonJS、ES Modules（ESM）支持。 |
| **进程管理** | process 对象提供环境变量、进程信息、信号处理等。 |

## 用法示例

### 1. 安装

```bash
# 通过官方安装包或包管理器安装
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 2. 创建一个简单的 HTTP 服务器

```js
// server.js
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, Node.js!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

运行：

```bash
node server.js
```

访问 <http://127.0.0.1:3000> 即可看到输出。

### 3. 使用 npm 安装第三方模块

```bash
# 安装 Express 框架
npm install express

# 创建 app.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello Express!');
});

app.listen(3000, () => console.log('Express server listening on port 3000'));
```

### 4. 使用 ES Modules

```js
// index.mjs
import http from 'node:http';

const server = http.createServer((req, res) => {
  res.end('ESM Hello!');
});

server.listen(3000);
```

运行：

```bash
node --experimental-modules index.mjs
```

## 开发与贡献

- Fork 本仓库 → Pull Request
- 运行测试：`npm test`
- 查看文档：`docs/`

## 许可证

MIT
