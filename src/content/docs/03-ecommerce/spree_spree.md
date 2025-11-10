---
title: spree
---

# Spree 项目描述

## 项目地址
[https://github.com/spree/spree](https://github.com/spree/spree)

## 主要特性
Spree 是一个开源的电子商务平台，基于 Ruby on Rails 框架构建。它提供了一个灵活、可扩展的解决方案，用于快速构建在线商店。主要特性包括：
- **多商店支持**：允许管理多个独立或关联的在线商店。
- **多语言和多货币**：支持国际化，包括本地化语言和货币转换。
- **库存管理**：实时跟踪产品库存，支持变体（如尺寸、颜色）。
- **支付集成**：内置支持多种支付网关，如 Stripe、PayPal 和 Authorize.net。
- **运费计算**：集成各种运费提供商，如 UPS、FedEx，支持自定义规则。
- **用户管理和权限**：角色-based 访问控制（RBAC），支持客户、管理员和员工角色。
- **SEO 优化**：内置元标签、URL 友好结构和 sitemap 生成。
- **移动响应式设计**：前端基于现代 CSS 框架，确保在各种设备上的良好体验。
- **扩展性**：通过 Rails 引擎机制，支持插件扩展，如社交登录、促销和分析工具。

## 主要功能
Spree 的核心功能覆盖电子商务的全生命周期：
- **产品管理**：添加、编辑产品，包括图像、规格、分类和税务设置。
- **购物车和结账**：用户友好的购物车，支持愿望清单、一键结账和订单跟踪。
- **促销和优惠**：创建折扣券、促销规则和捆绑销售。
- **订单处理**：后台管理订单状态、退货和退款流程。
- **内容管理**：页面、博客和静态内容的 CMS 功能。
- **报告和分析**：销售报告、库存洞察和客户行为跟踪。
- **API 支持**：RESTful API 允许第三方集成，如移动 App 或 ERP 系统。

## 用法
1. **安装**：
   - 确保安装 Ruby（推荐 3.0+）和 Rails（7.0+）。
   - 克隆仓库：`git clone https://github.com/spree/spree.git`。
   - 安装依赖：`bundle install` 和 `npm install`（如果使用前端资产）。
   - 设置数据库：`rails db:create db:migrate`（支持 PostgreSQL、MySQL 等）。
   - 运行服务器：`rails server`。

2. **配置**：
   - 编辑 `config/initializers/spree.rb` 配置站点名称、默认货币等。
   - 通过 Rails 控制台或后台面板（`/admin`）添加产品和设置。
   - 集成支付/运费：在后台启用并配置 API 密钥。

3. **开发和扩展**：
   - 使用 `spree install --sandbox` 创建沙箱环境进行测试。
   - 扩展功能：创建自定义 Rails 引擎或使用社区扩展（如 spree_auth_devise 用于认证）。
   - 部署：支持 Heroku、Capistrano 等；生产环境需配置缓存（如 Redis）和 CDN。

4. **后台管理**：
   - 访问 `/admin` 登录（默认 admin@example.com / test123）。
   - 管理所有功能，包括用户、产品和订单。

Spree 适合从小型商店到大型电商平台的开发，社区活跃，提供详细文档和示例。