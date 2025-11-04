
---
title: wechat-selkies
---


# wechat-selkies

> GitHub 主仓库: httpsgithub.com/nickrunning/wechat-selkies

## 简介

`wechat-selkies` 是一个基于 Node.js 的微信 Web 端自动化工具，利用 **Puppeteer**（Chrome 无头浏览器）实现扫码登录、消息收发、好友/群聊管理，并提供简洁的 API 供脚本或机器人使用。该项目把常见的微信交互抽象为事件驱动模式，极大简化了自动化脚本的编写。

## 主要特性

| 功能 | 说明 |
|------|------|
| **扫码登录** | 通过 `puppeteer` 打开微信网页版并自动获取二维码，支持手动扫描或自动识别（需额外配置） |
| **消息收发** | 监听 `message` 事件，支持文本、图片、语音、文件等多种消息类型；亦可主动发送 |
| **好友与群聊管理** | 自动获取好友列表、群聊列表；支持拉取好友资料、同步群聊成员 |
| **事件驱动** | 既可监听单条消息，也可订阅特定关键字/消息类型，实现灵活响应 |
| **插件化** | 自定义插件可挂载到事件链，方便扩展业务逻辑 |
| **配置文件** | 支持 `config.json` 或 `dotenv` 方式快速配置登录、日志、API 端点等 |
| **稳定的会话维护** | 自动重连、刷新二维码、处理页面弹窗，保持长期稳定运行 |

## 安装与使用

```bash
# 普通安装
npm install wechat-selkies

# 或者直接克隆仓库
git clone https://github.com/nickrunning/wechat-selkies.git
cd wechat-selkies && npm i
```

```js
// init.js
const { createClient } = require('wechat-selkies');

(async () => {
  const client = createClient();

  // 登录（首次需要扫码）
  await client.login();

  // 监听消息
  client.on('message', (msg) => {
    console.log(`收到来自 ${msg.fromName} 的消息: ${msg.content}`);
    // 自动回复
    if (msg.content.includes('你好')) {
      client.sendText(msg.fromId, '你好呀~');
    }
  });

  // 你也可以发送消息
  // await client.sendText('contact-id', 'Hello World!');

  // 让脚本保持运行
  process.on('SIGINT', () => client.close());
})();
```

> **注意**  
> - 第一次启动会打开浏览器并显示二维码，需使用手机微信扫描登录。  
> - 若想避免人工操作，可在项目根目录下修改 `config.json` 开启 `autoScan`（需安装 OCR 模块）。  
> - 发送图片/文件时需要提供本地路径或可访问的 URL。

## 进阶示例

```js
// autoReply.js
const { createClient } = require('wechat-selkies');
const client = createClient();

client('message', async (msg) => {
  if (msg.type === 'text') {
    if (msg.content.match(/^天气/)) {
      const city = msg.content.replace('天气', '').trim();
      const weather = await getWeather(city); // 自定义 API
      client.sendText(msg.fromId, `现在${city}的天气是: ${weather}`);
    }
  }
});

client.login();
```

## 贡献指南

1. 本仓库  
2. 新建分支 `feature/xxx`  
3. 运行 `npm test` 确保所有测试通过  
4. PR，需要包含详细说明与必要的文档更新  

## 许可

本项目采用 MIT 许可证，欢迎使用与贡献。

---
