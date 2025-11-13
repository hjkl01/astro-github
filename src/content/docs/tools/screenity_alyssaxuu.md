---
title: screenity
---

```markdown
# Screenity

> GitHub 项目地址: [https://github.com/alyssaxuu/screenity](https://github.com/uu/screenity)

## 一、项目概述  
Screenity 是一款 **跨平台、轻量级** 的屏幕录制与分享工具，采用 Rust + Naive UI 开发，主打简洁的 UI 与极致的性能。  
- **跨平台**：Windows、macOS 与 Linux 全都支持。  
- **极简 UI**：一键开启录制、不需复杂设置。  
- **多功能**：支持全屏幕、窗口、区域录制；录制时可伴随系统音频、麦克风音频；支持摄像头叠加。  
- **导出与分享**：录制完成后可直接保存为 MP4、JSON、GIF 等格式，并可以一键生成分享链接。  

## 二、主要特性

| 特色 | 说明 |
|------|------|
| **快捷录制** | 通过键盘热键快速开启/停止录制。 |
| **音频支持** | 同时捕获麦克风与系统音频。 |
| **摄像头叠加** | 兼容多种摄像头，并支持大小、位置调整。 |
| **窗口/区域录制** | 选择特定窗口或自定义矩形区域。 |
| **文件导出** | 支持 MP4、GIF、WebM、PNG（帧）等多种格式。 |
| **分享链接** | 通过内置服务器快速生成分享链接，支持第三方云存储。 |
| **可定制 UI** | 内置主题，支持随需切换。 |
| **轻量级** | 仅需 20MB 大小，运行无显卡需求。 |

## 三、功能详情

1. **启动与停止**  
   - 运行 `screenity` 即可进入主界面，点击“开始录制”即可启动。  
   - 或使用快捷键 `Ctrl+Shift+S`（Windows/Linux） / `Cmd+Shift+S`（macOS）进行切换。  

2. **录制模式**  
   - **全屏**：捕获当前显示器全部内容。  
   - **窗口**：选择单个窗口进行录制。  
   - **区域**：自定义拖拽矩形进行区域录制。  

3. **声音与摄像**  
   - 通过音量滑块灵活控制麦克风与系统音量。  
   - 开启摄像头后会在视频左下角以浮动窗口显示。  

4. **导出与分享**  
   - 录制结束后弹出导出界面，选择格式与位置。  
   - 开启“共享”功能后可生成短链，直接打开或复制。  

5. **快捷键配置**  
   - 在设置中自定义热键，例如 `Ctrl+Alt+R` 开始/停止录制。  

## 四、安装与使用

### 1. 安装（Windows/macOS/Linux）

#### a. 通过官方安装包

| 系统 | 下载链接 |
|------|----------|
| Windows | `https://github.com/alyssaxuu/screenity/releases/latest/download/screenity-setup.exe` |
| macOS | `https://github.com/alyssaxuu/screenity/releases/latest/download/screenity-mac.dmg` |
| Linux | `.AppImage` 或 `deb/rpm` 依据发行版下载 |

> **注意**：安装前请确保系统已安装.NET 6/7` 或相关依赖，或直接使用 AppImage。

#### b. 从源码构建

```bash
# 1. 克隆仓库
git clone https://github.com/alyssaxuu/screenity.git
cd screenity

# 2. 安装 Rust 环境（若未安装）
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# 3. 构建
cargo build --release

# 4. 可执行文件在 target/release/
```

### 2. 快速开始

1. **运行**  
   ```bash
   screenity
   ```
   或直接双击安装好的快捷方式。

2. **录制**  
   - 选择录制方式（全屏/窗口/区域）。  
   - 配置音频与摄像头。  
   - 点击“开始录制”或快捷键即可。

3. **停止录制**  
   再次点击“停止”或使用热键。

4. **导出/分享**  
   - 在弹出的导出对话框中选择文件位置与格式。  
   - 若需要共享，勾选“分享”后复制链接即可。

### 3. 常见快捷键（默认）

| 功能 | 快捷键 |
|------|--------|
| 开始/停止录制 | `Ctrl+Shift+S` (Windows/Linux) / `Cmd+Shift+S` (macOS) |
| 关闭窗口 | `Alt+F4` / `Cmd+W` |

> 如需更改，可在 **设置 → 键盘** 页面进行自定义。

## 五、常见问题

1. **录制后无声**  
   - 检查系统音量与麦克风权限。  
   - 确认 `SYSTEM_AUDIO` 与 `MIC_AUDIO` 开启。

2. **摄像头不显示**  
   - 重新插拔摄像头。  
   - 进入 **设置 → 摄像头** 检查是否正确识别。

3. **文件过大/帧率低**  
   - 在 **设置 → 录像** 调整分辨率与帧率。  
   - 使用硬件编码（如 NVENC）可提升压缩效率。

## 六、贡献

- Fork 本仓库 → 新建分支 → 提交 PR。  
- 详见 `CONTRIBUTING.md` 与 `ISSUE_TEMPLATE.md`。

---
> **项目主页**  
> https://github.com/alyssaxuu/screenity
