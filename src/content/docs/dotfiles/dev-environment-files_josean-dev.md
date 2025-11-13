---
title: dev-environment-files
---

# dev-environment-files_josean-dev

## 项目简介

这是一个完整的开发环境配置文件集合，由 Josean Martinez (josean-dev) 维护。该项目提供了针对 macOS 的现代化开发环境设置，包括 Neovim 编辑器、Tmux 多路复用器、终端配置、窗口管理器等组件。

## 主要功能

### 1. Neovim 配置

- 使用 lazy.nvim 作为插件管理器
- 包含完整的 LSP 支持、语法高亮、自动补全
- 集成 Telescope 模糊查找、Treesitter 语法解析
- 支持多种编程语言的开发环境

### 2. Tmux 配置

- 自定义快捷键和主题
- 支持窗口和面板管理
- 与 Neovim 无缝集成

### 3. 终端配置

- WezTerm 终端配置（替代之前的 Alacritty）
- Zsh shell 配置
- 自定义颜色主题

### 4. 窗口管理

- Yabai 磁贴窗口管理器配置
- Aerospace 窗口管理器配置
- Sketchybar 自定义菜单栏

### 5. 其他工具

- QMK 键盘固件配置
- 各种 CLI 工具集成

## 使用方法

### 安装步骤

1. **克隆仓库**

   ```bash
   git clone https://github.com/josean-dev/dev-environment-files.git
   cd dev-environment-files
   ```

2. **备份现有配置**

   ```bash
   # 备份现有配置文件
   cp ~/.zshrc ~/.zshrc.backup
   cp ~/.tmux.conf ~/.tmux.conf.backup
   # 等等
   ```

3. **复制配置文件**

   ```bash
   # 复制到相应位置
   cp .zshrc ~/.zshrc
   cp .tmux.conf ~/.tmux.conf
   cp -r .config/* ~/.config/
   ```

4. **安装依赖工具**

   **终端工具：**

   ```bash
   brew install wezterm
   brew install zsh
   ```

   **CLI 工具：**

   ```bash
   brew install fzf fd bat delta eza tldr thefuck
   ```

   **Neovim 相关：**

   ```bash
   brew install neovim
   brew install ripgrep
   brew install node  # 用于 TypeScript/JavaScript LSP
   ```

   **字体：**

   ```bash
   brew tap homebrew/cask-fonts
   brew install font-meslo-lg-nerd-font
   ```

5. **安装插件和语言服务器**
   - 打开 Neovim，lazy.nvim 会自动安装插件
   - Mason 会自动安装配置的语言服务器

### 配置说明

- **Neovim**: 配置文件位于 `.config/nvim/`
- **Tmux**: 配置文件为 `.tmux.conf`
- **Zsh**: 配置文件为 `.zshrc`
- **WezTerm**: 配置文件为 `.wezterm.lua`
- **Yabai/Sketchybar**: 配置文件位于 `.config/yabai/` 和 `.config/sketchybar/`

### 注意事项

- 这些配置主要用于 macOS
- 建议先备份现有配置
- 某些功能可能需要额外的手动配置
- 定期检查更新以获取最新功能

## 相关资源

- [YouTube 播放列表](https://youtube.com/playlist?list=PLnu5gT9QrFg36OehOdECFvxFFeMHhb_07) - 详细的设置教程
- [博客文章](https://josean.com/posts/how-to-setup-neovim-2024) - Neovim 设置指南
- [GitHub 仓库](https://github.com/josean-dev/dev-environment-files) - 源代码和文档
