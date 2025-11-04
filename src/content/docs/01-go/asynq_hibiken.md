
---
title: asynq
---


# Asynq（hibiken/asynq）

- **项目地址**: <https://github.com/hibiken/asynq>

## 主要特性

1. **高性能任务队列**  
   - 采用 Redis 作为后端，具备低延迟和高吞吐量。  
   - 支持批量任务、按优先级调度、任务重试等高级功能。

2. **分布式任务调度**  
   - 多个 worker 可同时消费同一队列，实现水平扩展。  
   - 支持工作线程池、任务分片、互斥执行。

3. **丰富的任务类型**  
   - 消息推送、图片处理、数据同步、定时任务等。  
   - 通过 TaskPayload 和 TaskType 实现业务无关的任务封装。

4. **容错与可靠性**  
   - 自动重试、死任务队列（Dead Letter Queue）。  
   - 支持任务可见性超时、防止重复消费。

5. **可观测性**  
   - 内置指标（Prometheus、StatsD）。  
   - Web UI / CLI 用于监控队列、任务、worker 状态。

6. **易用 Go SDK**  
   - 简洁接口：`Client.Enqueue`, `Client.EnqueueBulk`, `Client.Purge`, `Client.Retry`.  
   - 支持任务的钩子（hooks）和回调。

## 功能与用法

```go
import (
    "github.com/hibiken/asynq"
)

// 创建 client
client := asynq.NewClient(asynq.RedisClientOpt{Addr: "127.0.0.1:6379"})

// 定义任务
type EmailPayload struct {
    To      string
    Subject string
    Body    string
}
task := asynq.NewTask("email:send", json.RawMessage(`{"to":"alice@example.com","subject":"Hi","body":"Hello!"}`))

// 发送任务
if _, err := client.Enqueue(task, asynq.Queue("mail")); err != nil {
    log.Fatal(err)
}

// 创建 worker 并注册处理器
srv := asynq.NewServer(
    asynq.RedisClientOpt{Addr: "127.0.0.1:6379"},
    asynq.Config{
        Concurrency: 10,
        Queues: map[string]int{
            "default": 5,
            "mail":    3,
        },
    },
)

var emailHandler asynq.Handler = func(ctx context.Context, t *asynq.Task) error {
    var p EmailPayload
    if err := json.Unmarshal(t.Payload(), &p); err != nil {
        return err
    }
    // 发送邮件逻辑
    return nil
}

e := srv.Processor()
_ = e.Register("email:send", emailHandler)

// 启动 worker
if err := srv.Start(); err != nil {
    log.Fatal(err)
}
```

### 常用命令

| 命令 | 说明 |
|------|------|
| `asynq client enqueue …` | 通过 CLI 发送单个任务 |
| `asynq client purge …` | 清空队列 |
| `asynq server` | 启动 worker 服务 |
| `asynq monitor` | 监控 UI（可选） |

## 适用场景

- 需要异步处理高流量请求的后台任务。  
- 需要可靠的定时任务或 cron 作业。  
- 要对任务执行过程做可观测性监控。  

---

> 进一步了解请访问官方文档：<https://github.com/hibiken/asynq>。