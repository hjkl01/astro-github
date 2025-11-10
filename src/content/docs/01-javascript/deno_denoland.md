---
title: deno
---

# Deno

> **项目地址**: [https://github.com/denoland/deno](https://github.com/denoland/deno)

## 项目简介
Deno 是一个现代化、简洁、安全的 JavaScript/TypeScript 运行时，旨在解决 Node.js 在安全、模块管理、标准库与工具链方面的痛点。它由 Node.js 的创始人 Ryan Dahl 领导开发，强调一键即用、无须 `npm`，以及对最新 Web 标准的完整支持。

## 核心特性
- **原生 TypeScript**：无需编译器，直接执行 `.ts` 文件。
- **安全默认**：脚本默认被沙箱化，需显式授权文件、网络、环境等权限。
- **单一可执行文件**：一次下载即可跨平台使用，完全无依赖。
- **现代标准库**：内置 `std` 模块，覆盖文件系统、网络、测试、格式化等常见需求。
- **高效工具链**：集成 `deno run`, `deno fmt`, `deno lint`, `deno test`, `deno bundle` 等命令。
- **模块化导入**：支持按需从 URL、Deno.land、NPM 或本地路径加载模块，且自动缓存。
- **加载缓存**：首次下载后模块会被缓存，后续启动速度更快。

## 主要功能
- **脚本运行**  
  ```bash
  deno run app.ts
  ```
- **权限授权**  
  ```bash
  deno run --allow-read --allow-net app.ts
  ```
- **单文件脚本下载**  
  ```bash
  deno run https://deno.land/std/examples/welcome.ts
  ```
- **代码格式化**  
  ```bash
  deno fmt file.ts
  ```
- **单元测试**  
  ```bash
  deno test
  ```
- **打包为单文件**  
  ```bash
  deno bundle input.ts output.js
  ```
- **发布模块至 deno.land**  
  ```bash
  deno publish
  ```

## Quick Start
```bash
# 安装 Deno（macOS / Linux）
curl -fsSL https://deno.land/install.sh | sh

# 运行 TypeScript 示例
deno run --allow-net https://deno.land/std/examples/welcome.ts
```

## 开源协议
本项目基于 BSD 3-Clause 许可证发布。更多细节请参见 `LICENSE` 文件。