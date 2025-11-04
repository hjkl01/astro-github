
---
title: Bella
---


# Bella

> **GitHub 项目地址**  
> https://github.com/Jackywine/Bella

---

## 简介

Bella 是一个轻量级、易用的跨平台命令行工具，旨在帮助开发者快速完成常见任务（如项目脚手架、文件转换、代码生成等）。它基于现代 JavaScript/TypeScript 生态，提供可扩展的插件机制，支持用户自定义脚本与模板。

---

## 主要特性

| # | 特性 | 说明 |
|---|------|------|
| 1 | **跨平台支持** | Windows / macOS / Linux 直接运行，无需额外依赖。 |
| 2 | **CLI + API** | 命令行工具易于上手，同时提供 Node.js API，便于集成到 CI/CD 或自定义脚本。 |
| 3 | **插件体系** | 通过 `@bella/plugin-*` 可扩展功能，插件间互相解耦。 |
| 4 | **模板引擎** | 支持 Handlebars / EJS，快速生成项目文件。 |
| 5 | **配置文件** | `.bella.json` 支持全局与项目级配置，方便团队协作。 |
| 6 | **文件监控** | `bella watch` 能实时监控目录变化并同步更新。 |
| 7 | **错误追踪** | 内置友好错误提示和自动恢复机制。 |

---

## 安装

```bash
# 通过 npm 安装
npm install -g bella

# 或使用 yarn
yarn global add bella
```

> **依赖**  
> Node.js >= 18.x

---

## 基本用法

### 1. 初始化项目

```bash
bella init <project-name>
```

> 该命令会根据预置模板创建一个新的项目结构。  
> 你也可以使用自定义模板：
> ```bash
> bella init <project-name> --template ./my-template
> ```

### 2. 生成代码

```bash
bella generate <component-name>
```

> 自动根据 `component` 模板生成文件，可以通过 `--type` 指定类型。

### 3. 监控文件

```bash
bella watch
```

> 当源文件更改时自动触发编译、格式化等操作。

### 4. 设置全局配置

> 在根目录创建 `.bella.json`，示例：

```json
{
  "author": "Your Name",
  "license": "MIT",
  "plugins": [
    "@bella/plugin-eslint",
    "@bella/plugin-prettier"
  ]
}
```

---

## 示例

以下示例展示在一个 Vue 3 + Vite 项目中使用 Bella 快速创建组件、写单元测试：

```bash
# 先安装 Bella
npm -g bella

# 在项目根目录下
bella init vue3-vite-app

# 生成组件
bella generate MyButton --type component

# 生成测试
bella generate MyButton.test --type test
```

---

## 插件使用

Bella 的插件遵循统一的接口标准，使用方式如下：

```bash
# 安装插件
bella add @bella/plugin-eslint

# 查看已安装插件
bella list-plugins
```

---

## 贡献

欢迎 Issue / PR，详细贡献指南请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 参考

- 官方文档: https://github.com/Jackywine/Bella/tree/main/docs
- GitHub 仓库: https://github.com/Jackywine/Bella
- Issues: https://github.com/Jackywine/Bella/issues
