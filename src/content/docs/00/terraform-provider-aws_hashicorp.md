
---
title: terraform-provider-aws
---


# Terraform Provider for AWS

**GitHub**: <https://github.com/hashicorp/terraform-provider-aws>

## 主要特性

- **完整的 AWS 资源支持**  
  提供对 AWS 所有服务（EC2、S3、RDS、Lambda 等）的资源定义和管理。

- **官方维护**  
  由 HashiCorp 官方团队开发与维护，保证与 Terraform 生态的兼容性与安全性。

- **插件化架构**  
  采用 Terraform Provider 规范，可直接通过 `terraform init` 自动下载并使用。

- **可扩展资源**  
  支持自定义变量、数据源、资源生命周期管理，满足复杂基础设施需求。

- **跨平台**  
  支持 Windows、macOS、Linux 等主流操作系统。

## 功能概览

| 功能 | 说明 |
|------|------|
| 资源管理 | 创建、更新、删除 AWS 资源 |
| 数据源查询 | 获取已有资源信息（如实例 ID、AMI ID 等） |
| 变量支持 | 通过 `terraform.tfvars` 或环境变量传入参数 |
| 生命周期控制 | `create_before_destroy`、`prevent_destroy` 等属性 |
| 模块化 | 组合资源为模块，复用代码 |
| 版本控制 | Provider 版本锁定，确保环境一致性 |
| 代码生成 | 自动生成资源文档与示例 |

## 用法示例

```hcl
# 初始化 Provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  # 其他认证方式可通过环境变量或共享凭证文件配置
}

# 创建一个 S3 Bucket
resource "aws_s3_bucket" "example" {
  bucket = "my-unique-bucket-name"
  acl    = "private"
}

# 查询现有 EC2 实例信息
data "aws_instance" "example" {
  instance_id = "i-1234567890abcdef0"
}
```

## 开发与贡献

- Fork 本仓库，提交 Pull Request。
- CI 通过 GitHub Actions 自动跑单测与 lint。
- 详细贡献指南请参见项目根目录的 `CONTRIBUTING.md`。

## 文档与资源

- 官方文档: <https://registry.terraform.io/providers/hashicorp/aws/latest/docs>
- 示例代码: <https://github.com/hashicorp/terraform-provider-aws/tree/main/examples>
- 社区支持: Terraform Discord/Slack 频道

--- 

> 以上内容为对 `terraform-provider-aws` 项目的简要中文描述，包含主要特性、功能与使用方法。  
