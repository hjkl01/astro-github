---
title: ruoyi-vue-pro
---

# ruoyi-vue-pro

## 项目简介

RuoYi-Vue-Pro 是 RuoYi-Vue 的全新 Pro 版本，基于 Spring Boot + MyBatis Plus + Vue & Element 实现的后台管理系统 + 微信小程序。该项目支持 RBAC 动态权限、数据权限、SaaS 多租户、Flowable 工作流、三方登录、支付、短信、商城、CRM、ERP、AI 大模型等功能。

项目采用 MIT 开源协议，个人与企业可 100% 免费使用。代码整洁、架构清晰，遵循《阿里巴巴 Java 开发手册》规范。

## 主要功能

### 系统功能

- **用户管理**：用户配置，支持多终端认证
- **角色管理**：角色菜单权限分配，支持数据范围权限划分
- **菜单管理**：配置系统菜单、操作权限、按钮权限标识
- **部门管理**：树结构展现，支持数据权限
- **岗位管理**：用户所属职务管理
- **租户管理**：SaaS 多租户功能
- **租户套餐**：自定义租户权限
- **字典管理**：维护固定的数据
- **短信管理**：对接阿里云、腾讯云等短信平台
- **邮件管理**：邮箱账号、模板、发送日志
- **站内信**：系统内消息通知
- **操作日志**：系统正常操作日志记录
- **登录日志**：登录日志记录
- **错误码管理**：系统错误码管理
- **敏感词**：配置系统敏感词
- **应用管理**：SSO 单点登录应用管理
- **地区管理**：城市信息管理

### 工作流程

基于 Flowable 构建，支持 BPMN 和仿钉钉/飞书双设计器：

- 会签、或签、依次审批
- 驳回、转办、委派、加签、减签
- 撤销、终止
- 表单权限、超时审批、自动提醒
- 父子流程、条件分支、并行分支等

### 基础设施

- **代码生成**：前后端代码生成，支持 CRUD
- **系统接口**：基于 Swagger 生成 API 文档
- **数据库文档**：自动生成数据库文档
- **表单构建**：拖拽生成表单
- **配置管理**：动态配置参数
- **定时任务**：在线任务调度
- **文件服务**：支持多种云存储
- **WebSocket**：实时通信
- **API 日志**：访问日志、异常日志
- **MySQL 监控**：数据库连接池监控
- **Redis 监控**：Redis 使用情况监控
- **消息队列**：基于 Redis 实现
- **Java 监控**：基于 Spring Boot Admin
- **链路追踪**：接入 SkyWalking
- **日志中心**：轻量级日志中心
- **服务保障**：分布式锁、幂等、限流

### 数据报表

- **报表设计器**：数据报表、图形报表、打印设计
- **大屏设计器**：拖拽生成数据大屏

### 微信公众号

- 账号管理、数据统计、粉丝管理
- 消息管理、自动回复、标签管理
- 菜单管理、素材管理、图文管理

### 商城系统

- 商品管理、订单管理、物流管理
- 促销活动、积分系统、优惠券

### 会员中心

- 会员管理、会员标签、会员等级
- 会员分组、积分签到

### ERP 系统

- 采购管理、销售管理、库存管理
- 财务管理、生产管理

### CRM 系统

- 客户管理、销售机会、合同管理
- 售后服务、市场活动

### AI 大模型

- AI 对话、知识库管理
- 智能问答、内容生成

### 支付系统

- 应用信息、支付订单、退款订单
- 回调通知、接入示例

## 技术栈

### 后端

- **框架**：Spring Boot 2.7.18, Spring MVC, Spring Security
- **数据库**：MySQL 5.7+, Redis 5.0+, 支持多种数据库
- **ORM**：MyBatis Plus 3.5.7
- **工作流**：Flowable 6.8.0
- **消息队列**：Redis Stream, 支持 RabbitMQ, Kafka 等
- **监控**：Spring Boot Admin, SkyWalking
- **其他**：Lombok, MapStruct, Quartz, Swagger 等

### 前端

- **管理后台**：Vue3 + Element Plus, Vue3 + vben(ant-design-vue), Vue2 + Element UI
- **移动端**：uni-app (支持 APP、小程序、H5)
- **商城小程序**：uni-app

## 快速开始

### 环境要求

- JDK 8+ (master 分支) 或 JDK 17/21+ (master-jdk17 分支)
- MySQL 5.7+
- Redis 5.0+
- Node.js 16+ (前端开发)

### 后端启动

1. 克隆项目：

   ```bash
   git clone https://github.com/YunaiV/ruoyi-vue-pro.git
   cd ruoyi-vue-pro
   ```

2. 导入数据库：
   - 执行 `sql` 目录下的 SQL 脚本

3. 配置数据库连接：
   - 修改 `yudao-server/src/main/resources/application.yaml` 中的数据库配置

4. 启动后端服务：
   ```bash
   mvn clean install
   cd yudao-server
   mvn spring-boot:run
   ```

### 前端启动

1. 进入前端目录：

   ```bash
   cd yudao-ui-admin-vue3  # 或其他前端项目
   ```

2. 安装依赖：

   ```bash
   npm install
   ```

3. 启动开发服务器：
   ```bash
   npm run dev
   ```

### 访问地址

- 管理后台：http://localhost:8080
- API 文档：http://localhost:8080/doc.html
- 演示地址：https://doc.iocoder.cn

## 演示地址

- Vue3 + element-plus：http://dashboard-vue3.yudao.iocoder.cn
- Vue3 + vben(ant-design-vue)：http://dashboard-vben.yudao.iocoder.cn
- Vue2 + element-ui：http://dashboard.yudao.iocoder.cn

## 文档链接

- 启动文档：https://doc.iocoder.cn/quick-start/
- 视频教程：https://doc.iocoder.cn/video/
- 完整文档：https://doc.iocoder.cn

## 版本说明

- **完整版**：包括系统功能、基础设施、会员中心、数据报表、工作流程、商城系统、微信公众号、CRM、ERP 等
- **精简版**：只包括系统功能、基础设施功能

## 贡献

欢迎提交 Issue 和 Pull Request 来改进项目。

## 许可证

MIT License
