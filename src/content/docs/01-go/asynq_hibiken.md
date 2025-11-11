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

7. **任务去重**
   - 使用唯一选项防止重复任务执行。

8. **任务超时和取消**
   - 支持每个任务的超时和截止时间。

9. **任务聚合**
   - 允许将多个连续操作聚合到组任务中以进行批处理。

10. **加权优先级队列**
    - 支持加权优先级队列进行任务调度。

11. **严格优先级队列**
    - 支持严格优先级队列。

12. **Web UI**
    - 内置 Web UI 用于监控队列和任务。

13. **CLI 工具**
    - 命令行工具用于检查和控制队列和任务。

14. 周期性任务
     - 支持周期性任务调度。

15. 支持 Redis 哨兵
     - 支持 Redis 哨兵用于高可用性。

16. 与 Prometheus 集成
     - 集成 Prometheus 以收集和可视化队列指标。

## 安装

确保安装了 Go（下载：https://golang.org/dl/）。支持最后两个 Go 版本。

初始化项目并安装 Asynq 库：

```sh
go get -u github.com/hibiken/asynq
```

确保本地运行 Redis 服务器（版本 4.0 或更高）。

## 快速开始

### 创建任务

```go
package tasks

import (
    "context"
    "encoding/json"
    "fmt"
    "log"
    "time"
    "github.com/hibiken/asynq"
)

// 任务类型常量
const (
    TypeEmailDelivery   = "email:deliver"
    TypeImageResize     = "image:resize"
)

type EmailDeliveryPayload struct {
    UserID     int
    TemplateID string
}

type ImageResizePayload struct {
    SourceURL string
}

// 创建任务函数
func NewEmailDeliveryTask(userID int, tmplID string) (*asynq.Task, error) {
    payload, err := json.Marshal(EmailDeliveryPayload{UserID: userID, TemplateID: tmplID})
    if err != nil {
        return nil, err
    }
    return asynq.NewTask(TypeEmailDelivery, payload), nil
}

func NewImageResizeTask(src string) (*asynq.Task, error) {
    payload, err := json.Marshal(ImageResizePayload{SourceURL: src})
    if err != nil {
        return nil, err
    }
    return asynq.NewTask(TypeImageResize, payload, asynq.MaxRetry(5), asynq.Timeout(20 * time.Minute)), nil
}

// 处理任务函数
func HandleEmailDeliveryTask(ctx context.Context, t *asynq.Task) error {
    var p EmailDeliveryPayload
    if err := json.Unmarshal(t.Payload(), &p); err != nil {
        return fmt.Errorf("json.Unmarshal failed: %v: %w", err, asynq.SkipRetry)
    }
    log.Printf("Sending Email to User: user_id=%d, template_id=%s", p.UserID, p.TemplateID)
    // 发送邮件逻辑 ...
    return nil
}

// ImageProcessor 实现 asynq.Handler 接口
type ImageProcessor struct {
    // ... 结构体字段
}

func (processor *ImageProcessor) ProcessTask(ctx context.Context, t *asynq.Task) error {
    var p ImageResizePayload
    if err := json.Unmarshal(t.Payload(), &p); err != nil {
        return fmt.Errorf("json.Unmarshal failed: %v: %w", err, asynq.SkipRetry)
    }
    log.Printf("Resizing image: src=%s", p.SourceURL)
    // 图片调整大小逻辑 ...
    return nil
}

func NewImageProcessor() *ImageProcessor {
    return &ImageProcessor{}
}
```

### 客户端使用

```go
package main

import (
    "log"
    "time"
    "github.com/hibiken/asynq"
    "your/app/package/tasks"
)

const redisAddr = "127.0.0.1:6379"

func main() {
    client := asynq.NewClient(asynq.RedisClientOpt{Addr: redisAddr})
    defer client.Close()

    // 示例 1: 立即处理任务
    task, err := tasks.NewEmailDeliveryTask(42, "some:template:id")
    if err != nil {
        log.Fatalf("could not create task: %v", err)
    }
    info, err := client.Enqueue(task)
    if err != nil {
        log.Fatalf("could not enqueue task: %v", err)
    }
    log.Printf("enqueued task: id=%s queue=%s", info.ID, info.Queue)

    // 示例 2: 调度未来任务
    info, err = client.Enqueue(task, asynq.ProcessIn(24*time.Hour))
    if err != nil {
        log.Fatalf("could not schedule task: %v", err)
    }
    log.Printf("enqueued task: id=%s queue=%s", info.ID, info.Queue)

    // 示例 3: 设置其他选项
    task, err = tasks.NewImageResizeTask("https://example.com/myassets/image.jpg")
    if err != nil {
        log.Fatalf("could not create task: %v", err)
    }
    info, err = client.Enqueue(task, asynq.MaxRetry(10), asynq.Timeout(3 * time.Minute))
    if err != nil {
        log.Fatalf("could not enqueue task: %v", err)
    }
    log.Printf("enqueued task: id=%s queue=%s", info.ID, info.Queue)
}
```

### 服务器使用

```go
package main

import (
    "log"
    "github.com/hibiken/asynq"
    "your/app/package/tasks"
)

const redisAddr = "127.0.0.1:6379"

func main() {
    srv := asynq.NewServer(
        asynq.RedisClientOpt{Addr: redisAddr},
        asynq.Config{
            Concurrency: 10,
            Queues: map[string]int{
                "critical": 6,
                "default":  3,
                "low":      1,
            },
        },
    )

    mux := asynq.NewServeMux()
    mux.HandleFunc(tasks.TypeEmailDelivery, tasks.HandleEmailDeliveryTask)
    mux.Handle(tasks.TypeImageResize, tasks.NewImageProcessor())

    if err := srv.Run(mux); err != nil {
        log.Fatalf("could not run server: %v", err)
    }
}
```

## Web UI

Asynqmon 是一个基于 Web 的工具，用于监控和管理 Asynq 队列和任务。

安装：

```sh
go install github.com/hibiken/asynqmon@latest
```

运行：

```sh
asynqmon
```

## 命令行工具

Asynq 附带命令行工具来检查队列和任务状态。

安装：

```sh
go install github.com/hibiken/asynq/tools/asynq@latest
```

### 常用命令

| 命令                     | 说明                  |
| ------------------------ | --------------------- |
| `asynq client enqueue …` | 通过 CLI 发送单个任务 |
| `asynq client purge …`   | 清空队列              |
| `asynq server`           | 启动 worker 服务      |
| `asynq monitor`          | 监控 UI（可选）       |

## 适用场景

- 需要异步处理高流量请求的后台任务。
- 需要可靠的定时任务或 cron 作业。
- 要对任务执行过程做可观测性监控。

---
> 进一步了解请访问官方文档：<https://github.com/hibiken/asynq>。
