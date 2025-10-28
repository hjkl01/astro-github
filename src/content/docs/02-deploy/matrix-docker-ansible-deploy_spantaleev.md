
---
title: matrix-docker-ansible-deploy
---

# Matrix Docker Ansible Deploy 项目

## 项目地址
[https://github.com/spantaleev/matrix-docker-ansible-deploy](https://github.com/spantaleev/matrix-docker-ansible-deploy)

## 主要特性
- **自动化部署**：使用 Ansible 自动化工具一键部署 Matrix 服务器，支持 Docker 容器化运行，确保环境隔离和易于管理。
- **模块化设计**：项目高度模块化，支持可选组件的启用/禁用，如 Element Web 客户端、TurnServer（用于语音/视频通话）、Jitsi Meet（视频会议）等。
- **安全性优先**：内置 HTTPS 支持（通过 Let's Encrypt 自动获取证书）、防火墙配置和安全最佳实践，减少手动配置风险。
- **易于扩展**：支持自定义域名、数据库（PostgreSQL）、反向代理（nginx）等，适用于小型团队到大型社区的部署。
- **跨平台兼容**：基于 Docker 和 Ansible，支持 Linux 系统（如 Ubuntu、Debian），无需复杂依赖安装。
- **社区维护**：活跃的开源社区，提供详细文档和问题追踪，便于贡献和故障排除。

## 主要功能
- **Matrix 服务器核心**：部署 Synapse（Matrix 服务器后端），支持联邦聊天、端到端加密消息传递。
- **客户端集成**：可选安装 Element（Web 和移动客户端的前端），提供用户友好的聊天界面。
- **媒体和通信服务**：集成 mxisd（身份服务器）、ma1sd（应用服务）、Dimension（集成桥接）等，支持桥接到其他平台如 Slack、IRC。
- **高级功能**：支持语音/视频通话（通过 Coturn 和 Jitsi）、文件共享、机器人集成，以及监控工具如 Prometheus 和 Grafana。
- **备份与维护**：内置备份脚本和升级机制，确保数据安全和系统更新。

## 用法
1. **准备环境**：
   - 安装 Ansible（版本 4.10+）和 Git。
   - 克隆仓库：`git clone https://github.com/spantaleev/matrix-docker-ansible-deploy.git`。
   - 进入目录：`cd matrix-docker-ansible-deploy`。

2. **配置**：
   - 复制示例配置文件：`cp inventory/hosts.yml inventory/my-hosts.yml`。
   - 编辑 `inventory/my-hosts.yml`，设置目标服务器 IP、域名和启用组件（例如，`matrix_synapse_enabled: true`）。
   - 配置变量文件 `vars.yml`，包括管理员邮箱、密码等敏感信息。

3. **部署**：
   - 运行 Ansible playbook：`ansible-playbook -i inventory/my-hosts.yml setup.yml --become`。
   - 首次部署可能需几分钟，完成后访问你的域名（如 https://matrix.example.com）。

4. **维护与更新**：
   - 更新配置后重新运行 playbook：`ansible-playbook -i inventory/my-hosts.yml setup.yml --become`。
   - 启用新组件：在 `hosts.yml` 中设置相应变量，然后重新运行。
   - 备份：使用内置脚本 `ansible-playbook -i inventory/my-hosts.yml backup.yml`。
   - 卸载：运行 `ansible-playbook -i inventory/my-hosts.yml destroy.yml`。

详细文档请参考项目 README 和 docs 目录。建议在 VPS（如 DigitalOcean 或 AWS）上部署，并确保服务器有至少 2GB RAM。