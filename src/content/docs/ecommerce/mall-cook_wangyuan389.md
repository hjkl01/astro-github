---
title: mall-cook
---

# mall-cook 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/wangyuan389/mall-cook?utm_campaign=explore-email&utm_medium=email&utm_source=newsletter&utm_term=daily)

## 主要特性
mall-cook 是一个基于 Spring Boot 和 MyBatis 的开源电商系统，专注于餐饮外卖场景（“cook”可能指代烹饪或餐饮）。它采用前后端分离架构，前端使用 Vue.js，后端使用 Java 技术栈。核心特性包括：
- **模块化设计**：支持用户端、商家端和管理端三个角色，覆盖完整的电商流程。
- **高性能与可扩展性**：集成 Redis 缓存、JWT 认证、Elasticsearch 搜索，提升系统响应速度和可扩展性。
- **移动端适配**：支持微信小程序和 H5 页面，适用于外卖平台的移动应用。
- **安全机制**：内置用户权限管理、数据加密和防 SQL 注入。
- **开源免费**：基于 MIT 许可，适合学习和二次开发。

## 主要功能
- **用户端功能**：商品浏览、购物车管理、下单支付、订单跟踪、评价系统、地址管理、优惠券使用。
- **商家端功能**：店铺管理、商品上架、订单处理、库存管理、数据统计、提现申请。
- **管理端功能**：用户审核、商品审核、订单监控、平台配置、报表分析、角色权限控制。
- **其他功能**：支付集成（支持微信、支付宝）、物流跟踪、推送通知、数据备份与恢复。

## 用法
1. **环境准备**：
   - JDK 8+、MySQL 5.7+、Redis 3.0+、Node.js 12+。
   - 克隆仓库：`git clone https://github.com/wangyuan389/mall-cook.git`。

2. **后端部署**：
   - 进入 `mall-cook-backend` 目录，配置 `application.yml`（数据库、Redis 等连接）。
   - 执行 `mvn clean install` 编译项目。
   - 运行 `mvn spring-boot:run` 启动服务，默认端口 8080。

3. **前端部署**：
   - 进入 `mall-cook-frontend` 目录，安装依赖：`npm install`。
   - 配置环境变量（如 API 地址）。
   - 开发模式：`npm run dev`；生产构建：`npm run build`。

4. **数据库初始化**：
   - 执行 SQL 脚本（在 `doc/sql` 目录）创建数据库和表。
   - 导入初始数据。

5. **测试与运行**：
   - 访问后端 Swagger 接口文档：`http://localhost:8080/swagger-ui.html`。
   - 前端访问：`http://localhost:8081`（默认端口）。
   - 支持 Docker 一键部署，参考仓库 README 中的 Docker 指令。

项目适合电商或外卖系统开发者参考，详细用法请查看仓库的 README.md 文件。