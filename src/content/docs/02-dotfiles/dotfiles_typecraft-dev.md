---
title: dotfiles
---

## 功能

这个仓库包含typecraft-dev的dotfiles配置集合，包括以下工具的配置文件：

- **Neovim** (.config/nvim)：自定义的Neovim编辑器配置，使用Lua编写。
- **Hyprland** (.config/hypr)：Wayland合成器Hyprland的配置，包括窗口管理器设置。
- **Alacritty** (.config/alacritty)：GPU加速终端模拟器的配置。
- **Kitty** (.config/kitty)：快速、功能丰富的终端模拟器配置。
- **Ghostty** (.config/ghostty)：现代终端模拟器配置。
- **Tmux**：终端多路复用器配置。
- **Zsh** (.zshrc)：Zsh shell的配置文件。
- **Polybar** (.config/polybar)：状态栏配置。
- **Waybar** (.config/waybar)：Wayland状态栏配置。
- **Rofi/Wofi** (.config/rofi, .config/wofi)：应用启动器配置。
- **Picom** (.config/picom)：X11合成器配置。
- **Hyprlock/Hyprpaper** (.config/hypr)：Hyprland锁屏和壁纸配置。
- **Starship** (.config/starship)：Shell提示符配置。
- **Xresources**：X11资源配置。
- **Screenlayout** (.screenlayout)：显示器布局脚本。
- **Backgrounds** (.config/backgrounds)：壁纸文件。

这些配置旨在提供一个高度自定义的Linux桌面环境，专注于Wayland生态系统和现代工具。

## 用法

1. **克隆仓库**：

   ```bash
   git clone https://github.com/typecraft-dev/dotfiles.git
   cd dotfiles
   ```

2. **备份现有配置**（可选但推荐）：

   ```bash
   cp -r ~/.config ~/.config.backup
   ```

3. **安装配置**：
   - 手动复制配置文件到相应位置，例如：
     ```bash
     cp -r nvim/.config/nvim ~/.config/
     cp -r hyprland/.config/hypr ~/.config/
     # 依此类推
     ```
   - 或者使用符号链接：
     ```bash
     ln -s $(pwd)/nvim/.config/nvim ~/.config/nvim
     ```

4. **安装依赖**：
   - 确保安装了所有必需的软件包，如neovim, hyprland, alacritty, tmux, zsh等。
   - 对于Hyprland，需要Wayland支持的系统。

5. **重启会话**：
   - 重新登录或重启显示管理器以应用更改。

注意：这些配置是高度个性化的，可能需要根据您的系统进行调整。建议逐个测试配置以确保兼容性。
