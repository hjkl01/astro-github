
---
title: dev-environment-files
---


# dev-environment-files（josean-dev）

**项目地址**：<https://github.com/josean-dev/dev-environment-files>

## 主要特性

1. **统一的开发环境配置**  
   - 通过 `devcontainer.json` 和 Dockerfile，快速搭建与项目兼容的容器化开发环境。  
   - 支持多语言（Node.js, Python, Go, Rust 等）一键安装。

2. **VS Code 插件与设置**  
   - `extensions.json` 预装常用插件（ESLint, Prettier, GitLens 等）。  
   - `settings.json` 统一编码、排版、插件行为。

3. **快捷键与脚本**  
   - `keybindings.json` 封装常用操作（调试、查找、格式化）。  
   - `scripts/` 目录下的脚本实现自动化构建、测试、Lint 等。

4. **跨平台支持**  
   - 配置兼容 Windows、macOS、Linux。  
   - 默认使用 Docker，无需手动安装多版本语言运行时。

5. **可扩展与可复用**  
   - 所有配置文件皆可直接引用或复制到项目根目录，适用于多种类型项目。  
   - 通过 `env` 文件管理环境变量，易于切换线上/测试环境。

## 功能概览

| 功能 | 说明 |
|------|------|
| devcontainer | 内嵌 Docker 运行时，提供完整依赖与工具链。 |
| vsc-extensions | 自动安装必备 VS Code 插件，提升开发效率。 |
| coding-styles | 统一代码风格，集成 Prettier + ESLint。 |
| scripts  | `npm run dev`、`npm test`、`npm lint` 等简化命令。 |
| env-config | `.env.example` 支持不同环境变量模板。 |

## 用法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/josean-dev/dev-environment-files.git
   ```

2. **复制配置到项目根目录**  
   ```bash
   cp -r dev-environment-files/.project-config/ .
   # 其中 ./*.json 等文件会覆盖到项目根目录
   ```

3. **启动 VS Code**  
   - 在项目根目录打开 VS Code，按 `F1` → `Remote-Containers: Open Folder in Container`，让开发环境在 Docker 容器中运行。

4. **执行脚本**  
   ```bash
   npm run dev    # 启动开发服务器
   npm run test   # 运行单元测试
   npm run lint   # 代码检查与格式化
   ```

5. **添加自定义插件或脚本**  
   - 修改 `extensions.json` 或 `keybindings.json`，重新加载 VS Code 即可生效。

> ⚡️**提示**：如果你不想使用 Docker，只需修改 `devcontainer.json` 中的 `dockerComposeFile` 或移除它，改为直接使用本机环境。

## 参考

- [VS Code Remote-Containers 文档](https://code.visualstudio.com/docs/remote/containers)
- [Docker 官方文档](https://docs.docker.com/)
- [Node.js 官方文档](https://nodejs.org/)，以及对应语言的官方安装说明。

---

> 以上内容已保存到文件 `src/content/docs/00/dev-environment-files_josean-dev.md`。祝你使用愉快!