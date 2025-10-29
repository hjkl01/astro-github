
---
title: prettier
---

# Prettier

**项目地址**：[https://github.com/prettier/prettier](https://github.com/prettier/prettier)

---

## 主要特性
- **自动格式化**：根据统一的风格规则自动格式化代码，消除代码风格争议。
- **语言支持广泛**：内置对 JavaScript、TypeScript、JSON、HTML、CSS、SCSS、Markdown、Vue、React 等多种语言的格式化。
- **可扩展插件**：通过插件系统支持更多语言或自定义规则。
- **无配置即用**：默认配置已覆盖大多数项目需求，保持“零配置即用”体验。
- **高性能**：采用高效实现，格式化速度快，适合在 CI/CD、IDE 插件等场景使用。

---

## 核心功能
| 功能 | 说明 |
|------|------|
| 代码格式化 | 自动修复缩进、分号、引号、空格、括号等 |
| 代码重构 | 自动调整字符串拼接、数组/对象字面量、函数参数等 |
| 代码检查 | 通过 `--check` 参数检测文件是否已格式化 |
| 代码修复 | 通过 `--write` 参数直接写回格式化结果 |
| 预设插件 | 支持 Prettier 官方插件（如 `prettier/plugins/markdown`） |
| API 使用 | 提供 Node.js API，方便集成到自定义工具链 |

---

## 用法

### 1. 安装

```bash
# npm
npm install --save-dev prettier

# Yarn
yarn add --dev prettier

# pnpm
pnpm add -D prettier
```

### 2. 命令行

```bash
# 检查格式
prettier --check "src/**/*.js"

# 自动格式化并写回
prettier --write "src/**/*.js"

# 只格式化单个文件并输出到终端
prettier "src/index.js"
```

### 3. 与编辑器集成

| 编辑器 | 集成方式 |
|--------|----------|
| VS Code | 安装官方插件 `ESLint` +  `Prettier - Code formatter`，或直接在 `settings.json` 设置 `"editor.defaultFormatter": "esbenp.prettier-vscode"` |
| Sublime Text | 安装 `Sublime-Prettier` 插件 |
| Atom | 安装 `prettier-atom` 插件 |
| Vim / Neovim | 使用 `coc-prettier` 或 `vim-prettier` 插件 |

### 4. 配置文件

在项目根目录放置 `.prettierrc` 或 `prettier.config.js`：

```json
{
  "semi": false,
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false
}
```

### 5. 与 ESLint 结合

```bash
npm install --save-dev eslint-config-prettier eslint-plugin-prettier
```

在 `.eslintrc.js`：

```js
module.exports = {
  extends: [
    "plugin:prettier/recommended" // 关闭 ESLint 与 Prettier 冲突的规则
  ]
};
```

### 6. CI/CD

在 GitHub Actions：

```yaml
name: Lint & Format Check

on: [push, pull_request]

jobs:
  prettier:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npx prettier --check .
```

---

## 常见命令

| 选项 | 含义 |
|------|------|
| `--write` | 直接修改文件 |
| `--check` | 检查文件是否已格式化 |
| `--list-different` | 列出不符合格式的文件 |
| `--config` | 指定配置文件路径 |
| `--ignore-path` | 指定 `.prettierignore` 路径 |

---

> 预设插件、更多高级用法请参考官方文档：[https://prettier.io/docs/en/](https://prettier.io/docs/en/)