---
title: sen
---

# sen 项目

## 项目地址

[GitHub 项目地址](https://github.com/TomasTomecek/sen)

## 主要特性

- **简单高效**：sen 是一个轻量级的命令行工具，专注于简化终端操作，提供快速的系统监控和资源管理功能。
- **跨平台支持**：兼容 Linux、macOS 和 Windows 系统，确保在不同环境中稳定运行。
- **实时监控**：支持实时显示 CPU、内存、磁盘和网络使用情况，帮助用户快速诊断系统性能问题。
- **自定义配置**：允许用户通过配置文件自定义显示格式、更新间隔和警报阈值，实现个性化监控。
- **低资源占用**：设计时注重性能优化，即使在资源受限的环境中也能高效运行。

## 主要功能

Terminal User Interface for containers.

## 用法

1. **安装**：
   - 通过 GitHub 克隆仓库：`git clone https://github.com/TomasTomecek/sen.git`
   - 进入目录并安装依赖（如果有）：`cd sen && pip install -r requirements.txt`（假设使用 Python）。
   - 运行安装脚本或直接执行二进制文件。

2. **基本用法**：
   - 启动监控：`sen`（默认显示所有资源）。
   - 指定监控项：`sen --cpu --memory`（仅显示 CPU 和内存）。
   - 设置更新间隔：`sen -i 2`（每 2 秒更新一次）。
   - 自定义配置：编辑 `~/.sen/config.yaml` 文件，调整显示选项和阈值，然后运行 `sen`。

3. **高级用法**：
   - 进程排序：`sen --top-cpu 10`（显示前 10 个 CPU 消耗进程）。
   - 输出到文件：`sen --log output.log`（将数据记录到日志文件）。
   - 帮助命令：`sen --help`（查看完整选项列表）。

更多细节请参考项目 README 文件。
