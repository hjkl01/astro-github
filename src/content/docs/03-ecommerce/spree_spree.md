---
title: spree
---

# Spree 项目描述

## 项目地址

[https://github.com/spree/spree](https://github.com/spree/spree)

## 主要特性

Spree Commerce 是一个开源的电子商务平台，基于 Ruby on Rails 框架构建，提供完全控制和自定义能力。模块化和 API-first 架构，支持多供应商、多租户、多商店、多货币、多语言。主要特性包括：

- **模块化和可定制**：选择所需部分，自定义其余部分（storefront、订单处理、API 等）。
- **可组合和 API-first**：连接现有生态系统，使用 webhooks、属性、元数据、应用、订阅查询、API 扩展构建自定义工作流。
- **多商店支持**：在单个 Spree 实例上托管多个品牌/商店，每个有不同品牌、配置、支付方法、运费选项、产品目录等。
- **多供应商市场**：运行自己的市场，有多个供应商，每个有专用供应商仪表板。
- **多租户平台**：为客户、分销商、附属机构启动多租户电子商务平台。
- **B2B 电子商务**：从分销商捕获 6+ 位订单，使用安全支付和适合业务模型的结账流程。
- **全球商务就绪**：多货币、多语言、全翻译支持产品、类别等；不同地区的不同运费方法/成本；高级税费计算。
- **响应式管理面板**：管理产品、用户、订单、退货、发货等。
- **Spree 5 新特性**：完全重做的管理仪表板体验，提升团队生产力；移动优先、无代码可定制 storefront，提升转化和忠诚度；新集成如原生 Stripe 集成、Stripe Connect、Klaviyo 集成；企业版管理功能如审计日志、多供应商市场模块、多租户/白标 SaaS 电子商务模块、B2B 电子商务模块。

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

1. **快速开始**：
   - 访问 [Quickstart Guide](https://spreecommerce.org/docs/developer/getting-started/quickstart) 在 5 分钟内设置 Spree。
   - 检查最新的 [Spree 5 发布公告](https://spreecommerce.org/announcing-spree-5-the-biggest-open-source-release-ever/) 和演示。

2. **安装**：
   - 克隆仓库：`git clone https://github.com/spree/spree.git`。
   - 安装依赖：`bundle install`。
   - 设置数据库：`rails db:create db:migrate`。
   - 运行服务器：`rails server`。

3. **配置和开发**：
   - 通过后台面板（`/admin`）管理产品、用户、订单等。
   - 使用 API-first 架构集成自定义 storefront 或第三方服务。
   - 扩展：通过 webhooks、应用、插件自定义功能。

4. **部署**：
   - 支持 Docker、Kubernetes、Heroku 等。
   - 生产环境配置缓存、CDN 和监控。

Spree 适合各种电子商务用例，从 headless 微服务到多供应商市场。社区活跃，提供详细文档和企业支持。
