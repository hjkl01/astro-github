---
title: axios
---

## 项目简介

Axios 是一个基于 Promise 的 HTTP 客户端库，可用于浏览器和 Node.js 环境。它提供了简单易用的 API 来发送 HTTP 请求，支持请求和响应的拦截、数据转换、请求取消等功能。

## 主要功能

- **Promise 基础**：使用 Promise API 处理异步请求，支持 async/await 语法。
- **浏览器支持**：在浏览器中使用 XMLHttpRequests 发送请求。
- **Node.js 支持**：在 Node.js 中使用 http 模块发送请求。
- **拦截器**：支持请求和响应拦截器，用于添加自定义逻辑或转换数据。
- **数据转换**：自动序列化和解析 JSON 数据。
- **请求取消**：支持取消正在进行的请求。
- **跨站点请求伪造 (XSRF) 保护**：客户端支持防止 XSRF 攻击。
- **进度捕获**：支持上传和下载进度监控。
- **多种数据格式**：支持 application/x-www-form-urlencoded 和 multipart/form-data 格式。
- **TypeScript 支持**：提供完整的 TypeScript 类型定义。
- **解压缩**：自动解压缩响应体。
- **不安全 HTTP 解析器**：接受无效 HTTP 头部的解析器（不推荐）。
- **向后兼容选项**：用于旧版本兼容的选项，如静默 JSON 解析。
- **环境配置**：FormData 类等环境特定配置。
- **表单序列化器**：自定义表单数据序列化选项。
- **速率限制**：在 Node.js 中设置上传/下载速率限制。
- **Fetch 适配器**：使用 Fetch API 作为适配器，支持流式响应。
- **AxiosHeaders 快捷方式**：便捷的头部操作方法。
- **自定义实例**：创建具有预配置设置的 Axios 实例。
- **请求方法别名**：GET, POST, PUT, DELETE 等便捷方法。

## 安装

### 使用 npm

```bash
npm install axios
```

### 使用 yarn

```bash
yarn add axios
```

### 使用 pnpm

```bash
pnpm add axios
```

### 使用 bun

```bash
bun add axios
```

### CDN

```html
<script src="https://cdn.jsdelivr.net/npm/axios@1.6.7/dist/axios.min.js"></script>
```

## 基本用法

### 导入库

```javascript
import axios from 'axios';
// 或者使用 require
const axios = require('axios');
```

### 发送 GET 请求

```javascript
// 简单 GET 请求
const response = await axios.get('/user?ID=12345');

// 使用配置对象
axios
  .get('/user', {
    params: {
      ID: 12345,
    },
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
```

### 发送 POST 请求

```javascript
const response = await axios.post('/user', {
  firstName: 'Fred',
  lastName: 'Flintstone',
});
console.log(response);
```

### 并发请求

```javascript
function getUserAccount() {
  return axios.get('/user/12345');
}

function getUserPermissions() {
  return axios.get('/user/12345/permissions');
}

Promise.all([getUserAccount(), getUserPermissions()]).then(function (results) {
  const acct = results[0];
  const perm = results[1];
});
```

### 配置请求

```javascript
axios({
  method: 'post',
  url: '/user/12345',
  data: {
    firstName: 'Fred',
    lastName: 'Flintstone',
  },
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 1000,
});
```

### 使用拦截器

```javascript
// 请求拦截器
axios.interceptors.request.use(
  function (config) {
    // 在发送请求之前做些什么
    return config;
  },
  function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

// 响应拦截器
axios.interceptors.response.use(
  function (response) {
    // 对响应数据做点什么
    return response;
  },
  function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
  }
);
```

### 错误处理

```javascript
axios.get('/user/12345').catch(function (error) {
  if (error.response) {
    // 请求已发出，但服务器响应的状态码不在 2xx 范围内
    console.log(error.response.data);
    console.log(error.response.status);
    console.log(error.response.headers);
  } else if (error.request) {
    // 请求已发出，但没有收到响应
    console.log(error.request);
  } else {
    // 发送请求时出了点问题
    console.log('Error', error.message);
  }
  console.log(error.config);
});
```

### 使用 Fetch 适配器

```javascript
const { data } = await axios.get(url, {
  adapter: 'fetch',
});
```

### 自定义 Fetch API

```javascript
import customFetchFunction from 'customFetchModule';

const instance = axios.create({
  adapter: 'fetch',
  env: {
    fetch: customFetchFunction,
    Request: null,
    Response: null,
  },
});
```

### AxiosHeaders 快捷方式

```javascript
const headers = new AxiosHeaders();
headers.setContentType('application/json');
console.log(headers.getContentType()); // 'application/json'
```

### 创建自定义实例

```javascript
const instance = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 1000,
  headers: { 'X-Custom-Header': 'foobar' },
});
```

### 请求方法别名

```javascript
axios.get('/user/12345');
axios.post('/user', {
  firstName: 'Fred',
  lastName: 'Flintstone',
});
```

## 许可证

MIT License
