
---
title: rig
---


# Rig

---

**项目地址**: [https://github.com/0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig)

## 简介

`rig` 是一款轻量级的多语言项目脚手架工具，专为 Rust（以及 Go、Python 等）项目快速生成完整骨架、管理依赖、自动生成 CI/CD 配置，并提供插件化扩展功能。

## 主要特性

- **一键生成项目骨架**  
  支持多语言模板（Rust、Go、Python 等），一条命令即可创建项目根目录、`Cargo.toml`/`pyproject.toml`、`src/`、`tests/`、`README.md` 等文件。

- **自动生成 CI/CD 工作流**  
  默认集成 GitHub Actions（可添加 GitLab CI、Travis CI），支持自定义平台、并行作业等。

- **模块化插件系统**  
  通过插件机制轻松扩展功能，例如自动发布、文档生成、代码质量检查等。

- **许可证和作者信息管理**  
  一键插入 MIT / Apache-2.0 / GPL 等 LICENSE，自动补全作者信息。

- **TUI/CLI 双模交互**  
  支持命令行参数（`--help`、`--verbose`）和终端用户界面。

- **可配置的 `.rig.yaml`**  
  通过 YAML 配置文件自定义生成细节，例如默认章节、依赖列表、CI 触发条件等。

## 功能与用法

### 安装

```bash
# 通过 Cargo 安装
cargo install rig

# 或直接克隆源码自行编译
git clone https://github.com/0xPlaygrounds/rig.git
cd rig
cargo build --release
sudo cp target/release/rig /usr/local/bin
```

### 初始化新项目

```bash
# 生成 Rust 项目 myapp
rig init myapp --lang rust

# 生成 Python 项目 myproject
rig init myproject --lang python
```

`rig init` 会在当前目录下生成类似以下结构：

```
myapp/
├── Cargo.toml
├── src/
│   └── lib.rs
├── tests/
├── README.md
├── LICENSE
├── .github/work   └── ci.yml
└── .rig.yaml
```

### 添加模块/子包

```bash
# 对 Rust 项目添加 utils 模块
rig add-module utils

# 对 Python 项目添加 core 子包
rig add-module core
```

### 生成/更新 CI/CD

```bash
# 根据 .rig.yaml 自动生成 GitHub Actions
rig ci

# 或自定义平台和作业数
rig ci --platform ubuntu-20.04 --jobs 4
```

### 打包与发布

```bash
# Rust 发布到 crates.io
rig publish

# Python 发布到 PyPI
rig publish
```

### 文档生成

```bash
# 生成 Markdown/HTML 文档
rig docs
```

## 贡献

欢迎 Issues 与 PR！更多细节请查看项目根目录下的 [CONTRIBUTING.md](https://github.com/0xPlaygrounds/rig/blob/main/CONTRIBUTING.md)。

---

**项目地址**: <https://github.com/0xPlaygrounds/rig>
```

*文件路径: `src/content/docs/00/rig_0xPlaygrounds.md`*