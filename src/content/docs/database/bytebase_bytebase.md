---
title: bytebase
---

# Bytebase 项目

**GitHub 项目地址**: [https://github.com/bytebase/bytebase](https://github.com/bytebase/bytebase)

## 主要特性
Bytebase 是一个开源的数据库 DevSecOps 解决方案，专注于简化数据库变更管理。它提供了一个集中的平台，帮助团队安全、高效地处理数据库迁移、版本控制和合规审计。主要特性包括：
- **变更审批工作流**：支持自定义审批流程，确保数据库变更经过多级审查，避免生产环境风险。
- **数据库变更管理**：集成 SQL 审查、回滚机制和变更历史记录，支持多种数据库类型（如 MySQL、PostgreSQL、Oracle 等）。
- **安全与合规**：内置数据脱敏、访问控制和审计日志，帮助企业满足 GDPR、HIPAA 等合规要求。
- **GitOps 集成**：与 GitHub、GitLab 等 CI/CD 工具无缝集成，实现声明式数据库变更。
- **UI/CLI 界面**：提供直观的 Web 界面和命令行工具，便于开发者和 DBA 操作。
- **多租户支持**：适用于云原生环境，支持 Kubernetes 部署和多环境隔离。

## 主要功能
Bytebase 的核心功能围绕数据库生命周期管理展开：
- **SQL 编辑与审查**：内置 SQL 编辑器，支持语法高亮、自动补全和静态分析，检测潜在风险如 SQL 注入或性能问题。
- **变更管道**：自动化数据库 schema 变更，支持无锁迁移（Online Schema Change），最小化对业务的影响。
- **环境管理**：区分开发、测试、生产环境，提供环境级别的权限控制和数据同步。
- **监控与告警**：集成数据库监控，实时跟踪变更状态，并发送通知。
- **插件扩展**：支持自定义插件，如备份恢复、数据迁移工具集成。
- **团队协作**：角色-based 访问控制（RBAC），支持多人协作编辑和评论 SQL 变更。

## 用法
### 安装与部署
1. **前提条件**：确保系统安装 Docker（推荐）或 Go 1.19+ 用于从源代码构建。
2. **快速启动（Docker）**：
   ```
   docker run --init --name bytebase -p 8080:8080 bytebase/bytebase:2.18.1
   ```
   访问 `http://localhost:8080`，默认凭证为 `admin@bytebase.io / admin`。
3. **从源代码安装**：
   - 克隆仓库：`git clone https://github.com/bytebase/bytebase.git`
   - 构建：`make build`
   - 运行：`./bin/bytebase --data /path/to/data --port 8080`
4. **Kubernetes 部署**：使用 Helm Chart 安装，支持 Helm 3+。

### 基本用法
1. **配置环境**：登录后，创建工作空间，添加数据库实例（如连接 MySQL 服务器）。
2. **创建变更**：在 UI 中编写 SQL 脚本，选择目标环境，提交审批。
3. **审批与执行**：团队成员审查变更，批准后 Bytebase 自动执行，并记录日志。
4. **CLI 使用**：安装 CLI 后，运行命令如 `bb migrate --file schema.sql` 来应用变更。
5. **集成 GitOps**：配置 webhook，将 Git 仓库的 SQL 文件推送到 Bytebase 触发管道。
6. **监控变更**：在仪表盘查看历史记录、错误日志，并回滚如果需要。

更多细节请参考官方文档：https://www.bytebase.com/docs