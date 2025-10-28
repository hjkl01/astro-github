
---
title: wesnoth
---


# Wesnoth

**项目地址**: [https://github.com/wesnoth/wesnoth](https://github.com/wesnoth/wesnoth)

## 项目概述
Wesnoth 是一款开源的回合制策略游戏，基于 Hex（六边形）地图，支持单人和多人对战。其核心设计强调可扩展性与可定制性，玩家可以通过脚本、地图编辑器和插件自由创建和修改游戏内容。

## 主要特性

| 特性 | 说明 |
|------|------|
| **回合制战斗** | 采用基于六边形格点的移动与攻击，支持多种兵种、技能与装备。 |
| **可扩展脚本** | 通过其内置的脚本语言（WML）支持自定义单位、事件、AI、地图等。 |
| **地图编辑器** | 提供图形化地图编辑器（Wesnoth Map Editor），支持多层地图、资源、触发器等。 |
| **多平台** | 原生支持 Linux、Windows、macOS，亦可通过 Wine 或容器运行。 |
| **多人游戏** | 通过本地局域网、互联网或服务器（如 Wesnoth Server）实现多人对战。 |
| **自定义剧情** | 通过剧情脚本（WML）可实现剧情推进、对话、事件触发等。 |
| **社区插件** | 开放式插件系统，玩家可上传地图、模组、改版，社区活跃。 |
| **本地化支持** | 预置多语言资源，支持自定义翻译。 |

## 主要功能

1. **单人战役**  
   - 经典战役模式：基于预设剧情的线性或分支战役。  
   - 自定义战役：使用 WML 定义战役脚本，结合地图和单位自定义战役流程。

2. **多人对战**  
   - **局域网**：通过本机 IP 或局域网内直接匹配。  
   - **远程服务器**：可使用官方或第三方服务器进行匹配。  
   - **自建服务器**：使用 `wesnothd` 创建私有服务器，支持自定义配置。

3. **地图编辑与发布**  
   - **图形化地图编辑器**：拖拽地形、单位、资源、触发器。  
   - **脚本编辑**：直接编辑 WML 脚本，实现高级自定义。  
   - **分享与下载**：通过官方或社区网站上传、下载地图和 mod。

4. **脚本与 Mod 开发**  
   - **单位与技能**：自定义单位属性、技能、装备。  
   - **事件系统**：监听游戏事件并执行回调脚本。  
   - **AI 自定义**：编写或修改 AI 行为，支持多种策略。  
   - **插件系统**：开发插件并通过 `wesnoth` 自动加载。  

## 用法示例

### 启动游戏
```bash
# 运行默认配置
wesnoth

# 直接加载单人战役
wesnoth -campaign <战役名称>

# 启动多人服务器
wesnothd -f -c <服务器配置文件>
```

### 创建自定义地图
1. 打开 **Wesnoth Map Editor**  
2. 选择地形、放置单位、编辑触发器  
3. 保存为 `.map` 文件  
4. 在 `wesnoth` 中 `Campaigns` 目录下创建 `campaign` 文件夹，放入地图与脚本

### 编写 WML 脚本
```text
[scenario]
    id=example
    name="示例地图"
    map_data="{~add-ons/Example/map/example.map}"
    {DEFAULT_SCHEDULE}
    [side]
        side=1
        team_name=white
        controller=human
        type=Peasant
        [unit]
            x,y=5,5
            type=Peasant
        [/unit]
    [/side]
[/scenario]
```

## 贡献与支持
- **源码**：托管在 GitHub，使用 `git clone https://github.com/wesnoth/wesnoth.git`。  
- **文档**：可在 `doc` 目录查看详细开发说明。  
- **社区**：官方论坛、Discord、Reddit 以及各大地图/模组网站。

> **提示**：在开发自定义内容前建议先阅读官方的 **Wesnoth Manual** 与 **WML Reference**，以充分利用脚本功能与地图编辑器。

