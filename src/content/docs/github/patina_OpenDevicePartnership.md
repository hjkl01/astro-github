---
title: patina
---

# Patina  — OpenDevicePartnership 项目

> **项目地址**: <https://github.com/OpenDevicePartnership/patina>

## 项目概述
Patina 是一个面向低功耗物联网设备的开源软硬件平台，提供统一的硬件参考设计、固件框架以及软件生态。通过模块化设计，开发者可以快速搭建传感器节点、网关以及边缘计算功能。

## 主要特性
| 特性 | 说明 |
|------|------|
| **开源硬件** | 提供基于 STM32H7 / ESP32 的 PCB 设计与 BOM，支持模组化扩展。 |
| **低功耗体系** | 支持省电模式、睡眠管理；配合能源采集模块实现能量自供给。 |
| **模块化固件** | Bootloader → HAL → 驱动 → 应用层，代码可直接复用。 |
| **多种通信协议** | BLE, LoRa, NB‑eRT, 5G 以及 UART/SPI/I2C 等。 |
| **生态工具** | 示例固件、SDK、Python 配套库、Cloud 端演示。 |
| **易于上手** | 丰富的文档、Quick‑Start、示例代码，支持 `PlatformIO / Arduino`。 |

## 功能模块
1. **Bootloader** – OTA 支持，安全固件升级。  
2. **低功耗管理** – 节能策略、睡眠唤醒，电量监测。  
3. **硬件抽象层 (HAL)** – 统一 MCU 以及外设驱动。  
4. **网络协议栈** – BLE STK、LoRaWAN MAC、MQTT 等。  
5. **传感器驱动** – MPU6050, BMP280, SI7021 等常用传感器。  
6. **应用示例** – 环境监测、姿态检测、远程遥控。  

## 代码结构
```
patina/
├── docs/             # 技术文档与 Quick‑Start
├── examples/         # 示例固件
├── firmware/         # 主固件（HAL + 应用）
│   ├── bootloader/   # OTA & Bootloader
│   ├── hal/          # MCU & IC 驱动
│   ├── net/          # 网络协议
│   └── app/          # 业务层
├── hardware/         # PCB, BOM, BOM.xlsx
└── tools/            # 工具链脚本与固件编译器
```

## 用法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/OpenDevicePartnership/patina.git
   cd patina
   ```

2. **准备开发环境**  
   - 安装 `PlatformIO` 或 `STM32CubeIDE`（针对 STM32）  
   - 安装 `esp-idf`（如果搭建 ESP32 模块）  

3. **编译固件**  
   - STM32 示例  
     ```bash
     pio run -e stm32h7 -t upload
     ```
   - ESP32 示例  
     ```bash
     cd firmware/esp32
     idf.py build
     idf.py -p /dev/ttyUSB0 flash
     ```

4. **烧录硬件**  
   - 连接对应的 MCU 与 USB 供电  
   - 通过工具链直接烧录（见 `examples` 下的 `README`）  

5. **运行与调试**  
   - 使用 `idf.py monitor` 或 `pio device monitor` 查看串口日志  
   - 修改 `app/config.h` 配置网络参数、传感器采样率等  

6. **固件升级**  
   - 通过 OTA 接口（HTTP/HTTPS）上传新固件  
   - Bootloader 自动校验并刷入，失败时返回旧版本  

## 贡献

1. Fork 本仓库  
2. 创建新分支 `feat/<feature_name>`  
3. 编写代码并提交 `np-test`  
4. 提交 PR 并根据 Review 反馈完善  

## 许可证

MIT © OpenDevicePartnership

---