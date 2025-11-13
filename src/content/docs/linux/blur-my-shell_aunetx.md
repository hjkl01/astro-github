---
title: blur-my-shell
---


# blur-my-shell (by aunetx)

**项目地址**: https://github.com/aunetx/blur-my-shell

## 主要特性

- **系统桌面模糊**  
  为 GNOME 桌面、GTK3/GTK4 应用窗口以及 Unity/Unity‑Splash 桌面实现背景模糊效果。

- **支持多种渲染后端**  
  - `GLOES`（OpenGL ES）  
  - `GLSL`（OpenGL Shading Language）  
  - `Vulkan`（实验版）

- **兼容多种窗口**  
  - GNOME Shell  
  - Unity / Unity‑Splash  
  - GTK3/GTK4 对话框与工具栏

- **动态调整**  
  自动根据主题和时间调整模糊强度与透明度。

- **插件化与自定义**  
  通过配置文件 `~/.config/blur-my-shell/config.json` 进行细粒度设置。

## 功能概览

| 功能 | 说明 |
|------|------|
| `blur-my-shell` | 启动后在后台持续监控窗口变化并自动应用模糊。 |
| `bmctl` | 命令行工具，用于开启/关闭模糊、切换后端等。 |
| `bmctl status` | 查看当前系统状态与后端信息。 |
| `bmctl clearcache` | 清除内部缓存，解决不刷新问题。 |
| `bm` | 重新加载配置并应用新设置。 |

## 用法示例

```bash
# 安装
git clone https://github.com/aunetx/blur-my-shell.git
cd blur-my-shell
sudo ./install.sh

# 启 blur-my-shell
blur-my-shell

# 使用 bmctl
bmctl status          # 查看当前状态
bmctl clearcache      # 清除缓存
bmctl reload          # 重载配置
```

### 配置文件示例（`~/.config/blur-my-shell/config.json`）

```json
{
  "enabled": true,
  "forceEngine": "vulkan",
  "blurRadius": 15,
  "opacity": 0.8
}
```

> **提示**：若使用 `vulkan` 后端，请确认显卡驱动已开启硬件加速。

## 贡献与获取帮助

- 访问 GitHub Issues 页面报告问题或提交流程。  
- 查看 `docs/README.md` 或 `docs/reference.md` 了解更细致的配置与实现细节。

---
*以上内容为项目快速说明，更多详情请参阅官方 GitHub 文档。*
```
