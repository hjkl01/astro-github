
---
title: sa-sdk-android
---

# Sensors Analytics Android SDK

**项目地址：** [https://github.com/sensorsdata/sa-sdk-android](https://github.com/sensorsdata/sa-sdk-android)

## 主要特性
Sensors Analytics Android SDK 是神策数据（Sensors Analytics）提供的移动端数据采集工具，主要用于Android应用的埋点和数据分析。它支持实时数据上报、用户行为追踪和事件分析，具有以下核心特性：
- **实时数据采集**：支持事件、用户属性和页面浏览等数据的实时上报，确保数据准确性和时效性。
- **无埋点支持**：提供可视化埋点和全埋点功能，减少开发工作量。
- **用户画像与分群**：自动采集设备信息、用户行为，支持自定义用户属性和标签，用于用户画像构建。
- **数据加密与隐私保护**：集成数据加密传输、IP过滤和合规性功能，符合GDPR等隐私法规。
- **多平台兼容**：支持Android 4.0及以上版本，兼容主流Android设备和框架（如React Native、Unity）。
- **性能优化**：异步上报机制，减少对应用性能的影响，支持离线缓存和批量上报。

## 主要功能
- **事件追踪**：记录用户操作事件，如点击、页面停留、搜索等，支持自定义事件参数。
- **用户行为分析**：自动采集APP启动、页面访问、崩溃等系统事件，便于行为路径分析。
- **集成扩展**：支持与第三方SDK集成，如推送服务（极光推送）、支付SDK等。
- **调试与监控**：内置调试模式和日志输出，便于开发测试和问题排查。
- **A/B测试支持**：结合神策数据平台，实现实验管理和效果评估。

## 用法
### 1. 集成步骤
1. **添加依赖**：在项目的 `build.gradle` 文件中添加SDK依赖：
   ```
   implementation 'com.sensorsdata.analytics.android:AndroidSDK:4.x.x'  // 替换为最新版本
   ```
   同步项目后，SDK即可引入。

2. **初始化SDK**：在 `Application` 类或主Activity的 `onCreate` 方法中初始化：
   ```java
   import com.sensorsdata.analytics.android.sdk.SensorsDataAPI;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();
           SensorsDataAPI.sharedInstance(this, "YOUR_SERVER_URL", "YOUR_APP_ID");
       }
   }
   ```
   - `YOUR_SERVER_URL`：神策数据服务器地址（如 https://your-project.sensorsdata.cn）。
   - `YOUR_APP_ID`：项目ID，由神策数据平台提供。

3. **权限配置**：在 `AndroidManifest.xml` 中添加网络权限：
   ```xml
   <uses-permission android:name="android.permission.INTERNET" />
   <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
   ```

### 2. 数据上报示例
- **追踪事件**：
  ```java
  JSONObject properties = new JSONObject();
  properties.put("item_id", "12345");
  SensorsDataAPI.sharedInstance().track("Purchase", properties);
  ```
- **设置用户属性**：
  ```java
  SensorsDataAPI.sharedInstance().identify("user_id_123");
  JSONObject userProps = new JSONObject();
  userProps.put("age", 25);
  SensorsDataAPI.sharedInstance().profileSet(userProps);
  ```
- **页面停留追踪**：
  ```java
  SensorsDataAPI.sharedInstance().pageStart("HomePage");
  // 在页面结束时调用
  SensorsDataAPI.sharedInstance().pageEnd("HomePage");
  ```

### 3. 高级用法
- **启用调试模式**（开发时使用）：
  ```java
  SensorsDataAPI.sharedInstance().enableDebugMode();
  ```
- **自定义配置**：通过 `SensorsDataInitOptions` 对象设置上报间隔、加密等参数。
- **无埋点集成**：如果使用神策可视化埋点，无需手动代码，上报通过平台配置自动实现。
- **更新与卸载**：SDK支持APP更新事件自动追踪，确保数据连续性。

更多详细用法和API文档，请参考项目仓库的 README 和官方文档。建议结合神策数据平台使用，以实现完整的数据分析流程。