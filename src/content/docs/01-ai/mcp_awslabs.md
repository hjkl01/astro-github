---
title: mcp
---

# AWS MCP Servers

## 项目简介

AWS MCP Servers 是一个专门为 AWS 服务设计的 Model Context Protocol (MCP) 服务器套件。它通过标准的 MCP 客户端-服务器架构，为 AI 应用提供对 AWS 文档、上下文指导和最佳实践的访问，使云原生开发、基础设施管理和开发工作流程更加高效和易于使用。

## 主要功能

### 核心特性

- **改进输出质量**：通过在模型上下文中提供相关信息，显著改善针对 AWS 服务的模型响应，减少幻觉，提供更准确的技术细节。
- **访问最新文档**：弥补模型训练数据中可能缺失的最新发布、API 或 SDK 信息。
- **工作流自动化**：将常见 AWS 工作流转换为 AI 助手可以直接使用的工具。
- **专业领域知识**：提供 AWS 服务领域的深度、上下文知识。

### 支持的服务类型

- **基础设施与部署**：CDK、Terraform、CloudFormation、EKS、ECS 等
- **AI 与机器学习**：Bedrock、Nova Canvas、Q Business 等
- **数据与分析**：DynamoDB、Aurora、Redshift、Neptune 等
- **开发者工具**：IAM、代码文档生成、架构图生成等
- **集成与消息传递**：SNS/SQS、MQ、MSK 等
- **成本与运维**：Pricing、Cost Explorer、CloudWatch 等
- **医疗与生命科学**：HealthOmics、HealthLake 等

## 安装和使用

### 环境准备

1. 安装 `uv`：`curl -LsSf https://astral.sh/uv/install.sh | sh`
2. 安装 Python：`uv python install 3.10`
3. 配置 AWS 凭证：确保有访问所需 AWS 服务的权限

### 添加到 MCP 客户端

#### Amazon Q Developer CLI

在 `~/.aws/amazonq/mcp.json` 中添加配置：

```json
{
  "mcpServers": {
    "awslabs.core-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.core-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

#### Cursor

在 `.cursor/mcp.json` 中添加配置：

```json
{
  "mcpServers": {
    "awslabs.core-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.core-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

#### VS Code

在 `.vscode/mcp.json` 中添加配置：

```json
{
  "mcpServers": {
    "awslabs.core-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.core-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

### 使用示例

1. **基础设施即代码**：
   - 使用 CDK MCP Server：询问如何创建特定的 AWS 资源
   - 使用 Terraform MCP Server：获取 Terraform 配置的最佳实践

2. **文档查询**：
   - 使用 AWS Knowledge MCP Server：获取最新的 AWS 服务文档
   - 使用 AWS Documentation MCP Server：查询 API 参考

3. **成本估算**：
   - 使用 AWS Pricing MCP Server：估算 AWS 服务成本

4. **监控和运维**：
   - 使用 CloudWatch MCP Server：分析指标和日志

## 最佳实践

- 从 AWS API MCP Server 开始，它提供全面的 AWS 服务支持
- 根据具体需求添加专用服务器（如特定数据库或 AI 服务）
- 使用环境变量控制日志级别：`FASTMCP_LOG_LEVEL=ERROR`
- 对于生产环境，考虑使用托管的远程 MCP 服务器

## 安全注意事项

- 确保 AWS 凭证配置正确且遵循最小权限原则
- 定期轮换凭证
- 监控 MCP 服务器的使用情况
- 在使用前评估安全性和合规性要求

## 许可证

Apache-2.0 License
