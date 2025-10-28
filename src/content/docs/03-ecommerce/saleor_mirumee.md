
---
title: saleor
---

# Saleor 项目

**GitHub 项目地址:** [https://github.com/mirumee/saleor](https://github.com/mirumee/saleor)

## 主要特性
Saleor 是一个开源的电子商务平台，基于 Python 和 Django 框架构建，采用 GraphQL API 作为核心接口。它高度模块化、可扩展，支持多渠道销售（如网站、移动应用和 POS 系统）。关键特性包括：
- **无头架构（Headless Commerce）**：分离前端和后端，提供灵活的 API 集成，支持自定义前端（如 React、Vue.js）。
- **多租户支持**：允许多个商店在单一实例中运行，适合 SaaS 模式。
- **国际化与本地化**：支持多语言、多货币和多地区税率计算。
- **库存与订单管理**：实时库存跟踪、订单处理、退货和促销规则。
- **支付与集成**：集成 Stripe、PayPal 等支付网关，以及 ERP、CRM 等第三方服务。
- **SEO 和性能优化**：内置 SEO 工具、高性能缓存和 PWA 支持。
- **安全性**：符合 GDPR 和 PCI DSS 标准，提供用户认证和数据加密。

## 主要功能
- **产品管理**：创建、分类和变体产品，支持数字和实体商品。
- **购物车与结账**：高级购物车功能，包括优惠券、愿望清单和一键结账。
- **客户管理**：用户注册、个人信息管理、忠诚度程序和分销网络。
- **分析与报告**：仪表板提供销售数据、客户行为和库存洞察。
- **API 驱动**：GraphQL API 支持查询和变异操作，便于移动和 Web 开发。
- **扩展性**：通过插件系统添加自定义功能，如促销引擎或集成模块。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/mirumee/saleor.git`
   - 安装依赖：`pip install -r requirements.txt`
   - 设置环境变量（如数据库配置、SECRET_KEY），运行 `python manage.py migrate` 初始化数据库。
   - 启动开发服务器：`python manage.py runserver`

2. **配置**：
   - 使用 Django Admin 或 Dashboard 配置商店设置、产品和用户。
   - 集成前端：通过 GraphQL API 连接自定义前端框架。

3. **部署**：
   - 支持 Docker 部署：使用提供的 Dockerfile 和 docker-compose.yml。
   - 生产环境推荐使用 PostgreSQL 数据库、Redis 缓存和 Nginx 反向代理。
   - 访问 Dashboard：默认 URL 为 `/dashboard/`，初始凭证在文档中。

详细文档和示例见项目 README 和 [官方文档](https://docs.saleor.io/)。适合开发者构建可扩展的在线商店。