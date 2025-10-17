
---
title: wooey
---

# Wooey 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/wooey/wooey)

## 主要特性
Wooey 是一个开源的 Django 应用，用于创建和管理基于 Web 的命令行工具和工作流。它允许用户无需编写前端代码，即可将命令行脚本转换为用户友好的 Web 界面。主要特性包括：
- **命令行工具 Web 化**：自动将 Python 脚本（如使用 argparse 或 Click）转换为 Web 表单，支持参数输入、文件上传和结果可视化。
- **工作流管理**：支持构建多步骤工作流，允许用户链式执行多个工具。
- **用户界面友好**：内置响应式设计，支持实时进度跟踪、结果下载和历史记录。
- **集成简单**：基于 Django 框架，易于集成到现有 Django 项目中，支持数据库存储任务结果。
- **扩展性强**：支持插件系统和自定义模板，适用于科学计算、数据处理等场景。
- **开源免费**：MIT 许可，社区维护，提供 Docker 支持以便快速部署。

## 主要功能
- **工具注册**：通过装饰器（如 `@wooey_cmd`）快速注册命令行脚本，使其在 Web 上可用。
- **参数处理**：自动解析脚本参数，支持布尔值、选择框、文件上传、多选等输入类型。
- **执行与监控**：用户提交任务后，后台异步执行，支持进度条和日志查看。
- **结果输出**：生成报告、图表或文件下载，支持 Pandas DataFrame 等数据可视化。
- **权限与协作**：集成 Django 用户系统，支持任务共享和 API 访问。
- **部署选项**：支持本地开发、Heroku 或 Docker 部署。

## 用法
1. **安装**：
   - 确保 Python 3.6+ 和 Django 2.0+ 已安装。
   - 通过 pip 安装：`pip install django-wooey`。
   - 在 Django 项目中添加 `'wooey'` 到 `INSTALLED_APPS`。

2. **创建工具**：
   - 编写命令行脚本，例如使用 argparse：
     ```python
     import argparse
     from wooey import wooey_cmd

     @wooey_cmd
     def my_tool(input_file, output_dir):
         # 你的脚本逻辑
         pass

     if __name__ == '__main__':
         parser = argparse.ArgumentParser()
         parser.add_argument('input_file')
         parser.add_argument('output_dir')
         args = parser.parse_args()
         my_tool(args.input_file, args.output_dir)
     ```
   - 将脚本放置在 Django 应用的 `tasks.py` 或指定目录中。

3. **配置与运行**：
   - 在 `urls.py` 中包含 Wooey URL：`path('wooey/', include('wooey.urls'))`。
   - 运行 Django 服务器：`python manage.py runserver`。
   - 访问 `/wooey/` 即可看到工具列表，用户可提交任务。

4. **高级用法**：
   - 配置数据库：运行 `python manage.py migrate` 以创建任务表。
   - 自定义界面：修改 Wooey 模板或使用 Celery 集成异步任务。
   - 更多细节参考项目文档：https://wooey.readthedocs.io/。

此项目适合开发者快速构建 Web 工具原型，尤其在科研和自动化领域。