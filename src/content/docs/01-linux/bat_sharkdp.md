---
title: bat
---

# bat

bat 是一个 cat(1) 克隆，具有语法高亮和 Git 集成，增强了命令行中查看代码和文本文件的体验。

## 功能

- 语法高亮：支持多种编程语言。
- Git 集成：显示 Git 状态。
- 行号：可选显示行号。
- 主题：支持多种颜色主题。

## 用法

1. 安装：使用包管理器如 apt install bat。
2. 运行：bat file.txt
3. 配置：编辑 ~/.config/bat/config

## 许可证

## bat 根据 Apache License, Version 2.0 或 MIT 许可证发布。

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
