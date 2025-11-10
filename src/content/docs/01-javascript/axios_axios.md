---
title: axios
---


# Axios

> 项目地址: <https://github.com/axios/axios>

## 主要特性

| 特色 | 说明 |
|------|------|
| **浏览器和 node.js 双端** | 在浏览器中使用 `XMLHttpRequest`，在 node.js 中使用 `http`/`https`。 |
| **Promise API** | 基于 ES6 Promise，支持 `async/await`。 |
| **拦截器（Interceptors）** | 在请求/响应被处理前后可自定义逻辑。 |
| **请求/响应转换** | `transformRequest` 与 `transformResponse` 允许在发送/接收前修改数据。 |
| **自动处理 JSON** | 自动解析 JSON 响应并序列化请求体。 |
| **取消请求** | 通过 `CancelToken` 或 `AbortController` 取消请求。 |
| **全局与实例级配置** | 可全局设置默认值，也可创建 Axios 实例进行细粒度配置。 |
| **请求重试** | 可通过拦截器实现请求重试逻辑。 |
| **响应类型支持** | `json`, `blob`, `document`, `arraybuffer`, `text` 等。 |
| **跨域请求** | 支持 `withCredentials` 进行跨域 Cookie 传递。 |

## 功能概览

- **HTTP 方法**：`get`, `post`, `put`, `delete`, `head`, `options`, `patch` 等。
- **请求参数**：URL、请求体、配置对象（headers、params、timeout、responseType 等）。
- **响应对象**：`data`、`status`、`statusText`、`headers`、`config`、`request`。
- **拦截器 API**：
  ```js
  axios.interceptors.request.use(onFulfilled, onRejected);
  axios.interceptors.response.use(onFulfilled, onRejected);
  ```
- **取消请求**：
  ```js
  const CancelToken = axios.CancelToken;
  const source = CancelToken.source();

  axios.get('/user/12345', { cancelToken: source.token });

  // 取消请求
  source.cancel('Operation canceled by the user.');
  ```

## 使用方法

### 1. 安装

```bash
# npm
npm install axios

# yarn
yarn add axios
```

### 2. 基本请求

```js
import axios from 'axios';

// GET 请求
axios.get('/api/users')
  .then(response => console.log(response.data))
  .catch(error => console.error(error));

// POST 请求
axios.post('/api/users', {
  name: '张三',
  age: 28
})
.then(response => console.log(response.data))
.catch(error => console.error(error));
```

### 3. 使用 `async/await`

```js
async function fetchUsers() {
  try {
    const { data } = await axios.get('/api/users');
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
```

### 4. 创建实例

```js
const api = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 5000,
  headers: { 'X-Custom-Header': 'foobar' }
});

api.get('/users').then(res => console.log(res.data));
```

### 5. 请求拦截器

```js
api.interceptors.request.use(config => {
  // 在发送请求前做处理
  config.headers['Authorization'] = 'Bearer token';
  return config;
});
```

### 6. 响应拦截器

```js
api.interceptors.response.use(
  response => response, // 直接返回响应
  error => {
    // 统一错误处理
    if (error.response && error.response.status === 401) {
      // 处理未授权
    }
    return Promise.reject(error);
  }
);
```

### 7. 取消请求（AbortController）

```js
const controller = new AbortController();

axios.get('/api/slow', { signal: controller.signal })
  .then(res => console.log(res.data))
  .catch(err => console.error(err));

setTimeout(() => controller.abort(), 2000); // 2 秒后取消
```

### 8. 响应类型示例

```js
// 获取二进制文件
axios.get('/file.pdf', { responseType: 'blob' })
  .then(res => {
    const url = window.URL.createObjectURL(res.data);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'file.pdf');
    document.body.appendChild(link);
    link.click();
  });
```

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| **跨域请求失败** | 确认后端已开启 CORS，必要时设置 `withCredentials: true`。 |
| **请求被缓存** | 对 GET 请求使用 `paramsSerializer` 或在 URL 后添加随机查询参数。 |
| **响应过大** | 使用 `responseType: 'stream'`（node）或 `responseType: 'blob'`（浏览器）。 |

---
> **文档来源**：官方 README 与 GitHub 仓库（<https://github.com/axios/axios>）
