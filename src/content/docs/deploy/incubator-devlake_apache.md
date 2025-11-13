---
title: incubator-devlake
---

# Apache DevLake 项目

## 项目地址
[GitHub 项目地址](https://github.com/apache/incubator-devlake)

## 主要特性
Apache DevLake 是一个开源的工程智能平台，旨在帮助开发者团队通过数据驱动的方式提升工程效率和产品质量。其核心特性包括：
- **数据集成**：支持从多种工具（如 Jira、GitHub、GitLab、Jenkins 等）收集和标准化数据，实现多源数据统一管理。
- **插件化架构**：模块化设计，便于扩展和自定义插件，支持快速集成新工具和功能。
- **分析与洞察**：提供内置的分析管道，包括代码质量分析、工程指标计算、团队协作洞察等，帮助识别瓶颈和优化流程。
- **可视化仪表板**：直观的 UI 界面，支持自定义仪表板和报告，实时展示关键指标如周期时间、部署频率和变更失败率。
- **开源与社区驱动**：基于 Apache 许可，鼓励社区贡献，支持企业级部署和扩展。

## 主要功能
- **数据管道**：自动化采集、转换和存储工程数据，支持 ETL（Extract, Transform, Load）过程。
- **工程指标计算**：计算 DORA 指标（部署频率、变更失败率等）和自定义指标，用于 DevOps 成熟度评估。
- **AI 增强分析**：集成 AI 模型进行代码审查建议、异常检测和趋势预测。
- **报告与导出**：生成 PDF/CSV 报告，支持 API 访问，便于与其他 BI 工具集成。
- **安全性与合规**：数据加密、访问控制，确保敏感工程数据安全。

## 用法
1. **安装与部署**：
   - 克隆仓库：`git clone https://github.com/apache/incubator-devlake.git`
   - 使用 Docker 快速启动：运行 `docker-compose up`（需配置 `docker-compose.yml`）。
   - 或通过 Helm 在 Kubernetes 上部署，支持生产环境。

2. **配置数据源**：
   - 在 Web UI 中添加插件（如 GitHub 插件），输入 API Token 和项目 URL。
   - 配置采集任务，设置数据范围（如时间过滤、仓库列表）。

3. **运行分析**：
   - 创建项目，选择数据源，运行数据管道。
   - 在仪表板中查看指标，选择模板或自定义视图。

4. **扩展与自定义**：
   - 开发新插件：使用 Go 语言实现接口，参考文档构建。
   - API 使用：通过 RESTful API 查询数据，例如 `/api/projects` 获取项目列表。

详细文档请参考项目 README 和 [官方文档](https://devlake.apache.org/docs/)。