
---
title: terraform
---


# Terraform (HashiCorp)

项目地址: https://github.com/hashicorp/terraform

## 主要特性
- **声明式配置**：使用 HashiCorp Configuration Language (HCL) 或 JSON 编写资源描述，让 IaC 更易读写。
- **跨云支持**：内置对 AWS、Azure、GCP、Alibaba Cloud、OpenStack 等主流云平台的 provider。
- **状态管理**：自动跟踪已创建资源的状态，支持本地或远程后端（S3、Azure Storage、Consul 等）。
- **依赖关系图**：自动构建资源间依赖树，按正确顺序创建/销毁资源。
- **模块化复用**：将通用配置封装为模块，支持版本控制与复用。
- **计划 & 执行**：`terraform plan` 展示变更方案，`terraform apply` 一键执行。
- **扩展插件机制**：通过插件实现自定义 provider、 provisioner、linter 等。

## 核心功能
| 作用 | 说明 |
|------|------|
| **资源创建/销毁** | 通过 `terraform apply` 与 `terraform destroy` 自动管理云/本地资源生命周期。 |
| **变量与输出** | 支持动态输入变量与输出信息，便于自动化流水线与信息传递。 |
| **软件版本兼容** | 通过 `required_version` 指定 Terraform 版本，保证配置可复现。 |
| **远程后端** | 将状态文件存储在安全的远程后端，支持锁定与共享。 |
| **团队协作** | 通过语义化的计划文件呈现差异，方便审计与讨论。 |
| **社区生态** | 丰富的 provider 与模块源，即可从 Terraform Registry 获取。 |

## 用法
1. **安装**  
   ```bash
   brew tap hashicorp/tap
   brew install hashicorp/tap/terraform
   ```
2. **初始化**  
   ```bash
   terraform init          # 拉取 provider 与后端配置
   ```
3. **编写配置**（示例：AWS EC2）  
   ```hcl
   provider "aws" {
     region = "us-east-1"
   }

   resource "aws_instance" "web" {
     ami           = "ami-0c55b159cbfafe1f0"
     instance_type = "t2.micro"
   }
   ```
4. **预览变更**  
   ```bash
   terraform plan
   ```
5. **应用配置**  
   ```bash
   terraform apply
   ```
6. **销毁资源**  
   ```bash
   terraform destroy
   ```

> 通过结合 CI/CD（GitHub Actions、GitLab CI 等）可实现可重复、自动的基础设施部署流程。  

```
