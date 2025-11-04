
---
title: Handy
---

下面请参考该文件的完整 Markdown 内容：

# Handy（cjpais/Handy）

> 项目地址：<https://github.com/cjpais/Handy>

---

## 简介

Handy 是一个面向 .NET/C# 开发者的通用工具库，旨在简化日常编程工作，减少重复代码。它集成了若干常用的扩展方法、单例实现、事件总线、协程管理以及线程安全包装等功能，覆盖了从单线程到多线程、从 UI 交互到后台处理等多大场景。

---

## 主要特性

| 序号 | 功能模块 | 特色 | 适用场景 |
|------|----------|------|----------|
| 1 | **扩展方法** | 通过 `.Extension` 命名空间提供的链式调用，极大提升代码可读性。例如：`string.IsNullOrWhiteSpace()`、`list.ForEachAsync()` 等 | 泛型集合、字符串、异步处理 |
| 2 | **单例与懒加载** | `Singleton<T>`、`LazySingleton<T>` 等通用单例实现，无需手动管理 | 配置、缓存、全局工具 |
| 3 | **事件总线** | `EventBus` 提供基于类型的发布/订阅模式，支持优先级、延迟执行 |MVVM、插件通信、解耦组件 |
| 4 | **协程 & 异步辅助** | `CoroutineRunner`、`AsyncUtils` 等包装，能在 Unity、WPF 等框架中使用协程/异步执行任务 | UI 刷新、网络请求、后端任务 |
| 5 | **安全集合 & 线程包装** | `ConcurrentSet<T>`, `ReadWriteLock` 等线程安全容器与锁，配合 `AsyncContext` 简化多线程访问 | 并发请求、后台计算 |
| 6 | **日志与调试** | `ILogger` 接口与多种实现（Console、File、Debug）支持统一日志管理 | 诊断、监控 |
| 7 | **配置与缓存** | `Config<T>`, `ObjectCache` 提供类型安全的配置读取与内存缓存 | 应用设置、重用实例 |
| 8 | **网络与序列化** | `HttpClientFactory`, `JsonHelper` 等易用包装，支持自动重试、泛型序列化 | REST API、数据传输 |

---

## 功能说明

1. **链式扩展**  
   ```csharp
   var result = new List<int> { 1, 2, 3, 4 }
                 .Where(x => x % 2 == 0)
                 .Take(2)
                 .Sum();
   ```

2. **单例获取**  
   ```csharp
   var logger = Singleton<ILogger>.Instance;
   ```

3. **事件发布/订阅**  
   ```csharp
   EventBus.Pub(new DataLoadedEvent(data));
   EventBus.Sub<DataLoadedEvent>(e => Console.WriteLine($"Data size: {e.Data.Count}"));
   ```

4. **协程执行**  
   ```csharp
   CoroutineRunner.Start(() =>
   {
       // long running task
   });
   ```

5. **线程安全集合**  
   ```csharp
   var set = new ConcurrentSet<string>();
   set.Add("item");
   ```

---

## 使用方法

1. **添加引用**  
   通过 NuGet 安装：  
   ```bash
   dotnet add package Handy
   ```

   或直接克隆源码后编译：
   ```bash
   git clone https://github.com/cjpais/Handy.git
   cd Handy
   dotnet build
   dotnet pack
   ```

2. **在项目中使用**  
   ```csharp
   using Handy.Extensions;
   using Handy.Events;
   using Handy.Coroutines;
   using Handy.Collections;
   ```

3. **配置**  
   若使用配置功能，放置 `appsettings.json`，项目会自动读取对应的类型：
   ```csharp
   var config = Config<MySettings>.Get();
   ```

4. **日志**  
   通过 `ILogger` 接口注入，支持多种后端：
   ```csharp
   var logger = Logger.Get<ConsoleLogger>();
   logger.Info("Application started");
   ```

---

## 示例项目

- **Console Demo**：演示了日志、单例、事件总线、协程与安全集合的使用。  
- **Web API Demo**：集成 `HttpClientFactory` 与 `EventBus`，展示异步请求与消息派发。  

> 详细代码与使用示例请参阅仓库根目录下的 `Examples` 文件夹。

---

> **额外信息**  
> 该库保持轻量级，核心依赖少，且兼容 .NET Standard 2.1 及更高版本。

> **贡献**  
> 若您有改进建议或想提交 PR，请 Fork发送 Pull Request，欢迎社区参与。

---

> — End —
