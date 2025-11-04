
---
title: lingo.dev
---


# lingo.dev（lingodotdev 项目）

**项目地址**: https://github.com/lingodotdev/lingo.dev

## 主要特性

- **统一多语言游戏配套工具**：提供一套可复用的工具，方便开发多语言版本的游戏。
- **高度可扩展的脚本系统**：支持使用自定义脚本快速实现游戏逻辑。
- **跨平台支持**：兼容 Windows、macOS 以及 Linux，并可编译为 WebAssembly。
- **内置 UI 引擎**：简化 UI 设计与交互，支持皮肤自定义。
- **调试工具**：包含实时日志、断点调试及性能分析。
- **资源管理器**：高效管理游戏资源（图片、音频、脚本等），支持热更新。

## 主要功能

| 功能 | 描述 |
|------|------|
| **脚本编辑器** | 基于 Lua 或 TypeScript，支持自动补全、语法检查 |
| **资源打包** | 通过 CLI 或 GUI 打包资源，生成压缩包或单文件 |
| **本地化工具** | 提供多语言字符串提取、模板生成和校对功能 |
| **协作模式** | 通过 GitHub Actions 实现持续集成与自动部署 |
| **插件系统** | 可插拔扩展功能，例如第三方支付、社交分享 |
| **接口文档生成** | 自动生成 API 文档，支持 Markdown 与 HTML 输出 |

## 用法

### 1. 克隆仓库

```bash
git clone https://github.com/lingodotdev/lingo.dev.git
cd lingo.dev
```

### 2. 环境依赖

```bash
# 安装 Node.js 16+ 与 pnpm
pnpm install
```

### 3. 开发

```bash
# 启动开发服务器
pnpm dev
```

- 浏览器访问 `http://localhost:5173`。

### 4. 构建

```bash
pnpm build
```

- 构建产物位于 `dist/`。

### 5. 打包资源

```bash
# 资源打包示例
pnpm run pack:resources
```

- 打包完成后生成的文件在 `build/assets/`。

### 6. 本地化

```bash
# 提取字符串
pnpm run i18n:extract

# 生成校对文件
pnpm run i18n:prepare
```

- 生成的文件位于 `src/locales/`。

### 7. 插件使用

- 将插件代码放入 `plugins/` 目录。
- 在 `config/plugin.json` 中列出插件名称。
- 重新构建即可。

## 参与贡献

- Fork → 代码改动 → Push → Pull Request
- 请遵循 `conventional commits` 规范。

## 许可

MIT License - 详情见 [LICENSE](LICENSE)。
