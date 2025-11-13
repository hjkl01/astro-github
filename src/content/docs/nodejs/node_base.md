---
title: node
---


# Node 基础框架 (Node Base)

## 项目地址
https://github.com/base/node

## 主要特性
- **插件化架构**：通过 `node.yml` 配置文件，支持官方及社区插件，插件可自行扩展功能。
- **统一配置管理**：使用 `node.yml`（或 `node.json`）统一存放环境变量、构建选项、插件列表等。
- **内置脚本与任务**：提供 `run`, `build`, `test`, `deploy` 四大核心命令，可在配置文件中自定义脚本。
- **交互式 CLI**：支持命令帮助、自动补全、历史记录，使用体验与现代框架保持一致。
- **跨平台兼容**：原生支持 Windows、macOS、Linux，自动处理路径、权限等差异。
- **热重载开发模式**：`node dev` 命令启动开发服务，文件更改即可自动重启或热更新。

## 快速使用

```bash
# 安装全局 CLI
npm install -g @base/node

# 创建新项目
node init my-app
cd my-app

# 安装示例插件
npm i @base/web

# 启动开发环境
node dev

# 生产构建
node build

# 运行测试
node test
```

## 配置示例（`node.yml`）

```yaml
env:
  NODE_ENV: development
  PORT: 3000

plugins:
  - @base/web
  - @base/db

tasks:
  build:
    script: "webpack --mode production"
  test:
    script: "jest"
```

## 插件使用示例

```bash
# 安装插件
npm i @base/example-plugin

# 在 node.yml 启用
plugins:
  - @base/example-plugin

# 在代码中调用
const plugin = require('@base/example-plugin')
plugin.doSomething()
```

## 贡献指南
1. Fork 本仓库  
2. 创建功能/修复的分支  
3. 提交 Pull Request，遵循 `conventional commits` 标准  
4. 通过 CI 后，等待合并

## 支持与反馈
- Issue 跟踪: https://github.com/base/node/issues  
- 文档 Wiki: https://github.com/base/node/wiki  
