---
title: ast-grep
---

## 功能介绍

ast-grep 是一个基于抽象语法树（AST）的代码结构搜索、lint 和重写工具。它使用 Rust 编写，提供了一种直观的方式来搜索和修改代码结构，而非简单的文本匹配。

### 主要功能

- **代码结构搜索**：使用 AST 模式匹配代码，支持通配符（如 `$MATCH`）来匹配任意 AST 节点。
- **代码重写**：支持将匹配的代码结构重写为新的形式。
- **Linting**：可以编写 YAML 配置来定义代码规范规则。
- **多语言支持**：基于 tree-sitter，支持多种编程语言。
- **命令行界面**：提供直观的 CLI 工具，支持批量操作。

## 用法

### 安装

可以通过多种方式安装 ast-grep：

- npm: `npm install --global @ast-grep/cli`
- pip: `pip install ast-grep-cli`
- Homebrew: `brew install ast-grep`
- Cargo: `cargo install ast-grep --locked`

### 基本用法

ast-grep 的基本命令格式为：

```
ast-grep --pattern '模式代码' --rewrite '重写代码' --lang 语言
```

#### 示例

1. **搜索和重写变量声明**：

   ```
   ast-grep --pattern 'var code = $PATTERN' --rewrite 'let code = new $PATTERN' --lang ts
   ```

2. **重写空值合并操作符**：

   ```
   ast-grep -p '$A && $A()' -l ts -r '$A?.()'
   ```

3. **使用 YAML 配置 linting 规则**：
   可以创建 `.sgconfig.yml` 文件来定义规则，例如：
   ```yaml
   rule:
     pattern: 'console.log($$$)'
     message: '避免使用 console.log'
   ```

更多用法和示例请参考 [官方文档](https://ast-grep.github.io/)。
