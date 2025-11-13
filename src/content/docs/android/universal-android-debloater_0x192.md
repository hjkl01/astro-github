---
title: universal-android-debloater
---


# Universal Android Debloater（0x192）

> 官方仓库地址：<https://github.com/0x192/universal-android-debloater>

## 主要特性

- **全系统去壳**：一次性删除或保留你不想要的原装应用包，减轻系统负担。
- **白名单/黑名单**：使用预设或自定义白名单，保证系统或你需要保留的包不会被误删。
- **多品牌/多ROM通用**：支持 Google、Samsung、Huawei、Xiaomi、OPPO、Vivo 等主流手机品牌及各种 ROM。
- **解锁备份功能**：在删除前自动生成 apk 备份，必要时可直接恢复。
- **轻量化脚本**：仅依赖 ADB，支持 Linux/macOS/Windows 三大终端，无需额外依赖。
- **交互式菜单**：按键操作直观，支持原始系统尝试与用户交互模式。

## 核心功能

| 功能 | 说明 |
|------|------|
| **列表扫描** | 读取设备上所有已安装包，过滤出可删/不可删列表。 |
| **批量删除** | 通过 ADB 快速一次性卸载所有不在白名单中的包。 |
| **备份恢复** | 在删除前将被删包自动转存至本地目录，支持手动恢复。 |
| **自定义脚本** | 通过 `config.ini` 或 `.debloat_template` 预置你自己的白名单。 |
| **时间进度显示** | 在删除过程中以进度条形式实时反馈完成情况。 |
| **日志记录** | 产生 `debloat.log` 供后期排查或复盘。 |

## 用法

> **Prerequisites**  
> 1. 已安装 [ADB](https://developer.android.com/studio/command-line/adb) 并配置到环境变量。  
> 2. 设备开启 `USB Debugging`，已通过 USB 或 Wi‑Fi 与电脑连通。  
> 3. 电脑要能正常访问 `Android SDK` 或 `platform-tools`。

1. **克隆/下载项目**  

   ```bash
   git clone https://github.com/0x192/universal-android-debloater.git
   cd universal-android-debloater
   ```

2. **运行脚本**（Linux/macOS）  

   ```bash
   chmod +x debloat.sh
   ./debloat.sh
   ```

   **Windows**  

   ```cmd
   debloat.bat
   ```

3. **交互流程**  
   - 第一次运行会自动检测手机并列出所有已安装包。  
   - 通过数字键（如 `1`、`2` 等）选择：  
     - `1`：执行去壳。  
     - `2`：备份后去壳。  
     - `3`：恢复备份。  
     - `0`：退出。  
   - 确认后脚本会自动完成操作，并在根目录生成 `backup/` 和 `debloat.log`。

4. **自定义白名单**  
   - 打开 `config.ini`，在 `whitelist=` 行后添加你想保留的包名（每行一个）。  
   - 保存后再次运行脚本即可生效。

5. **日志与恢复**  
   - 所有操作都会写入 `debloat.log`，可用来检查错误。  
   - 若误删，则通过 `backup/` 下的 `.apk` 重新手动安装：  
     ```bash
     adb install backup/<package_name>.apk
     ```

> **⚠️ 小贴士**：在执行前请确保已备份重要数据；若设备曾使用 `custom ROM` 或 `非官方 ADB`, 可能需要 `root` 权限完成部分删除。

--- 

**项目地址**: <https://github.com/0x192/universal-android-debloater>  
```
