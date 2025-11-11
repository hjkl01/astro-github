---
title: KeymouseGo
---

# KeymouseGo 项目

## 项目地址

[https://github.com/taojy123/KeymouseGo](https://github.com/taojy123/KeymouseGo)

## 主要特性

KeymouseGo 是一个用 Python 语言编写的跨平台自动化工具，主要用于记录和重放鼠标键盘操作。它支持 Windows、macOS 和 Linux 系统，具有以下核心特性：

- **跨平台支持**：支持 Windows、Linux、macOS，无需额外依赖。
- **简单易用**：桌面模式录制操作，命令行运行脚本，适合重复任务自动化。
- **宏录制重放**：记录鼠标点击和键盘输入，重放时自动执行，可设置重复次数。
- **热键控制**：默认启动热键 F6，终止热键 F9。
- **脚本编辑**：支持 JSON5 格式脚本，可手动编辑添加延时和复杂操作。
- **轻量级**：体积小，绿色软件，不占用过多资源。

## 主要功能

- **录制操作**：开始录制后，记录鼠标点击和键盘动作（不记录鼠标移动轨迹）。
- **重放脚本**：选择脚本文件，设置重复次数（0为无限循环），启动执行。
- **命令行运行**：直接运行脚本文件，支持指定重复次数。
- **脚本语法**：使用 JSON5 格式定义事件，包括鼠标动作、键盘按键、延时和文本输入。
- **高级功能**：支持相对坐标、鼠标移动、拖拽等，详见 Wiki。

## 用法

### 安装

1. 下载可执行文件：从 [GitHub Releases](https://github.com/taojy123/KeymouseGo/releases) 下载对应平台的二进制文件，直接运行。
2. 或源码安装：
   - 安装 Python 3.7+。
   - 克隆仓库：`git clone https://github.com/taojy123/KeymouseGo.git`
   - 安装依赖：`pip install -r requirements-*.txt`（根据平台选择）。
   - 打包：使用 pyinstaller 打包为可执行文件。

### 基本用法

- **桌面模式**：
  1. 点击“录制”开始录制操作。
  2. 进行鼠标点击和键盘输入。
  3. 点击“结束”停止录制，生成脚本文件。
  4. 选择脚本，设置重复次数，点击“启动”执行。
- **命令行模式**：
  - 运行脚本：`./KeymouseGo scripts/文件名.txt`
  - 指定重复次数：`./KeymouseGo scripts/文件名.txt -rt 3`
- **脚本示例**（JSON5格式）：
  ```json5
  {
    scripts: [
      {
        type: 'event',
        event_type: 'EM',
        delay: 1000,
        action_type: 'mouse left down',
        action: ['0.2604%', '0.4630%'],
      },
      {
        type: 'event',
        event_type: 'EM',
        delay: 100,
        action_type: 'mouse left up',
        action: [-1, -1],
      },
      {
        type: 'event',
        event_type: 'EX',
        delay: 100,
        action_type: 'input',
        action: '你好 world',
      },
    ],
  }
  ```
- **注意**：录制时不记录鼠标移动；运行前可能需管理员权限；Mac 用户需添加辅助功能权限。
