
---
title: memos
---


# Memos 使用说明

> GitHub 项目地址：<https://github.com/usememos/memos>

---

## 一、项目概述

Memos 是一款轻量、开源、跨平台的笔记与知识管理系统。支持 Markdown、标签、链接、代码块、文件上传等多种内容类型，旨在帮助个人或团队快速记录、整理、共享知识。项目采用 Go 语言开发，前端使用 Vue3，后端提供 RESTful API 与 GraphQL，支持 Docker、Kubernetes 等容器化部署。

---

## 二、主要特性

| # | 特性 | 说明 |
|---|------|------|
| 1 | **Markdown 支持** | 通过 Markdown 语法编写笔记，支持代码高亮、表格、数学公式等。 |
| 2 | **标签与分类** | 给笔记打标签，支持多标签查询、标签云。 |
| 3 | **全文检索** | 内置全文索引，支持关键字搜索、模糊匹配。 |
| 4 | **文件上传** | 支持图片、文档、代码片段等文件上传，生成可直接嵌入的链接。 |
| 5 | **权限与分享** | 公开/私有笔记，支持链接分享、协作者编辑。 |
| 6 | **多端同步** | 通过 API 在多台设备间同步数据，支持 Web、桌面、移动端。 |
| 7 | **插件/扩展** | 通过插件接口可接入第三方服务（如 Git、ChatGPT）。 |
| 8 | **容器化部署** | 官方提供 Docker Compose、Dockerfile、Helm Chart，便于快速部署。 |
| 9 | **备份与恢复** | 支持数据库备份、导入导出，恢复历史数据。 |
|10 | **多语言支持** | UI 提供多语言切换，默认中文/英文。 |

---

## 三、核心功能

1. **创建/编辑笔记**  
   - 通过 Web UI 或 API 创建笔记，支持 Markdown 编辑器。  
   - 自动保存草稿，支持版本回溯。  

2. **管理标签**  
   - 新增、编辑、删除标签。  
   - 通过标签过滤笔记。  

3. **搜索**  
   - 关键字搜索、正则搜索、时间范围搜索。  

4. **分享**  
   - 生成公开链接，设置访问权限。  
   - 通过内嵌链接分享给团队成员。  

5. **文件管理**  
   - 上传文件后生成可访问 URL。  
   - 支持文件预览。  

6. **API**  
   - `GET /api/v1/notes`：获取笔记列表。  
   - `POST /api/v1/notes`：创建笔记。  
   - `PUT /api/v1/notes/:id`：更新笔记。  
   - `DELETE /api/v1/notes/:id`：删除笔记。  
   - 其它接口包括标签、文件、用户等。  

7. **权限控制**  
   - 角色体系：管理员、成员、访客。  
   - 对笔记、标签、文件分别设置读/写权限。  

---

## 四、快速安装与使用

### 4.1 Docker 部署（推荐）

```bash
# 克隆仓库
git clone https://github.com/usememos/memos.git
cd memos

# 启动数据库（PostgreSQL 15+）
docker run -d --name memos-db \
  -e POSTGRES_PASSWORD=your_password \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=memos \
  -p 5432:5432 postgres:15

# 启动 Memos
docker run -d --name memos \
  -e MEMOS_DB_DSN="postgres://postgres:your_password@host.docker.internal:5432/memos?sslmode=disable" \
  -p 5234:5234 \
  usememos/memos:latest
```

> **注意**  
> - `MEMOS_DB_DSN` 必须指向可访问的 PostgreSQL。  
> - 生产环境请开启 HTTPS（使用 Nginx/Traefik 等反向代理）并配置 `MEMOS_SERVER_HTTPS_KEY`、`MEMOS_SERVER_HTTPS_CERT`。  

### 4.2 二进制部署

```bash
# 下载最新发行版
wget https://github.com/usememos/memos/releases/latest/download/memos-linux-amd64.tar.gz
tar -xzf memos-linux-amd64.tar.gz
cd memos

# 配置环境变量
export MEMOS_DB_DSN="postgres://postgres:your_password@localhost:5432/memos?sslmode=disable"

# 启动
./memos
```

### 4.3 登录与使用

1. 打开浏览器访问 `http://<host>:5234`。  
2. 第一次访问会弹出管理员注册页面，填写邮箱、密码完成注册。  
3. 登录后即可创建笔记、上传文件、添加标签。  
4. 使用左侧导航栏快速切换标签、搜索框、设置页。  

### 4.4 API 调用示例

```bash
# 创建笔记（JSON）
curl -X POST http://localhost:5234/api/v1/notes \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"content":"# 这是标题\n内容文字"}'
```

> 生成的 `Authorization` Token 可在用户设置 > API Token 页面获取。

---

## 五、常见问题

- **如何导入已有 Markdown 笔记？**  
  通过 API 批量上传，或直接在 Web UI 使用“导入 Markdown”功能。  

- **如何备份数据库？**  
  PostgreSQL 直接使用 `pg_dump` 或 `pg_basebackup`，Memos 本身不提供备份脚本。  

- **是否支持多租户？**  
  默认不支持多租户，建议在容器化部署时为每个团队部署独立实例。  

---

## 六、贡献与交流

- Issue 反馈：<https://github.com/usememos/memos/issues>  
- Pull Request：欢迎 PR，遵循项目代码规范。  
- 社区交流：Telegram 群、Discord 服务器等（可在 README 中查找链接）。  

---

> **项目地址**  
> - GitHub: <https://github.com/usememos/memos>  
> - 官方文档: <https://docs.usememos.com>  

祝使用愉快！  
