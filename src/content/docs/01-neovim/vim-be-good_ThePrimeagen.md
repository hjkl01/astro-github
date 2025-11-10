---
title: vim-be-good
---

# vim-be-good

## 项目简介

vim-be-good 是一个专为 Neovim 设计的插件，旨在通过游戏的方式帮助用户提高 Vim 移动操作的熟练度。它提供了一系列有趣的游戏，让你在实践中掌握基本的 Vim 命令和移动技巧。

## 主要功能

- **游戏化学习**：将 Vim 移动练习转化为游戏形式，使学习过程更加有趣和互动。
- **多种游戏模式**：
  - `relative`：使用相对跳转删除指定行。
  - `ci{`：替换花括号或方括号内的内容。
  - `whackamole`：快速导航到指定字符并切换大小写。
- **难度调整**：支持不同难度级别，帮助用户逐步提升技能。
- **实时反馈**：游戏过程中提供即时反馈，帮助用户了解自己的表现。

## 安装方法

### 使用插件管理器

对于 Neovim 用户，可以使用如 vim-plug 等插件管理器安装：

```vim
Plug 'ThePrimeagen/vim-be-good'
```

### 使用 Docker

项目提供 Docker 镜像，支持稳定版和最新版：

- 稳定版：`docker run -it --rm brandoncc/vim-be-good:stable`
- 最新版：`docker run -it --rm brandoncc/vim-be-good:latest`

## 使用方法

1. 确保你在 Neovim 的空文件中（非空文件会报错）。
2. 运行 `:VimBeGood` 命令查看可用游戏列表。
3. 选择一个游戏开始练习，例如 `:VimBeGood relative`。
4. 根据游戏提示完成任务，提高你的 Vim 移动技能。

## 注意事项

- 仅支持 Neovim 5.x 及以上版本。
- 代码基于直播开发，结构可能不完美，但功能完整。
- 如果有新游戏想法，欢迎提交 Issue 或 PR。

## 贡献

欢迎贡献代码！请 Fork 项目，创建功能分支，进行修改后提交 PR。

## 相关链接

- [GitHub 仓库](https://github.com/ThePrimeagen/vim-be-good)
- [作者 Twitch 频道](https://twitch.tv/ThePrimeagen)
