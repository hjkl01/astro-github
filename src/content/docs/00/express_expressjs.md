
---
title: express
---


# Express.js

> 项目地址: https://github.com/expressjs/express

Express.js 是一个极简、灵活的 Node.js Web 框架，用于快速构建 Web 应用与 API。其核心理念是通过中间件（middleware）组合实现功能，提供丰富的路由、模板、错误处理等特性。

## 主要特性

| 特性 | 说明 |
|------|------|
| **路由** | 支持 HTTP 方法（GET、POST、PUT、DELETE 等）和路径参数、查询字符串、RESTful 路由。 |
| **中间件** | 核心概念：可在请求生命周期中插入自定义逻辑，支持链式调用。 |
| **模板引擎** | 原生支持 `Jade/Pug`, `EJS`, `Handlebars` 等，可通过 `app.set('view engine', 'pug')` 设置。 |
| **静态文件服务** | `express.static()` 自动托管 `public/` 目录下的文件。 |
| **错误处理** | 统一错误处理中间件，返回标准化错误信息。 |
| **Cookie & Session** | 通过 `cookie-parser`、`express-session` 等插件实现。 |
| **Body 解析** | `express.json()`、`express.urlencoded()` 处理请求体。 |
| **跨域** | 可使用 `cors` 中间件开启跨域访问。 |
| **插件生态** | 丰富的第三方中间件，支持验证、日志、性能监控等。 |

## 安装

```bash
npm install express
```

## 基本用法

```js
const express = require('express');
const app = express();

// 解析 JSON 体
app.use(express.json());

// 静态文件
app.use(express.static('public'));

// 路由
app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

app.post('/api/data', (req, res) => {
  const data = req.body;
  res.json({ received: data });
});

// 错误处理中间件
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Error' });
});

// 启动服务器
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

## 进一步学习

- 官方文档: https://expressjs.com/
- GitHub 仓库: https://github.com/expressjs/express
- 示例项目: https://github.com/expressjs/express/tree/master/examples

```

*(将上述内容保存为 `src/content/docs/00/express_expressjs.md`。)*
