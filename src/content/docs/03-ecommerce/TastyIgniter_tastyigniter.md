---
title: TastyIgniter
---

# TastyIgniter 项目描述

## 项目地址
https://github.com/tastyigniter/TastyIgniter

## 主要特性
TastyIgniter 是一个基于 Laravel 框架的开源餐厅管理平台和在线订购系统，专为餐饮业设计。它提供模块化架构，支持自定义扩展，适用于小型餐厅、咖啡店或大型连锁店。主要特性包括：
- **响应式设计**：支持桌面、平板和移动设备，提供无缝的用户体验。
- **多语言支持**：内置多语言功能，便于国际化部署。
- **权限管理**：基于角色的访问控制（RBAC），管理员可管理用户权限。
- **扩展性强**：通过 Composer 安装插件，支持主题自定义和第三方集成。
- **安全性**：集成 Laravel 的安全机制，包括 CSRF 保护和 SQL 注入防护。

## 主要功能
TastyIgniter 的核心功能覆盖餐厅运营的各个方面：
- **菜单管理**：创建和管理菜品、类别、价格和库存，支持图片上传和变体（如大小、辣度）。
- **在线订购**：客户可通过前端界面浏览菜单、下订单，支持外卖和堂食。
- **订单处理**：后端仪表板实时跟踪订单状态，支持打印厨房订单和发票。
- **客户管理**：维护客户资料、订单历史和忠诚度程序。
- **支付集成**：支持 Stripe、PayPal 等支付网关，以及现金支付。
- **报告与分析**：生成销售报告、库存报告和客户洞察。
- **预订系统**：管理餐厅桌位预订和事件。
- **促销与折扣**：设置优惠券、折扣码和促销活动。

## 用法
### 安装
1. **系统要求**：PHP 7.4+、MySQL 5.7+、Composer 和 Node.js。
2. **克隆仓库**：`git clone https://github.com/tastyigniter/TastyIgniter.git`。
3. **安装依赖**：进入项目目录，运行 `composer install` 和 `npm install`。
4. **配置环境**：复制 `.env.example` 为 `.env`，设置数据库连接和应用密钥（`php artisan key:generate`）。
5. **运行迁移**：`php artisan migrate` 和 `php artisan db:seed` 初始化数据库。
6. **启动服务器**：`php artisan serve` 访问 `http://localhost:8000`。

### 基本用法
- **管理员面板**：登录后端（`/admin`），配置菜单、用户和设置。
- **前端使用**：客户访问网站首页浏览菜单、下单。支持购物车和结账流程。
- **自定义**：通过管理面板添加菜品，或编辑主题文件进行 UI 调整。使用插件扩展功能，如集成外卖平台。
- **部署**：上传到共享主机或 VPS，配置 Nginx/Apache 服务器，并设置 cron 任务处理后台作业。

更多详情请参考官方文档：https://docs.tastyigniter.com。