---
title: overlord
---

# Overlord 项目

**项目地址:** [https://github.com/bilibili/overlord](https://github.com/bilibili/overlord)

## 主要特性
Overlord 是哔哩哔哩（Bilibili）开源的 Android 客户端开发框架，基于 MVP 架构设计，旨在简化移动应用开发流程。其核心特性包括：
- **模块化设计**：支持多模块项目结构，便于团队协作和代码复用。
- **网络请求封装**：集成 Retrofit 和 RxJava，提供简洁的 API 调用方式，支持缓存和错误处理。
- **UI 组件库**：内置常用 UI 组件，如 RecyclerView 适配器、图片加载（基于 Glide）和弹窗管理。
- **数据管理**：使用 AutoValue 和 Dagger2 实现依赖注入和数据绑定，提高代码可维护性。
- **测试友好**：支持单元测试和 UI 测试框架集成，便于 CI/CD 流程。
- **性能优化**：内置内存泄漏检测和 ANR 监控工具。

## 主要功能
- **网络层**：处理 HTTP 请求、JSON 解析和文件上传/下载。
- **业务逻辑层**：MVP 模式分离视图和模型，支持异步操作和状态管理。
- **工具类库**：包括日志记录、权限管理、SharedPreferences 封装和事件总线（EventBus）。
- **集成扩展**：易于集成第三方库，如 Firebase、腾讯地图等。
- **构建配置**：使用 Gradle 管理依赖，支持多环境构建（Debug/Release）。

## 用法
1. **克隆项目**：  
   ```
   git clone https://github.com/bilibili/overlord.git
   cd overlord
   ```

2. **导入 IDE**：使用 Android Studio 打开项目根目录，Gradle 会自动同步依赖。

3. **配置环境**：  
   - 在 `local.properties` 中设置 SDK 路径。  
   - 修改 `build.gradle` 中的 API 密钥（如网络接口）。  

4. **运行示例**：  
   - 打开 `app` 模块，点击运行按钮启动 Demo App。  
   - 示例模块展示了网络请求、列表加载和登录功能的使用。  

5. **自定义开发**：  
   - 在 `base` 模块中扩展 BaseActivity/BaseFragment。  
   - 使用 `network` 模块的 ApiService 类发起请求，例如：  
     ```java
     ApiService.getInstance().getUserInfo(userId)
         .subscribeOn(Schedulers.io())
         .observeOn(AndroidSchedulers.mainThread())
         .subscribe(response -> { /* 处理响应 */ });
     ```  
   - 集成到新项目：复制所需模块到你的 Gradle 项目中，并添加依赖。  

项目适用于 Android 开发，推荐 Kotlin 迁移以提升现代性。更多细节请参考仓库 README。