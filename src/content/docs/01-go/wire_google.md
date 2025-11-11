---
title: wire
---

# Wire

## 项目简介

Wire 是 Google 开发的 Go 语言代码生成工具，用于自动化依赖注入（Dependency Injection）。它通过编译时生成代码来连接组件，避免使用全局变量，鼓励显式初始化。Wire 不依赖运行时状态或反射，使得代码即使在手动初始化时也能正常工作。

## 主要功能

- **编译时依赖注入**：在编译时生成初始化代码，确保类型安全和性能。
- **显式依赖管理**：依赖关系通过函数参数表示，便于理解和维护。
- **代码生成**：自动生成 wire_gen.go 文件，包含初始化逻辑。
- **无运行时开销**：生成的代码是纯 Go 代码，无需额外运行时库。

## 安装

使用以下命令安装 Wire：

```bash
go install github.com/google/wire/cmd/wire@latest
```

确保 `$GOPATH/bin` 在你的 `$PATH` 中。

## 基本用法

1. 定义提供者函数（Provider Functions）：这些函数创建和返回依赖项。
2. 使用 `wire.Build` 函数声明依赖图。
3. 运行 `wire` 命令生成代码。

示例：

```go
// +build wireinject

package main

import "github.com/google/wire"

func InitializeApp() (*App, error) {
    wire.Build(NewApp, NewDB, NewLogger)
    return &App{}, nil
}
```

运行 `wire` 后，会生成 `wire_gen.go` 文件。

## 文档

- [教程](https://github.com/google/wire/blob/main/_tutorial/README.md)
- [用户指南](https://github.com/google/wire/blob/main/docs/guide.md)
- [最佳实践](https://github.com/google/wire/blob/main/docs/best-practices.md)
- [FAQ](https://github.com/google/wire/blob/main/docs/faq.md)

## 项目状态

Wire 目前处于 beta 阶段，被认为是功能完整的。我们不再接受新功能请求，但欢迎 bug 报告和修复。

## 社区

如有问题，请使用 [GitHub Discussions](https://github.com/google/wire/discussions)。
