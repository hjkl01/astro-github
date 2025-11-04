
---
title: protobuf
---


# Protocol Buffers (protobuf)

**项目地址**：<https://github.com/protocolbuffers/protobuf>

## 简介
Protocol Buffers（简称 protobuf）是 Google 开发的一种语言中立、平台中立、可扩展的序列化结构数据方法。它兼顾了高效、简洁和可前后兼容性，广泛用于 RPC、数据存储、通信协议等场景。

## 主要特性
- **语言中立**：支持 C++, Java, Python, Go, C#, Ruby, JavaScript、Kotlin、Swift 等多种语言。
- **平台中立**：生成的代码可在不同操作系统、硬件架构之间无缝运行。
- **高效序列化**：二进制格式比 XML/JSON 体积更小，解析更快。
- **可扩展性**：向后/向前兼容，可在不破坏旧数据的前提下添加新字段。
- **IDL 机制**：使用 `.proto` 文件定义数据结构，生成对应语言的类/结构体。

## 功能
- **消息定义与编译**：使用 `protoc` 编译器将 `.proto` 文件转换为目标语言代码。
- **RPC 支持**：通过 gRPC 等框架实现高性能远程过程调用。
- **数据验证**：支持字段类型、默认值、枚举、嵌套消息、oneof、map 等高级语法。
- **插件机制**：可自定义插件扩展 `protoc` 的功能，例如生成 JSON 序列化、数据库映射等。

## 用法示例

### 1. 定义 `.proto` 文件 (`person.proto`)
```proto
syntax = "proto3";

package demo;

message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
}
```

### 2. 编译生成代码
```bash
# 生成 Go 代码
protoc --go_out=. person.proto
```

### 3. 在代码中使用（Go）
```go
package main

import (
	"fmt"
	"demo"

	"google.golang.org/protobuf/proto"
)

func main() {
	p := &demo.Person{
		Name:  "Alice",
		Id:    123,
		Email: "alice@example.com",
	}

	// 序列化
	data, err := proto.Marshal(p)
	if err != nil {
		panic(err)
	}

	// 反序列化
	var p2 demo.Person
	if err := proto.Unmarshal(data, &p2); err != nil {
		panic(err)
	}
	fmt.Println(p2)
}
```

## 进一步阅读
- 官方文档: <https://protobuf.dev/>
- gRPC 框架: <https://grpc.io/>

---

*保持更新请关注 GitHub 项目页面。```
