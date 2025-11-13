---
title: drone
---

# Drone 项目概述

**项目地址：** [https://github.com/harney/drone](https://github.com/harney/drone)

## 主要特性
Drone 是一个开源的持续集成和持续部署 (CI/CD) 平台，基于容器化技术构建。它具有以下核心特性：
- **容器化执行**：每个构建任务在独立的 Docker 容器中运行，确保环境隔离和可重复性。
- **简单配置**：使用 YAML 文件（.drone.yml）定义流水线，支持插件生态系统扩展功能。
- **与 Git 集成**：无缝支持 GitHub、GitLab 等代码托管平台，通过 webhook 触发构建。
- **轻量级**：无代理架构，易于部署在各种环境中，如 Kubernetes、Docker 等。
- **安全与可扩展**：支持秘密管理、权限控制，并通过插件实现自定义任务（如部署、测试等）。

## 主要功能
- **构建与测试**：自动拉取代码、编译、运行单元测试和集成测试。
- **部署自动化**：集成部署插件，支持推送镜像到仓库、部署到云服务等。
- **通知与报告**：构建完成后发送通知到 Slack、Email 等，并生成报告。
- **多管道支持**：允许定义多个阶段（如 build、test、deploy），并行或顺序执行。
- **插件系统**：内置插件用于 Docker、Slack、AWS 等，社区贡献丰富。

## 用法指南
1. **安装与部署**：
   - 使用 Docker 快速启动：`docker run --restart=always -p 80:80 --env-file drone.env drone/drone server`
   - 配置数据库（如 SQLite 或 PostgreSQL）和 GitHub OAuth。
   - 访问 Web 界面激活仓库，启用 Drone。

2. **配置流水线**：
   - 在仓库根目录创建 `.drone.yml` 文件，例如：
     ```
     kind: pipeline
     type: docker
     name: default

     steps:
     - name: build
       image: golang
       commands:
       - go build
       - go test
     ```
   - 推送代码到仓库，Drone 会自动触发构建。

3. **扩展与管理**：
   - 添加插件：如 `docker://plugins/docker` 用于构建镜像。
   - 通过 Web UI 查看构建日志、历史记录和管理秘密。
   - 高级用法：集成 Kubernetes 部署，或自定义插件开发。

更多详情请参考项目文档：[https://docs.drone.io/](https://docs.drone.io/)