
---
title: wave
---

# H2O Wave 项目

## 项目地址
[https://github.com/h2oai/wave](https://github.com/h2oai/wave)

## 主要特性
H2O Wave 是一个开源的 Python 框架，用于构建实时 Web 应用程序。它专注于简化数据科学和机器学习工作流的 Web 接口开发，具有以下核心特性：
- **实时响应式 UI**：支持动态更新用户界面，无需页面刷新，实现流畅的交互体验。
- **Python 原生开发**：使用纯 Python 编写前后端逻辑，无需 JavaScript 或 HTML/CSS 知识，降低开发门槛。
- **内置组件库**：提供丰富的 UI 组件，如图表、表格、按钮和表单，支持快速构建仪表板和应用。
- **高性能后端**：基于异步编程（asyncio），适合处理大数据和实时数据流。
- **易于部署**：支持单文件应用部署，可轻松集成到服务器或云环境中。
- **开源与社区支持**：由 H2O.ai 维护，许可为 Apache 2.0，适用于商业和研究用途。

## 主要功能
- **Web 应用构建**：快速创建交互式 Web 应用，如数据可视化仪表板、实时监控工具和 AI 模型接口。
- **数据集成**：无缝连接数据库、CSV 文件或实时数据源，支持 Pandas 和 H2O 等库。
- **用户交互**：处理用户输入、事件触发和状态管理，实现响应式设计。
- **扩展性**：支持自定义组件和第三方集成，适用于机器学习管道、业务智能（BI）工具等场景。
- **安全与认证**：内置用户认证和会话管理，确保应用安全。

## 用法
1. **安装**：使用 pip 安装框架：
   ```
   pip install h2o-wave
   ```

2. **基本应用创建**：编写一个简单的 Python 脚本（例如 `app.py`）：
   ```python
   from h2o_wave import site, ui

   @site("/demo")
   async def main(q):
       if q.args == {}:
           q.page['example'] = ui.markdown_card(
               box='1 1 2 2',
               title='欢迎使用 H2O Wave',
               content='这是一个简单的示例应用。'
           )
       await q.page.save()

   if __name__ == '__main__':
       from h2o_wave import run
       run("http://localhost:10101", "demo")
   ```

3. **运行应用**：在终端执行 `python app.py`，然后在浏览器访问 `http://localhost:10101/demo`。

4. **高级用法**：
   - 添加交互组件：使用 `ui.button` 或 `ui.plot` 等构建动态页面。
   - 处理事件：在路由函数中响应用户操作，如按钮点击或表单提交。
   - 部署：使用 Docker 或云服务（如 AWS、GCP）部署生产环境，支持多用户访问。

更多细节请参考官方文档：https://wave.h2o.ai/docs/