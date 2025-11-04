
---
title: go-feature-flag
---


# go-feature-flag (Thomas Poignant)

**GitHub 地址**  
<https://github.com/thomaspoignant/go-feature-flag>

---

## 1️⃣ 概述

`go-feature-flag` 是一款用 Go 编写的开源 Feature Flag（功能开关）库。它帮助开发者在运行时动态开启或关闭功能，支持多种数据源、分段投放、A/B 测试以及目标化投放。具有轻量、易用、可扩展的特点，适用于微服务、CLI、Web 等多种场景。

---

## 2️⃣ 主要特性

| 特性 | 说明 |
|------|------|
| **多数据源支持** | JSON、YAML、Viper、S3、Redis、HTTP 等均可作为 Feature Flag 的存储/获取方式 |
| **分段/投放** | 支持百分比投放（percentage rollouts）、单机中止、按目标（目标式投放） |
| **命名空间 & 版本** | 通过 `Namespace` 管理多套 Flag，支持 `snapshot` 与 `live` 两种模式 |
| **客户端 SDK** | `Client` 接口允许自定义实现，例如针对 HTTP 或数据库 |
| **热更新** | 当底层数据源变更时，可通过 watcher 自动刷新 Flag 配置 |
| **规则 & 条件** | 支持自定义逻辑规则（如数据驱动的多级决策、分段投放） |
| **可视化交互** | 与 LaunchDarkly、Split 等第三方工具兼容，可通过 `cdk` 或 REST API 管理 |
| **性能优先** | 采用内存缓存 + 非阻塞 I/O，满足高并发读取需求 |
| **安全** | 支持使用 TLS、Token、Basic Auth 等方式访问外部数据源 |
| **易于测试** | 提供 mock Client、simulated 客户端以便单元测试 |
| **社区与文档** | 官方 Docs、示例项目、GoDoc 生成的 API 文档齐全 |

---

## 3️⃣ 快速上手

### 3.1 安装

```bash
go get github.com/thomaspoignant/go-feature-flag
```

### 3.2 基本使用

```go
package main

import (
    "context"
    "fmt"
    "github.com/thomaspoignant/go-feature-flag"
)

func main() {
    ctx := context.Background()

    // 加载本地 JSON 配置文件
    manager, err := gff.NewManager()
    if err != nil {
        panic(err)
    }
    if err := manager.Load(gff.JsonFile("./flags.json")); err != nil {
        panic(err)
    }

    // 查询 Flag
    enabled, err := manager.IsEnabled("new-dashboard", ctx, &gff.Context{
        Name: "user-123",
        Value: map[string]interface{}{
            "email": "example@test.com",
        },
    })
    if err != nil {
        panic(err)
    }

    if enabled {
        fmt.Println("新仪表盘已开启")
    } else {
        fmt.Println("仍使用旧仪表盘")
    }
}
```

### 3.3 示例配置（flags.json）

```json
{
  "experiments": [
    {
      "name": "new-dashboard",
      "on": true,
      "variations": {
        "on": true,
        "off": false
      },
      "rules": [
        {
          "weight": 0.5,
          "targeting": [
            {
              "attribute": "email",
              "var": "@"
            }
          ]
        }
      ]
    }
  ]
}
```

### 3.4 使用多数据源

```go
// 使用 Redis 作为 Flag 数据源
manager, _ := gff.NewManager(gff.Redis("localhost:6379", "flags-key"))
```

### 3.5 热更新

```go
// 监听并自动刷新 configuration
manager.OnUpdate(func() {
    fmt.Println("Feature flag 配置已刷新")
})
```

---

## 4️⃣ 进阶使用

| 题目 | 说明 |
|------|------|
| **自定义 Client** | 通过实现 `gff.Client` 接口，替换默认的 HTTP/Redis/文件客户端。 |
| **滚动投放** | 利用 `Rollout` 结构实现增量投放与灰度发布。 |
| **多环境切换** | 通过 `Namespace` 隔离 `dev`/`staging`/`prod` 环境。 |
| **与 CI/CD 集成** | 将 Flag 配置打包进 Docker 镜像或统一管理，配合 `gff-cli` 触发 FAIF。 |
| **日志与监控** | `gff` 提供 `WithLogger` 选项，借助 Zap/Logrus 记录开启/关闭事件。 |
| **Test & Mocks** | 在单元测试中使用 `gff.MockClient` 或 `gff.SimulateManager`。 |

---

## 5️⃣ 贡献与社区

* Issues / PR：请在 GitHub 讨论与提交。  
* 官方文档：<https://gofeatureflag.io/docs>  
* 示例项目：<https://github.com/thomaspoignant/go-feature-flag/tree/master/examples>  
* 频繁版本发布：`v1.x` 兼容 `v2.x`，请检查迁移路径。  

---

> **TIP**  
> 由于 Feature Flag 的性能要求较高，推荐在生产环境中使用 **内存 + Redis** 组合以获得最佳体验。

--- 

**文件路径**: `src/content/docs/00/go-feature-flag_thomaspoignant.md`  
> *请将上述 Markdown 保存至该文件。*