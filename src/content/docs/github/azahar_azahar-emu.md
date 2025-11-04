
---
title: azahar
---


# Azahar Emulator (azahar-emu)

## 项目地址  
[https://github.com/azahar-emu/azahar](https://github.com/azahar-emu/azahar)

---

## 主要特性  
- **完整的 Azahar CPU 模拟**：支持 8 位指令集、寄存器、程序计数器、堆栈指针等核心硬件功能。  
- **内存与 I/O 设备仿真**：实现 64KB RAM、ROM、外设地址映射（UART、LCD、键盘、定时器等）。  
- **命令行工具**：提供 `azahar` CLI，可直接在终端运行、调试程序。  
- **调试与跟踪**：支持设置断点、单步执行、寄存器/内存观察窗口。  
- **跨平台**：兼容 Windows、macOS、Linux，使用纯 Python 代码实现。  
- **插件化**：通过 `plugin` 目录可扩展自定义外设或执行环境。  
- **测试与文档**：自带单元测试、示例程序、详细的使用文档。  

---

## 功能概览  

| 功能 | 说明 |
|------|------|
| **CPU 执行** | 解析并执行 Azahar 汇编指令，支持跳转、条件跳转、子程序调用。 |
| **内存映射** | 通过 `memory.map` 配置文件定义内存布局，支持 ROM 与 RAM 的分区。 |
| **串口通信** | UART 模拟，能够与终端或其他程序进行文本交换。 |
| **显示设备** | 简易 LCD 模拟，支持字符显示，提供 `azahar lcd` 命令查看屏幕内容。 |
| **键盘输入** | 通过 `azahar key` 模拟键盘事件，可在程序中读取键盘扫描码。 |
| **定时器** | 生成周期性中断，支持时间延迟、计时器事件。 |
| **调试器** | `azahar debug <file>` 启动调试会话，支持断点、单步、寄存器查看。 |

---

## 用法

### 安装

```bash
pip install azahar-emu
```

### 运行程序

```bash
azahar run path/to/program.az
```

> 其中 `program.az` 为 Azahar 汇编或二进制文件。

### 调试

```bash
azahar debug path/to/program.az
```

在调试会话中可使用以下命令：

| 命令 | 作用 |
|------|------|
| `break <addr>` | 在指定地址设置断点 |
| `step` | 单步执行一条指令 |
| `continue` | 继续执行直到下一个断点或程序结束 |
| `regs` | 显示 CPU 寄存器状态 |
| `mem <addr> <len>` | 查看指定地址的内存内容 |

### 示例

```bash
# 运行 Hello World 示例
azahar run examples/hello_world.az
```

### 配置

在项目根目录创建 `memory.map` 来定义内存布局，例如：

```txt
ROM_START 0x0000 0x2000
RAM_START 0x2000 0x6000
UART_BASE 0x6000 0x0010
LCD_BASE  0x6010 0x0020
```

---

## 贡献

请先阅读 `CONTRIBUTING.md`，然后提交 PR。  
所有 PR 需通过 CI（GitHub Actions）测试。

---

## 许可

本项目采用 MIT 许可证，详见 `LICENSE`。  

---