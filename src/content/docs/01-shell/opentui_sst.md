---
title: opentui
---

# OpenTUI (sst/opentui)

> 项目地址: <https://github.com/sst/opentui>

## 概述

OpenTUI 是一个用于构建终端用户界面 (TUI) 的 TypeScript 库。它提供了现代化的 API 来创建命令行应用程序的交互式界面。目前仍在开发中，还未准备好用于生产环境。它将成为 [opencode](https://opencode.ai) 和 [terminaldotshop](https://terminal.shop) 的基础 TUI 框架。

## 主要特性

- **TypeScript 原生支持**：使用 TypeScript 构建，提供类型安全。
- **多种框架集成**：支持 React、SolidJS 等现代前端框架。
- **核心库独立运行**：`@opentui/core` 包完全独立工作，提供命令式 API 和所有基础组件。
- **跨平台兼容**：可在多个操作系统上运行。
- **Zig 构建**：使用 Zig 语言进行底层实现，确保高性能。
- **组件化设计**：提供可重用的组件，便于组合使用。
- **事件驱动**：支持用户输入和其他事件的处理。
- **主题自定义**：允许自定义主题和界面外观。

## 包结构

- **`@opentui/core`** - 核心库，提供命令式 API 和所有基础组件。
- **`@opentui/solid`** - SolidJS 协调器。
- **`@opentui/react`** - React 协调器。
- **`@opentui/vue`** - Vue 协调器（未维护）。
- **`@opentui/go`** - Go 绑定（未维护）。

## 要求

- **Zig**：必须安装 [Zig](https://ziglang.org/learn/getting-started/) 来构建包。

## 安装

### TypeScript/JavaScript

```bash
bun install @opentui/core
```

## 用法

### 快速开始

```bash
# 使用 bun 创建新项目
bun create tui

# 运行示例
cd packages/core
bun run src/examples/index.ts
```

### 开发示例

```typescript
import { createApp } from '@opentui/core';

// 创建 TUI 应用
const app = createApp();

// 添加组件和事件处理
// ... 具体 API 见文档
```

### 基本示例

```typescript
import { createApp } from '@opentui/core';

// 创建 TUI 应用
const app = createApp();

// 添加组件和事件处理
// ... 具体 API 见文档
```

## 开发

### 本地开发链接

当开发 OpenTUI 时，可以使用 `link-opentui-dev.sh` 脚本创建符号链接：

```bash
./scripts/link-opentui-dev.sh /path/to/your/project
```

选项：

- `--react` - 同时链接 `@opentui/react`
- `--solid` - 同时链接 `@opentui/solid` 和 `solid-js`
- `--dist` - 链接构建的 `dist` 目录而不是源码
- `--copy` - 复制 dist 目录而不是符号链接

## 文档和支持

- 官方文档: <https://opentui.com>
- GitHub: <https://github.com/sst/opentui>
- 社区展示: [awesome-opentui](https://github.com/msmps/awesome-opentui)

## 注意事项

- 该项目目前处于开发阶段，不适合生产环境使用。
- 需要 Zig 环境来构建和开发。
