---
title: nesrom
---


# nesrom_dream1986

## 项目地址
[https://github.com/dream1986/nesrom](https://github.com/dream1986/nesrom)

## 项目概述
`nesrom` 是一个专门用于读取和解析 NES（Nintendo Entertainment System）ROM 文件的轻量级 Python 库。它可以帮助开发者快速获得 ROM 的结构信息、映射器类型、内存布局等细节，适用于游戏分析、逆向工程、模拟器开发以及任何需要对 NES ROM 进行低级操作的场景。

## 主要特性
| 功能 | 说明 |
|------|------|
| **ROM 头解析** | 读取并解析 16 字节的 iNES 头，获取 NES 版本、PRG/CHR ROM 大小、镜像类型等信息。 |
| **Mapper 检测** | 自动识别 ROM 所使用的映射器（Mapper）编号，支持 0~255 号映射器。 |
| **TRainer 支持** | 检测并读取 512 字节的 Trainer 数据（如果存在）。 |
| **PRG/CHR 数据提取** | 直接获取 PRG ROM（程序代码）和 CHR ROM（图形数据）的字节数组。 |
| **镜像信息** | 提供镜像方式（垂直/水平/单屏）和屏幕镜像方向的查询。 |
| **命令行工具** | 通过 `nesrom <ROM 文件>` 查看 ROM 的完整信息，支持 `--json` 输出。 |
| **易用的 API** | 只需几行代码即可读取 ROM 并访问其内部结构。 |

## 用法示例

### 1. 安装
```bash
pip install nesrom
```

### 2. Python API
```python
from nesrom import NESROM

# 读取 ROM
rom = NESROM.from_file('SuperMario.nes')

# 打印基本信息
print(f"Mapper: {rom.mapper}")
print(f"PRG ROM: {rom.prg_size} KB")
print(f"CHR ROM: {rom.chr_size} KB")
print(f"Mirror: {rom.mirror_type}")

# 访问 PRG/CHR 数据
prg_data = rom.prg
chr_data = rom.chr

# 若存在 Trainer
if rom.trainer:
    print(f"Trainer found: {len(rom.trainer)} bytes")
```

### 3. 命令行工具
```bash
# 查看 ROM 信息
nesrom SuperMario.nes

# JSON 输出
nesrom SuperMario.nes --json
```

## 常见问题（FAQ）

| 题目 | 说明 |
|------|------|
| **为什么我的 ROM 显示 Mapper 为 0？** | Mapper 0 是最常见的 NROM，通常用于 2.56 MB 以内的 ROM。若你使用的是更高级的 Mapper，请确认 ROM 为 iNES 2.0 格式。 |
| **如何处理 iNES 2.0 头？** | `nesrom` 自动识别 iNES 2.0 并正确解析其额外字段。 |
| **如何获取镜像方向？** | 使用 `rom.mirror_type`（例如 `HORIZONTAL`, `VERTICAL`, `SINGLE_SCREEN_UP`, `SINGLE_SCREEN_DOWN`）。 |

## 贡献
欢迎提交 Issue 与 Pull Request。若你想加入新的 Mapper 支持或修复解析错误，直接在 `nesrom/mappers.py` 添加相应逻辑即可。

--- 

> **路径**  
> `src/content/docs/00/nesrom_dream1986.md`
