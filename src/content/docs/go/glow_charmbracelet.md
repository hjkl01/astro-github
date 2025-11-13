---
title: glow
---

# Charmbracelet Glow

> 项目地址: https://github.com/charmbracelet/glow

## 简介

Charmbracelet Glow 是一个轻量级的命令行 Markdown 渲染器，直接在终端中将 Markdown 文档渲染为美观的彩色输出，兼容多种终端环境。

## 主要特性

- **轻量 & 纯 Go**：不依赖外部二进制，可直接交叉编译发布。
- **终端主题**：支持多种终端主题（如 `light`, `dark`, `dracula` 等），可自定义样式。
- **高亮代码**：内置多语言高亮支持。
- **表格与图像**：渲染 Markdown 表格及支持图片占位符。
- **目录与跳转**：支持 `table of contents` 与页面跳转。
- **自动缩进与格式化**：自带高级 Markdown 语法解析。
- **TUI 模式**：无参数运行进入文本用户界面，浏览本地 Markdown 文件。
- **CLI 支持**：渲染文件、标准输入、从 GitHub/GitLab 仓库获取 README、HTTP URL。
- **字词换行**：支持最大宽度设置。
- **分页**：使用分页器显示输出。
- **配置文件**：支持 YAML 配置，设置默认选项。

## 功能

| 功能                          | 说明                           |
| ----------------------------- | ------------------------------ |
| `glow file.md`                | 渲染单个 Markdown 文件         |
| `glow -theme dracula file.md` | 指定终端主题                   |
| `glow --linkify`              | 自动将 URL 变成可点击链接      |
| `glow --max-width 80`         | 限制输出宽度                   |
| `glow -o out.txt file.md`     | 将渲染结果输出到文件           |
| `glow -D`                     | 启用调试模式，展示内部解析过程 |
| `glow -V`                     | 查看版本信息                   |

## 安装

### 包管理器

```bash
# macOS 或 Linux
brew install glow

# macOS (MacPorts)
sudo port install glow

# Arch Linux
pacman -S glow

# Nix shell
nix-shell -p glow --command glow

# FreeBSD
pkg install glow

# Solus
eopkg install glow

# Windows (Chocolatey, Scoop, Winget)
choco install glow
scoop install glow
winget install charmbracelet.glow

# Android (termux)
pkg install glow

# Ubuntu (Snapcraft)
sudo snap install glow

# Debian/Ubuntu
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install glow

# Fedora/RHEL
echo '[charm]
name=Charm
baseurl=https://repo.charm.sh/yum/
enabled=1
gpgcheck=1
gpgkey=https://repo.charm.sh/yum/gpg.key' | sudo tee /etc/yum.repos.d/charm.repo
sudo yum install glow
```

### Go

```bash
go install github.com/charmbracelet/glow/v2@latest
```

### 构建 (需要 Go 1.21+)

```bash
git clone https://github.com/charmbracelet/glow.git
cd glow
go build
```

## 使用

### TUI 模式

```bash
glow  # 无参数运行，启动文本用户界面浏览本地 Markdown 文件
```

### CLI 模式

```bash
# 渲染文件
glow README.md

# 从标准输入渲染
echo "# Hello" | glow -

# 从 GitHub/GitLab 获取
glow github.com/charmbracelet/glow

# 从 HTTP 获取
glow https://example.com/file.md

# 字词换行
glow -w 60 README.md

# 分页显示
glow -p README.md

# 指定主题
glow -s dark README.md

# 输出到文件
glow -o rendered.txt README.md
```

## 配置文件

运行 `glow config` 打开配置文件（使用 $EDITOR）。或手动创建 `glow.yml`。

示例配置：

```yaml
# 样式名称或 JSON 路径 (默认 "auto")
style: 'light'
# 鼠标滚轮支持 (TUI 模式)
mouse: true
# 使用分页器显示 Markdown
pager: true
# 字词换行列数
width: 80
# 显示所有文件，包括隐藏和忽略的文件
all: false
# 显示行号 (TUI 模式)
showLineNumbers: false
# 保留输出中的换行符
preserveNewLines: false
```

## 进一步使用

- 支持管道：`cat file.md | glow`
- 生成标题目录：`glow -t` 生成只含 Markdown 标题的目录
- 调试模式：`glow -D` 显示内部解析过程
- 查看版本：`glow -V`

---
> 更多信息请参见官方文档或 GitHub 仓库。
