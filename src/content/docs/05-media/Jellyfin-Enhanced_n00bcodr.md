---
title: Jellyfin-Enhanced
---


# Jellyfin Enhanced  
项目地址: https://github.com/n00bcodr/Jellyfin-Enhanced

## 主要功能  
1. **多功能播放控制**  
   - 快进/快退、跳过片头/片尾、压制广告  
   - 自定义播放速度、淡入淡出  
2. **字幕与音轨管理**  
   - 自动下载并缓存多语言字幕  
   - 一键切换字幕/音轨，支持字幕同时显示  
3. **录像与截图**  
   - 立即截图或录制片段  
   - 自动生成缩略图并上传到媒资库  
4. **跨平台监控**  
   - 通过 WebSocket 与 Jellyfin 服务器实时同步播放状态  
   - 支持移除、恢复、暂停正在播放的媒体  
5. **插件化扩展**  
   - 支持自定义插件开发接口，扩展第三方资源获取、转码等功能  

## 特色亮点  
- **与 Jellyfin 原生 UI 深度集成**：无缝嵌入播放界面，操作习惯保持一致。  
- **多语言支持与可配置性**：所有文字可在配置文件中切换，支持 UTF-8/GB2312。  
- **低资源占用**：插件仅在播放时激活，后台保持最小占用。  

## 用法示例  

### 安装  
1. 下载插件包或克隆本仓库。  
2. 将 `Jellyfin-Enhanced.dll`（以及同目录下的 `plugin.xml`）放入  
   ```
   <Jellyfin 数据目录>/Plugins/
   ```  
3. 重新启动 Jellyfin。  

### 配置  
1. 登录 Jellyfin 后台。  
2. 前往 **插件管理** → **Jellyfin Enhanced**。  
3. 根据需要开启/关闭功能，填写字幕/音轨下载源，调整截图分辨率等。  

### 使用  
- 播放视频时，页面左下角会出现 `Enhanced` 按钮。  
- 点击按钮即可打开功能面板。  
- 快捷键（可在配置中修改）：  
  - `Shift+←/→` 快退/快进 10 秒  
  - `Shift+↑/↓` 快退/快进 30 秒  
  - `Alt+S` 切换字幕  
  - `Ctrl+S` 截图  
  - `Ctrl+R` 录制片段  

### 示例代码（插件调用）  
```csharp
// 在插件内部获取播放器
var player = context.GetService<IPlayer>();
player.Seek(TimeSpan.FromSeconds(120)); // 跳到 2 分钟位置
```

## 支持与贡献  
- **Issue tracker**: https://github.com/n00bcodr/Jellyfin-Enhanced/issues  
- **Pull requests**: https://github.com/n00bcodr/Jellyfin-Enhanced/pulls  

> 如需更多高级功能，欢迎提交 Issue 或 PR。祝使用愉快！  
