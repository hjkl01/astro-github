
---
title: nsq
---

# NSQ 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/nsqio/nsq)

## 主要特性
NSQ 是一个实时分布式消息队列系统，设计用于高性能和可扩展性。其核心特性包括：
- **高吞吐量和低延迟**：支持每秒数百万消息的处理，适用于实时应用。
- **分布式架构**：无单点故障，支持水平扩展，通过多个节点实现负载均衡。
- **简单易用**：使用 Go 语言开发，提供简单的二进制分发，无需复杂的依赖。
- **容错机制**：内置重连、消息持久化和备份，支持消息丢失的恢复。
- **无 broker 设计**：直接使用主题（topics）和通道（channels）进行消息路由，避免复杂的中介层。
- **多语言支持**：提供官方客户端库，支持 Go、Python、Java 等多种语言。

## 主要功能
NSQ 的核心功能围绕消息的生产、消费和路由：
- **消息发布**：生产者通过 nsq_pub 工具或客户端 API 将消息发布到指定主题。
- **消息订阅**：消费者通过 nsq_sub 工具或客户端订阅通道，接收并处理消息。
- **主题与通道**：主题用于分类消息，通道用于隔离消费者，支持多消费者并行处理。
- **发现与负载均衡**：使用 nsqlookupd 服务进行节点发现，nsqd 作为消息守护进程处理实际消息。
- **监控与管理**：内置 HTTP API 支持监控队列状态、统计信息和动态配置。
- **持久化选项**：支持磁盘队列持久化，确保消息不丢失。

## 用法
### 安装
1. 下载预编译二进制文件或从源代码构建：
   ```
   go get github.com/nsqio/nsq
   make install
   ```
2. 或者使用 Docker：
   ```
   docker pull nsqio/nsq
   ```

### 基本部署
1. 启动查找服务（nsqlookupd）：
   ```
   nsqlookupd --tcp-address=0.0.0.0:4160 --http-address=0.0.0.0:4161
   ```
2. 启动消息守护进程（nsqd），连接查找服务：
   ```
   nsqd --lookupd-tcp-address=127.0.0.1:4160 --lookupd-http-address=127.0.0.1:4161
   ```
3. 启动管理界面（nsqadmin）：
   ```
   nsqadmin --lookupd-http-address=127.0.0.1:4161
   ```

### 基本用法示例
- **发布消息**（使用 nsq_pub）：
  ```
  echo "Hello NSQ" | nsq_pub --topic=test nsqd:4150
  ```
- **订阅消息**（使用 nsq_sub）：
  ```
  nsq_sub --topic=test --channel=test_channel --output-handler=cat nsqd:4150
  ```
- **使用客户端库**：例如在 Go 中：
  ```go
  package main
  import (
      "github.com/nsqio/go-nsq"
      "log"
  )

  func main() {
      producer, _ := nsq.NewProducer("127.0.0.1:4150", nsq.NewConfig())
      producer.Publish("test", []byte("Hello NSQ"))
      producer.Stop()
  }
  ```

更多细节请参考项目文档：https://nsq.io/