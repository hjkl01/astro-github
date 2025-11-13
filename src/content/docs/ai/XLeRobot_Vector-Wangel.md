---
title: XLeRobot
---

# XLeRobot

## 项目简介

XLeRobot 是一个实用的低成本双臂移动家用机器人，旨在将 Embodied AI 带给每个人。项目基于开源项目如 LeRobot、SO-100/SO-101、Lekiwi 和 Bambot，提供了完整的硬件设计、软件栈和模拟环境。

## 主要功能

- **双臂操纵**：配备两个 SO-100 机械臂，支持复杂的双臂操作任务
- **移动平台**：基于 IKEA 购物车改造的移动底盘，提供室内导航能力
- **多模态感知**：支持 RGB 摄像头、深度摄像头等多种传感器
- **实时控制**：支持键盘、Xbox 控制器、Switch Joycon 和 VR 设备进行远程控制
- **模拟环境**：提供完整的 MuJoCo 模拟环境，支持强化学习和 VLA 算法开发
- **家用任务**：适用于拾取物体、导航、日常家务等任务

## 技术特点

- **低成本**：基础版本仅需约660美元（不含电池和购物车）
- **开源**：基于 Apache-2.0 许可证，完全开源
- **模块化设计**：硬件和软件高度模块化，便于定制和扩展
- **跨平台**：支持多种操作系统和开发环境

## 使用方法

### 1. 硬件准备

- 购买所需零件（参考 BOM 清单）
- 3D 打印机器人部件
- 组装硬件（总组装时间约4小时）

### 2. 软件安装

- 克隆项目仓库：`git clone https://github.com/Vector-Wangel/XLeRobot`
- 安装依赖：按照文档安装 Python 环境和相关库
- 配置硬件连接

### 3. 运行和控制

- 使用键盘或游戏控制器进行实时控制
- 在模拟环境中测试算法
- 部署到真实机器人进行任务执行

## 文档和资源

- **官方文档**：[https://xlerobot.readthedocs.io](https://xlerobot.readthedocs.io)
- **GitHub 仓库**：[https://github.com/Vector-Wangel/XLeRobot](https://github.com/Vector-Wangel/XLeRobot)
- **Discord 社区**：[https://discord.gg/bjZveEUh6F](https://discord.gg/bjZveEUh6F)

## 贡献

欢迎对项目进行贡献！请参考 [CONTRIBUTING.md](https://github.com/Vector-Wangel/XLeRobot/blob/main/CONTRIBUTING.md) 了解如何参与开发。

## 许可证

本项目采用 Apache-2.0 许可证。
