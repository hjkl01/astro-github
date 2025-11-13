---
title: call-center-ai
---

# Call Center AI

使用 Azure 和 OpenAI GPT 的 AI 驱动呼叫中心解决方案。

## 功能

- **增强通信和用户体验**：集成入站和出站呼叫与专用电话号码，支持多种语言和语音音调，并允许用户通过 SMS 提供或接收信息。对话实时流式传输以避免延迟，可以在断开连接后恢复，并存储以供将来参考。
- **高级智能和数据管理**：利用 gpt-4.1 和 gpt-4.1-nano 进行细致理解。它可以讨论私人敏感数据，遵循检索增强生成（RAG）最佳实践，理解特定领域术语，生成自动化待办事项列表，过滤不当内容，并检测越狱尝试。
- **定制、监督和可扩展性**：提供可定制提示、功能标志、人机代理回退、呼叫录音和品牌特定自定义语音。在 Azure 上部署，具有容器化、无服务器架构，便于低维护和弹性扩展。
- **云原生部署**：使用 Azure Communication Services、Cognitive Services 和 OpenAI 资源进行安全、快速迭代。

## 用法

### API 调用以发起呼叫

发送 POST 请求以发起呼叫：

```bash
curl --header 'Content-Type: application/json' \
  --request POST \
  --url https://xxx/call \
  --data '{
    "bot_company": "Contoso",
    "bot_name": "Amélie",
    "phone_number": "+11234567890",
    "task": "Help the customer with their digital workplace.",
    "agent_phone_number": "+33612345678",
    "claim": [
      {
        "name": "hardware_info",
        "type": "text"
      }
    ]
  }'
```

### 部署

#### 先决条件

- Azure CLI、Twilio CLI（可选）、yq、Bash、Make
- Azure 资源：资源组、Communication Services、电话号码

#### Azure 上的远程部署

1. 从 `config-remote-example.yaml` 创建 `config.yaml`
2. 运行 `az login`
3. 执行 `make deploy name=my-rg-name`

#### 本地部署

1. 安装 Rust、uv，运行 `make install`
2. 从 `config-local-example.yaml` 创建 `config.yaml`
3. 运行 `make deploy-bicep deploy-post name=my-rg-name`
4. 启动隧道：`make tunnel`
5. 运行 `make dev` 进行开发

### 高级配置

- 通过在 App Configuration 中将 `recording_enabled` 设置为 `true` 来启用呼叫录音
- 定制语言、审核级别、声明模式、提示等
- 与 AI Search 集成以进行自定义训练数据
- 使用 Twilio 进行 SMS

### 监控

应用程序将跟踪和指标发送到 Azure Application Insights，以监控应用程序行为、LLM 指标和自定义指标，如呼叫延迟。

## Demo

A French demo is available on YouTube showcasing inbound calls, conversation storage, and data extraction.
