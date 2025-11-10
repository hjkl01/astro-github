---
title: stremio-web
---

# Stremio Web

## 功能

Stremio Web 是一个现代化的媒体中心，提供一站式视频娱乐解决方案。用户可以通过易于安装的插件发现、观看和组织视频内容。

主要功能包括：

- **Board**：展示用户的内容板。
- **Discover**：发现新的视频内容。
- **Meta Details**：查看媒体的详细信息。

## 用法

### 前置条件

- Node.js 12 或更高版本
- pnpm 10 或更高版本

### 安装依赖

```bash
pnpm install
```

### 启动开发服务器

```bash
pnpm start
```

### 生产构建

```bash
pnpm run build
```

### 使用 Docker 运行

```bash
docker build -t stremio-web .
docker run -p 8080:8080 stremio-web
```

许可证：GPL-2.0
