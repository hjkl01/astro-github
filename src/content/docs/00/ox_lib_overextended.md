---
title: Ox
---

# ox_lib

## 项目简介

ox_lib 是一个 FiveM 资源和脚本库，为 Lua 和 JavaScript 提供可重用的模块、方法和 UI 元素。它是一个独立的库，旨在简化 FiveM 脚本开发。

## 主要功能

ox_lib 提供了丰富的模块，包括：

### Interface 模块

- **Alert Dialog**: 显示警告对话框
- **Clipboard**: 剪贴板操作
- **Context Menu**: 上下文菜单
- **Input Dialog**: 输入对话框
- **Menu**: 菜单系统
- **Notifications**: 通知系统
- **Progress**: 进度条
- **Radial Menu**: 径向菜单
- **Skill Check**: 技能检查
- **TextUI**: 文本 UI

### 其他核心模块

- **ACL**: 访问控制列表
- **AddCommand**: 添加命令
- **AddKeybind**: 添加按键绑定
- **Array**: 数组操作工具
- **Cache**: 缓存系统
- **Callback**: 回调函数
- **Class**: 类系统
- **Cron**: 定时任务
- **DisableControls**: 禁用控制
- **Dui**: 动态 UI
- **GetClosestObject/Ped/Player/Vehicle**: 获取最近的实体
- **GetNearbyObjects/Peds/Players/Vehicles**: 获取附近的实体
- **Grid**: 网格系统
- **Locale**: 本地化
- **Logger**: 日志记录
- **Marker**: 标记
- **Math**: 数学工具
- **PlayAnim**: 播放动画
- **Points**: 点系统
- **Print**: 打印工具
- **Raycast**: 射线投射
- **Require**: 模块加载
- **Scaleform**: Scaleform UI
- **Streaming**: 流媒体
- **String**: 字符串工具
- **Table**: 表操作
- **Timer**: 定时器
- **VehicleProperties**: 车辆属性
- **Version**: 版本管理
- **WaitFor**: 等待函数
- **Zones**: 区域系统

## 安装方法

### 下载 Release

从 GitHub Releases 下载最新版本：

```
https://github.com/overextended/ox_lib/releases/latest/download/ox_lib.zip
```

### 构建源码

```bash
git clone https://github.com/overextended/ox_lib.git
cd ox_lib/web
pnpm i
pnpm build
```

## 配置

使用 convars 进行配置：

```lua
-- 设置主题颜色
setr ox:primaryColor blue
setr ox:primaryShade 8

-- 允许用户选择语言
setr ox:userLocales 1

-- 进度条道具限制
setr ox:progressPropLimit 2
```

需要授予 ACE 权限：

```lua
add_ace resource.ox_lib command.add_ace allow
add_ace resource.ox_lib command.remove_ace allow
add_ace resource.ox_lib command.add_principal allow
add_ace resource.ox_lib command.remove_principal allow
```

## 使用方法

### 在 fxmanifest.lua 中启用

添加为共享脚本：

```lua
shared_scripts {
    '@ox_lib/init.lua',
}
```

或简写形式：

```lua
shared_script '@ox_lib/init.lua'
```

### 指定要导入的模块

```lua
ox_libs {
    'locale',
    'math',
    'table',
}
```

### 在脚本中使用

启用后，可以使用以下全局变量：

- `lib`: 动态导入 ox_lib 模块
- `require`: 导入自己的模块
- `cache`: 缓存系统

### 图标使用

使用 Font Awesome 6.0 图标：

```lua
-- 默认 solid 类型
icon = 'apple'

-- 指定类型
icon = {'fab', 'apple'}
```

## 构建 UI

如果需要修改 UI：

1. 安装 Node.js (LTS)
2. 安装 pnpm: `npm install -g pnpm`
3. 构建：
   ```bash
   cd ox_lib/web
   pnpm i
   pnpm build
   ```

开发模式：

- `pnpm start`: 浏览器热重载
- `pnpm start:game`: 游戏内开发

## 文档和支持

- 官方文档: https://overextended.dev/ox_lib
- GitHub: https://github.com/overextended/ox_lib
- npm 包: https://www.npmjs.com/package/@overextended/ox_lib
