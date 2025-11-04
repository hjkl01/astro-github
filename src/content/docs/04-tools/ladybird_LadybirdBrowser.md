
---
title: ladybird
---


# Ladybird 浏览器

**项目地址**  
https://github.com/LadybirdBrowser/ladybird

---

## 项目概述
Ladybird 是一款用 Rust 编写的轻量级、跨平台 Web 浏览器，基于 WebKitGTK 作为渲染引擎。核心目标是提供简洁、安全的上网体验，具备内置广告拦截、隐私保护和极低的资源占用。

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **轻量与性能** | 对系统资源占用极低（内存 < 100 MB），启动速度快 |
| **隐私保护** | 默认启用隐私模式；禁用第三方 cookie、跟踪脚本，支持自定义隐私策略 |
| **广告拦截** | 内置广告拦截规则集（EasyList、EasyPrivacy），可手动配置或更新 |
| **跨平台** | 目前支持 Linux（GTK + WebKitGTK）；未来计划支持 Windows/macOS |
| **简洁 UI** | 单窗口多标签，地址栏、书签栏、历史记录、书签管理器 |
| **脚本与扩展** | 通过 JavaScript 库提供插件接口（实验性） |
| **下载管理** | 集成下载部件，支持暂停/恢复、选择保存路径 |
| **键盘快捷键** | 常用快捷键（Ctrl+T 新标签，Ctrl+W 关闭标签，Ctrl+L 聚焦地址栏等） |
| **可配置渲染像选项（如开启 WebGL、CSS3 等） |

---

## 功能亮点

1. **快速启动**：一次编译即可得到完整二进制，可直接放置于 `$PATH`，不需要额外脚本。  
2. **高安全性**：Rust 对内存安全性的保证，所有网络请求都通过 WebKit 沙盒机制。  
3. **可定制插件**：支持用户通过 `~/.config/ladybird/plugins/` 放置 JavaScript 脚本，自动加载。  
4. **统一配置**：全局设置文件 `~/.config/ladybird/config.ini`，支持主题、快捷键、隐私等级等。  
5. **编辑器模式**：在启用 `--edit` 模式下直接打开本地文件，适合开发者查看 HTML/CSS/JS。  

---

## 快速安装与使用

### 1. 安装

#### 从官方预编译包安装（Linux）
```bash
sudo apt install ladybird           # Debian/Ubuntu
sudo dnf install ladybird           # Fedora
```

#### 使用 Cargo 编译安装
```bash
# 安装 Rust 工具链（如果尚未安装）
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# 克隆仓库
git clone https://github.com/LadybirdBrowser/ladybird.git
cd ladybird

# 编译并安装
cargo install --path .
```

### 2. 运行

```bash
ladybird               # 启动默认窗口
ladybird https://example.com   # 直接打开指定 URL
```

### 3. 常用命令行选项

| 选项 | 说明 |
|------|------|
| `--url <URL>` | 直接打开指定网页 |
| `--incognito` | 隐私模式（无缓存/历史） |
| `--debug` | 启用调试模式（打印网络日志） |
| `--headless` | 无窗口模式，用于命令行抓取 |
| `--help` | 显示可用选项 |

### 4. 配置

- **配置文件路径**：`~/.config/ladybird/config.ini`  
- **主题切换**：编辑 `theme` 字段为 `light` / `dark` / 自定义 CSS 路径。  
- **快捷键自定义**：在 `keybindings.json` 中按键映射。

### 5. 开发与贡献

1. Fork 该仓库。  
2. 创建 feature branch（`feature/<name>`）并提交代码。  
3. 提交 PR 并遵循代码规范（`cargo fmt`、`cargo clippy`）。  

---

## 许可证

本项目采用 AGPL-3.0 许可证，源代码可在 GPL 条件下自由使用与修改。

---

> **备注**：本说明基于 README 及项目源码整理，版本信息请以最新 commit 为准。  
