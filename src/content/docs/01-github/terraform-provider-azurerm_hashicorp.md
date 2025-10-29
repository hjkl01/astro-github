
---
title: terraform-provider-azurerm
---


# Terraform AzureRM Provider (HashiCorp)

**项目地址**  
[https://github.com/hashicorp/terraform-provider-azurerm](https://github.com/hashicorp/terraform-provider-azurerm)

## 概述  
Terraform AzureRM Provider 是 HashiCorp 官方维护的 Azure Resource Manager（ARM）提供者，用于通过 Terraform 配置和管理 Microsoft Azure 的资源。它支持几乎所有 Azure 服务，并允许用户以声明式方式定义基础设施。

## 主要特性  
- **完整的 Azure 资源覆盖**：支持计算、网络、存储、数据库、身份验证、监控等 Azure 资源。  
- **声明式配置**：将 Azure 资源定义为代码，支持版本控制、审计与回滚。  
- **状态管理**：使用 Terraform 状态文件（可选远程后端）保持资源与实际环境的一致。  
- **依赖关系解析**：自动推断资源依赖，按正确顺序创建或删除。  
- **模块化与共享**：支持自定义模块，便于重用与分享。  
- **插件化**：可通过 `terraform init` 自动下载与安装。  
- **安全**：支持 Azure AD、Service Principal、Managed Identity 等多种身份验证方式。

## 支持资源（示例）  
- 虚拟机 (`azurerm_linux_virtual_machine`, `azurerm_windows_virtual_machine`)  
- 虚拟网络 (`azurerm_virtual_network`, `azurerm_subnet`)  
- 存储账户 (`azurerm_storage_account`)  
- SQL 数据库 (`azurerm_sql_server`, `azurerm_sql_database`)  
- AKS、VM Scale Set、App Service、Function App 等  
- 资源组、标签、角色分配、策略等  
> *完整资源列表请参阅官方文档。*

## 基本用法  
```hcl
# 1. 配置提供者
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# 2. 定义资源
resource "azurerm_resource_group" "rg" {
  name     = "example-rg"
  location = "East US"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "example-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# 3. 初始化并应用
# $ terraform init
# $ terraform plan
# $ terraform apply
```

## 认证方式  
- **Service Principal**（推荐）  
  ```hcl
  provider "azurerm" {
    features {}

    subscription_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    tenant_id       = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    client_id       = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    client_secret   = "xxxxxxxxxxxx"
  }
  ```
- **Azure CLI 登录**  
  ```hcl
  provider "azurerm" {
    features {}
    use_msi = true  # 若使用托管身份
  }
  ```

## 远程后端示例（Terraform Cloud）  
```hcl
terraform {
  backend "remote" {
    organization = "my-org"

    workspaces {
      name = "example-workspace"
    }
  }
}
```

## 常用命令  
| 命令 | 作用 |
|------|------|
| `terraform init` | 初始化工作目录，下载插件 |
| `terraform plan` | 预览变更 |
| `terraform apply` | 应用变更 |
| `terraform destroy` | 销毁所有资源 |
| `terraform fmt` | 格式化配置文件 |
| `terraform validate` | 校验语法与语义 |

## 贡献与支持  
- **贡献**：Fork → Pull Request；遵循官方贡献指南。  
- **问题与讨论**：GitHub Issues、Discussions。  
- **文档**：位于 `docs/` 目录，涵盖所有资源与参数。

---  

> **提示**：始终使用最新稳定版本的 provider，并在 `terraform init` 时指定版本约束，以保证构建的一致性。