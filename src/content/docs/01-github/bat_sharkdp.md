
---
title: bat
---


# bat（sharkdp/bat）

项目地址: <https://github.com/sharkdp/bat>

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **高亮语法** | 支持 200+ 语言的语法高亮，使用 `tree-sitter` 解析器，兼容 `ls` 的颜色化输出。 |
| **行号** | 可显示绝对行号、相对行号或两者混合，支持自定义样式。 |
| **目录树** | `bat -p` 或 `bat -l` 可递归显示目录结构，类似 `tree`。 |
| **分页** | 与 `less` 集成，支持 `--paging=never`、`always`、`auto` 等模式。 |
| **自定义主题** | 通过 `~/.config/bat/themes` 添加/修改颜色主题，支持 `.bat` 配置文件。 |
| **文件比较** | `bat --diff file1 file2` 比较两文件差异，带颜色高亮。 |
| **多文件合并** | `bat file*` 统一显示多文件内容，自动分隔。 |
| **文本搜索** | 支持正则表达式搜索，配合 `--highlight-line` 高亮匹配行。 |
| **可配置性** | 通过 `~/.config/bat/config` 或环境变量 `BAT_*` 全面自定义行为。 |

---

## 安装

```bash
# 通过 Cargo
cargo install bat

# 或使用包管理器
# Ubuntu/Debian
sudo apt install bat

# macOS (Homebrew)
brew install bat

# Arch Linux
pacman -S bat
```

---

## 用法示例

```bash
# 基本使用
bat file.rs

# 显示行号
bat --line-range :200 file.rs

# 高亮搜索关键字
bat -p -l rust file.rs | bat -p -l rust --highlight-search 'fn'

# 目录树
bat -p src/

# 比较文件
bat --diff old.txt new.txt

# 通过配置文件自定义主题
echo -e "[bat]\ntheme = \"Monokai\"\ntheme_overrides = \"~/.config/bat/themes/custom.theme\"" > ~/.config/bat/config
```

---

## 配置示例（`~/.config/bat/config`）

```toml
# 颜色主题
theme = "Nord"

# 行号显示
line-number = true
line-range = ":"

# 自动分页
paging = "auto"

# 其他
style = "plain"  # 或 "grid"、"side-by-side"
```

---

## 参考

- 官方文档: <https://github.com/sharkdp/bat>  
- 主题库: <https://github.com/sharkdp/bat/tree/master/themes>  
- 配置文件示例: <https://github.com/sharkdp/bat/blob/master/README.md>
