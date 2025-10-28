
---
title: yaak
---


# yaak (Mountain‑Loop)

- **项目地址**: <https://github.com/mountain-loop/yaak>

---

## 项目简介
`yaak` 是一款 **轻量级命令行工具**，用于快速生成、管理和执行多语言脚本与项目模板。它的主要目标是提升跨平台开发效率，简单易用且高度可定制。

---

## 主要特性  

| 特性 | 描述 |
|------|------|
| **多语言支持** | 自动识别并执行 `.py`, `.js`, `.ts`, `.go`, `.rs` 等多种脚本。 |
| **模板管理** | 支持自定义项目模板，模板文件以 `yaml` 或 `json` 形式描述，`yaak init` 可以基于模板快速生成项目骨架。 |
| **执行日志** | 自动记录执行日志，支持 `--verbose` 打印详细信息；日志可输出到文件或标准输出。 |
| **插件机制** | 支持自定义插件，插件可在执行前后插入钩子，实现任务自动化。 |
| **跨平台** | 兼容 Windows、macOS、Linux，依赖 Python3，极小化环境配置。 |
| **CLI 友好** | 提供完整的 `--help` 文档，支持 `--config` 指定全局配置文件。 |
| **安全沙盒** | 对外部脚本执行使用 `subprocess.run` 时限制 `cwd` 与 `env`，降低恶意执行风险。 |

---

## 功能概览  

1. **初始化项目**  
   ```bash
   yaak init <template-name> [project-name]
   ```
   根据指定模板创建新项目，自动创建目录结构、基础文件与依赖描述文件。

2. **脚本执行**  
   ```bash
   yaak run <script-path> [--args ...]
   ```
   自动识别脚本语言并执行，支持传递自定义参数。

3. **批量执行**  
   ```bash
   yaak batch <script-dir> [--filter pattern]
   ```
   扫描目录下符合条件的脚本并按顺序执行，适合批处理任务。

4. **插件管理**  
   ```bash
   yaak plugin list
   yaak plugin install <name>
   yaak plugin remove <name>
   ```
   查看、安装、移除插件，插件位于 `~/.yaak/plugins/` 目录下。

5. **配置管理**  
   ```bash
   yaak config [--set key=value] [--get key]
   ```
   读写全局配置文件 `~/.yaak/config.yaml`。

6. **日志与调试**  
   ```bash
   yaak log [--tail] [--since datetime]
   ```
   查看最近日志，可持续跟踪实时输出。

---

## 使用示例  

```bash
# 1. 通过模板创建新项目
yaak init python-web my-sample-app

# 2. 进入项目目录
cd my-sample-app

# 3. 安装依赖（示例：pip, npm 等）
yaak run install.sh

# 4. 运行项目
yaak run run.py

# 5. 批量执行所有测试脚本
yaak batch tests --filter "test_*.py"

# 6. 安装自定义插件
yaak plugin install my-custom-plugin

# 7. 查看日志
yaak log --tail
```

---

## 贡献与文档  
- **源码**: <https://github.com/mountain-loop/yaak>
- **Issue**: <https://github.com/mountain-loop/yaak/issues>
- **Wiki**: 详细文档请见仓库 Wiki 页面。

> 以上内容为 `yaak` 项目的核心特性、功能与基本使用方法，协助快速上手与集成。