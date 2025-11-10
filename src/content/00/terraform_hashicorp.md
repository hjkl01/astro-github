# Terraform (hashicorp/terraform)

## 功能

Terraform 是一个用于安全高效地构建、更改和版本化基础设施的工具。它可以将 API 编码为声明式配置文件，这些文件可以在团队成员之间共享、编辑、审查和版本化。

### 主要特性

- **基础设施即代码 (Infrastructure as Code)**: 使用高级配置语法描述基础设施。这允许数据中心的蓝图被版本化，并像其他代码一样对待。此外，基础设施可以被共享和重用。
- **执行计划 (Execution Plans)**: Terraform 有一个“规划”步骤，它生成一个执行计划。执行计划显示调用 apply 时 Terraform 将做什么。这让您避免在 Terraform 操作基础设施时的任何意外。
- **资源图 (Resource Graph)**: Terraform 构建所有资源的图，并并行化创建和修改任何非依赖资源。由于此原因，Terraform 以尽可能高效的方式构建基础设施，操作员可以洞察基础设施中的依赖关系。
- **变更自动化 (Change Automation)**: 复杂的变更集可以以最少的人工交互应用于基础设施。通过前面提到的执行计划和资源图，您确切知道 Terraform 将改变什么以及以什么顺序，从而避免许多可能的人为错误。

## 用法

### 安装

从 [Terraform 官方网站](https://developer.hashicorp.com/terraform/install) 下载并安装 Terraform。

### 基本工作流程

1. **初始化 (Init)**: 在包含 Terraform 配置文件的目录中运行 `terraform init` 来初始化工作目录。
2. **规划 (Plan)**: 运行 `terraform plan` 来创建执行计划，显示将要进行的更改。
3. **应用 (Apply)**: 运行 `terraform apply` 来应用更改。
4. **销毁 (Destroy)**: 运行 `terraform destroy` 来销毁基础设施。

### 示例配置

一个简单的 Terraform 配置示例 (main.tf):

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1d0"
  instance_type = "t2.micro"
}
```

### 文档和学习资源

- [官方网站](https://developer.hashicorp.com/terraform)
- [文档](https://developer.hashicorp.com/terraform/docs)
- [教程](https://developer.hashicorp.com/terraform/tutorials)
- [HashiCorp Discuss](https://discuss.hashicorp.com/c/terraform-core)

### 许可证

Business Source License 1.1
