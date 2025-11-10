---
title: awx
---

# AWX 项目

## 项目地址
[https://github.com/ansible/awx](https://github.com/ansible/awx)

## 主要特性
AWX 是 Ansible Tower 的开源版本，提供了一个基于 Web 的用户界面、REST API 和任务引擎，用于管理和自动化 Ansible 任务。它支持多租户环境、角色-based 访问控制（RBAC）、工作流可视化和集成多种认证方式。主要特性包括：
- **Web 界面**：直观的图形化界面，用于管理和监控 Ansible 任务执行。
- **REST API**：完整的 API 支持，允许与其他工具集成和自动化操作。
- **多租户支持**：通过组织和团队实现资源隔离，适合企业级部署。
- **任务调度和执行**：支持定时任务、实时执行和作业模板。
- **库存管理和凭证**：安全存储主机库存、凭证和变量，支持多种云提供商。
- **工作流引擎**：可视化构建复杂的工作流程，支持条件分支和并行执行。
- **日志和审计**：详细的任务日志、事件跟踪和审计报告。
- **集成扩展**：支持 LDAP、SAML 等认证，以及与 Git、Jenkins 等工具的集成。

## 主要功能
AWX 的核心功能围绕 Ansible 的自动化能力扩展，提供以下模块：
- **项目管理**：从 SCM（如 Git）同步 Ansible playbook 和角色。
- **作业模板**：定义可重用的 Ansible 任务模板，支持变量注入和调研表单。
- **库存（Inventory）**：动态或静态管理主机组，支持云库存插件（如 AWS、Azure）。
- **凭证管理**：加密存储 SSH 密钥、API 令牌等，支持机器、云和网络凭证类型。
- **工作流模板**：串联多个作业模板，形成复杂自动化流程。
- **系统管理**：集群部署、备份恢复和性能监控。
- **报告与通知**：生成执行报告，支持 webhook 和 email 通知。

## 用法
AWX 部署通常使用 Docker 或 Kubernetes。以下是基本用法指南：

### 1. 安装与部署
- **前提**：安装 Docker、Docker Compose 或 Kubernetes。
- **快速启动**（使用 Docker Compose）：
  1. 克隆仓库：`git clone https://github.com/ansible/awx.git`
  2. 进入目录：`cd awx`
  3. 配置 `inventory` 文件（设置管理员密码、数据库等）。
  4. 运行：`ansible-playbook -i inventory install.yml`
- **Kubernetes 部署**：使用 Helm Chart 或 Operator，从仓库的 `installer` 目录部署。

### 2. 基本操作
- **访问界面**：部署后，通过浏览器访问 `http://localhost`（默认端口 80），使用 admin 用户登录。
- **创建项目**：在“Projects”页面添加 Git 仓库 URL，同步 playbook。
- **添加库存**：在“Inventories”中创建组，添加主机 IP/主机名。
- **配置凭证**：在“Credentials”中上传密钥或令牌。
- **运行任务**：创建“Job Templates”，选择项目、库存和 playbook，点击“Launch”执行。
- **API 使用**：通过 `/api/v2/` 端点发送 HTTP 请求，例如使用 curl 创建作业：`curl -X POST -u admin:password http://awx/api/v2/job_templates/1/launch/`
- **高级用法**：使用工作流模板构建多步自动化，或通过 RBAC 管理用户权限。

更多详情请参考官方文档：https://github.com/ansible/awx/blob/devel/INSTALL.md