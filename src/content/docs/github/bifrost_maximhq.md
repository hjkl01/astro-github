
---
title: bifrost
---


# Bifrost

**GitHub 地址**: <https://github.com/maximhq/bifrost>

---

## 项目概述

Bifrost 是一个基于命令行的自动化代码生成工具，旨在从 **OpenAPI**（Swagger）规范快速生成多语言 SDK、文档、Stub 和 Mock 代码。通过插件化架构、可定制模板以及易用的 CLI，Bifrost 能帮助前后端团队实现高效协同，缩短 API 对接周期。

---

## 主要特性

| 功能          | 说明 |
|---------------|------|
| **多语言 SDK 生成** | 支持 TypeScript、Python、Java、Go、Kotlin 等主流语言。可一次性生成多语言版本。 |
| **轻量级 CLI** | 一键执行 `bifrost generate` 等命令，自动完成 All-In-One 生成流程。 |
| **插件化架构** | 通过 `--plugin` 参数引入功能插件（如认证、日志、错误处理等），可自行扩展。 |
| **可定制模板** | 默认模板可直接使用，也可复制到项目根目录后按需修改，支持自定义模板仓库。 |
| **测试 Stub / Mock** | 自动生成符合 OpenAPI 规范的单元测试 Stub 与 Mock 代码，快速构建测试环境。 |
| **配置文件驱动** | 支持 `bifrost.yaml` 配置文件，统一管理生成参数。 |
| **强类型输出** | 生成的 SDK 代码均采用严格类型，使开发者在 IDE 中获得完整 IntelliSense。 |
| **文档与示例** | 同时生成 Markdown/HTML 文档和调用示例，方便快速查看与学习。 |

---

## 快速用法

> 先确保已安装 Python 3.8+，然后通过 `pip install bifrost` 安装。

```bash
# 安装（仅需一次）
pip install bifrost

# 在项目根目录下创建 bifrost.yaml (可选)
cat <<'YAML' > bifrost.yaml
spec: "./openapi.yaml"
output: "./gen"
languages:
  - python
  - ts
plugins:
  - auth
  - logging
YAML

# 生成 SDK、文档、Stub 等
bifrost generate

# 只生成 TypeScript SDK
bifrost generate --spec=./openapi.yaml --lang=ts --output=./sdk_ts

# 生成多语言 SDK，并启用插件
bifrost generate --spec=./openapi.yaml --lang=python --lang=go --plugin=auth --plugin=logging

# 查看帮助信息
bifrost -h
bifrost generate -h
```

---

## 配置文件示例 (`bifrost.yaml`)

```yaml
# openapi.yaml 为 API 规范文件
spec: "./api/openapi.yaml"

# 生成目录
output: "./"

# 需要生成的 SDK 语言列表
languages:
  - python
  - ts
  - go

# 需要加载的插件（直接使用插件名即可）
plugins:
  - auth   # 认证相关代码
  - logging  # 日志相关代码
```

---

## 典型工作流程

1. **准备**: 创建/更新 OpenAPI 规范文件（`.yaml` / `.json`）。  
2. **配置**: 在 `bifrost.yaml` 中指定规范路径、输出目录、语言、插件。  
3. **生成**: 运行 `bifrost generate`。  
4. **使用/发布**: 生成的 SDK 可直接在项目中 import/使用，或发布到内部仓库。  
5. **维护**: 规范变更后重新运行 `generate`，即可同步更新 SDK 与文档。

---

# 结语

Bifrost 通过把 API 结构化规范与代码生成功能统一化，为团队提供了一种统一、高效、可扩展的 API 开发与维护方案。无论是构建微服务、RESTful API 还是 GraphQL 代理，Bifrost 都能在几分钟内完成 SDK 与文档的完整生成，极大提高开发与测试效率。
