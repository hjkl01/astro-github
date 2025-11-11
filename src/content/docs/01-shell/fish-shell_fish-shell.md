---
title: fish-shell
---

# fish-shell

fish (friendly interactive shell) 是一个智能且用户友好的命令行 shell，适用于 macOS、Linux 和其他 Unix-like 系统。它提供了语法高亮、自动建议、强大的 tab 补全等功能，无需额外配置即可使用。

## 主要功能

- **语法高亮**：实时高亮显示命令语法，帮助用户快速识别错误。
- **自动建议**：根据历史命令和上下文提供智能建议，按右箭头键接受。
- **Tab 补全**：支持文件、命令、变量等的智能补全，包括子命令和选项。
- **脚本友好**：支持现代脚本特性，如数组、函数和条件语句。
- **可配置**：通过 `fish_config` 工具提供 Web 界面进行配置。
- **跨平台**：支持多种操作系统和包管理器安装。

## 安装方法

### macOS

- 使用 Homebrew：`brew install fish`
- 使用 MacPorts：`sudo port install fish`
- 从官网下载安装包：[fishshell.com](https://fishshell.com/)

### Linux

- Ubuntu/Debian：添加 PPA 并安装
  ```
  sudo apt-add-repository ppa:fish-shell/release-4
  sudo apt update
  sudo apt install fish
  ```
- 其他发行版：从 openSUSE Build Service 下载包，或从源码构建。

### Windows

- 通过 WSL 安装（使用 Linux 包）。
- 使用 Cygwin 或 MSYS2。

### 从源码构建

需要 Rust 1.85+、CMake 3.15+ 等依赖。

```
mkdir build; cd build
cmake ..
cmake --build .
sudo cmake --install .
```

## 使用方法

1. 安装后，在终端运行 `fish` 启动 shell。
2. 查看帮助：运行 `help` 或访问 [fishshell.com/docs](https://fishshell.com/docs/current/)。
3. 基本用法类似 bash/zsh，但有一些差异，如变量赋值无需 `$`，使用 `set` 命令。
4. 配置：运行 `fish_config` 打开 Web 配置界面。
5. 脚本编写：fish 脚本以 `.fish` 为扩展名，支持函数定义等。

## 示例

- 设置变量：`set myvar hello`
- 定义函数：
  ```
  function greet
      echo "Hello, $argv[1]!"
  end
  ```
- 运行函数：`greet world`

更多详细信息请参考官方文档：[fishshell.com](https://fishshell.com/)
