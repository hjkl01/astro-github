
---
title: newbee-mall
---

# newbee-mall 项目

## 项目地址
[GitHub 项目地址](https://github.com/newbee-ltd/newbee-mall)

## 主要特性
newbee-mall 是一个基于 Spring Boot + MyBatis + Vue.js 的前后端分离电商项目，旨在提供一个完整的在线商城解决方案。主要特性包括：
- **前后端分离架构**：后端使用 Spring Boot 框架，前端采用 Vue.js 实现，易于扩展和维护。
- **响应式设计**：支持 PC 和移动端适配，提供良好的用户体验。
- **模块化开发**：包含用户管理、商品管理、订单处理、支付集成等核心模块。
- **数据库支持**：使用 MySQL 作为主数据库，支持数据持久化和事务管理。
- **安全机制**：集成 JWT 认证、权限控制，防范常见安全风险。
- **高性能**：采用 Redis 缓存、Elasticsearch 搜索，提升查询和加载速度。

## 主要功能
- **用户端功能**：
  - 用户注册、登录和个人信息管理。
  - 商品搜索、浏览和分类查看。
  - 购物车添加、修改和结算。
  - 订单创建、支付（集成支付宝/微信支付）和订单跟踪。
  - 收藏夹和评价系统。
- **管理员端功能**：
  - 商品入库、编辑和上架管理。
  - 用户管理、订单审核和退款处理。
  - 统计报表，包括销售数据和用户行为分析。
  - 系统配置，如轮播图、优惠券和活动管理。
- **其他功能**：
  - 秒杀活动和限时抢购。
  - 多级商品分类和标签系统。
  - 消息通知和客服支持集成。

## 用法
1. **环境准备**：
   - 安装 JDK 8+、Node.js 12+、MySQL 5.7+ 和 Redis。
   - 克隆仓库：`git clone https://github.com/newbee-ltd/newbee-mall.git`。

2. **后端部署**：
   - 进入 `mall-admin` 或 `mall-portal` 目录。
   - 配置 `application.yml` 文件，包括数据库连接、Redis 和支付密钥。
   - 运行 `mvn clean install` 编译项目。
   - 启动 Spring Boot 应用：`mvn spring-boot:run` 或使用 IDE 运行主类。
   - API 端口默认 8080。

3. **前端部署**：
   - 进入 `mall-front` 目录。
   - 运行 `npm install` 安装依赖。
   - 配置 `src/api/config.js` 中的后端 API 地址。
   - 开发模式：`npm run dev`。
   - 生产构建：`npm run build`，然后部署 dist 目录到 Nginx 或其他服务器。

4. **数据库初始化**：
   - 在 MySQL 中创建数据库 `newbee_mall`。
   - 执行 `sql` 目录下的 SQL 文件初始化表结构和测试数据。

5. **测试与运行**：
   - 访问前端页面（默认 localhost:8081）。
   - 使用 Postman 测试后端 API。
   - 项目支持 Docker 部署，参考 `docker-compose.yml` 文件一键启动。

项目适合学习电商系统开发或作为基础模板二次开发，详细文档见仓库 README。