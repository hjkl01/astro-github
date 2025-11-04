
---
title: ruoyi-vue-pro
---


# 项目名称：ruoyi-vue-pro（YunaiV）

## 项目地址
- GitHub: [https://github.com/YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro)

## 主要特性
- **前后端分离**：前端基于 Vue 3 + Vite + Element Plus，后端基于 Spring Boot 3 + MyBatis-Plus。
- **多租户支持**：同一套代码即可支持多租户业务，租户隔离、租户级权限管理。
- **权限体系**：基于 RBAC 的细粒度权限控制，支持角色、菜单、按钮、数据权限。
- **代码生成器**：一键生成模块代码（前后端），支持自定义模板与字段配置。
- **系统监控**：实时监控系统日志、接口调用、线程信息、内存使用等。
- **任务调度**：Quartz 任务调度，可通过后台 UI 维护定时任务。
- **文件管理**：支持文件上传、下载、分片上传、文件版本管理。
- **统一异常处理**：全局异常处理、统一返回结构，支持多语言提示。
- **国际化**：前后端均支持多语言切换。
- **日志审计**：操作日志、登录日志、接口日志，支持导出和查询。
- **多种数据库**：支持 MySQL、PostgreSQL、SQL Server 等主流数据库。

## 功能模块
1. **系统管理**  
   - 用户管理、角色管理、部门管理、岗位管理、字典管理、参数管理、菜单管理、按钮权限、数据权限  
2. **系统监控**  
   - 在线用户、接口监控、线程信息、系统日志、异常日志  
3. **系统工具**  
   - 代码生成、表单设计、SQL 执行、任务调度、邮件/短信/微信通知  
4. **数据管理**  
   - 数据权限、数据导入导出、数据监控  
5. **前端示例**  
   - 仪表盘、工作流、表单、报表、图表示例

## 快速使用

### 环境准备
- JDK 17+  
- Maven 3.8+  
- Node 20+  
- MySQL 8+ (或其他支持的数据库)

### 后端（Spring Boot）
```bash
# 进入项目根目录
cd ruoyi-vue-pro/backend

# 复制配置文件
cp application.yml.example application.yml
# 根据自己的数据库修改 application.yml

# 启动项目
mvn spring-boot:run
```

### 前端（Vue 3）
```bash
# 进入前端目录
cd ruoyi-vue-pro/frontend

# 安装依赖
npm i

# 开发模式
npm run dev
```

### 初始化数据库
- 访问 `http://localhost:8080/doc.html` 查看接口文档，执行 `init.sql` 脚本完成基础数据（管理员账号：`admin` / 密码：`123456`）。

### 访问
- 登录后台管理系统：`http://localhost:3000`  
- 默认管理员账号 `admin`，密码 `123456`。

## 开发与贡献
1. Fork 本仓库  
2. 新建功能分支 `git checkout -b feature/xxx`  
3. 提交代码后创建 Pull Request，说明功能与改动  
4. 按照项目编码规范提交

> 参考官方文档：`docs/guide.md`  
> 代码规范与提交规范请查看 `.github/workflows` 与 `commitlint` 配置。

## 许可证
本项目使用 Apache License 2.0 许可证，详情请参阅 `LICENSE` 文件。

---

*项目地址已包含在上方，请直接使用 Markdown 语法保存至 `src/content/docs/00/ruoyi-vue-pro_YunaiV.md`。*
