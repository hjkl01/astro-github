
---
title: packages
---


# Typst Packages 目录

> **仓库地址**: https://github.com/typst/packages

---

## 项目概述

`typst/packages` 是 Typst 官方维护的 **包管理与发布中心**，用于托管、展示、搜索以及安装 Typst 生态中的各种插件、模板与资源。  
该仓库统一管理了所有可发布的包，并提供了构建、发布和版本管理的一站式工具链。

---

## 主要特性

| 特性 | 描述 |
|------|------|
| **官方包仓库** | 所有官方认证包均托管在此，保证包的安全性和兼容性。 |
| **元数据统一** | 每个包通过 `manifest.typ`/`meta.toml` 定义名称、版本、依赖、描述等信息。 |
| **CI 自动化发布** | GitHub Actions 自动编译、打包及发布到 Typst 官方包索引。 |
| **依赖管理** | 自动解析并下载依赖，支持多版本冲突解决。 |
| **版本回退与更新** | 支持 `typst pkg upgrade`、`typst pkg rollback` 等命令。 |
| **文档生成** | 自动从源码提取文档并在 `docs/` 目录生成 Markdown/HTML。 |
| **搜索与过滤** | 通过 `search` API 快速定位所需包。 |

---

## 功能模块

1. **Package CLI**  
   - `typst pkg init <name>`：创建新包骨架。  
   - `typst pkg add <name@ver>`：添加依赖。  
   - `typst pkg remove <name>`：移除依赖。  
   - `typst pkg publish`：上传至官方仓库。  
   - `typst pkg install <name>`：本地安装。  
   - `typst pkg upgrade`：批量升级依赖。  

2. **Metadata 校验器**  
   - 检查 `manifest.typ`/`meta.toml` 的语法，确保符合规范。  

3. **Build & Test**  
   - `typst build`：构建项目为 PDF/HTML。  
   - `typst test`：运行单元/集成测试。  

4. **Documentation Generator**  
   - `typst docs`：从源码自动生成 API 文档与使用示例。  

5. **Package Index**  
   - `index.yaml`：全局包索引，用于搜索与依赖解析。  

---

## 用法示例

### 创建并发布一个新包

```bash
# 1. 创建骨架
typst pkg init my-awesome-lib

# 2. 添加依赖（可选）
typst pkg add typst-core@1.0.0

# 3. 编写源文件 & 生成文档
#    src/my-awesome-lib.typ
#    docs/index.md
typst build  # 生成 output

# 4. 让 GitHub Actions 触发发布（推送至主分支）
git push origin main
```

### 安装已发布的包

```bash
typst pkg install my-awesome-lib
```

### 更新依赖

```bash
typst pkg upgrade
```

### 查看包信息

```bash
typst pkg info my-awesome-lib
```

---

## 贡献

1. Fork 本仓库。  
2. 创建功能分支 (`feat/…` 或 `fix/…`)。  
3. 编写/更新 README、文档并提交 PR。  
4. PR 必须通过 CI 检测（`.typ` 合法、文档无误、版本号递增）。

---

## 许可证

MIT © Typst Tech. See [LICENSE](LICENSE) for details.
