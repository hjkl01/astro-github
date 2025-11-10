---
title: erpnext
---

# ERPNext 项目

**项目地址:** [https://github.com/frappe/erpnext](https://github.com/frappe/erpnext)

## 主要特性
ERPNext 是一个开源的企业资源计划 (ERP) 系统，由 Frappe 框架构建。它集成了多个业务模块，支持模块化扩展，具有高度的可定制性和用户友好的界面。主要特性包括：
- **开源免费**：基于 MIT 许可，完全开源，无需许可费用。
- **模块化设计**：支持会计、库存、销售、采购、人力资源、制造、项目管理、CRM 等核心模块，可根据需求启用或禁用。
- **多语言支持**：内置中文界面，支持全球多语言和多货币。
- **移动端兼容**：响应式设计，支持手机和平板访问。
- **自定义功能**：通过低代码工具（如 DocTypes）轻松自定义表单、工作流和报告。
- **集成能力**：支持 API 接口，与第三方工具（如支付网关、电商平台）集成。
- **安全性**：角色-based 访问控制、数据加密和审计日志。

## 主要功能
ERPNext 覆盖企业运营的全流程，提供以下核心功能：
- **会计与财务**：记账、发票管理、预算控制、税务计算和财务报告，支持多公司和多分支机构。
- **库存管理**：仓库跟踪、批次/序列号管理、入库/出库、库存盘点和供应链优化。
- **销售与 CRM**：客户管理、报价、订单处理、机会跟踪和销售分析。
- **采购与供应商**：供应商评估、采购订单、物料需求规划 (MRP) 和供应商门户。
- **人力资源**：员工档案、薪资计算、考勤、招聘和绩效评估。
- **制造**：生产计划、物料清单 (BOM)、工作订单和质量控制。
- **项目管理**：任务跟踪、甘特图、时间表和成本控制。
- **网站与门户**：内置 CMS，支持创建企业网站、客户门户和自助服务。
- **报告与分析**：实时仪表板、自定义报告和数据可视化工具。

## 用法
### 安装
1. **前提要求**：Python 3.7+、MariaDB 10.3+、Redis、Node.js 和 Yarn。推荐在 Linux（如 Ubuntu）或 Docker 环境中部署。
2. **克隆仓库**：`git clone https://github.com/frappe/erpnext.git`
3. **安装 Frappe 框架**（ERPNext 依赖）：使用 frappe-bench 工具，一键安装。
   - 运行：`pip install frappe-bench`
   - 初始化：`bench init frappe-bench && cd frappe-bench`
   - 获取 ERPNext：`bench get-app erpnext https://github.com/frappe/erpnext`
   - 创建站点：`bench new-site your-site.local`
   - 安装应用：`bench --site your-site.local install-app erpnext`
4. **启动**：`bench start`，访问 `http://localhost:8000` 并完成向导设置。
5. **Docker 部署**：使用官方 Docker Compose 文件快速部署，支持一键安装。

### 使用步骤
1. **初始设置**：登录后，通过设置向导配置公司信息、货币、用户角色和启用模块。
2. **日常操作**：从仪表板导航到相应模块，例如创建销售订单（销售 > 订单 > 新建），系统自动链接库存和会计。
3. **自定义**：在“自定义”模块中修改表单字段、添加工作流或生成报告。
4. **维护**：定期更新（`bench update`），备份数据（`bench backup`），并通过社区论坛或文档求助。
5. **扩展**：集成 API 或开发自定义应用，使用 Frappe 的 JavaScript/Python 框架。

更多详情请参考官方文档：[ERPNext Documentation](https://docs.erpnext.com)。