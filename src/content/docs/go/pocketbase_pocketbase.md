---
title: pocketbase
---

# PocketBase

**项目地址**: https://github.com/pocketbase/pocketbase  

PocketBase 是一个轻量级、零配置且开箱即用的后端解决方案，使用 Go 语言编写，默认提供 REST、WebSocket、Protobuf 等多种协议。它将数据库、身份验证、文件存储、实时订阅、自动化脚本与管理面板合并于一体，适合快速原型开发与小型项目部署。  

## 主要特性

| 特性 | 说明 |
|------|------|
| **零配置** | 只需下载二进制文件或 Docker 镜像，直接运行即可。 |
| **内嵌 SQLite** | 所有数据默认存储在 `pocketbase.db` 文件，无需外部数据库服务器。 |
| **完整身份验证** | 支持 Email/Password、社交登录 (Google, GitHub)、自定义字段与自定义注册/登录流程。 |
| **多租户** | 单个实例可托管多个集合（表）并通过 API Token 控制访问。 |
| **文件存储** | 支持上传、下载、预览图片、视频等，文件默认存放在 `public` 目录。 |
| **实时订阅** | 通过 WebSocket、Subscription API 实现实时数据推送。 |
| **管理控制台** | 自带 Web UI，支持 CRUD、视图、图表、数据导入/导出、系统日志。 |
| **API 自动生成** | 自动生成 REST、GraphQL、Protobuf、gRPC、WebSocket 接口。 |
| **脚本与插件** | 通过 JS/TS 脚本实现业务逻辑、Webhook、单点登录、邮件通知等。 |
| **部署灵活** | 支持 Docker/Compose、云主机、裸机、Edge（如 Cloudflare Workers）等多种部署方式。 |

## 功能模块

| 模块 | 细节 |
|------|------|
| **Records** | 用于 CRUD 记录，支持过滤、排序、分页、聚合、视图（视图/选择器）。 |
| **Auth** | 建立用户、组织、角色；支持自定义表单字段与多因素验证。 |
| **Data** | 通过 REST/WebSocket/Python 等方式读取/写入数据库，可直接在控制台操作。 |
| **Storage** | 上传、下载、删除文件；跨域、访问权限细粒度控制。 |
| **Events** | 通过内部事件系统触发脚本（`beforeCreate`, `afterUpdate`, `onLogin` 等）。 |
| **Auto-Generated APIs** | `GET /api/records/:collectionId`、`POST /api/records/:collectionId` 等。 |
| **Admin UI** | 访问 `http://localhost:8090/_/`，可直接对收藏、字段、用户进行管理。 |

## 快速使用

1. **下载 & 启动**  
   ```bash
   # 直接下载最新版本
   curl -Ls https://github.com/pocketbase/pocketbase/releases/latest/download/pocketbase_$(uname -s)_$(uname -m).tar.gz | tar xzf -
   # 运行
   ./pocketbase serve
   ```
   或使用 Docker:
   ```bash
   docker run --rm -p 8090:8090 -v $(pwd)/pb-data:/pb-data ghcr.io/pocketbase/pocketbase:latest serve
   ```

2. **访问管理后台**  
   在浏览器打开 `http://localhost:8090/_/`，使用默认账号 `admin@pocketbase.io` / `admin` 登录。  
   - 创建 **Collections**（表）  
   - 定义字段（Text, Number, List, Relation 等）  
   - 配置权限（Read, Create, Update, Delete）

3. **使用 API**  
   ```bash
   # 获取所有记录
   curl http://localhost:8090/api/collections/<collection_id>/records
   # 创建记录
   curl -X POST http://localhost:8090/api/collections/<collection_id>/records \
        -H "Content-Type: application/json" \
        -d '{"title":"Hello", "content":"World"}'
   ```

4. **文件上传**  
   ```bash
   curl -F "file=@/path/to/image.png" http://localhost:8090/api/storage/<bucket>/<file_name>
   ```

5. **实时订阅**  
   ```js
   const socket = new WebSocket("ws://localhost:8090/api/updates");
   socket.onmessage = (event) => {
     const data = JSON.parse(event.data);
     console.log("实时更新:", data);
   };
   ```

6. **在前端快速接入**  
   通过 `fetch` 或 `axios` 调用 REST API，或使用官方 SDK（JavaScript/TypeScript）  
   ```ts
   import PocketBase from 'pocketbase';
   const pb = new PocketBase('http://localhost:8090');
   const user = await pb.collection('users').authWithPassword('login', 'pass');
   const records = await pb.collection('posts').getFullList();
   ```

## 部署建议

- **生产环境**：建议使用 Docker + Reverse Proxy（如 Nginx/Traefik）、持久化卷、TLS 证书。  
- **无服务器**：与 Netlify、Vercel 或 Cloudflare Functions 配合，利用 `pocketbase` 的自托管 API。  
- **扩展**：使用 `pocketbase/plugins` 目录添加自定义插件，实现业务扩展。

> **贴士**：所有配置和脚本均位于 `pocketbase.json` 与 `main.js`，可随时根据业务需求修改。

---
**官网 & 文档**  
- 官方网站: https://pocketbase.io  
- 开发者文档: https://pocketbase.io/docs/  
Happy coding!