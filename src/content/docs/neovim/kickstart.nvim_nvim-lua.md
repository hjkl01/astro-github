---
title: kickstart.nvim
---

# kickstart.nvim（nvim-lua/kickstart.nvim）

项目地址：<https://github.com/nvim-lua/kickstart.nvim>

## 项目概述

> Description from GitHub: A launch point for your personal nvim configuration

## 主要特性

| 特色           | 说明                                                                                  |
| -------------- | ------------------------------------------------------------------------------------- |
| **插件管理**   | 使用 `lazy.nvim` 作为插件管理器，按需加载、并行安装插件。                             |
| **基础插件**   | 包含常用插件：nvim-treesitter、nvim-lspconfig、nvim-cmp、telescope、neotest 等。      |
| **通信与 LSP** | 快速配置多种语言服务器（Python、TypeScript、Lua 等），并集成 LSP UI、诊断和代码动作。 |
| **补全**       | 通过 `nvim-cmp` 为多种补全来源（LSP、snippets、buffer、path）提供统一体验。           |
| **主题与界面** | 默认 `tokyonight` 主题，支持透明、状态栏、标题栏等自定义。                            |
| **键盘映射**   | 以键位“jk”离开 insert mode、用 `gd` 跳转到定义、`K` 查看 hover 等快捷键。             |
| **测试与调试** | 集成 `neotest`，支持多语言测试框架（Python pytest、Rust cargo test 等）。             |
| **代码片段**   | `LuaSnip` 提供多种内置片段，支持 Snippet 触发。                                       |
| **文件管理**   | `telescope.nvim` 提供快速文件搜索、buffers、git 状态等功能。                          |
| **外观优化**   | 支持透明窗口、残留行、圆角、光标等高质量视觉体验。                                    |

## 使用方法

1. **克隆仓库**

   ```bash
   git clone https://github.com/nvim-lua/kickstart.nvim ~/.config/nvim
   ```

2. **安装 lazy.nvim**  
   运行 Vim/ Neovim 并执行：

   ```vim
   :Lazy sync
   ```

   这将自动下载插件并同步安装。

3. **启动 Neovim**

   ```bash
   nvim
   ```

   第一次启动会进 `lazy` 进行插件安装，等待完成后即成为完备开发环境。

4. **自定义配置**
   - `init.lua`：全局设置、键位、插件加载顺序。
   - `lua/plugins.lua`：插件列表及其配置信息。
   - `lua/keymaps.lua`：快捷键映射。  
     可根据个人需求修改这些文件后重新执行 `:Lazy sync` 或重启 Neovim。

5. **常用命令**  
   | 命令 | 说明 |
   |------|------|
   | `:Lazy` | 打开插件管理器，查看已安装、待更新或可选插件。 |
   | `:LspInfo` | 查看 LSP 服务器信息。 |
   | `:Telescope find_files` | 快速打开文件。 |
   | `:Git status` | 查看 git 状态。 |
   | `:Neotest run` | 运行当前文件的测试。 |
   | `:bash .` | 打开终端。 |

## 快捷键简介

| 快捷键       | 功能                   |
| ------------ | ---------------------- |
| `jk`         | 退出 Insert 模式       |
| `gd`         | 跳转到定义（LSP）      |
| `gD`         | 跳转到声明（LSP）      |
| `<Leader>rn` | 重命名符号（LSP）      |
| `K`          | 查看 hover 信息（LSP） |
| `gd`         | 跳转到定义             |
| `gr`         | 跳转到引用             |
| `<Leader>f`  | 格式化文件（LSP）      |
| `<Leader>t`  | 运行 Neotest 相关命令  |

---

> 该项目仅为示例，实际使用时请根据项目需求做适配或自行扩展。祝你玩得愉快！
