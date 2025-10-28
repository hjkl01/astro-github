
---
title: vim-translator
---

# vim-translator 项目

**GitHub 项目地址**: [https://github.com/voldikss/vim-translator](https://github.com/voldikss/vim-translator)

## 主要特性
- **集成翻译引擎**：支持 Google Translate、Youdao、DeepL、Microsoft Translator 等多种翻译服务，提供准确的翻译结果。
- **多语言支持**：可翻译英文、中文、日文等常见语言，并支持自定义语言对。
- **Vim 友好界面**：无缝集成 Vim 编辑器，支持弹出窗口、浮动窗口或新标签页显示翻译结果。
- **批量翻译**：可翻译选中文本、单词、句子或整个文件内容。
- **离线模式**：部分引擎支持缓存或本地翻译，减少网络依赖。
- **自定义配置**：高度可配置，包括 API 密钥、翻译引擎优先级和输出格式。
- **扩展性**：支持命令行模式和脚本集成，适用于自动化任务。

## 主要功能
- **单词/短语翻译**：光标置于单词上，一键获取翻译、发音和解释。
- **选中文本翻译**：选中任意文本段落，进行即时翻译。
- **文件翻译**：翻译整个缓冲区或指定文件，支持输出到新缓冲区。
- **历史记录**：保存翻译历史，便于回顾和复用。
- **发音支持**：集成 TTS（文本到语音）功能，播放翻译结果的发音。
- **API 集成**：允许用户输入自定义 API 密钥以访问高级翻译服务。

## 用法
1. **安装**：
   - 使用 Vim 插件管理器（如 Vim-Plug）安装：
     ```
     Plug 'voldikss/vim-translator'
     ```
   - 运行 `:PlugInstall` 完成安装。

2. **配置**：
   - 在 `~/.vimrc` 或 `init.vim` 中添加基本配置：
     ```
     let g:translator_default_engines = ['google', 'haici']
     let g:translator_proxy = 'socks5://127.0.0.1:1086'  " 如需代理
     nmap <leader>t <Plug>Translate
     vmap <leader>t <Plug>TranslateV
     ```
   - 保存并重启 Vim，或运行 `:source %` 生效。

3. **基本命令**：
   - **翻译单词**：在 Normal 模式下，光标置于单词，按 `<leader>t`（默认映射）或运行 `:Translate`。
   - **翻译选中文本**：在 Visual 模式下选中文本，按 `<leader>t` 或运行 `:TranslateV`。
   - **翻译整个行**：运行 `:TranslateL` 或 `:1,10Translate`（指定行范围）。
   - **翻译文件**：运行 `:TranslateB`（当前缓冲区）或 `:w !translator`（通过管道）。
   - **查询历史**：运行 `:TranslatorHistory` 查看翻译记录。
   - **自定义**：使用 `:help translator` 查看完整命令和选项。

更多细节请参考项目 README。