---
title: mise
---


# mise (by jdx)

- **项目地址**: https://github.com/jdx/mise

## 主要特性

| 特色 | 说明 |
|------|------|
| **轻量化** | 单个可执行文件，GitHub release 页面直接下载，内置快捷命令，启动速度快 |
| **多语言支持** | 兼容 Node、Python、Ruby、Go、Rust、.NET、Java、Lua、Elixir 等 100+ 生态工具 |
| **`.tool-versions` 配置** | 在项目根目录声明所需工具与版本，类似 asdf 但更简洁、速度更快 |
| **插件化** | 通过 `mise plugin` 支持第三方插件，新增语言/工具几乎无缝集成 |
| **全局与项目级别** | `mise use --global` 设置全局默认版本，`mise use` 或 `.tool-versions` 设置项目级别 |
| **自动切换** | `mise shell` 侦测 `.tool-versions` 自动切换到对应版本，支持 `mise exec` 与 `mise run` |
| **交互式安装** | 自动下载对应工具版本，缓存本地，已安装的版本不会再次下载 |

## 核心命令

| 命令 | 用途 |
|------|------|
| `mise install < TOOL_NAME >` | 安装工具或指定版本：`mise install python@3.11.4` |
| `mise use < TOOL_NAME >` | 切换工具版本到全局或局部 |
| `mise which < TOOL_NAME >` | 查看当前使用的工具路径 |
| `mise ls-remote < TOOL_NAME >` | 列出远程可用版本 |
| `mise ls `< TOOL_NAME > or `mise ls` | 列出本地已安装版本 |
| `mise run < TASK >` | 在当前项目的环境中执行已定义的任务 |
| `mise exec < TOOL_NAME > < CMD >` | 直接执行指定工具的命令，如 `mise exec python --version` |
| `mise plugin install < PLUGIN_NAME >` | 安装插件 |

## 安装步骤

```bash
# 方式 1：使用安装脚本
curl -fsSL https://mise.jdx.dev/install.sh | sh

# 方式 2：通过 Homebrew（macOS/Linux）
brew install jdx/mise/mise

# 方式 3：手动下载
# 访问 https://github.com/jdx/mise/releases，下载对应系统的二进制文件，解压后加入 PATH
```

## 开箱即用示例

1. **创建项目目录**  
   ```bash
   mkdir myproj && cd myproj
   ```

2. **声明工具与版本**  
   在项目根目录新建 `.tool-versions`：  
   ```
   node 20.13.0
   python 3.11.6
   rust stable
   ```

3. **同步安装**  
   ```bash
   mise sync
   # 或者
   mise install
   ```

4. **使用工具**  
   ```bash
   # 直接使用已安装工具
   node --version
   python --version
   ```

5. **执行项目中定义的脚本**  
   在 `package.json` 或 `mise.toml` 定义任务后，执行：  
   ```bash
   mise run build
   ```

## 进一步阅读

- 官方文档: https://mise.jdx.dev
- GitHub 仓库: https://github.com/jdx/mise
- 发行管理: https://github.com/jdx/mise/releases

---
**保存路径**: `src/content/docs/00/mise_jdx.md`
