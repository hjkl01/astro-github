
---
title: ToolJet
---


# ToolJet

> 项目地址: <https://github.com/ToolJet/ToolJet>

## 主要特性

| 特性 | 说明 |
|------|------|
| **低代码平台** | 通过可视化拖拽和配置，快速创建 Web 应用。 |
| **多数据源** | 原生支持 PostgreSQL、MySQL、MongoDB、SQLite 等，也可通过 API 接口集成任何 REST/GraphQL 服务。 |
| **组件化** | 内置表格、图表、表单、地图、聊天等组件，支持自定义组件。 |
| **实时协作** | 多人同屏编辑、实时预览，任务同步与权限管理。 |
| **自定义安全** | 细粒度 RBAC、SAML/OIDC 单点登录与外部身份提供商集成。 |
| **CI/CD 支持** | 与 Docker、Kubernetes、GitHub Actions 集成，实现一键部署与自动化。 |
| **插件生态** | 可通过插件商店或自行开发插件，扩展功能。 |
| **开源** | MIT 许可，社区可自由修改、发布。 |

## 核心功能

1. **应用开发**  
   - 拖拽式 UI 编辑器  
   - 可视化数据库查询  
   - 事件驱动的逻辑配置（onClick, onChange 等）  

2. **数据管理**  
   - 多种数据库直接连接，无需代码写入  
   - 支持视图、存储过程、SQL 语句执行  
   - 数据同步与缓存层（Redis）  

3. **用户与权限**  
   - 行级/列级权限配置  
   - 角色与组管理  
   - OAuth2 / OIDC 认证  

4. **部署与运维**  
   - Docker Compose / Helm chart  
   - 集成 CI/CD pipelines  
   - 日志收集（Prometheus, Grafana）  

5. **插件与扩展**  
   - 通过 NodeJS 插件框架添加新组件或数据源  
   - 主题定制（CSS/SCSS）  

## 使用方法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/ToolJet/ToolJet.git
   cd ToolJet
   ```

2. **安装依赖**  
   ```bash
   npm install
   ```

3. **启动本地开发环境**  
   ```bash
   npm run dev
   ```
   默认访问 <http://localhost:3000>。

4. **构建生产包**  
   ```bash
   npm run build
   ```

5. **Docker 部署**  
   ```bash
   docker compose up -d
   ```

6. **插件添加**  
   - 在 `src/plugins` 目录下创建插件文件  
   - 使用 `npm run dev:plugin` 预览插件  
   - `npm run publish:plugin` 打包发布

> 详细配置与进阶使用请参考项目文档和官方教程。

```



路径：`src/content/docs/00/ToolJet_ToolJet.md