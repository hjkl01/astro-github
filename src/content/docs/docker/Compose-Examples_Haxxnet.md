
---
title: Compose-Examples
---

# Compose-Examples 项目

## 项目地址
[GitHub 项目地址](https://github.com/Haxxnet/Compose-Examples)

## 主要特性
- **Docker Compose 示例集合**：该项目提供了一系列使用 Docker Compose 的实际示例，帮助开发者快速上手容器化应用部署。
- **多样化场景支持**：涵盖 Web 应用、数据库集成、微服务架构等多种常见场景，支持多容器协作。
- **易于扩展**：基于标准 Docker Compose 文件格式，便于自定义和修改配置。
- **开源免费**：MIT 许可，社区贡献友好，适合学习和生产环境参考。

## 主要功能
- **快速部署**：通过简单的 YAML 配置文件，一键启动多个容器服务，包括 Nginx、MySQL、Redis 等流行组件。
- **环境隔离**：实现服务间的网络、卷挂载和环境变量管理，确保开发、测试和生产环境的隔离。
- **监控与日志**：集成日志收集和基本监控功能，便于调试和运维。
- **跨平台兼容**：支持 Linux、macOS 和 Windows 系统，适用于各种开发环境。

## 用法
1. **克隆项目**：
   ```
   git clone https://github.com/Haxxnet/Compose-Examples.git
   cd Compose-Examples
   ```

2. **选择示例**：浏览项目目录，选择感兴趣的示例文件夹（如 `webapp` 或 `database`）。

3. **启动服务**：
   ```
   docker-compose up -d
   ```
   - `-d` 参数表示后台运行。

4. **查看日志**：
   ```
   docker-compose logs
   ```

5. **停止服务**：
   ```
   docker-compose down
   ```

6. **自定义配置**：编辑 `docker-compose.yml` 文件，调整端口、镜像或卷路径后重新运行 `docker-compose up`。

项目适合初学者和中级开发者学习 Docker Compose 的最佳实践，建议结合官方 Docker 文档使用。