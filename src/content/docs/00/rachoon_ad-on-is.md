---
title: rachoon
---

# rachoon

🦝 Rachoon — A self-hostable way to handle invoices

## 功能

Rachoon 是一个现代的自托管发票平台，专为自由职业者、小企业和希望完全控制账单的人设计。它帮助您轻松创建和跟踪发票，具有其吉祥物——好奇的浣熊的魅力。

### 主要功能

- **发票与报价**：在几秒钟内创建和管理发票和报价。
- **客户管理**：保持所有客户信息井井有条且可搜索。
- **支付跟踪**：记录支付状态、查看余额并跟踪逾期发票。
- **自定义品牌**：使用 nunjucks 高度自定义模板。
- **多货币与税支持**：灵活的税费和货币设置，支持全球账单。
- **PDF 导出**：即时下载专业外观的 PDF。
- **仪表板洞察**：获取收入、待付款和客户统计的快照。

## 用法

### 安装

使用 Docker Compose 进行安装：

```yaml
services:
  rachoon:
    image: ghcr.io/ad-on-is/rachoon
    container_name: rachoon
    environment:
      - APP_KEY=<some-app-key> # min 32 characters - used to encrypt and sign sensitive data
      - DB_CONNECTION=pg
      - GOTENBERG_URL=http://gotenberg:3000
      - PG_HOST=postgres16
      - PG_PORT=5432
      - PG_USER=<root-user>
      - PG_PASSWORD=<root-password>
      - PG_DB_NAME=rachoon
    ports:
      - 8080:8080

  gotenberg:
    image: gotenberg/gotenberg:8

  postgres16:
    container_name: postgres16
    image: postgres:16
    environment:
      - POSTGRES_USER=<root-user>
      - POSTGRES_PASSWORD=<root-password>
    volumes:
      - ./rachoon-data:/var/lib/postgresql/data
```

### 首次使用

1. 访问：http://localhost:8080/signup
2. 创建您的账户
3. 开始开票

## 技术栈

- **前端**：Nuxt.js
- **后端**：adonisJS
- **数据库**：PostgreSQL
- **PDF 引擎**：Gotenberg
- **部署**：Docker 就绪，可在任何地方运行。
