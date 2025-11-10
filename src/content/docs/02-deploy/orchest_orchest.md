---
title: orchest
---

# Orchest 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/orchest/orchest)

## 主要特性
Orchest 是一个开源的自动化机器学习（AutoML）和数据科学工作流平台，旨在简化数据科学家和机器学习工程师的工作流程。它具有以下主要特性：
- **可视化工作流编辑器**：通过拖拽式界面构建和管理复杂的工作流，支持 Jupyter Notebook、Python 脚本和自定义步骤的无缝集成。
- **容器化执行环境**：每个工作流步骤运行在独立的 Docker 容器中，确保环境隔离、可重现性和依赖管理。
- **版本控制集成**：内置 Git 支持，允许直接在平台内管理代码版本和协作。
- **交互式开发**：支持实时交互的 Jupyter 环境，结合管道式执行，实现从数据探索到模型部署的全流程自动化。
- **可扩展性**：支持自定义管道步骤、事件驱动的自动化和与外部工具（如 MLflow、Airflow）的集成。
- **自托管部署**：易于在本地或云端部署，支持 Kubernetes 等容器编排工具。

## 主要功能
Orchest 的核心功能聚焦于数据科学和 ML 管道的端到端管理：
- **工作流构建**：创建序列化或并行化的步骤链，每个步骤可以是 Notebook、脚本或外部服务调用。
- **环境管理**：预配置多种 Python 环境（如数据科学包、ML 框架），用户可自定义 Dockerfile 来扩展环境。
- **调度与监控**：支持定时任务、事件触发和实时日志监控，便于调试和优化管道。
- **数据处理**：内置数据加载、清洗和转换工具，支持与 S3、数据库等数据源的集成。
- **模型训练与部署**：简化 ML 模型的训练、评估和部署，支持 A/B 测试和生产化。
- **协作支持**：多用户访问控制、共享项目和 API 接口，便于团队协作。

## 用法指南
1. **安装与部署**：
   - 克隆仓库：`git clone https://github.com/orchest/orchest.git`。
   - 使用 Docker Compose 快速启动：运行 `make services-up`（需安装 Docker 和 Docker Compose）。
   - 访问 Web 界面：默认在 `http://localhost:4000` 打开 Orchest 仪表板。

2. **创建项目**：
   - 在仪表板中点击“New Project”，选择 Git 仓库或本地目录初始化项目。
   - 项目结构包括 `/pipeline.json`（定义工作流）和步骤文件夹。

3. **构建工作流**：
   - 进入项目，点击“New Pipeline”创建管道。
   - 拖拽步骤块（如 Jupyter Notebook 或 Python 脚本）到画布，连接它们形成流程。
   - 在 Notebook 步骤中编写代码，使用 Orchest 的文件系统 API（如 `from orchest import get_data`）传递数据。

4. **运行与调试**：
   - 点击“Run”执行管道，查看实时日志和输出。
   - 使用“Step Settings”配置环境变量、依赖和交互模式。
   - 调试时，可暂停步骤或回滚到特定版本。

5. **高级用法**：
   - 自定义环境：编辑 `/environment.Dockerfile` 并重建容器。
   - 集成外部服务：通过 API 或事件钩子连接其他工具。
   - 部署到生产：使用 Helm Chart 在 Kubernetes 上扩展。

更多细节请参考项目文档：https://docs.orchest.io/。