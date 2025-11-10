---
title: ripgrep
---

以下为 `src/content/docs/00/ripgrep_BurntSushi.md` 的 Markdown 内容（已包含项目地址）：

```markdown
# ripgrep (rg)

**项目地址**  
[https://github.com/BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)

## 主要特性

| 特色 | 简介 |
|------|------|
| **极致速度** | 通过 Rust 编写，使用 `regex` crate，搜索耗时极低。 |
| **递归搜索** | 自动递归遍历目录，默认跳过 Git, SVN, Mercurial 的 `ignore` 文件。 |
| **正则表达式** | 支持 PCRE 风格的正则表达式；配合 `-e` 可多模式搜索。 |
| **忽略规则** | 自动读取 `.gitignore`、`.ignore`、`.rgignore`；可用 `-g` / `-G` 覆盖。 |
| **多文件类型** | 通过 `--type` 或自定义 `--type-add` 仅搜索特定文件类型。 |
| **并行处理** | 自动利用多核 CPU，提供 `-j` 或 `-p` 控制线程数。 |
| **二级索引** | 使用 `-i` / `-S` 在大文件（>2GB）中快速定位。 |
| **输出丰富** | 支持行号（`-n`）、全名（`-H`）、匹配行高亮（`--color`）。 |
| **集成复杂工具** | 可与 `fd`、`ag`、`grep` 结合使用。 |

## 基本用法

```bash
# 1. 单模式搜索
rg "foo"          # 搜索当前目录及子目录中的 "foo"

# 2. 递归搜索并显示行号
rg -n "hello"    # 匹配行号显示

# 3. 搜索指定文件类型
rg --type rust "todo"  # 仅在 *.rs 文件中搜索

# 4. 添加自定义文件类型
rg --type-add css:*.c*.css "color"  # 在 *.css/.scss 文件中搜索

# 5. 忽略部分路径
rg -g "!test/" "bar"  # 忽略 test/ 目录

# 6. 并行搜索
rg -j 4 "main"      # 使用 4 个线程

# 7. 高亮显示匹配
rg --color=always "fn main"  # 强制使用高亮

# 8. 输出完整路径
rg -H "print"     # 打印时包含完整文件路径

# 9. 搜索二进制文件
rg -a "pattern"   # 包括二进制内容

# 10. 查看帮助
rg --help
```

## 常用选项概览

| 选项 | 作用 |
|------|------|
| `-i, --ignore-case` | 忽略大小写 |
| `-w, --word-regexp` | 仅匹配完整单词 |
| `-x, --line-regexp` | 匹配整行 |
| `-v, --invert-match` | 反向匹配 |
| `-p, --search-path` | 指定搜索路径 |
| `-f, --file` | 从文件读取模式列表 |
| `-a, --text` | 处理二进制文件为文本 |
| `-I, --no-ignore` | 关闭忽略文件 |
| `-g, --glob` | 通过 glob 过滤文件 |
| `-G, --glob-quiet` | 关闭 glob 的忽略 |
| `-y, --encoding` | 指定文件编码 |
| `-o, --only-matching` | 仅输出匹配内容 |
| `-j, --threads` | 设置最大线程数 |
| `--stats` | 打印统计信息 |

---
> 适用于任何需要快速、准确文本搜索的项目，尤其在 Rust 开发、日志查阅、代码审查等场景中表现突出。  
```
