
---
title: bk-cmdb
---

# Tencent bk-cmdb 项目

## 项目地址
[GitHub 项目地址](https://github.com/Tencent/bk-cmdb)

## 主要特性
Tencent bk-cmdb（蓝鲸配置平台）是一个开源的配置管理数据库（CMDB）项目，由腾讯开发，主要用于IT资产和配置项的管理。它支持多租户架构、容器化部署（如Docker和Kubernetes），并提供高可用性和可扩展性。核心特性包括：
- **拓扑模型管理**：支持自定义业务拓扑模型，实现主机、设备、网络等资源的层级化管理。
- **数据一致性**：通过API和订阅机制，确保配置数据在多系统间实时同步。
- **安全审计**：内置权限控制、操作日志和审计功能，符合企业级安全要求。
- **高性能查询**：采用高效的数据库设计，支持复杂查询和海量数据处理。
- **集成能力**：易于与蓝鲸其他组件（如作业平台、监控平台）集成，支持RESTful API。

## 主要功能
- **主机管理**：自动发现、注册和管理主机资源，支持代理（Agent）模式采集主机信息。
- **模型定义**：定义对象模型（如业务、集群、模块、主机），支持属性扩展和关系建模。
- **配置同步**：通过订阅器机制，实现配置变更的推送和同步。
- **查询与报表**：提供CC（Configuration Center）API，支持按拓扑路径查询资源，支持导出报表。
- **插件扩展**：支持自定义插件，用于扩展数据源或处理逻辑。

## 用法
1. **环境准备**：
   - 安装依赖：Python 3.x、MySQL 5.7+、Redis、Etcd（用于分布式锁）。
   - 克隆仓库：`git clone https://github.com/Tencent/bk-cmdb.git`。

2. **部署**：
   - 使用Docker Compose快速部署：进入`bin/docker`目录，运行`docker-compose up -d`。
   - 或手动部署：配置`conf`目录下的配置文件（如`app.conf`），启动服务`python apps/backend/manage.py runserver`。
   - 初始化数据库：运行迁移脚本`python apps/backend/manage.py migrate`。

3. **使用**：
   - 通过Web界面（默认端口8000）登录，创建业务模型。
   - 调用API示例：使用POST请求到`/api/v1/cc/search/business/`查询业务列表，需要认证Token。
   - 集成开发：参考`docs/api`目录的API文档，编写脚本同步配置。
   - 监控与维护：查看日志文件，定期备份数据库。

详细文档见项目`docs`目录和GitHub Wiki。