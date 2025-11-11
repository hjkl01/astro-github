---
title: airweave
---

# Airweave

Airweave 是一个完全开源的上下文检索层，用于跨应用和数据库的 AI 代理。它连接到应用、生产力工具、数据库或文档存储，并将它们的内容转换为可搜索的知识库，通过标准化接口为代理提供访问。

## 功能

- **数据同步**：从 30+ 个来源同步数据，最小配置。
- **实体提取**：转换管道。
- **多租户架构**：使用 OAuth2。
- **增量更新**：使用内容哈希。
- **语义搜索**：用于代理查询。
- **版本控制**：数据变更。

## 用法

### 快速开始

#### 托管服务：Airweave Cloud

访问 [app.airweave.ai](https://app.airweave.ai/)。

#### 自托管

确保安装 Docker 和 Docker Compose，然后：

```bash
git clone https://github.com/airweave-ai/airweave.git
cd airweave
chmod +x start.sh
./start.sh
```

访问仪表板：http://localhost:8080。

### 前端

- 在 http://localhost:8080 访问 UI。
- 连接来源、配置同步和查询数据。

### API

- Swagger 文档：http://localhost:8001/docs。
- 创建连接、触发同步和搜索数据。

### SDK

#### Python

```bash
pip install airweave-sdk
```

```python
from airweave import AirweaveSDK

client = AirweaveSDK(api_key="YOUR_API_KEY", base_url="http://localhost:8001")
collection = client.collections.create(name="My Collection")
# ... 更多用法见文档
```

#### TypeScript/JavaScript

```bash
npm install @airweave/sdk
```

```typescript
import { AirweaveSDKClient, AirweaveSDKEnvironment } from '@airweave/sdk';

const client = new AirweaveSDKClient({
  apiKey: 'YOUR_API_KEY',
  environment: AirweaveSDKEnvironment.Local,
});
// ... 更多用法见文档
```

## 支持的集成

包括 Airtable、Asana、GitHub、Google Drive、Notion、Slack 等 30+ 个来源。
