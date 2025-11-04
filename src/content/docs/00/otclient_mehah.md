
---
title: otclient
---


# OTClient (mehah 版)

> 项目地址: <https://github.com/mehah/otclient>

## 项目简介
OTClient 是一个开源的 **OpenTibia** 客户端，采用 C++ 编写，支持多平台（Windows、Linux、macOS）。mehah 的分支在原始 OTClient 基础上做了若干改进，保持了高度的可定制性与脚本化能力。

## 主要特性
- **跨平台**：一次编译即可在 Windows、Linux 及 macOS 上运行。  
- **Lua 脚本引擎**：几乎所有客户端行为、宏、插件均可通过 Lua 脚本实现。  
- **高性能渲染**：使用 OpenGL/DirectX 渲染引擎，支持 2D/3D 混合渲染。  
- **可扩展插件系统**：插件可在运行时加载、卸载，支持热重载。  
- **网络协议完整实现**：支持 OpenTibia 协议 v10.x 及其后续版本。  
- **资源打包**：支持使用 `otclient-res` 打包资源（纹理、音效、脚本等）。  
- **调试与日志**：内置调试窗口、日志系统，方便开发者排查问题。  

## 功能概览
| 功能               | 描述 |
|--------------------|------|
| **角色创建/登录** | 支持多账号管理与快捷登录。 |
| **地图与视角** | 3D 视角、地图缩放、视图旋转。 |
| **聊天系统** | 私聊、公共聊天、频道管理、表情包。 |
| **技能与属性** | 实时显示角色属性、技能成长曲线。 |
| **宏与脚本** | 通过 Lua 定义动作宏、自动战斗脚本。 |
| **插件** | 第三方插件（如画图、快捷键、自动拾取）可直接安装。 |
| **资源管理** | 支持自定义贴图、音效、字体。 |
| **网络监控** | 捕获/分析服务器数据包，便于调试。 |

## 用法

### 1. 克隆仓库
```bash
git clone https://github.com/mehah/otclient.git
cd otclient
```

### 2. 安装依赖（示例：Ubuntu）
```bash
sudo apt-get install build-essential cmake git libgl1-mesa-dev libx11-dev
```

### 3. 编译
```bash
mkdir build && cd build
cmake ..
make -j$(nproc)
```

### 4. 启动
```bash
./otclient
```

### 5. 配置
- **Lua 脚本**：放在 `scripts/` 目录下，重启客户端后自动加载。  
- **插件**：放在 `plugins/` 目录，支持热重载（F5）。  
- **资源**：放在 `resources/` 目录，使用 `otclient-res` 进行打包。  

### 6. 常用热键
| 键位 | 功能 |
|------|------|
| **F5** | 重新加载 Lua 脚本 |
| **F6** | 切换视角 |
| **Ctrl+R** | 测试插件/脚本 |

> **提示**：若遇到编译或运行错误，查看 `logs/` 目录下的日志文件，或在 Issues 区提交问题。  

--- 

> 以上内容仅为快速入门，更多高级使用请参考官方文档及源码注释。  

