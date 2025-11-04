
---
title: lf
---

**项目地址**：<https://github.com/gokcehan/lf>

**主要特性**  
- **Vim‑style 操作**：使用 `h/j/k/l`、`gg/G`、`w/b` 等快捷键浏览文件；支持多选、复制、粘贴、删除等操作。  
- **多面板视图**：可按 */、“`split`”键切换单/双/多面板，面板间使用 `ctrl‑h/j/k/l` 或 `tab/shift‑tab` 切换。  
- **异步文件处理**：复制、删除、重命名等操作在后台执行，主界面保持响应。  
- **可自定义键盘映射**：通过 `~/.config/lf/lfrc` 或环境变量 `LF_COMMAND`、`LF_APP` 等文件自定义绑定。  
- **总览与预览**：支持 `l` 预览选中文件内容，`p` 打开终端预览程序。  
- **搜索与过滤**：使用 `:` 进入命令行，下输入 `find <pattern>` 实时过滤文件。  
- **可脚本化**：`lf` 与 shell/程序（如 `ripgrep`、`fd`、`bat`）无缝结合，支持 `filter`、`preview`、`sort` 等脚本命令。  
- **跨平台**Windows、macOS、Linux）— 只需要安裝 Go 或预编译二进制文件。

**功能概览**  
| 功能 | 说明 |
|------|------|
| 浏览 | 利用目录结构查看与导航文件 |
| 操作 | 复制、剪切、粘贴、删除、快照、重命名 |
| 预览 | 预览文本/图片/多媒体内容 |
| 多面板 | 同时打开多个目录进行并行操作 |
| 过滤 | 快速定位文件、使用正则表达式过滤 |
| 单字/多字键 | 支持 Vim/Emacs 两种键盘模式 |
| 配置 | UI 配色、快捷键、默认程序等设定可自定义 |

**简易用法**  

1. **安装**  
   ```bash
   # 通过 Homebrew (macOS)
   brew install lf

   # 或直接下载预编译二进制
   wget https://github.com/gokcehan/lf/releases/latest/download/lf_<系统>_<arch>.tar.gz
   tar xzf *gz
   sudo mv lf /usr/local/bin/
   ```

2. **启动**  
   ```bash
   lf            # 进入当前目录
   lf /path/to/  # 指定启动目录
   ```

3. **常用命令**  
   - `h/j/k/l`：切换面板/移动光标
   - `gg` / `G`：跳到起始/末尾
   - `w` / `b`：跳到下/上单词
   - `:edit`：用默认编辑器打开文件
   - `:find hello`：搜索包含 “hello” 的文件
   - `:toggle hidden`：显示/隐藏隐藏文件
   - `x`：递归删除
   - `y`：复制文件/目录
   - `p`：粘贴
   - `d`：移动到剪贴板
   - `:` 后跟自定义外部命令，示例：`:shell ls -lah`

4. **自定义**  
   在 **~/.config/lf/lfrc** 中添加键绑定、过滤器或预览程序，例如：
   ```
   map h back-directory
   map l open
   filter ripgrep -l '' .  # 只列出匹配的文件
   preview bat --style=numbers
   ```

5. **插件 & 预设**  
   与外部插件（如: `fd`, `bat`, `fzf`）配合使用，快速调用下载文件或强大预览。

**总结**  
lf 是一款轻量、可高度自定义的终端文件管理器，结合 Vim 键盘习惯和异步执行特性，适合需要在终端快速浏览、管理文件并整合脚本的使用者。其完整的配置文件、键位映射与插件生态，让你可以根据个人工作流定制一套高效的文件管理体验。