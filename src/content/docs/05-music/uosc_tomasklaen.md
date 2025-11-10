---
title: uosc
---

# uosc

## 1. 项目简介  
uosc 是一个用于 Node.js 的 OSC（Open Sound Control）库，提供简洁的 API 用于发送、接收以及解析 OSC 消息，支持 UDP 与 WebSocket。

## 2. 主要特性  
- **轻量级**：仅几百行代码，依赖最小化。  
- **全功能**：支持 OSC 地址、数据类型、时间戳、Bundle 等完整规范。  
- **UDP & WebSocket**：默认 UDP，附加 WebSocket 封装，便于浏览器端使用。  
- **监听模式**：可按地址模式（`/foo`、`/bar/*`、`/baz/#`）订阅消息。  
- **Type‑safe**：使用 TypedArray 加速数据读写。  

## 3. 安装  
```bash
npm install uosc
```

## 4. 基本用法  

### 4.1 创建客户端并发送  
```js
const uosc = require('uosc');
const client = uosc.createClient('127.0.0.1', 8000);

client.send('/audio/freq', [440, 0.8]); // 频率，音量
```

### 4.2 创建服务器并接收  
```js
const uosc = require('uosc');
const server = uosc.createServer(8000, (socket, msg, rinfo) => {
    console.log('Received msg:', msg.address, msg.args);
});
```

### 4.3 订阅地址模式  
```js
server.addListener/*', (msg) => {
    console.log('Audio msg:', msg);
});
```

### 4.4 发送 Bundle  
```js
const bundle = uosc.createBundle(0, [
    { address: '/audio/vol', args: [0.5] },
    { address: '/audio/freq', args: [880] }
]);
client.sendBundle(bundle);
```

## 5. API 说明  

| 方法 | 作用 |
| ---- | ---- |
| `uosc.createClient(host, port)` | 创建 UDP/WS 客户端 |
| `uosc.createServer(port, [callback])` | 创建 UDP/WS 服务器 |
| `client.send(address, args)` | 发送单条 OSC 消息 |
| `client.sendBundle(bundle)` | 发送 Bundle |
| `server.addListener(address, fn)` | 注册地址监听器 |
| `server.removeListener(address, fn)` | 移除监听器 |
| `uosc.encodeMessage(msg)` | 手动编码消息 |
| `uosc.decodeMessage(buffer)` | 手动解码消息 |

## 6. 参考  
- 官方文档与示例在 GitHub  
- 支持的类型：`f`(float), `i`(int), `s`(string), `b`(blob), `m`(midi), `T`, `F`, `N`, `-`, `[]` (数组)

## 项目地址  
[https://github.com/tomasklaen/uosc](https://github.com/tomasklaen/uosc)