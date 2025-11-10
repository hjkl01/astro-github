---
title: terraform-provider-aws
---

# Terraform AWS Provider

## 功能介绍

Terraform AWS Provider 是 HashiCorp 开发的 Terraform 提供商，用于管理 Amazon Web Services (AWS) 资源。它允许用户使用 Terraform 的声明式配置语言来创建、更新和删除 AWS 资源，如 EC2 实例、S3 存储桶、IAM 角色等。

主要功能包括：

- 支持数百种 AWS 资源和服务
- 基础设施即代码 (IaC) 管理
- 状态管理以跟踪资源变化
- 与 Terraform 生态系统集成

## 用法

### 安装和配置

1. 安装 Terraform：从 [terraform.io](https://terraform.io) 下载并安装 Terraform CLI。

2. 配置 AWS 凭据：设置 AWS_ACCESS_KEY_ID 和 AWS_SECRET_ACCESS_KEY 环境变量，或使用 AWS CLI 配置。

3. 创建 Terraform 配置：编写 `.tf` 文件定义资源。

   示例配置：

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

4. 初始化：`terraform init`

5. 规划：`terraform plan`

6. 应用：`terraform apply`

### 更多信息

- [官方文档](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [教程](https://learn.hashicorp.com/collections/terraform/aws-get-started)
- [GitHub 仓库](https://github.com/hashicorp/terraform-provider-aws)
