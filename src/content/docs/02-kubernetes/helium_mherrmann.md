
---
title: helium
---

# Helium 项目

## 项目地址
[GitHub 项目地址](https://github.com/mherrmann/helium)

## 主要特性
Helium 是一个用于生成和管理 Kubernetes 部署的工具，主要特性包括：
- **自动化部署生成**：基于简单的 YAML 配置自动生成 Kubernetes 部署文件，支持容器镜像、环境变量和资源限制的配置。
- **多环境支持**：易于切换开发、生产等环境，通过配置文件管理差异化设置。
- **集成 CI/CD**：设计用于与 GitHub Actions 或其他 CI 工具集成，便于自动化构建和部署。
- **轻量级**：无需复杂依赖，使用 Python 脚本实现，易于安装和运行。
- **自定义扩展**：支持插件式扩展，允许用户添加自定义逻辑。

## 主要功能
- **生成 Kubernetes 资源**：从输入 YAML 文件生成 Deployment、Service、ConfigMap 等 Kubernetes 资源清单。
- **环境变量注入**：自动处理秘密和配置的注入，支持从文件或环境变量加载。
- **验证和测试**：内置验证功能，确保生成的 YAML 符合 Kubernetes 规范。
- **批量操作**：支持对多个应用或服务进行批量部署生成。

## 用法
1. **安装**：克隆仓库后，使用 `pip install -r requirements.txt` 安装依赖。
2. **配置**：在 `config/` 目录下创建 YAML 文件，定义应用规格，例如：
   ```yaml
   app:
     name: myapp
     image: nginx:latest
     replicas: 3
     env:
       - name: PORT
         value: "80"
   ```
3. **运行**：执行 `python helium.py generate -f config/myapp.yaml -o output/` 生成 Kubernetes 文件。
4. **部署**：使用 `kubectl apply -f output/` 应用生成的资源到 Kubernetes 集群。
5. **高级用法**：通过命令行选项如 `--env prod` 指定环境，或 `--dry-run` 预览生成结果而不实际输出文件。

更多细节请参考仓库的 README.md 文件。