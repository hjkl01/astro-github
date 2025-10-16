
---
title: django-oscar
---

# Django Oscar 项目

## 项目地址
[GitHub 项目地址](https://github.com/django-oscar/django-oscar)

## 主要特性
Django Oscar 是一个开源的 Django 应用程序框架，专为构建可定制的在线电商网站而设计。它采用模块化设计，允许开发者灵活扩展和自定义功能。主要特性包括：
- **高度可定制**：基于 Django 的类视图（Class-Based Views）和模型，提供“可插拔”的架构，用户可以轻松覆盖或扩展核心组件，而无需从头构建电商系统。
- **多商店支持**：支持多站点、多货币和多语言的电商平台，适用于 B2C、B2B 等场景。
- **丰富的核心功能**：内置产品目录管理、购物车、结账流程、订单处理、促销规则（如折扣、优惠券）和库存管理。
- **集成友好**：无缝集成 Django 的生态系统，支持第三方支付网关（如 Stripe、PayPal）、搜索引擎（如 Haystack）和缓存系统。
- **安全性与扩展性**：遵循 Django 的最佳实践，提供安全的用户认证、权限控制，并支持大规模部署。

## 主要功能
- **产品管理**：支持产品分类、属性、变体（如尺寸、颜色）和搜索功能。管理员可以通过 Django Admin 界面轻松管理商品。
- **购物车与结账**：用户友好的购物车，支持匿名用户和持久化购物车。结账流程包括地址管理、支付和订单确认。
- **订单与履行**：处理订单生命周期，包括发货、退款和客户服务。支持与仓库系统的集成。
- **促销与营销**：内置优惠规则引擎，支持范围促销、产品折扣和捆绑销售。
- **仪表板与报告**：提供商家仪表板，用于监控销售、库存和分析数据。
- **API 支持**：通过 Django REST Framework 扩展，提供 RESTful API，便于移动端或 headless 电商开发。

## 用法
1. **安装**：
   - 确保安装 Python 3.8+ 和 Django 3.2+。
   - 使用 pip 安装：`pip install django-oscar`。
   - 对于完整功能，可能需要额外依赖如 `django-photologue`（图像处理）或 `celery`（异步任务）。

2. **项目设置**：
   - 创建新 Django 项目：`django-admin startproject myproject`。
   - 在 `settings.py` 中添加 Oscar 应用：`INSTALLED_APPS` 中包含 `'oscar'` 和其依赖（如 `'oscar.apps.analytics'`）。
   - 配置数据库（推荐 PostgreSQL）和静态文件。运行迁移：`python manage.py migrate`。
   - 设置 URL：在 `urls.py` 中包含 Oscar 的 URL 配置：`path('shop/', include('oscar.urls'))`。

3. **自定义与开发**：
   - 使用 Oscar 的“应用钩子”（app hooks）来覆盖默认视图和模型。例如，创建自定义 `Product` 模型继承 Oscar 的基类。
   - 运行开发服务器：`python manage.py runserver`，访问 `/shop/` 查看默认电商界面。
   - 通过 Django Admin 添加产品、类别和促销规则。
   - 对于生产环境，配置支付后端、邮件服务和部署（如使用 Gunicorn + Nginx）。

4. **示例用法**：
   - 构建简单电商：继承 Oscar 的模板和视图，添加自定义页面。
   - 扩展高级功能：集成第三方服务，如添加 Elasticsearch 搜索或 Stripe 支付。
   - 文档参考：项目提供详细的[官方文档](https://django-oscar.readthedocs.io/)，包括教程和 API 参考。

Django Oscar 适合有 Django 经验的开发者快速搭建专业电商平台，社区活跃，支持长期维护。