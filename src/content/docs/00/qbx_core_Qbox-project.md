
---
title: qbx_core
---

# Qbx_Core — Qbox 项目核心框架

• **项目地址**：<https://github.com/Qbox-project/qbx_core>

## 简介
Qbx_Core 是一个基于 FiveM 的高效、模块化核心框架，旨在为服务器开发者提供统一、可扩展的底层功能。它采用了 ESX 的灵感，同时加入了更高性能的数据缓存、事件系统与灵活的角色管理，极大地简化了复杂服务器逻辑的实现。

## 主要特性

| 序号 | 特性 | 说明 |
| ---- | ---- | ---- |
| 1 | **模块化架构** | 资源按模块拆分（如 Banco、Inventory、Jobs），方便按需加载、重写与维护。 |
| 2 | **事件系统** | 原生事件、延迟事件、广播事件，支持多线程安全。 |
| 3 | **角色 & 许可系统** | `QBXPlayer` 对象持有角色与权限，轻松实现 `isAdmin`、`hasPermission` 等检查。 |
| 4 | **缓存层** | 玩家/角色/公司等全局缓存，减少数据库访问。 |
| 5 | **数据库抽象** | 通过 `qb-core` 内置 DB 玩家层，支持 MySQL/MariaDB。 |
| 6 | **命令 & 控制台** | `QBCore.Commands` 集成 `addCommand` 与 `addPermission`，配合 `QBCore.Console` 统一控制台输出。 |
| 7 | **接口与 Export** | 通过 `exports['qb-core']` 暴露核心接口，外部资源易于集成。 |
| 8 | **多线程安全** | `lib/ThreadSafe` 确保 QBCore 内部数据在多线程环境下正确同步。 |
| 9 | **错误与日志** | `QBCore.Log.Debug`, `QBCore.Log.Error`, `QBCore.Log.Warn` 可自定义日志级别与输出路径。 |
| 10 | **脚本化配置** | `shared/config.lua` 与 `server/config.lua` 支持动态更新，无需重启服务器。 |

## 关键功能

1. **玩家管理**
   - 载入/保存玩家数据（金钱、属性、角色）
   - 角色切换 & 属性显示
   - 玩家心跳系统（保活与死亡检查）

2. **角色系统（Jobs）**
   - `AddJob`, `RemoveJob`, `SetJobGrade` 等 API
   - `OpenJobMenu`, `JobLicense` 等 UI 集成

3. **财产系统**
   - 公司、房产（`qb-garage`, `qb-dealer`）管理
   - 账单 & 商业收入跟踪

4. **通知与聊天**
   - `TriggerLocalChatMessage`, `Notify` 推送
   - 跨服务器/跨资源聊天桥接

5. **资源管理**
   - `QBCore.Server:Start`, `QBCore.Server:Stop`
   - 模块化 `Require` 系统加载自定义脚本

6. **API 与导出**
   - `QBCore.Functions.GetPlayer`, `QBCore.Functions.GetWeaponSlot`
   - `exports['qb-core']:GetCoreObject()` 可在其他资源中获取核心对象

## 快速上手

```lua
-- 初始化 QBCore
local QBCore = exports['qb-core']:GetCoreObject()

-- 监听玩家加入事件
RegisterServerEvent('QBCore:Client:OnPlayerLoaded')
AddEventHandler('QBCore:Client:OnPlayerLoaded', function()
    local src = source
    local Player = QBCore.Functions.GetPlayer(src)
    TriggerClientEvent('QBCore:Notify', src, "欢迎回来！")
end)
```

### 1. 数据库

```sql
CREATE TABLE `users` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `citizenid` VARCHAR(50) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `money` INT DEFAULT 0,
  `cash` INT DEFAULT 0
  -- 其它列省略
);
```

> 相关字段与结构请参照 `resources/[qb]/[qb-core]/system/db.sql`。

### 2. 启动服务器

```bash
# server.cfg
ensure qb-core
ensure qb-admin
-- 其它资源
```

### 3. 编写自定义资源

```lua
-- myjob/server/main.lua
local QBCore = exports['qb-core']:GetCoreObject()

QBCore.Functions.CreateJob("myjob", "自定义工作", { ["rank0"] = { label = "职员", salary = 500 } })

-- 注册事件
RegisterServerEvent('myjob:reward')
AddEventHandler('myjob:reward', function()
    local src = source
    local Player = QBCore.Functions.GetPlayer(src)
    if Player then
        Player.Functions.AddMoney('cash', 100)
    end
end)
```

> 更详细的 API 见 `documentation/ensha/core/api.md`。

## 常见问题

| 领域 | 问题 | 解决方案 |
| ---- | ---- | -------- |
| 玩家数据 | 载入失败 | 检查数据库连接，确保 `citizenid` 唯一；清理 `persistent-data` 目录 |
| 角色权限 | 权限失效 | 确认 `config.lua` 中 `jobs` 权限配置，且 `QBCore.Player:SetPermission` 被正确调用 |
| 事件失效 | 找不到事件名 | 使用 `print(eventName)` 检查是否被重写，从资源树查看是否覆盖文件 |

---

**提示**  
- 在调试时，可通过 `QBCore.Log.Debug("信息")` 在控制台输出详细日志。  
- `resources/[qb]/[qb-core]/system/events/test.lua` 内嵌了常用事件范例，建议先行阅读。

祝你玩得开心，祝服务器开发顺利！