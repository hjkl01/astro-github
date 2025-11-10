---
title: Cemu
---


# Cemu (Cemu Project)

## 项目地址  
[https://github.com/cemu-project/Cemu](https://github.com/cemu-project/Cemu)

## 概述  
Cemu 是一款针对 Windows 的 Wii U 模拟器，采用开源代码，目标是提供与原机相当甚至更高的兼容性和性能。  
该项目使用 C++ 开发，支持 4K 超分辨率渲染、完整的游戏手柄和网络功能，并拥有插件系统以扩展功能。

## 主要特性  
- **高性能渲染**：使用 DirectX 12/11/9、OpenGL、Vulkan 等后端，可在 4K 分辨率下保持高帧率。  
- **完整的游戏手柄支持**：支持 Xinput、DirectInput、PS4、PS5、Switch、Steam Input 等多种控制器。  
- **自定义插件与脚本**：可加载 DLL 插件并编写 Lua 脚本，扩展图形、音频、输入等功能。  
- **网络与多玩家**：内置网络模拟器，支持本地多玩家和在线联机。  
- **图形调试与性能分析**：提供 GPU 调试、帧率计数、纹理查看等工具。  
- **Cheat Engine**：集成 Cheat Engine，支持游戏内作弊码。  
- **多语言界面**：支持多国语言，界面可自定义。

## 功能  
| 功能 | 说明 |
|------|------|
| **游戏加载** | 通过 `Cemu.exe` 打开 `.dsy`（游戏配置文件）或直接拖放 `.iso` / `wbfs`。 |
| **图形设置** | 分辨率、渲染质量、抗锯齿、阴影、纹理过滤等可手动调节。 |
| **音频设置** | 采样率、延迟、混音等。 |
| **输入设置** | 手柄映射、按键绑定、触控板支持。 |
| **插件管理** | 在 `plugins/` 目录放置 DLL，可在设置中启用。 |
| **日志与调试** | 在 `logs/` 目录生成详细日志，支持 `--debug` 命令行参数。 |
| **网络** | 支持本地多玩家、局域网联机；可调节延迟、丢包等网络参数。 |
| **截图/录像** | 通过快捷键或菜单保存截图、录制游戏视频。 |
| **脚本** | `scripts/` 目录可放置 Lua 脚本，支持自动化启动、配置加载等。 |

## 使用方法  

1. **克隆仓库**  
   ```bash
   git clone https://github.com/cemu-project/Cemu.git
   cd Cemu
   ```

2. **编译**  
   - 在 Windows 上使用 Visual Studio 2022 打开 `Cemu.sln`，构建 `Release` 或 `Debug` 版本。  
   - 或使用 CMake：`cmake -G "Visual Studio 17 2022" -A x64 .`，然后生成并编译。  

3. **运行**  
   - 双击 `Cemu.exe` 或在命令行执行 `Cemu.exe`。  
   - 通过文件菜单选择 `Open Game`，浏览到游戏的 `.dsy` 文件（可在游戏文件夹内右键生成）。  
   - 也可直接将 `.iso` / `wbfs` 拖放到窗口中。  

4. **配置**  
   - 进入 `Settings`（设置）菜单调整图形、音频、网络、输入等。  
   - 通过 `Plugins` 选项卡加载自定义插件。  
   - 快捷键 `Ctrl+I` 打开输入映射，`Ctrl+G` 打开图形调试。  

5. **运行参数**（可选）  
   ```bash
   Cemu.exe --debug   # 启用调试模式
   Cemu.exe --no-gui  # 无 GUI 模式
   ```

6. **插件与脚本**  
   - 将 DLL 插件放在 `plugins/` 目录，并在 `Settings → Plugins` 启用。  
   - 将 Lua 脚本放在 `scripts/` 目录，使用 `Settings → Scripts` 加载。  

7. **截图与录像**  
   - 截图快捷键 `F1`（保存 PNG），录像快捷键 `F2`（录制 MKV）。  
   - 录像文件位于 `Cemu/recordings/`。  

## 贡献  
- Fork 仓库，提交 Pull Request。  
- 关注 Issues，参与 bug 修复与功能讨论。  
- 阅读 `CONTRIBUTING.md` 了解贡献指南。  

---
> **注**：本项目为开源项目，使用 GPL‑3.0 许可证。请遵守相应条款进行使用与分发。  
