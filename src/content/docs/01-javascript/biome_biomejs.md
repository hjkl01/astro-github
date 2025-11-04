
---
title: biome
---


# Biome (biomejs/biome)

> 项目地址: <https://github.com/biomejs/biome>

Biome 是一个现代化、开源的 JavaScript/TypeScript 代码质量工具，集成了代码规范检查、格式化、类型检查与错误诊断，旨在提供统一且高效的开发体验。

## 主要特性

| 特性 | 说明 |
|------|------|
| **Linting（代码规范检查）** | 通过内置规则自动检测代码中的错误、潜在 bug 与不规范写法。支持 ESLint、TSLint 兼容模式。 |
| **Formatting（代码格式化）** | 自动格式化代码，保证统一风格；支持 Prettier 风格的 JSON 配置。 |
| **Type Checking（类型检查）** | 利用 TypeScript 编译器进行类型检查，捕获类型错误。 |
| **JSON & YAML Validation** | 对 JSON/YAML 文件进行语法与语义校验。 |
| **Editor Integration** | 原生支持 VS Code、JetBrains 系列 IDE、CLI 等多种编辑器。 |
| **Zero-config & Extensible** | 默认配置即可使用，支持自定义规则与插件。 |
| **Performance** | 用 Rust 编写，运行速度快，内存占用低。 |
| **GitHub Actions** | 通过官方 Action 快速集成 CI/CD 流水线。 |

## 安装方式

```bash
# npm
npm install biome --save-dev

# yarn
yarn add biome --dev

# pnpm
pnpm add biome --save-dev
```

## 基本用法

### CLI

```bash
# 检查所有文件
biome check .

# 只检查 JavaScript/TypeScript
biome check src/**/*.ts

# 自动修复
biome check . --apply

# 格式化
biome format .

# 仅格式化
biome format src/**/*.js --write
```

### 配置文件

在项目根目录创建 `biome.json`：

```json
{
  "extends": [
    "biome/js",
    "biome/typescript"
  ],
  "lint": {
    "rules": {
      "no-console": "error",
      "prefer-const": "warn"
    }
  },
  "formatter": {
    "indent": 2
  }
}
```

- `extends`：继承官方规则集或自定义集合。
- `lint.rules`：可开启、关闭或调整规则级别。
- `formatter`：格式化相关选项。

## VS Code 集成

1. 安装 `Biome` 插件。  
2. 在 VS Code 设置中启用 `biome.enable`。  
3. 保存文件时自动格式化，错误/警告会以诊断信息显示。

## GitHub Actions

```yaml
name: Lint & Format
on: [push, pull_request]
jobs:
  biome:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: biomejs/setup-biome@v1
      - run: biome check .
```

## 常见命令

| 命令 | 功能 |
|------|------|
| `biome check` | 进行 lint + type-check + format 检查 |
| `biome format` | 仅进行代码格式化 |
| `biome lint` | 仅进行 lint 检查 |
| `biome test` | 运行项目中的测试（兼容 Jest、Vitest 等） |

## 进一步阅读

- 官方文档: <https://biomejs.dev/>
- 配置示例: <https://github.com/biomejs/biome/tree/main/examples>
- 贡献指南: <https://github.com/biomejs/biome/blob/main/CONTRIBUTING.md>
