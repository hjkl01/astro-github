---
title: turborepo
---

# Turborepo

Turborepo 是一个为 JavaScript 和 TypeScript 代码库打造的高性能构建系统，使用 Rust 编写。

## 功能

- **任务缓存**：缓存任务输出以避免重复工作。
- **依赖图**：理解任务依赖关系以实现高效执行。
- **并行执行**：同时运行独立任务。
- **远程缓存**：与团队成员共享缓存。
- **守护进程**：后台进程以优化性能。
- **监视模式**：在文件更改时自动重新运行任务。
- **代码生成**：使用生成器来搭建代码。

## 安装

将 Turborepo 作为开发依赖项安装：

```bash
pnpm add turbo --save-dev --ignore-workspace-root-check
# 或
yarn add turbo --dev --ignore-workspace-root-check
# 或
npm install turbo --save-dev
# 或
bun install turbo --dev
```

## 用法

### 配置

创建 `turbo.json` 文件来定义任务：

```json
{
  "$schema": "https://turborepo.com/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

### 运行任务

使用以下命令运行任务：

```bash
turbo run build
turbo run dev
```

### 监视模式

启用监视模式以在更改时重新运行任务：

```bash
turbo watch dev lint test
```

### 其他命令

- `turbo query`：查询依赖图。
- `turbo telemetry enable/disable`：管理遥测。

更多详细信息，请访问 [turborepo.com](https://turborepo.com)。
