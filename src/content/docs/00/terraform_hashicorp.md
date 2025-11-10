---
title: Terraform
---

# Terraform

## 功能

Terraform 是一个用于安全高效地构建、更改和版本化基础设施的工具。它可以将 API 编码为声明式配置文件，这些文件可以在团队成员之间共享、编辑、审查和版本化。

### 主要特性

- **基础设施即代码**：使用高水平配置语法描述基础设施。这允许数据中心的蓝图被版本化，并像其他代码一样对待。此外，基础设施可以被共享和重用。
- **执行计划**：Terraform 有一个“规划”步骤，其中生成执行计划。执行计划显示调用 apply 时 Terraform 将做什么。这让您避免在 Terraform 操作基础设施时的任何意外。
- **资源图**：Terraform 构建所有资源的图，并并行化创建和修改任何非依赖资源。因此，Terraform 以尽可能高效的方式构建基础设施，操作员可以洞察基础设施中的依赖关系。
- **变更自动化**：复杂的变更集可以以最少的人工交互应用于基础设施。通过前面提到的执行计划和资源图，您确切知道 Terraform 将改变什么以及以什么顺序，从而避免许多可能的人为错误。

## 用法

### 入门

如果您是 Terraform 的新手并想开始创建基础设施，请查看 HashiCorp 学习平台上的[入门指南](https://learn.hashicorp.com/terraform#getting-started)。还有[其他指南](https://learn.hashicorp.com/terraform#operations-and-development)来继续您的学习。

### 基本命令

- `terraform init`：初始化工作目录，下载提供商插件。
- `terraform plan`：生成执行计划，显示将要进行的更改。
- `terraform apply`：应用更改到基础设施。
- `terraform destroy`：销毁基础设施。

### 文档和资源

- 官方网站：[https://developer.hashicorp.com/terraform](https://developer.hashicorp.com/terraform)
- 文档：[https://developer.hashicorp.com/terraform/docs](https://developer.hashicorp.com/terraform/docs)
- 教程：[https://developer.hashicorp.com/terraform/tutorials](https://developer.hashicorp.com/terraform/tutorials)
- 论坛：[HashiCorp Discuss](https://discuss.hashicorp.com/c/terraform-core)
- 认证考试：[HashiCorp Certified: Terraform Associate](https://www.hashicorp.com/certification/#hashicorp-certified-terraform-associate)

### 开发

此仓库仅包含 Terraform 核心，包括命令行界面和主图引擎。提供商作为插件实现，Terraform 可以自动下载发布在 [Terraform Registry](https://registry.terraform.io) 上的提供商。

- 要了解更多关于编译 Terraform 和贡献建议更改的信息，请参考[贡献指南](https://github.com/hashicorp/terraform/blob/main/.github/CONTRIBUTING.md)。
- 要了解更多关于我们如何处理错误报告的信息，请参考[错误分类指南](https://github.com/hashicorp/terraform/blob/main/BUGPROCESS.md)。

### 许可证

[Business Source License 1.1](https://github.com/hashicorp/terraform/blob/main/LICENSE)
