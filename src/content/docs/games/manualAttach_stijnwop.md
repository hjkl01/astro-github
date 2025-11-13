---
title: manualAttach
---

# ManualAttach for Farming Simulator 25

ManualAttach 是一个 Farming Simulator 25 的修改（mod），旨在强制玩家手动连接和断开工具，实现更真实的农业模拟体验。该 mod 禁用从车辆内快速切换工具的功能，要求玩家下车进行操作。

## 功能

### Attach/Detach Implements（连接/断开工具）

- 当连接工具时，脚本强制工具保持在降低状态。
- 某些工具（如前装载机、滑移转向器、铲子、伸缩叉车、联合收割机和钩式升降机）有例外，可以在车辆内连接和断开。
- 连接软管和动力输出轴仍需手动连接。
- 要断开工具，必须先降低工具，并确保动力输出轴和连接软管已断开。
- Mod 禁用从车辆内连接和断开工具（上述例外除外），不再允许快速切换工具。

### Attach/Detach Power Take Off（连接/断开动力输出轴）

- 按 `Z` 键连接/断开动力输出轴。
- 注意：工具需要动力输出轴，否则无法启动。

### Attach/Detach Connection Hoses（连接/断开连接软管）

- 长按 `Z` 键（短时间）连接/断开连接软管。
- 如果未连接连接软管，可能导致：
  - 无法控制液压系统（例如移动部件、折叠、使用脊标记等）。
  - 无法使用灯光。
  - 刹车被阻塞。

## Mod 支持

对于创建或修改车辆和工具，可以使用 `attacherJoint` 和 `inputAttacherJoint` XML 条目控制连接行为。使用 `isManual` 和 `isAuto` 属性定义连接行为。

### 属性概述

- `isManual="true/false"` — 强制手动连接。玩家必须手动连接工具；游戏不会自动连接。
- `isAuto="true/false"` — 强制自动连接。工具一旦进入范围就会连接，无论手动设置如何。

示例：

```xml
<!-- 工具侧 '手动连接' -->
<inputAttacherJoint isManual="true" jointType="X" .... />

<!-- 车辆侧 '手动连接' -->
<attacherJoint isManual="true" jointType="X" ..... />

<!-- 工具侧 '标准连接' -->
<inputAttacherJoint isManual="false" jointType="X" .... />

<!-- 车辆侧 '标准连接' -->
<attacherJoint isManual="false" jointType="X" ..... />

<!-- 工具侧 '启用自动连接' -->
<inputAttacherJoint isAuto="true" jointType="X" .... />

<!-- 车辆侧 '启用自动连接' -->
<attacherJoint isAuto="true" jointType="X" ..... />

<!-- 工具侧 '禁用自动连接' -->
<inputAttacherJoint isAuto="false" jointType="X" .... />

<!-- 车辆侧 '禁用自动连接' -->
<attacherJoint isAuto="false" jointType="X" ..... />
```

## 警告

这是一个开发版本！

- 开发版本可能破坏游戏或您的存档！
- 开发版本尚未支持完整的功能包！

## 许可证

GPL-3.0 许可证

## 贡献者

感谢所有贡献者，包括 stijnwop 和其他开发者。

## 下载

从 [GitHub Releases](https://github.com/stijnwop/manualAttach/releases) 下载最新版本。
