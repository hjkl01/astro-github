
---
title: gae-init
---

# gae-init 项目

## 项目地址
[https://github.com/gae-init/gae-init](https://github.com/gae-init/gae-init)

## 主要特性
gae-init 是一个用于 Google App Engine (GAE) 的 Python 应用初始化和脚手架工具。它旨在简化 GAE 项目的设置和开发流程，提供模块化的结构和自动化配置。主要特性包括：
- **模块化架构**：支持易于扩展的模块系统，允许开发者添加自定义模块如认证、表单处理等。
- **内置工具集**：集成 Webapp2 框架、Jinja2 模板引擎、Bootstrap 前端框架，以及其他常用库如 WTForms 和 Tipfy。
- **多环境支持**：内置开发、测试和生产环境的配置管理，支持本地开发服务器和 GAE 部署。
- **CLI 工具**：提供命令行界面，用于快速生成项目、安装依赖和运行应用。
- **安全性与最佳实践**：预配置 CSRF 保护、用户认证（支持 Google OAuth）和错误处理机制。
- **开源与社区驱动**：基于 MIT 许可，鼓励社区贡献，适用于中小型 Web 应用开发。

## 主要功能
- **项目生成**：自动创建 GAE 兼容的项目结构，包括 app.yaml、main.py 和静态资源目录。
- **依赖管理**：使用 pip 和 requirements.txt 处理 Python 依赖，支持 GAE 的 sandbox 限制。
- **认证系统**：内置用户登录/登出功能，支持多用户角色管理。
- **表单与验证**：集成 WTForms 用于表单处理和数据验证。
- **模板渲染**：使用 Jinja2 提供动态页面渲染，支持国际化 (i18n)。
- **API 支持**：易于构建 RESTful API，结合 GAE 的任务队列和数据存储 (Datastore)。
- **部署自动化**：一键部署到 GAE，支持版本管理和流量分配。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/gae-init/gae-init.git`
   - 进入目录：`cd gae-init`
   - 运行初始化脚本：`python init.py`（确保已安装 Python 2.7 和 GAE SDK）。

2. **生成项目**：
   - 使用 CLI：`python gae.py create myapp`（替换 `myapp` 为项目名）。
   - 这将生成一个新的 GAE 项目目录，包含所有必要文件。

3. **开发与运行**：
   - 进入项目目录：`cd myapp`
   - 安装依赖：`pip install -r requirements.txt -t lib`
   - 运行本地服务器：`dev_appserver.py .`
   - 访问 `http://localhost:8080` 测试应用。

4. **自定义与扩展**：
   - 编辑 `modules/` 目录下的模块文件以添加功能。
   - 配置 `app.yaml` 以调整路由和环境变量。
   - 对于认证，修改 `modules/auth.py` 并集成 Google 账户。

5. **部署**：
   - 使用 GAE 控制台或 CLI：`appcfg.py update .`
   - 确保项目符合 GAE 配额和安全规则。

更多细节请参考项目 README 和文档。