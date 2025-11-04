
---
title: cli
---


# CLI

**仓库地址**: <https://github.com/npm/cli>

---

## 主要特性

- **包管理**  
  - **安装**: `npm install <package>` 或 `npm i <package>`  
  - **卸载**: `npm uninstall <package>` 或 `npm un <package>`  
  - **更新**: `npm update <package>`

- **脚本执行**  
  - 在 `package.json` 的 `scripts` 字段中定义脚本，使用 `npm run <script>` 运行。  
  - 支持自定义命令别名，例如 `npm test`, `npm start`, `npm build` 等。

- **依赖处理**  
  - 自动解析 `package.json` 中的 `dependencies` 和 `devDependencies`。  
  - 支持在全局或本地安装，使用 `-g` 或 `--global`。

- **缓存与离线模式**  
  - 使用本地缓存避免重复下载。  
  - 离线安装模式 `npm install --offline`。

- **配置与自定义**  
  - 通过 `.npmrc` 或 `npm config` 命令管理全局或项目级配置。  
  - 支持自定义 registry、代理、压缩包拆分等。

- **常用命令**  
  - `npm help <command>`：查看命令帮助。  
  - `npm list`：查看项目依赖树。  
  - `npm outdated`：查看可更新包。  
  - `npm link`：在本地开发环境中链接包。

## 功能概览

| 功能 | 命令示例 | 描述 |
|------|----------|------|
| **安装包** | `npm install lodash` | 下载并安装到 `node_modules`。 |
| **全局安装** | `npm install -g typescript` | 全局安装 TypeScript。 |
| **卸载包** | `npm uninstall react` | 从 `node_modules` 移除包。 |
| **执行脚本** | `npm run build` | 根据 `scripts.build` 执行构建脚本。 |
| **查看配置** | `npm config get registry` | 查看当前 registry 设置。 |
| **更改配置** | `npm config set save-prefix "^"` | 设置保存前缀。 |
| **离线安装** | `npm install --offline` | 使用缓存离线安装。 |

## 用法示例

```bash
# 初始化项目
npm init

# 安装依赖
npm install express --save
npm install mocha --save-dev

# 运行脚本
npm run test

# 更新所有可用的包
npm update

# 查看过期的包
npm outdated

# 设定自定义 registry
npm config set registry https://registry.npm.taobao.org

# 全局安装
npm i -g yarn
```

> ⚡ **提示**：更多详细用法请参考官方文档或运行 `npm help`。

---