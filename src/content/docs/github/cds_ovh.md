
---
title: cds
---

# CDS 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/ovh/cds)

## 主要特性
CDS (Continuous Delivery Service) 是一个开源的持续集成与持续交付 (CI/CD) 平台，由 OVH 开发。它支持多语言、多环境的自动化构建、测试和部署流程。主要特性包括：
- **工作流引擎**：可视化工作流设计，支持 YAML 或图形界面定义管道，支持并行和条件执行。
- **插件系统**：高度可扩展，支持多种集成插件，如 Git、Docker、Kubernetes 等。
- **多租户支持**：适合企业级使用，支持多个项目和团队隔离。
- **API 驱动**：提供 RESTful API，便于与其他工具集成。
- **安全性**：内置秘密管理、钩子验证和权限控制。
- **自托管**：可以部署在私有云或本地环境中。

## 主要功能
- **管道管理**：创建、编辑和监控 CI/CD 管道，支持构建、测试、发布等阶段。
- **集成与钩子**：与 GitHub、GitLab 等 VCS 集成，通过 webhook 触发构建。
- **工件管理**：处理构建输出，支持上传/下载工件。
- **通知与报告**：集成 Slack、Email 等通知，支持 JUnit 测试报告。
- **广播与协作**：实时广播事件，支持团队协作和审计日志。
- **扩展性**：支持自定义钩子和行动器，适用于 DevOps 自动化。

## 用法
1. **安装与部署**：
   - 使用 Docker Compose 或 Kubernetes 部署 CDS UI、API 和 Engine。
   - 示例命令：克隆仓库后运行 `make install` 进行本地安装。

2. **配置项目**：
   - 通过 Web UI 或 CLI 创建项目，添加 VCS 仓库。
   - 定义工作流：使用 YAML 文件描述阶段、作业和步骤，例如：
     ```
     version: v1.0
     pipeline:
       build:
         - script:
             - echo "Building..."
     ```

3. **运行管道**：
   - 推送代码到仓库触发 webhook，CDS 自动执行管道。
   - 监控：在 UI 中查看日志、状态和工件。

4. **CLI 使用**：
   - 安装 CDS CLI：`go get github.com/ovh/cds/cli`。
   - 示例：`cds project create myproject` 创建项目；`cds run workflow myworkflow` 手动运行。

详细文档见项目 README 和 [官方文档](https://ovh.github.io/cds/)。