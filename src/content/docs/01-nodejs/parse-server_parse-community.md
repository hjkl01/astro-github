---
title: parse-server
---

# Parse Server

## 项目地址
[GitHub 项目地址](https://github.com/parse-community/parse-server#getting-started)

## 主要特性
Parse Server 是一个开源的后端服务器框架，由 Parse 社区维护。它基于 Node.js 构建，提供了一个完整的后端即服务 (BaaS) 解决方案。主要特性包括：
- **用户认证**：支持多种认证方式，如电子邮件/密码、OAuth（Facebook、Google 等）和自定义认证。
- **数据存储**：使用 MongoDB 或其他数据库作为后端，提供实时数据同步和查询功能，支持复杂的关系型数据模型。
- **云函数**：允许开发者编写服务器端 JavaScript 函数来处理业务逻辑，支持触发器（如 beforeSave、afterSave）。
- **推送通知**：集成推送服务（如 Firebase Cloud Messaging），支持移动应用的实时通知。
- **文件存储**：支持文件上传和存储，可集成云存储服务如 AWS S3 或 GridFS。
- **实时消息**：通过 LiveQuery 功能实现实时数据订阅和更新。
- **GraphQL 支持**：内置 GraphQL API，允许灵活的查询和变更数据。
- **可扩展性**：模块化设计，支持自定义适配器和插件，便于集成第三方服务。

## 主要功能
Parse Server 的核心功能旨在简化移动和 Web 应用的开发，提供开箱即用的后端服务：
- **数据库操作**：CRUD 操作（创建、读取、更新、删除），支持 ACL（访问控制列表）来管理数据权限。
- **角色与权限管理**：内置用户角色系统，确保数据安全。
- **仪表板**：提供 Parse Dashboard 用于可视化管理数据、用户和文件。
- **多租户支持**：可配置为支持多个应用实例。
- **离线支持**：通过 Parse SDK 实现本地数据缓存和同步（适用于客户端）。
- **安全特性**：防范常见攻击，如 SQL 注入、CSRF，并支持 HTTPS 和 JWT 令牌。

## 用法
### 安装与设置
1. **前提条件**：安装 Node.js（v14+）和 MongoDB。
2. **安装 Parse Server**：
   ```
   npm install -g parse-server
   ```
3. **基本启动**：
   创建一个 `index.js` 文件：
   ```javascript
   const express = require('express');
   const ParseServer = require('parse-server').ParseServer;

   const app = express();
   const api = new ParseServer({
     databaseURI: 'mongodb://localhost:27017/dev', // MongoDB 连接字符串
     appId: 'myAppId',
     masterKey: 'myMasterKey', // 用于管理员访问
     serverURL: 'http://localhost:1337/parse', // 服务器 URL
   });

   app.use('/parse', api);
   app.listen(1337, () => {
     console.log('Parse Server running on port 1337.');
   });
   ```
   运行：`node index.js`。

### 客户端集成
- **iOS/Android/Web**：使用官方 Parse SDK（如 parse-ios-sdk、parse-android-sdk 或 JavaScript SDK）。
- 示例（JavaScript SDK）：
  ```javascript
  Parse.initialize('myAppId', 'myJSKey');
  Parse.serverURL = 'http://localhost:1337/parse';

  // 保存对象
  const GameScore = Parse.Object.extend('GameScore');
  const gameScore = new GameScore();
  gameScore.set('score', 1337);
  gameScore.set('playerName', 'Sean Plott');
  gameScore.setACL(new Parse.ACL(Parse.User.current()));
  gameScore.save().then((obj) => {
    console.log('Saved successfully');
  });
  ```

### 高级用法
- **云函数**：在 `cloud/main.js` 中定义函数，然后通过 `Parse.Cloud.run('hello', {useMasterKey: true})` 调用。
- **部署**：支持 Heroku、AWS 等云平台部署，或使用 Docker 容器化。
- **文档参考**：详见官方 GitHub 仓库的 [Getting Started](https://github.com/parse-community/parse-server#getting-started) 部分，包含完整配置指南和迁移工具（从 Parse.com 迁移）。