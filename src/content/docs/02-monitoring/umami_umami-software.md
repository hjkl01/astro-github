---
title: umami-software/umami
---

# Umami

Umami 是一个简单、快速、隐私导向的 Google Analytics 替代品。它专注于提供网站分析功能，同时保护用户隐私。

## 功能

- **隐私导向**：不收集个人数据，符合 GDPR 和其他隐私法规。
- **简单易用**：提供直观的仪表板，显示页面浏览量、访客来源等关键指标。
- **自托管**：可以部署在自己的服务器上，完全控制数据。
- **实时数据**：提供实时分析和报告。
- **自定义事件**：支持跟踪自定义事件和转化。

## 用法

### 从源码安装

1. **要求**：
   - Node.js 18.18 或更高版本
   - PostgreSQL 数据库（最低 v12.14）

2. **获取源码并安装依赖**：

   ```
   git clone https://github.com/umami-software/umami.git
   cd umami
   pnpm install
   ```

3. **配置环境**：
   创建 `.env` 文件，设置数据库连接：

   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/dbname
   ```

4. **构建应用**：

   ```
   pnpm run build
   ```

   这将创建数据库表，并生成默认管理员账户（用户名：admin，密码：umami）。

5. **启动应用**：
   ```
   pnpm run start
   ```
   默认在 `http://localhost:3000` 运行。

### 使用 Docker 安装

运行以下命令启动 Umami 和 PostgreSQL：

```
docker compose up -d
```

或拉取官方镜像：

```
docker pull docker.umami.is/umami-software/umami:latest
```

### 更新

从源码更新：

```
git pull
pnpm install
pnpm run build
```

Docker 更新：

```
docker compose pull
docker compose up --force-recreate -d
```

更多详细信息，请参考 [官方文档](https://umami.is/docs/)。
