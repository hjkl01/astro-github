
---
title: dynaconf
---

# Dynaconf 项目

**GitHub 项目地址:** [https://github.com/rochacbruno/dynaconf](https://github.com/rochacbruno/dynaconf)

## 主要特性
Dynaconf 是一个 Python 配置管理库，旨在提供灵活、可靠的配置解决方案。它支持多种配置来源，包括 YAML、TOML、JSON、INI 和环境变量等格式。主要特性包括：
- **多格式支持**：无缝处理 YAML、JSON、TOML、INI 等配置文件，以及环境变量和 Python 对象。
- **分层配置**：支持多环境配置（如开发、生产、测试），通过命名空间管理不同场景。
- **动态加载**：配置可以实时更新，无需重启应用，支持热重载。
- **验证与默认值**：内置配置验证机制，并提供默认值fallback，确保配置的完整性。
- **安全性**：支持加密敏感配置（如密码、密钥），并防止配置泄露。
- **易用性**：简单 API 接口，兼容 Django、Flask 等框架，减少 boilerplate 代码。

## 主要功能
- **配置读取与写入**：从文件或环境变量加载配置，支持嵌套结构和列表。
- **环境管理**：通过 `settings.ENV_FOR_DYNACONF` 变量切换环境，实现配置隔离。
- **全局设置**：使用 `Dynaconf` 类创建全局配置实例，支持单例模式。
- **插件扩展**：可集成 Redis、Vault 等外部存储，实现分布式配置。
- **类型转换**：自动将配置值转换为所需类型（如字符串转整数），并处理缺失值。

## 用法示例
### 安装
```bash
pip install dynaconf
```

### 基本用法
1. **创建配置文件**（例如 `settings.yaml`）：
   ```yaml
   default:
     name: "My App"
     debug: true
     database:
       host: "localhost"
       port: 5432
   production:
     debug: false
     database:
       host: "prod-db.example.com"
   ```

2. **在 Python 代码中使用**：
   ```python
   from dynaconf import Dynaconf

   # 初始化配置
   settings = Dynaconf(
       envvar_prefix="MYAPP",  # 环境变量前缀
       settings_files=['settings.yaml'],  # 配置文件路径
   )

   # 访问配置
   print(settings.name)  # 输出: My App
   print(settings.debug)  # 输出: true (根据环境)
   print(settings.database.host)  # 输出: localhost 或 prod-db.example.com

   # 设置环境
   import os
   os.environ['ENV_FOR_DYNACONF'] = 'production'
   settings = Dynaconf(...)  # 重新加载生产环境配置
   ```

3. **使用环境变量**：
   ```bash
   export MYAPP_DATABASE__HOST=remote-host
   export MYAPP_DEBUG=false
   ```
   配置会优先从环境变量加载，覆盖文件配置。

更多高级用法请参考官方文档。