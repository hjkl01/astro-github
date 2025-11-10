---
title: nonebot2
---

# NoneBot2 项目

**GitHub 项目地址：** [https://github.com/nonebot/nonebot2](https://github.com/nonebot/nonebot2)

## 主要特性
NoneBot2 是一个现代、简洁、易用的 Python 异步 QQ 机器人框架，专为开发 QQ 机器人而设计。它基于 asyncio 和 FastAPI，支持插件化开发，强调模块化和可扩展性。主要特性包括：
- **异步支持**：充分利用 Python 的 asyncio 实现高并发处理，适合处理大量消息。
- **插件系统**：模块化设计，用户可以轻松编写和加载插件，实现功能复用。
- **事件驱动**：基于事件机制响应消息、群聊事件等，支持自定义事件处理器。
- **依赖注入**：内置依赖注入系统，便于管理配置、数据库等资源。
- **Web API 支持**：集成 FastAPI，提供 HTTP API 接口，便于外部调用和 Web 钩子。
- **多适配器**：支持多种 QQ 协议适配器（如 OneBot v11），易于切换后端。
- **类型提示**：全面使用 type hints 和 mypy 支持，提高代码可靠性和开发效率。
- **国际化**：支持多语言配置，适合全球开发者。

## 主要功能
NoneBot2 提供了一系列核心功能，用于构建智能 QQ 机器人：
- **消息处理**：支持文本、图片、语音、@消息等 QQ 消息类型，可实现回复、转发等操作。
- **群管理和权限控制**：内置角色系统（如主人、管理员），支持群聊禁言、踢人等管理功能。
- **数据库集成**：易于集成 SQLAlchemy 或其他 ORM，支持数据持久化。
- **定时任务**：通过 APScheduler 实现定时执行任务，如每日提醒。
- **自然语言处理**：可扩展集成 NLP 库，实现聊天机器人、智能问答。
- **插件市场**：社区插件丰富，包括天气查询、翻译、游戏等功能。
- **日志和监控**：内置日志系统和错误处理，支持 Sentry 等监控工具。

## 用法
### 安装
1. 确保 Python 版本 >= 3.8。
2. 使用 pip 安装：
   ```
   pip install nonebot2
   ```
3. 对于 QQ 适配器，安装 OneBot 驱动：
   ```
   pip install nonebot-adapter-onebot
   ```

### 快速启动
1. 创建项目目录：
   ```
   mkdir my_bot
   cd my_bot
   nonebot init
   ```
   这会生成 `pyproject.toml`、`bot.py` 和 `config.py` 等文件。

2. 配置 `config.py`：
   ```python
   from nonebot import get_driver

   driver = get_driver()

   @driver.on_startup
   async def _():
       print("Bot 启动中...")

   nonebot.init()
   driver.run(host="127.0.0.1", port=8080)
   ```

3. 编写插件：在 `src/plugins/` 目录下创建插件文件，例如 `hello.py`：
   ```python
   from nonebot import on_command
   from nonebot.adapters.onebot.v11 import Bot, Event

   hello = on_command("hello")

   @hello.handle()
   async def handle_hello(bot: Bot, event: Event):
       await hello.finish("Hello World!")
   ```

4. 运行机器人：
   ```
   nb run
   ```
   然后通过 QQ 客户端连接到本地 OneBot 服务（需单独运行 go-cqhttp 或类似工具）。

### 开发插件
- 使用 `@on_command`、`@on_message` 等装饰器定义事件处理器。
- 通过 `require` 和 `provide` 管理插件依赖。
- 测试：使用 `nb test` 命令运行单元测试。

更多细节请参考官方文档：https://nonebot.dev/