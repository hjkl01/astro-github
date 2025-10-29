
---
title: dyad
---


# dyad

https://github.com/dyad-sh/dyad

## 简介
dyad 是一个轻量级的命令行工具，旨在简化项目的构建、部署和管理流程。它支持多种插件和脚本，可与现有工作流无缝集成。

## 安装
```bash
npm install -g dyad
```

## 基本用法
```bash
# 初始化项目
dyad init

# 运行构建
dyad build

# 部署到目标环境
dyad deploy
```

## 主要特性
- **插件化架构**：通过`dyad-plugin-*`可扩展构建、测试、部署功能。
- **多环境支持**：一次配置即可在本地、CI 与云端部署。
- **自定义任务**：在`scripts`目录下添加自定义脚本，使用`dyad task <name>`执行。
- **命令别名**：使用`dyad alias add <alias> <command>`快速调用复杂命令。
- **可视化日志**：支持彩色输出与实时进度条，易于监控任务状态。

## 配置文件
```json
// dyad.json
{
  "tasks": {
    "build": "npm run build",
    "deploy": "scp dist/* user@server:/var/www"
  },
  "plugins": [
    "dyad-plugin-testing",
    "dyad-plugin-deployment"
  ]
}
```

## 贡献
欢迎提交 issue 或 pull request。请在提交前先阅读 `CONTRIBUTING.md`。

---

> 项目地址: https://github.com/dyad-sh/dyad

