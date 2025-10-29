
---
title: gpt-load
---


# gpt-load

项目地址: https://github.com/tbphp/gpt-load

## 主要特性

- **轻量级 PHP 封装**：提供对 OpenAI GPT‑3.5 / GPT‑4 接口的简洁封装，避免手写 HTTP 请求。
- **多种模型支持**：可直接指定 `model` 参数（如 `gpt-3.5-turbo`、`gpt-4` 等）。
- **完整的 API 支持**：实现 `chat`, `completion`, `embedding` 等常用接口。
- **流式响应**：支持 `stream` 模式，边产生边返回文本。
- **可配置**：支持通过环境变量或配置数组设置 `api_key`、`timeout`、`model` 等。
- **Composer 安装**：可直接通过 `composer require tbphp/gpt-load` 安装。

## 主要功能

| 功能 | 说明 | 关键方法 |
|------|------|----------|
| Chat Completion | 交互式对话 | `chat(array $messages, array $options = [])` |
| Text Completion | 单句生成 | `completion(string $prompt, array $options = [])` |
| Embedding | 文本嵌入 | `embedding(string $input, array $options = [])` |
| Streaming | 实时返回 | `stream(array $messages, callable $callback)` |

> **注意**：所有方法默认使用 `model` 配置，若想临时更改可通过 `$options['model']` 覆盖。

## 安装方式

```bash
composer require tbphp/gpt-load
```

## 快速上手

```php
<?php
require __DIR__ . '/vendor/autoload.php';

use Tbphp\GptLoad\GptLoad;

// 初始化实例
$gpt = new GptLoad([
    'api_key' => 'YOUR_OPENAI_API_KEY',   // 必填
    'model'   => 'gpt-3.5-turbo',         // 可选，默认值
]);

// 1. Chat Completion
$chatResponse = $gpt->chat([
    ['role' => 'system', 'content' => 'You are a helpful assistant.'],
    ['role' => 'user',   'content' => 'Tell me a funny joke.']
]);

echo $chatResponse['content']; // 输出模型回复

// 2. Text Completion
$completion = $gpt->completion('Once upon a time', [
    'max_tokens' => 50,
    'temperature' => 0.7,
]);

echo $completion['content'];

// 3. Embedding
$embedding = $gpt->embedding('Hello world');
print_r($embedding['embedding']); // 数组形式的向量

// 4. Streaming
$gpt->stream(
    [
        ['role' => 'user', 'content' => 'Explain quantum computing.'],
    ],
    function ($chunk) {
        echo $chunk; // 每收到一块文本立即输出
    }
);
```

## 代码结构

```
src/
├─ GptLoad.php          // 主类，封装 OpenAI 请求
├─ HttpClient.php       // 基于 Guzzle 的 HTTP 客户端
└─ Config.php          // 配置管理
```

## 贡献与支持

- 本项目遵循 MIT 许可证。
- 如遇到 bug 或功能需求，欢迎提交 Issues 或 PR。

