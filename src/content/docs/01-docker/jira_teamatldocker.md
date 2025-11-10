---
title: jira
---

# Jira Docker Compose 项目

## 项目地址
[GitHub 项目地址](https://github.com/teamatldocker/jira/blob/master/docker-compose.yml)

## 主要特性
- **容器化部署**：使用 Docker Compose 简化 Jira 软件的安装和运行，支持一键启动 Atlassian Jira 实例。
- **数据库集成**：内置 PostgreSQL 数据库容器，与 Jira 容器联动，确保数据持久化和高可用性。
- **轻量级配置**：预配置了端口映射、卷挂载和环境变量，便于自定义调整。
- **跨平台兼容**：适用于 Linux、macOS 和 Windows，支持开发、测试和生产环境快速部署。

## 主要功能
- **Jira 核心服务**：提供完整的 Jira 项目管理功能，包括问题跟踪、敏捷看板、工作流配置和报告生成。
- **数据持久化**：通过 Docker 卷机制存储 Jira 配置和数据库数据，避免容器重启时数据丢失。
- **网络隔离**：使用 Docker 网络实现 Jira 和数据库之间的安全通信，支持外部访问。
- **扩展性**：易于集成插件和附加服务，如邮件服务器或备份工具。

## 用法
1. **前提条件**：确保已安装 Docker 和 Docker Compose。
2. **克隆仓库**：从 GitHub 下载 docker-compose.yml 文件，或直接复制内容。
3. **配置调整**：编辑 docker-compose.yml 文件，修改环境变量（如 Jira 许可证密钥、数据库密码）和端口（如 8080）。
4. **启动服务**：在文件目录下运行 `docker-compose up -d`，启动 Jira 和 PostgreSQL 容器。
5. **访问 Jira**：在浏览器打开 `http://localhost:8080`，完成初始设置（如管理员账户创建）。
6. **停止服务**：运行 `docker-compose down` 停止容器；使用 `docker-compose down -v` 删除卷以清理数据。
7. **日志查看**：使用 `docker-compose logs` 检查容器日志以排查问题。