
---
title: aigcpanel
---


# aigcpanel（ModStart AI GCP Panel）

> **项目地址**  
> https://github.com/modstart-lib/aigcpanel

---

## 一、项目简介  
`aigcpanel` 是 ModStart 生态下的一个 **AI GCP 管理面板**，为开发者提供一套完整的 AI 模型、推理、监控与计费管理工具。  
- 采用 **Laravel 8+** 为后端框架，前端使用 **Vue + Element Plus**。  
- 兼容 Google Cloud Platform（GCP），支持 GCP AI Platform、Cloud Functions、Storage 等服务。  
- 内置多租户、角色权限、日志审计等企业级功能。  

---

## 二、主要特性  

| 关键功能 | 说明 |
|--------|------|
| **模型管理** | 支持上传、版本化、发布 AI 模型，自动生成推理入口。 |
| **推理引擎** | 通过 GCP AI Platform 或自定义云函数分发推理请求，支持批量推理与实时推理。 |
| **任务调度** | 内置任务队列，可设置定时推理、批量训练计划。 |
| **监控与报警** | 收集预测请求流量、延迟、错误率，支持 Grafana/Prometheus 对接；支持自定义报警阈值。 |
| **日志审计** | 记录所有操作日志，可导出并支持 ELK/Fluentd 集成。 |
| **计费管理** | 按调用次数、使用时长、存储空间生成费用报表，支持多账户分账。 |
| **可插拔插件** | 支持自定义插件，扩展第三方 AI 平台（OpenAI、Azure 等）。 |
| **多租户 & 角色权限** | 细粒度 ACL，支持组织、项目、用户分级权限。 |

---

## 三、安装与使用  

> 下面的命令假设你已在 Laravel 项目根目录下执行。

### 1. Composer 安装

```bash
composer require modstart-lib/aigcpanel
```

### 2. 发布资源

```bash
php artisan vendor:publish --provider="ModStart\Aigcpanel\AigcpanelServiceProvider" --tag="config"
php artisan vendor:publish --provider="ModStart\Aigcpanel\AigcpanelServiceProvider" --tag="migrations"
php artisan vendor:publish --provider="ModStart\Aigcpanel\AigcpanelServiceProvider" --tag="views"
```

### 3. 数据库迁移

```bash
php artisan migrate
```

### 4. 初始化

```bash
php artisan aigcpanel:install
```

> 该命令会创建默认管理员账号、初始化 GCP 相关配置，并加载基础设置。

### 5. 启动

```bash
php artisan serve
```

> 访问 `http://localhost:8000/aigcpanel` 进入后台管理面板。

---

## 四、快速上手示例

```php
// 在 controller 中创建一个 AI 推理任务
use ModStart\Aigcpanel\Models\AiTask;

$task = AiTask::create([
    'name' => '图片分类',
    'input_file' => $request->file('image')->store('images'),
    'model_id' => 1,  // 预先上传的模型 ID
    'status' => 'pending',
]);

// 调度任务
AiTask::dispatch($task->id);
```

### 查看运行日志

```bash
php artisan aigcpanel:log
```

### 生成费用报表

```bash
php artisan aigcpanel:report --start=2024-01-01 --end=2024-01-31
```

---

## 五、常见问题

| 问题 | 解决方案 |
|------|----------|
| GCP 认证失败 | 检查 `config/aigcpanel.php` 的 `google_credentials_path` 路径；确认 JSON 密钥已正确放置。 |
| 推理延迟高 | 在 GCP 控制台检查实例规格，或开启即时推理（Edge TPU）。 |
| 日志不完整 | 转到 `storage/logs` 或 ELK 集成查看。 |

---

> **提示**  
> - 所有接口均已通过 Swagger 生成文档，请访问 `http://<your-domain>/api/documentation`。  
> - 可在 `app/Providers/AigcpanelServiceProvider.php` 中自定义路由、管道等。

--- 

> **更多信息**  
> 项目的完整文档、示例代码以及社区支持请查看官方 GitHub 仓库。  
> GitHub 地址: https://github.com/modstart-lib/aigcpanel
