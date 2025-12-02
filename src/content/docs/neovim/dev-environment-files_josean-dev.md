---
title: dev-environment-files
---

# dev-environment-files

这是一个由 josean-dev 维护的开发环境配置文件集合，主要用于设置和优化开发工作流。项目包含了 Neovim、Tmux、WezTerm 等工具的配置，以及一些 macOS 相关的窗口管理器设置。

## 主要功能

### Neovim 配置

- 使用 lazy.nvim 作为插件管理器
- 包含丰富的插件，如 Telescope（模糊查找）、Treesitter（语法高亮）、LSP（语言服务器协议）支持等
- 支持多种编程语言的自动补全、格式化和 linting
- 自定义颜色方案和界面优化

### Tmux 配置

- 提供 .tmux.conf 文件，用于配置 Tmux 会话管理
- 支持窗口和面板的快速导航

### 终端设置

- WezTerm 配置（.wezterm.lua），替代了之前的 Alacritty
- Zsh 配置（.zshrc），包含别名和插件设置
- 颜色方案文件

### 窗口管理器

- Yabai 和 Aerospace：macOS 上的平铺窗口管理器配置
- Sketchybar：自定义菜单栏

## 用法

1. **克隆仓库**：

   ```
   git clone https://github.com/josean-dev/dev-environment-files.git
   ```

2. **安装依赖**：
   - 对于 Neovim：安装 Neovim 0.9+、Ripgrep、Nerd Font 等
   - 对于终端：安装 WezTerm、fzf、bat、eza 等 CLI 工具
   - 对于 macOS：安装 Yabai、Aerospace、Sketchybar 等

3. **复制配置文件**：
   - 将 .config 目录复制到你的主目录
   - 复制 .zshrc、.tmux.conf 等文件

4. **启动 Neovim**：
   - 首次运行时，lazy.nvim 会自动安装插件
   - Mason 会安装语言服务器

注意：这些配置主要用于 macOS 环境，其他系统可能需要调整。建议先备份现有配置，并根据个人需求修改。
