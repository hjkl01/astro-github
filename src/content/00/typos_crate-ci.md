# typos

## 功能介绍

typos 是一个源代码拼写检查器，用于查找和纠正源代码中的拼写错误。它具有以下特点：

- **快速性能**：足够快以在大型代码库（monorepos）上运行
- **低假阳性**：可以安全地在 PR 上运行
- **多种集成**：支持 GitHub Actions、pre-commit 等
- **可配置**：支持自定义字典、忽略规则等

## 安装

### 下载预构建二进制文件

从 [GitHub Releases](https://github.com/crate-ci/typos/releases) 下载预构建的二进制文件。

### 使用 Rust 安装

```bash
cargo install typos-cli --locked
```

### 使用 Homebrew 安装

```bash
brew install typos-cli
```

### 使用 Conda 安装

```bash
conda install typos
```

### 使用 Pacman 安装

```bash
sudo pacman -S typos
```

## 基本用法

### 检查拼写错误

运行以下命令查看代码库中的拼写错误：

```bash
typos
```

### 自动修复拼写错误

运行以下命令自动修复发现的拼写错误：

```bash
typos --write-changes
# 或简写
typos -w
```

如果存在歧义（多个可能的修正），typos 会报告给用户而不自动修正。

## 配置

### 忽略误报

有时看似拼写错误的内容是故意的，如人名、缩写或本地化内容。可以通过 `_typos.toml` 文件配置忽略规则。

#### 忽略标识符

```toml
[default.extend-identifiers]
# 忽略特定标识符
AttributeIDSupressMenu = "AttributeIDSupressMenu"
```

#### 忽略单词

```toml
[default.extend-words]
# 不要修正姓氏 "Teh"
teh = "teh"
```

#### 排除文件

```toml
[files]
extend-exclude = ["localized/*.po"]
```

### 文件类型配置

对于某些文件类型，可以禁用内容检查但仍检查文件名：

```toml
[type.po]
extend-glob = ["*.po"]
check-file = false
```

运行 `typos --type-list` 查看支持的文件类型。

## 集成

### GitHub Actions

在 `.github/workflows/typos.yml` 中添加：

```yaml
name: Typos
on: [pull_request]

jobs:
  typos:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: crate-ci/typos@master
```

### pre-commit

在 `.pre-commit-config.yaml` 中添加：

```yaml
repos:
  - repo: https://github.com/crate-ci/typos
    rev: v1.39.0
    hooks:
      - id: typos
```

### 其他集成

- [🐊Putout Processor](https://github.com/putoutjs/putout-processor-typos)
- [Visual Studio Code](https://github.com/tekumara/typos-vscode)
- [typos-lsp](https://github.com/tekumara/typos-vscode)

## 高级用法

### 自定义集成

typos 提供构建块用于自定义集成：

- 从 stdin 读取，写入 stdout：`typos - --write-changes`
- 生成 diff：`typos dir/file --diff`
- JSON 输出：`typos dir/file --format json`

### 调试

查看有效配置：

```bash
typos --dump-config -
```

查看处理的文件：

```bash
typos --files
typos --identifiers
typos --words
```

启用调试日志：

```bash
typos -v
```

## 许可证

双重许可证：MIT 或 Apache 2.0
