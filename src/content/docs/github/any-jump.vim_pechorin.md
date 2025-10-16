
---
title: any-jump.vim
---

# any-jump.vim 项目

**GitHub 项目地址:** [https://github.com/pechorin/any-jump.vim](https://github.com/pechorin/any-jump.vim)

## 主要特性
any-jump.vim 是一个 Vim 插件，提供快速跳转和搜索代码符号的功能，支持多种语言和项目类型。主要特性包括：
- **多语言支持**：兼容 JavaScript、Python、Go、Rust、Java、C/C++ 等常见编程语言。
- **多种搜索后端**：支持 ripgrep、ag（The Silver Searcher）、pt（The Platinum Searcher）、grep 等工具，自动选择最优后端。
- **智能过滤**：自动过滤二进制文件、节点模块等无关目录，提高搜索效率。
- **双向跳转**：支持跳转到定义或引用，并可轻松返回原位置。
- **异步搜索**：使用异步方式进行搜索，避免阻塞 Vim 编辑器。
- **自定义配置**：允许用户自定义搜索命令、忽略模式和快捷键。

## 主要功能
- **符号搜索与跳转**：在项目中搜索光标下的符号（如函数、变量），并跳转到其定义或使用位置。
- **全局搜索**：支持在整个项目或指定目录中搜索文本。
- **列表预览**：搜索结果以快速列表形式显示，支持预览和选择跳转。
- **返回功能**：使用快捷键返回上一个跳转位置。
- **集成 LSP**：可选与 Language Server Protocol 集成，提供更精确的跳转（需额外配置）。

## 用法
1. **安装**：
   - 使用 Vim 插件管理器如 vim-plug：在 `~/.vimrc` 中添加：
     ```
     Plug 'pechorin/any-jump.vim'
     ```
     然后运行 `:PlugInstall`。
   - 或手动克隆仓库到 `~/.vim/pack/plugins/start/` 目录。

2. **基本配置**：
   - 在 `~/.vimrc` 中添加默认配置（可选）：
     ```
     let g:any_jump_window_width_ratio = 0.8  " 窗口宽度比例
     let g:any_jump_window_height_ratio = 0.6 " 窗口高度比例
     let g:any_jump_shorten_length = 1        " 缩短路径显示
     ```

3. **常用命令**：
   - `:AnyJump`：在当前光标符号上搜索并跳转（默认映射 `<Leader>aj`）。
   - `:AnyJump!`：打开搜索结果列表，选择后跳转。
   - `:AnyJumpLastReturn`：返回上一个跳转位置（默认映射 `<Leader>al`）。
   - `:AnyJumpAll`：在所有缓冲区中搜索当前符号。
   - `:AnyJumpCurrentFile`：仅在当前文件中搜索。
   - 自定义快捷键示例：在 `~/.vimrc` 中：
     ```
     nnoremap <leader>j :AnyJump<CR>
     nnoremap <leader>l :AnyJumpLastReturn<CR>
     ```

4. **使用步骤**：
   - 打开 Vim 编辑器，定位到要搜索的符号。
   - 输入 `:AnyJump` 或使用快捷键。
   - 如果结果多，会弹出列表窗口，选择目标行按 Enter 跳转。
   - 跳转后，使用 `:AnyJumpLastReturn` 返回原位置。

更多细节请参考项目 README。