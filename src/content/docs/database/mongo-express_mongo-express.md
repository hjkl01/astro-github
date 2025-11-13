---
title: mongo-express
---

# mongo-express 项目

## 项目地址
[GitHub 项目地址](https://github.com/mongo-express/mongo-express)

## 主要特性
mongo-express 是一个轻量级的 Web 界面，用于 MongoDB 数据库的管理。它基于 Node.js 开发，提供了一个直观的图形化工具来浏览、查询和操作 MongoDB 数据。核心特性包括：
- **Web-based 界面**：通过浏览器访问，支持实时查看和编辑数据库。
- **多数据库支持**：可以连接多个 MongoDB 实例，并切换管理不同数据库。
- **用户认证**：内置基本认证机制，支持用户名/密码登录。
- **实时查询**：支持 MongoDB 查询语言（包括聚合管道），并显示结果。
- **数据操作**：允许创建、读取、更新和删除（CRUD）集合中的文档。
- **文件上传**：支持上传文件到 GridFS。
- **主题和自定义**：可自定义界面主题和配置选项。
- **Docker 支持**：易于通过 Docker 部署，适合容器化环境。

## 主要功能
- **数据库浏览**：列出所有数据库、集合，并查看文档结构。
- **查询与过滤**：执行自定义查询，支持排序、分页和投影。
- **文档编辑**：直接在界面中编辑 JSON 文档，支持批量操作。
- **索引管理**：查看和创建集合索引。
- **统计信息**：显示数据库统计、集合大小和性能指标。
- **连接管理**：支持 MongoDB 的副本集、共享集群和 SSL 连接。
- **导出/导入**：基本的数据导出功能（JSON 格式）。

## 用法
### 安装与运行
1. **前提条件**：确保 Node.js 已安装（推荐 v14+），并有 MongoDB 服务器运行。
2. **克隆仓库**：
   ```
   git clone https://github.com/mongo-express/mongo-express.git
   cd mongo-express
   ```
3. **安装依赖**：
   ```
   npm install
   ```
4. **配置**：
   编辑 `config.js` 或使用环境变量设置 MongoDB 连接字符串（如 `ME_CONFIG_MONGODB_URL=mongodb://localhost:27017`），以及认证信息（如 `ME_CONFIG_BASICAUTH_USERNAME` 和 `ME_CONFIG_BASICAUTH_PASSWORD`）。
5. **启动**：
   ```
   npm start
   ```
   应用将在 `http://localhost:8080` 上运行。使用浏览器访问，并输入认证凭据登录。

### Docker 部署（推荐）
使用官方 Docker 镜像快速启动：
```
docker run -it --rm \
  -p 8081:8081 \
  -e ME_CONFIG_MONGODB_URL="mongodb://mongo:27017" \
  -e ME_CONFIG_BASICAUTH_USERNAME=admin \
  -e ME_CONFIG_BASICAUTH_PASSWORD=pass \
  mongo-express
```
- 将 `mongo:27017` 替换为你的 MongoDB 主机和端口。
- 访问 `http://localhost:8081`。

### 使用界面
- 登录后，选择数据库和集合。
- 使用左侧导航浏览数据。
- 在查询栏输入 MongoDB 查询（如 `{ "field": "value" }`）并执行。
- 编辑文档时，直接修改 JSON 并保存。

更多细节请参考项目 README 和官方文档。