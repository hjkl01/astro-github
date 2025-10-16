
---
title: term.everything
---

# Term Everything 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/mmulet/term.everything/blob/main/resources/HowIDidIt.md)

## 主要特性
Term Everything 是一个基于终端的快速文件搜索工具，灵感来源于 Windows 的 Everything 软件。它利用高效的索引机制，在 Linux/macOS 等 Unix-like 系统上实现亚秒级文件搜索。主要特性包括：
- **实时索引**：自动监控文件系统变化，保持文件索引更新，支持 NTFS 文件系统（通过 fuse 挂载）。
- **模糊搜索**：支持模糊匹配、路径过滤和大小写不敏感搜索，快速定位文件或目录。
- **轻量高效**：使用 Rust 语言开发，资源占用低，搜索速度极快（通常 <100ms）。
- **跨平台支持**：主要针对 Linux，但可扩展到其他系统；集成终端命令行界面（CLI）。
- **自定义过滤**：允许排除特定目录或文件类型，优化搜索范围。

## 主要功能
- **文件搜索**：通过命令行输入关键词，列出匹配的文件路径、名称和元数据（如大小、修改时间）。
- **路径导航**：支持直接打开搜索结果的文件或目录，使用系统默认编辑器或文件管理器。
- **索引管理**：手动或自动构建/更新文件索引，支持增量更新以处理大文件系统。
- **高级查询**：结合正则表达式、AND/OR 操作符进行复杂搜索；输出格式可自定义（JSON、表格等）。
- **监控与通知**：后台守护进程监控文件变化，实时同步索引。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/mmulet/term.everything.git`
   - 安装依赖：使用 Cargo（Rust 包管理器）运行 `cargo build --release`。
   - 对于 NTFS 支持，确保安装 `ntfs-3g` 并挂载驱动器。

2. **初始化索引**：
   - 首次运行：`term_everything index /path/to/search/root`（指定搜索根目录，如 `/` 或 `/home`）。
   - 自动模式：配置后台服务以定期更新索引。

3. **搜索文件**：
   - 基本搜索：`term_everything search "keyword"`（例如，`term_everything search "report.pdf"`）。
   - 高级搜索：`term_everything search "keyword" --path "/docs" --regex --case-insensitive`。
   - 输出结果：默认显示路径列表；使用 `--open` 直接打开文件。

4. **管理与配置**：
   - 更新索引：`term_everything update`。
   - 配置排除规则：在 `~/.config/term_everything/config.toml` 中编辑过滤器，如排除 `.git` 目录。
   - 帮助：运行 `term_everything --help` 查看完整选项。

该工具适合开发者或系统管理员，用于高效管理大量文件。更多细节请参考项目仓库的 HowIDidIt.md 文件。