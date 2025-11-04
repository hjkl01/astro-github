
---
title: registry
---


# Model Context Protocol (MCP) Registry

> **项目地址**：<https://github.com/modelcontextprotocol/registry>

## 1. 项目概述  
MCP Registry 是 Model Context Protocol 的核心组件，用来统一管理模型上下文（metadata、版本、依赖、运行时信息等）。它为多模态 AI 生态系统提供了可插拔的、可版本化的上下文存储与检索机制，支持在不同平台（本地、本地网络、云）间共享与复现模型上下文。

---

## 2. 特性

| 特性 | 说明 |
|------|------|
| **可插拔存储** | 支持本地文件系统、SQLite、Redis、以及自定义存储槽（通过插件或实现接口） |
| **版本控制** | 每个上下文都有自动生成的 UUID 与可选版本号；更改后可保留历史记录 |
| **兼容性检查** | 在注册或查询时自动比对协议版本、必需字段与类型，确保上下文符合 MCP 规范 |
| **元数据查询** | 提供高效的 *lookup*、*list*、*search* 接口，支持标签、通配符、范围查询 |
| **CLI 工具** | `mcp-registry` 命令行可完成注册、更新、删除、导出/导入 |
| **安全与权限** | 通过可选的认证插件支持基于角色/权限的访问控制 |
| **可扩展** | 通过 Python `EntryPoint` 机制可自由扩展字段类型、序列化器、验证器 |

---

## 3. 主要接口与使用方式

### 3.1 安装

```bash
pip install mcp-registry  # 或直接从源码安装
```

### 3.2 Python API

```python
from mcp_registry import Registry, Context, ContextVersion

# 初始化（使用默认存储：文件系统）
registry = Registry()

# 创建一个上下文
context = Context(
    name="text-generator",
    description="Large language model for text generation",
    version=ContextVersion(major=1, minor=0, patch=0),
    metadata={
        "framework": "PyTorch",
        "parameters": 125_000_000,
        "license": "Apache-2.0",
        "tags": ["language-model", "text"]
    }
)

# 注册上下文
entry_id = registry.register(context)
print("已注册，id:", entry_id)

# 查询
retrieved = registry.get(entry_id)
print("检索到:", retrieved.name, retrieved.version)

# 列表
for ctx in registry.list():
    print(f"{ctx.id} - {ctx.name} ({ctx.version})")

# 删除
registry.remove(entry_id)

# 导出为 JSON
registry.export_to_file("registry.json")

# 从文件导入
registry.import_from_file("registry.json")
```

### 3.3 CLI 工具

```bash
# 查看帮助
mcp-registry --help

# 注册上下文
mcp-registry register --name "image-classifier" \
    --framework "TensorFlow" \
    --parameters 65e6 \
    --version "0.2" \
    --tags "vision,classifier"

# 查询
mcp-registry get <context-id>

# 列表
mcp-registry list --tag vision

# 删除
mcp-registry delete <context-id>

# 导出
mcp-registry export registry.json

# 导入
mcp-registry import registry.json
```

---

## 4. 插件与自定义

- **自定义存储**：实现 `mcp_registry.storage.StorageInterface` 并在 `setup.py` 中注册即可。
- **自定义字段类型**：通过 `mcp_registry.field.FieldFactory` 注册新字段，支持 JSON / Protobuf 序列化。
- **安全插件**：实现 `mcp_registry.auth.AuthProvider`，可对注册/查询请求进行鉴权。

---

## 5. 进阶使用

> **版本升级与迁移**  
> 当升级 MCP 协议版本时，使用 `registry.upgrade()` 自动迁移旧版上下文，保持兼容。  

> **批量导入**  
> `mcp-registry import-batch /path/to/metadatas.json` 支持一次性导入多条上下文记录。  

> **审计日志**  
> 通过 `registry.get_log()` 可查看所有操作执行历史，支持时间过滤与操作类型查询。

---

## 6. 常见问题

| 问题 | 解答 |
|------|------|
| 寻找旧版本上下文 | `registry.get("<id>", version="1.0")` 或通过 `registry.search(version="<1.1")` |
| 多租户场景 | 通过插件实现 `AuthProvider` 并在 `Registry` 初始化时传入 `user="namespace1"` |
| 兼容多语言客户端 | 管理器提供可序列化的 JSON/YAML 端点，可通过 HTTP API 或 gRPC 访问 |

---

## 7. 贡献

1. Fork 本仓库  
2. 使用 `tox` 进行测试  
3. 提交 PR 并注明已完成的功能模块  

---

> **项目地址**：<https://github.com/modelcontextprotocol/registry>
