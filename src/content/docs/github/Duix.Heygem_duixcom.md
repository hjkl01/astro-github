---
title: Duix.Heygem
---


# Duix.Heygem

**项目地址**: https://github.com/duixcom/Duix.Heygem

## 主要特性
- 统一的 HeyGem API 客户端封装
- 支持文本生成、对话、嵌入、模型管理等多种功能
- 同步与异步调用兼容
- 自动重试与速率限制处理
- 可自定义请求参数、模型、温度等

## 功能
- `HeygemClient`：核心客户端，提供生成、聊天、嵌入接口
- `ChatCompletionProvider`：对话式文本生成
- `EmbeddingsProvider`：文本向量嵌入
- `CompletionProvider`：传统文本补全
- 环境变量与配置文件支持（如 `HEY_GEM_API_KEY`、`HEY_GEM_MODEL` 等）

## 用法

```csharp
using Duix.Heygem;

// 初始化客户端（可使用环境变量或显式传参）
var client = new HeygemClient(apiKey: "YOUR_API_KEY");

// 同步调用
var completion = client.Completion("请给出一个简短的问候语");

// 异步调用
var chatAsync = await client.ChatAsync("你好，HeyGem");

// 使用依赖注入（例如在 ASP.NET Core 中）
builder.Services.AddHeyClient(apiKey: "YOUR_API_KEY");
```

> 详细使用方法请参考仓库中的 README_zh.md。
