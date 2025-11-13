---
title: opentofu
---

# OpenTofu

## 简介

OpenTofu 是一个开源工具，用于安全高效地构建、更改和版本化基础设施。它可以管理现有的流行服务提供商以及自定义的内部解决方案。OpenTofu 是 Terraform 的一个分支，专注于基础设施即代码（Infrastructure as Code）。

## 主要功能

- **基础设施即代码**：使用高级配置语法描述基础设施，将数据中心蓝图版本化并像其他代码一样对待。此外，基础设施可以共享和重用。
- **执行计划**：OpenTofu 有一个“规划”步骤，生成执行计划。执行计划显示应用时 OpenTofu 将做什么，避免意外。
- **资源图**：OpenTofu 构建所有资源的图，并并行化创建和修改非依赖资源。因此，OpenTofu 以最高效的方式构建基础设施，并让操作员了解基础设施中的依赖关系。
- **变更自动化**：复杂的变更集可以以最少的人工交互应用于基础设施。通过前面提到的执行计划和资源图，您确切知道 OpenTofu 将改变什么以及以什么顺序，避免许多可能的错误。

## 用法

1. **安装**：访问 [安装指南](https://opentofu.org/docs/intro/install) 获取最新版本。
2. **基本使用**：
   - 初始化项目：`tofu init`
   - 规划变更：`tofu plan`
   - 应用变更：`tofu apply`
   - 销毁资源：`tofu destroy`
3. **配置**：使用 HCL（HashiCorp Configuration Language）编写配置文件，定义资源、提供商等。

## 社区和支持

- 主页：[opentofu.org](https://opentofu.org)
- Slack 社区：[加入 Slack](https://opentofu.org/slack/)
- GitHub：[opentofu/opentofu](https://github.com/opentofu/opentofu)
- 许可证：MPL-2.0
