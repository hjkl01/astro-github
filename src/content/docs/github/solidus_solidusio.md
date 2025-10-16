
---
title: solidus
---

# Solidus 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/solidusio/solidus)

## 主要特性
Solidus 是一个开源的 Ruby on Rails 电商平台，基于 Spree 框架开发而成。它高度模块化、可扩展，支持多店铺、多语言和多货币功能。主要特性包括：
- **模块化设计**：核心功能分离为独立 gem，便于自定义和集成。
- **多租户支持**：支持多个独立商店或店铺管理。
- **支付和运费集成**：内置支持多种支付网关（如 Stripe、PayPal）和运费计算器。
- **库存管理**：实时库存跟踪、变体支持和供应商管理。
- **SEO 和前端友好**：内置 SEO 优化、响应式主题和 API 支持。
- **安全性**：遵循 Rails 最佳实践，包括加密和权限控制。
- **社区驱动**：活跃的开源社区，提供插件生态和持续更新。

## 主要功能
Solidus 提供完整的电商功能集，包括：
- **产品管理**：创建、分类和变体产品，支持图像、规格和税务规则。
- **购物车和结账**：用户友好的购物车、订单处理和客单支持。
- **用户和权限**：角色-based 访问控制（RBAC），支持管理员、客户和员工角色。
- **报告和分析**：内置报表工具，跟踪销售、库存和客户行为。
- **API 和集成**：RESTful API 支持第三方集成，如移动 App 或 ERP 系统。
- **国际化**：支持 i18n、多货币汇率和本地化内容。
- **促销和优惠**：折扣码、促销规则和积分系统。

## 用法
1. **安装**：
   - 确保 Ruby (2.7+) 和 Rails (6.1+) 已安装。
   - 使用 Bundler 创建新应用：`rails new my_store && cd my_store`。
   - 添加 Solidus 到 Gemfile：`gem 'solidus'`, 然后运行 `bundle install`。
   - 安装 Solidus：`rails g solidus:install --user_class=Spree::User` 并运行 `rails db:migrate`。

2. **配置**：
   - 编辑 `config/initializers/spree.rb` 配置站点设置，如默认货币、税率和支付方法。
   - 自定义主题：通过资产管道或集成前端框架如 Bootstrap。

3. **运行和开发**：
   - 启动服务器：`rails server`。
   - 访问后台：`/admin`（默认凭证：admin@example.com / test123）。
   - 添加产品：在后台创建分类和产品，或通过 Rails 控制台/种子数据导入。

4. **扩展**：
   - 安装扩展 gem，如 `solidus_paypal` 或 `solidus_stripe`，然后运行相应迁移。
   - 自定义：覆盖控制器、视图或模型以适应业务需求。
   - 部署：支持 Heroku、Capistrano 等，支持 Docker 容器化。

Solidus 适合构建可扩展的在线商店，文档详见 [官方指南](https://guides.solidus.io/)。