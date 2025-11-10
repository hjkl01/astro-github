---
title: paperless-ngx
---


# paperless-ngx

**项目地址**：<https://github.com/paperless-ngx/paperless-ngx>

## 项目简介

paperless-ngx 是一个开源的文档管理系统，旨在帮助个人和团队轻松组织、索引和检索纸质文件、扫描件和电子文件。它基于 Docker 容器化，支持多语言、全文搜索、标签管理、文件转化等功能。

## 主要特性

| 特性 | 说明 |
|------|------|
| **文档索引** | 自动识别并索引PDF、图片、Office 文档、文本文件等，支持 OCR（Tesseract）提取内容。 |
| **全文搜索** | 通过 Elasticsearch 或 Whoosh（默认）实现高效全文检索，支持模糊查询、布尔运算和正则表达式。 |
| **标签与归档** | 通过预定义或自定义标签对文档进行分类；支持自动归档规则（按日期、文件类型、标签等）。 |
| **文件转化** | 支持将PDF、图像、Office文档等转换为统一的PDF格式，提升兼容性。 |
| **多语言支持** | 默认支持中文、英文等多种语言，界面与 OCR 文字识别均可切换。 |
| **API 接口** | 提供 RESTful API，支持与第三方应用（如邮件、文件同步服务）集成。 |
| **Docker 原生** | 通过 Docker Compose 一键部署，支持持久化存储、网络配置及版本管理。 |
| **安全性** | 基于 HTTPS、JWT 认证、细粒度权限控制，支持 LDAP/Google OAuth 等身份验证。 |
| **插件机制** | 通过插件可扩展功能，如与 Google Drive、Dropbox、WebDAV 等服务集成。 |

## 核心功能

1. **文档导入**  
   - 支持从文件夹、扫描设备、邮件附件、云存储等多种来源批量导入。  
   - 自动执行 OCR、分类、标签分配、归档。

2. **文档搜索**  
   - 通过关键词、标签、日期范围、文件类型等多维度过滤。  
   - 支持全文检索与模糊匹配。

3. **文档管理**  
   - 查看、编辑、删除文档及其元数据。  
   - 通过标签、归档规则快速定位文件。  
   - 批量操作（批量标签添加、批量归档等）。

4. **系统管理**  
   - 用户与权限管理（管理员、普通用户）。  
   - 日志审计、备份与恢复。  
   - 定时任务（归档、索引、清理旧文件）。

5. **API 与集成**  
   - 提供完整的 REST API，支持自动化脚本、第三方应用调用。  
   - 通过插件与外部服务无缝对接（Google Drive、Dropbox、WebDAV 等）。

## 安装与使用

### 1. 准备环境

- Docker Engine 18.06+  
- Docker Compose 1.25+  
- 服务器或本地机器（可使用 Raspberry Pi、NAS 等）

### 2. 克隆仓库

```bash
git clone https://github.com/paperless-ngx/paperless-ngx.git
cd paperless-ngx
```

### 3. 配置

- 复制示例配置文件：

```bash
cp docker-compose.yml.example docker-compose.yml
```

- 编辑 `docker-compose.yml` 或 `.env`，设置数据库、网络、存储路径等：

```env
PAPERLESS_MODE=dev
PAPERLESS_DB_HOST=postgres
PAPERLESS_DB_PORT=5432
PAPERLESS_DB_NAME=paperless
PAPERLESS_DB_USER=paperless
PAPERLESS_DB_PASSWORD=paperless
```

- 挂载持久化目录：

```
/path/to/data:/usr/src/paperless/data
/path/to/media:/usr/src/paperless/media
```

### 4. 启动

```bash
docker compose up -d
```

- 第一次启动会自动创建数据库、索引，并在浏览器打开 `http://localhost:8000`（或指定端口）。

### 5. 登录

- 默认管理员账号：`admin@paperless.com`  
- 默认密码：`admin`

> 建议首次登录后立即修改密码。

### 6. 文档导入

- 通过 Web UI 上传文件，或将文件放入指定的 `consume` 文件夹（如 `/path/to/data/consume`），系统会自动处理。

### 7. 查询与管理

- 在 UI 中使用搜索栏、标签筛选、归档视图浏览文档。  
- 通过 API 进行自动化查询，例如：

```bash
curl -X GET "http://localhost:8000/api/documents/?search=invoice" \
     -H "Authorization: Token <YOUR_TOKEN>"
```

### 8. 备份与恢复

- 备份数据库：`docker exec <container> pg_dump -U paperless paperless > dump.sql`  
- 备份文件：复制 `data` 与 `media` 目录。  
- 恢复时，先恢复数据库，再复制文件并重新启动容器。

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| OCR 识别错误 | 确认 `tesseract` 语言包已安装，或更换 `OCR_LANGUAGES` 配置 |
| 索引慢 | 调整 `ELASTICSEARCH_URL` 或切换至 Whoosh（默认） |
| Docker 容器崩溃 | 查看日志：`docker logs <container>`，检查磁盘空间、权限问题 |

## 进一步阅读

- 官方文档: <https://docs.paperless-ngx.com/>  
- 贡献指南: <https://github.com/paperless-ngx/paperless-ngx/blob/main/CONTRIBUTING.md>  
- API 参考: <https://docs.paperless-ngx.com/api/>  

---
> 以上内容为项目的核心功能与使用方式概述，若需更详细的操作步骤，请查阅官方文档。
