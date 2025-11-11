---
title: Rime Frost
---

# rime-frost by gaboolic

## 项目简介

白霜拼音（rime-frost）是一个基于 Rime 输入法框架的中文拼音输入方案配置。它使用 745,396,750 字的高质量语料进行分词和词频统计，打造纯净、词频准确、智能的词库。白霜词库是目前 Rime 方案下最好的开源词库之一，旨在提供不输于商业输入法的输入体验。

该项目基于雾凇拼音（rime-ice）的配置和词库进行优化，删除了不健康词汇、冷僻词，并调整了字频和词频。支持全拼和双拼输入，并可选辅助码功能。

## 主要功能

- **高质量词库**：基于大规模中文语料统计字频、词频，提供准确的候选词排序。
- **纯净词库**：删除废词、不健康词汇，确保输入体验干净。
- **辅助码支持**：可选墨奇辅助码，按 \` 键开启，不影响正常打字。
- **多种输入模式**：支持全拼、双拼（多种双拼方案）、T9 等。
- **丰富功能**：
  - 符号输入：`/fh` 等触发更多符号。
  - 带调韵母：`/a` `/e` `/u` 等。
  - 日期时间：`rq` `sj` `xq` `dt` `ts`。
  - 部件拆字反查：`uU`。
  - Unicode 字符：`U`。
  - 数字金额大写：`R`。
  - 农历：`N`。
  - 计算器：`V`。

## 安装方法

### 手动下载安装

1. 下载本仓库的压缩包（Code - Download ZIP）或 [releases](https://github.com/gaboolic/rime-frost/releases) 最新的 source-code.zip。
2. 解压到对应平台的 Rime 配置路径：
   - **Windows**：`%APPDATA%\Rime`
   - **Mac**：
     - 鼠须管：`~/Library/Rime`
     - fcitx5-Mac：`~/.local/share/fcitx5/rime`
   - **Linux**：
     - fcitx5-rime：`~/.local/share/fcitx5/rime`
     - ibus-rime：`~/.config/ibus/rime`
   - **Android**：
     - fcitx5-安卓版：`/Android/data/org.fcitx.fcitx5.android/files/data/rime`
     - 同文：`/rime`
     - 雨燕：已内置白霜词库，直接安装使用。
   - **iOS**：仓输入法已内置，可通过输入方案设置更新。
3. 重新部署输入法，选择白霜拼音。

### 通过 Git 安装

**首次安装**：

```bash
git clone --depth 1 https://github.com/gaboolic/rime-frost Rime
```

**后续更新**：

```bash
cd Rime
git pull
```

### 通过东风破安装

选择配方（others/recipes/\*.recipe.yaml）：

```bash
rime-install gaboolic/rime-frost:others/recipes/full
```

## 使用方法

1. 安装后，在输入法设置中选择白霜拼音方案。
2. 重新部署生效。
3. 开始输入中文，支持全拼、双拼等模式。
4. 可选开启辅助码：按 \` 键进入辅助码模式。
5. 使用各种触发指令，如 `/fh` 输入符号，`rq` 输入日期等。

## 示例输入效果

- 输入 `gegegojx`：哥哥、各个、阁阁 等候选。
- 输入 `mggjdgg`：美国、美国 等。
- 更多示例见项目 README 中的截图。

## 许可证

GPL-3.0 License

## 相关链接

- [项目主页](https://github.com/gaboolic/rime-frost)
- 基于项目：[rime-ice](https://github.com/iDvel/rime-ice)
- 相关方案：[rime-shuangpin-fuzhuma](https://github.com/gaboolic/rime-shuangpin-fuzhuma)、[rime-wubi-sentence](https://github.com/gaboolic/rime-wubi-sentence)
