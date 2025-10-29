
---
title: embassy
---


# Embassy – Rust 异步嵌入式开发框架

**GitHub 项目地址:** <https://github.com/embassy-rs/embassy>

## 主要特性

| 特性 | 说明 |
|---|---|
| **无阻塞异步** | 基于 `#![no_std]`，使用 `async/await` 语法来实现非阻塞 I/O。 |
| **轻量级任务调度** | 内置单核/多核调度器，支持任务优先级与抢占。 |
| **与 HAL 集成** | 与 `embedded-hal` 兼容的驱动通过 `embassy-…` 继续层实现。 |
| **硬件加速** | 支持 NVIC、RTIC、CPUA 与 `cortex-m` 等体系结构专用优化。 |
| **编译时安全** | 通过类型系统与信息流分析确保资源安全、无数据竞争。 |
| **支持时间与计数器** | 提供 `Timer`, `Instant`, `Duration` 等抽象，支持硬件计时器。 |
| **异步网络** | 集成 `embassy-net`, `embassy-uwb`, `embassy-protocols` 等网络协议栈。 |

## 核心模块

- `embassy`：时钟、调度器与同步原语。  
- `embassy-sync`：异步锁、通道、事件、定时器。  
- `embassy-net`：IP、TCP/UDP、DNS、DHCP、NTP 等网络支持。  
- `embassy-time`：`Timer` 与 `Instant` 的实现。  
- `embassy-boot`：持续运行与快速重启。  

## 快速上手示例

```rust
#![no_std]
#![no_main]
#![feature(abi_X86_interrupt)]

use embassy::executor::Spawner;
use embassy::time::Timer;

/// 简单的闪烁 LED
#[embassy::task]
async fn blink(spawner: Spawner) {
    loop {
        // 这里写开灯代码
        Timer::after_millis(500).await;
        // 这里写关灯代码
        Timer::after_millis(500).await;
    }
}

#[embassy::main]
async fn main(spawner: Spawner) {
    // 初始化硬件
    // ...

    // 启动任务
    spawner.spawn(blink()).unwrap();
}
```

## 快速构建

```bash
# 克隆仓库
git clone https://github.com/embassy-rs/embassy.git
cd embassy

# 交叉编译
cargo build --features="<'feature-list'>" --target=<目标芯片>
```

> 更多配置、特性与依赖请查阅仓库 README。

## 参考文档

- 官方手册: <https://embassy.dev/>  
- 示例项目: <https://github.com/embassy-rs/embassy/tree/main/examples>  

``` 

```

```

*(保存为 `src/content/docs/00/embassy_embassy-rs.md`)