---
title: gitlogue
---

## gitlogue

gitlogue 是一个终端工具，用于将 Git 提交历史转换为生动的动画回放。它模拟真实的代码编辑过程，包括打字动画、光标移动、删除操作和文件树变化，将代码变更转化为视觉体验。主要用于屏幕保护、演示、教育和内容创作。

### 主要特性

- **提交动画回放**：模拟真实打字、删除和文件操作，支持语法高亮（支持 29 种语言，如 Bash、C、Go、Python、Rust 等）。
- **项目文件树**：显示目录结构及变更统计。
- **屏幕保护模式**：无限循环随机提交播放。
- **主题支持**：内置 9 种主题，支持完全自定义。
- **性能优化**：基于 Rust 构建，轻量且快速。
- **过滤和自定义**：按作者、日期、提交范围过滤，支持忽略文件模式和速度调整。

### 安装步骤

推荐使用安装脚本：

```bash
curl -fsSL https://raw.githubusercontent.com/unhappychoice/gitlogue/main/install.sh | bash
```

其他方式：

- Homebrew：`brew install gitlogue`
- Cargo：`cargo install gitlogue`
- Arch Linux：`pacman -S gitlogue`
- Nix：`nix run github:unhappychoice/gitlogue`（或安装到配置文件）
- 从源码：克隆仓库后运行 `cargo install --path .`

更多选项见 [安装指南](docs/installation.md)。

### 基本用法

- **启动屏幕保护**：`gitlogue`
- **查看特定提交**：`gitlogue --commit abc123`
- **回放提交范围**：`gitlogue --commit HEAD~5..HEAD`
- **按时间顺序回放**：`gitlogue --order asc`
- **循环播放**：`gitlogue --commit abc123 --loop`
- **按作者过滤**：`gitlogue --author "john"`
- **按日期过滤**：`gitlogue --after "2024-01-01" --before "1 week ago"`
- **更改主题**：`gitlogue --theme dracula`
- **调整打字速度**：`gitlogue --speed 20`（毫秒/字符）
- **忽略文件**：`gitlogue --ignore "*.ipynb"`
- **主题管理**：`gitlogue theme list`（列出主题）、`gitlogue theme set dracula`（设置默认主题）

配置通过 `~/.config/gitlogue/config.toml` 文件，支持默认主题、速度和背景设置。详情见 [配置指南](docs/configuration.md)。

### 其他注意事项

- **警告**：非传统屏幕保护器，无电源管理功能；OLED 显示器长时间使用可能导致烧屏。
- **相关项目**：类似 GitType（打字游戏）、tarts（终端屏幕保护集合）等。
- **许可证**：ISC License。
- **贡献**：欢迎贡献，见 [贡献指南](docs/CONTRIBUTING.md)。
