---
title: semaphore
---

# Ansible Semaphore 项目

## 项目地址
[GitHub 项目地址](https://github.com/ansible-semaphore/semaphore)

## 主要特性
Ansible Semaphore 是一个开源的 Web 界面工具，用于简化 Ansible 的任务管理和自动化。它提供了一个用户友好的界面，帮助团队协作执行 Ansible playbook，而无需直接使用命令行。主要特性包括：
- **Web 仪表板**：直观的图形界面，支持 playbook 的可视化管理和执行。
- **任务调度**：支持 cron-like 调度器，允许定时运行 Ansible 任务。
- **访问控制**：基于角色的访问控制 (RBAC)，支持用户管理和权限分配。
- **密钥管理**：内置 SSH 密钥和 Ansible Vault 集成，确保安全存储敏感信息。
- **事件日志和通知**：实时日志查看、错误跟踪，以及集成 Slack、Discord 等通知服务。
- **多环境支持**：支持多个库存 (inventory) 和环境配置，适用于 DevOps 工作流。
- **API 支持**：提供 RESTful API，便于与其他工具集成。
- **Docker 支持**：易于通过 Docker 部署和运行。

## 主要功能
- **Playbook 管理**：上传、编辑和组织 Ansible playbook，支持 Git 仓库集成。
- **库存管理**：管理主机库存，支持动态库存和分组。
- **任务执行**：一键运行 playbook，支持并行执行和实时输出监控。
- **模板系统**：使用 Jinja2 模板自定义任务参数。
- **审计和合规**：记录所有任务执行历史，便于审计和调试。
- **扩展性**：支持插件和自定义钩子 (hooks)，增强功能。

## 用法
1. **安装**：
   - 通过 Docker 快速部署：运行 `docker run -p 3000:3000 -v /path/to/data:/data semaphoreui/semaphore`。
   - 或从源代码构建：克隆仓库，使用 Go 构建二进制文件，然后运行 `./semaphore server`。

2. **配置**：
   - 访问 Web 界面（默认 http://localhost:3000），创建管理员账户。
   - 配置 Git 仓库：添加 Ansible 项目仓库 URL 和凭据。
   - 设置库存：导入主机列表和分组。
   - 管理密钥：上传 SSH 私钥或 Vault 密码。

3. **使用流程**：
   - 创建任务：选择 playbook、库存和参数，点击“运行”执行。
   - 调度任务：设置重复间隔和条件。
   - 监控：查看仪表板上的执行状态、日志和输出。
   - 协作：邀请用户，分配角色（如查看者、编辑者）。

更多详细用法请参考项目文档：https://docs.ansible-semaphore.com/