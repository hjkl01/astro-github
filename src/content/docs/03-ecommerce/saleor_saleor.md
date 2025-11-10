---
title: saleor
---

# Saleor 项目

## 项目地址
[GitHub 项目地址](https://github.com/saleor/saleor)

## 主要特性
Saleor 是一个开源的电子商务平台，基于 Python 和 Django 框架构建，采用 GraphQL API 作为核心接口。它高度模块化、可扩展，支持多语言、多货币和多门店管理。关键特性包括：
- **无头架构（Headless）**：分离前端和后端，便于集成各种前端框架如 React、Vue 或移动应用。
- **GraphQL 支持**：提供高效的 API 查询和 mutation 操作，支持实时数据订阅。
- **多渠道销售**：支持在线商店、实体店、社交媒体和市场平台的多渠道整合。
- **库存与订单管理**：实时库存跟踪、订单处理、退货和促销规则。
- **支付与物流集成**：内置 Stripe、PayPal 等支付网关，以及 UPS、FedEx 等物流服务。
- **SEO 和分析**：内置 SEO 工具、Google Analytics 集成和报告仪表板。
- **安全性与合规**：支持 GDPR、PCI DSS 合规，包含用户认证和数据加密。

## 主要功能
- **产品管理**：创建、分类和变体产品，支持数字和物理商品，包含图片、规格和定价。
- **用户与权限**：客户账户管理、角色-based 访问控制（RBAC），支持员工和管理员权限。
- **购物车与结账**：高级购物车功能，包括优惠券、税费计算和一键结账。
- **内容管理**：页面构建器、博客和自定义 CMS 模块。
- **扩展性**：插件系统允许自定义 webhook、集成第三方服务如 ERP 或 CRM。
- **移动友好**：响应式设计，支持 PWA（渐进式 Web 应用）。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/saleor/saleor.git`
   - 安装依赖：使用 Python 3.8+ 和 pip 安装 requirements.txt。
   - 设置数据库：支持 PostgreSQL 或 MySQL，运行迁移：`python manage.py migrate`。
   - 启动服务器：`python manage.py runserver`。

2. **配置**：
   - 编辑 `settings.py` 配置数据库、邮件服务和 API 密钥。
   - 使用 Docker 部署：运行 `docker-compose up` 以快速启动开发环境。

3. **开发与使用**：
   - 通过 Django 管理面板（`/dashboard/`）管理后台。
   - 构建前端：使用 Saleor 的 Storefront API 集成自定义 UI。
   - API 测试：使用 GraphQL Playground（`/graphql/`）查询数据。
   - 生产部署：推荐使用 Heroku、AWS 或 Kubernetes，支持 CI/CD 管道。

项目文档详见仓库的 `docs/` 目录，适合开发者构建自定义电商解决方案。