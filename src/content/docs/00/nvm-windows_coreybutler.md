
---
title: nvm-windows
---


# nvm-windows (Node Version Manager for Windows)

> **项目地址**：<https://github.com/coreybutler/nvm-windows>

## 主要特性

- **多版本管理**：在同一台 Windows 机器上安装、卸载、切换多个 Node.js 版本。  
- **命令行工具**：通过 `nvm` 命令行操作，支持 `install`、`uninstall`、`list`、`use`、`latest` 等常用命令。  
- **自动更新 Node.js**：`nvm use latest` 可直接切换到最新稳定版。  
- **配置文件**：`nvmrc` 文件支持项目级别的 Node 版本声明，`nvm use` 可自动读取。  
- **兼容性**：无须管理员权限即可安装，支持旧版 Node 和 LTS 版本。  
- **系统环境变量管理**：安装时会自动配置 `PATH`，确保 `node`、`npm` 可直接使用。  

## 基本用法

```bash
# 安装指定版本
nvm install 14.18.1

# 安装最新版本
nvm latest

# 列出已安装的版本
nvm list

# 使用指定版本
nvm use 14.18.1

# 卸载版本
nvm uninstall 14.18.1
```

> 运行 `nvm` 时若无参数，显示帮助信息。

## 高级功能

- **全局与本地版本冲突解决**  
  在项目根目录放置 `.nvmrc`，执行 `nvm use` 时会自动切换到该文件指定的版本。  
- **批处理脚本**  
  通过 `nvm install 14.18.1 && nvm use 14.18.1` 组合实现一键安装+切换。  
- **代理配置**  
  可通过 `nvm settings` 配置 HTTP/HTTPS 代理，适用于公司网络。  

## 配置文件

- `C:\Users\<用户名>\nvm\nvm-settings.txt`：全局配置（如代理、安装路径）。  
- `C:\Users\<用户名>\nvm\nvmrc`：项目级别的 Node 版本声明。  

## 常见问题

| 现象 | 解决方案 |
|------|----------|
| `nvm` 命令未识别 | 确认 `C:\Users\<用户名>\nvm` 已加入系统 `PATH`，重启终端 |
| 安装后 `node -v` 仍旧旧版 | 运行 `nvm use <版本>` 后重启命令行 |
| `npm install` 报错依赖缺失 | 确认已切换到对应 Node 版本，或删除 `node_modules` 并重新安装 |

> 详细信息请参阅官方 README 与 Issue Tracker。  

---  

> **文件路径**：`src/content/docs/00/nvm-windows_coreybutler.md`

