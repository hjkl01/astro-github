---
title: azure-sdk-for-python
---


# Azure SDK for Python

项目地址: <https://github.com/Azure/azure-sdk-for-python>

## 主要特性

- **全面覆盖 Azure 服务**：包含 Azure Storage、Azure Compute、Azure Cosmos DB、Azure Functions、Azure Key Vault 等近百个服务的 Python SDK。
- **同步 & 异步支持**：每个 SDK 均提供同步 API 与 `asyncio` 异步 API，兼容传统同步代码与现代异步代码。
- **自动化版本管理**：所有 SDK 与核心库遵循严格的语义化版本控制，保证向后兼容。
- **易于使用的资源管理**：提供统一的 `azure.identity` 库，支持多种身份验证方式（环境变量、Managed Identity、Azure CLI、交互式登录等）。
- **丰富的工具支持**：提供代码生成器、测试框架和文档生成工具，便于快速构建和维护 SDK。

## 功能概览

| 服务 | 主要功能 |
|------|----------|
| **Azure Storage** | Blob、Table、Queue、File 存储 |
| **Azure Compute** | 虚拟机、器实例、App Service 管理 |
| **Azure Cosmos DB** | NoSQL 数据库访问 |
| **Azure Key Vault** | 密钥、机密与证书管理 |
| **Azure Functions** | 云函数调用 |
| **Azure Machine Learning** | 训练、部署、推理 |
| **Azure DevOps** | Pipelines、Artifacts、Repos 接口 |
| **Azure Networking** | 虚拟网络、负载均衡、网络安全组等 |

## 用法示例

```bash
# 安装
pip install azure-storage-blob
```

```python
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# 通过 DefaultAzureCredential 自动获取凭据
credential = DefaultAzureCredential()
service_client = BlobServiceClient(account_url="https://<storage-account>.blob.core.windows.net/", credential=credential)

# 列出所有容器
containers = service_client.list_containers()
for container in containers:
    print(container['name'])
```

异步用法：

```python
import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.storage.blob.aio import BlobServiceClient

async def main():
    async with DefaultAzureCredential() as cred:
        async with BlobServiceClient(account_url="https://<storage-account>.blob.core.windows.net/", credential=cred) as service_client:
            async for container in service_client.list_containers():
                print(container["name"])

asyncio.run(main())
```

## 开发与贡献

- **本地编译**：执行 `./scripts/gen.sh` 生成 SDK 代码。
- **运行测试**：`pytest` 或 `pytest -m core` 进行单元测试。
- **提交 PR**：遵循官方 `CONTRIBUTING.md` 说明进行代码提交。

---
> 以上内容提供 Azure SDK for Python 的核心特性、功能与使用示例，便于快速上手与集成。 
