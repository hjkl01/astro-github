
---
title: dynaconf
---

# Dynaconf 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/dynaconf/dynaconf)

## 主要特性
Dynaconf 是一个用于 Python 项目的配置管理库，旨在提供简单、灵活且强大的配置解决方案。其核心特性包括：

- **多格式支持**：支持 YAML、JSON、INI、TOML、Python 文件等多种配置格式，便于从不同来源加载配置。
- **环境变量集成**：无缝集成环境变量，支持将环境变量覆盖配置文件中的设置，实现动态配置调整。
- **分层配置**：支持多层级配置（如默认配置、生产配置、开发配置），允许根据环境（如 dev、prod）加载不同配置。
- **验证与类型检查**：内置配置验证功能，确保配置值的类型和范围正确，避免运行时错误。
- **懒加载**：配置按需加载，提高性能和内存效率。
- **加密支持**：可选的加密功能，用于保护敏感配置信息。
- **工作区支持**：支持多工作区（workspaces），适用于复杂项目中的模块化配置管理。
- **严格模式**：可选的严格模式，强制检查所有必需配置项的存在性。

Dynaconf 设计简洁，易于扩展，适用于小型脚本到大型企业级应用的各种场景。

## 主要功能
Dynaconf 的功能聚焦于简化配置管理，提供以下关键能力：

- **配置加载与访问**：通过 `Dynaconf` 类或 `settings` 对象轻松加载和访问配置，例如 `settings.USER_NAME`。
- **环境隔离**：使用 `settings = Dynaconf(envvar_prefix='MYAPP')` 指定前缀，支持不同环境的隔离配置。
- **默认值与覆盖**：自动处理默认值，并允许通过环境变量或命令行参数覆盖。
- **配置导出**：可以将配置导出为文件或字典，便于调试或迁移。
- **插件扩展**：支持自定义加载器和验证器，允许用户扩展功能。
- **Flask/Django 集成**：内置对流行 Web 框架的集成，简化 Web 应用中的配置管理。

这些功能使 Dynaconf 成为处理复杂配置场景的理想选择，尤其在微服务或多环境部署中。

## 用法示例
Dynaconf 的用法简单，以下是基本步骤和示例（假设已安装 `pip install dynaconf`）：

### 1. 基本安装与初始化
```python
from dynaconf import Dynaconf

# 初始化配置
settings = Dynaconf(
    envvar_prefix="MYAPP",  # 环境变量前缀
    settings_files=['settings.toml', 'settings.yaml'],  # 配置文件列表
    environments=True,  # 启用环境支持（如 .toml[dev]）
    load_dotenv=False,  # 是否加载 .env 文件
)
```

### 2. 配置文件的示例（settings.toml）
```toml
[default]
debug = true
database_url = "sqlite:///dev.db"

[production]
debug = false
database_url = "postgresql://user:pass@localhost/prod_db"
```

### 3. 访问配置
```python
# 访问默认配置
print(settings.debug)  # True

# 设置环境变量 MYAPP_ENV=production，然后访问
import os
os.environ['MYAPP_ENV'] = 'production'
print(settings.debug)  # False
print(settings.database_url)  # postgresql://user:pass@localhost/prod_db

# 覆盖配置
settings.debug = False  # 临时覆盖
```

### 4. 验证配置
```python
from dynaconf.validators import ValidationError

# 定义验证规则
settings.validators.register(
    'database_url', must_exist=True, is_type_of=str
)

# 加载时自动验证
try:
    settings.load()
except ValidationError as e:
    print(f"配置错误: {e}")
```

### 5. 高级用法：工作区
```python
# 为不同模块创建工作区
api_settings = settings.using('api')  # 加载 api/settings.toml
print(api_settings.api_key)
```

更多用法请参考官方文档：https://dynaconf.readthedocs.io/。Dynaconf 支持快速上手，并提供丰富的示例和最佳实践。