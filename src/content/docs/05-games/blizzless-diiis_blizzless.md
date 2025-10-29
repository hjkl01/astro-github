
---
title: blizzless-diiis
---

# Blizzless Diiis

*项目地址:* https://github.com/blizzless/blizzless-diiis

## 简介

Blizzless Diiis 是一款基于 Diablo II（圣物版）原版的温和补丁，旨在让游戏在现代 Windows 系统（Windows 10/11/Win Server 等）上无缝运行。通过修复原版游戏中的崩溃、性能瓶颈以及兼容性问题，提供更稳定、无错误的游戏体验。

## 主要特性

| 功能 | 说明 |
|------|------|
| **兼容性修复** | 解决因 64 位系统导致的崩溃、显示错误及 “Missing LDB” 等问题。 |
| **性能提升** | 启用 DirectX 11 渲染、帧率上限等设置，保持画面流畅。 |
| **资源更新** | 替换低分辨率纹理、音频，提升画面效果。 |
| **自动更新** | 可配置为自动检测并下载 Diablo II 补丁。 |
| **配置文件** | 通过 `blizzless.ini` 进行功能开关与细节调优。 |
| **社区支持** | 开源维护，新问题可在仓库 Issues 中追踪。 |

## 使用方法

1. **准备游戏**  
   确认您已合法拥有 Diablo II。

2. **克隆仓库**  
   ```bash
   git clone https://github.com/blizzless/blizzless-diiis.git
   cd blizzless-diiis
   ```

3. **安装依赖**（可选）  
   Windows 下直接使用发布版压缩包即可；自行编译需安装 Visual Studio 2019+、.NET Framework 4.8 与 `NuGet`。

4. **运行安装脚本**  
   ```bash
   setup.bat   # 或在 Linux/Mac 下 ./setup.sh
   ```  
   脚本自动下载补丁、解压并替换原始文件，同时生成 `blizzless.ini`。

5. **启动游戏**  
   直接双击 `Diablo II.exe` 或通过游戏启动器指向已补丁的路径即可。

6. **配置调优**（可选）  
   打开 `blizzless.ini`，按需修改参数，例如：
   ```ini
   [Rendering]
   EnableDX11=1
   MaxFPS=99
   ```

## 参考文件

- `README.md`: 本文档  
- `blizzless.ini`: 调整配置  
- `setup.bat`/`setup.sh`: 安装脚本  
- `Assets/`: 更新资源集合  
- `Docs/`: 详细文档与常见问题  

如需进一步帮助，请参阅本仓库 Issues 或加入社区 Discord。