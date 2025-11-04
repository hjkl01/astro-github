
---
title: zephyr
---


# Zephyr RTOS（Zephyr Project）

- **项目地址**: https://github.com/zephyrproject-rtos/zephyr

## 主要特性

| 特性 | 说明 |
|------|------|
| **超低资源占用** | 核心内核小于 10 KB，支持 32‑bit 与 64‑bit 微控制器 |
| **模块化架构** | 核心、驱动、文件系统、网络、蓝牙等按需编译，灵活配置 |
| **多平台支持** | Cortex‑M, ARMv8‑M, ARC, RISC‑V, x86, PowerPC 等 |
| **实时性能** | 低延迟、中断优先级可配置、可实现秒级定时 |
| **安全特性** | 安全启动、加密驱动、硬件加速、访问分离 |
| **开发工具链** | 官方支持 GCC/Clang (Zephyr SDK)、CMake、West 统一工具链 |
| **社区生态** | 丰富的示例、文档、社区支持，持续集成（CI）与自动化测试 |

## 核心功能

- **任务/线程管理**：支持多优先级线程、定时器、消息队列、信号量、互斥锁等同步原语。
- **设备驱动**：统一的设备模型（device tree、CMake 配置）支持 GPIO、UART、SPI、I2C、PWM、ADC、CAN、Ethernet、USB、蓝牙等。
- **文件系统**：支持 FCB、LittleFS、NFFS 等轻量级文件系统。
- **网络协议栈**：IP、IPv4/IPv6、UDP/TCP、MQTT、CoAP、Modbus 等，支持 6LoWPAN、Thread、Zigbee 等协议。
- **蓝牙**：蓝牙低功耗（BLE）与经典蓝牙协议栈，支持 GATT、HCI、LE Advertising、连接等。
- **安全**：安全启动、Secure Firmware Update、TLS、DTLS、加密驱动（AES、SHA、RSA 等）。
- **实时调试与分析**：支持 SEGGER J-Link、OpenOCD、SystemView、Tracealyzer、Zephyr Trace 等工具。

## 用法示例

1. **克隆仓库并安装 West 工具**  
   ```bash
   git clone https://github.com/zephyrproject-rtos/zephyr.git
   cd zephyr
   pip3 install -U west
   west init -l .
   west update
   west zephyr-export
   ```

2. **安装 Zephyr SDK**  
   ```bash
   wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.2/zephyr-sdk-0.16.2-linux-x86_64.tar.gz
   tar -xvf zephyr-sdk-*.tar.gz
   ./setup.sh
   ```

3. **编译示例项目**  
   ```bash
   cd zephyr/samples/hello_world
   west build -b <board_name> .
   west flash
   ```

4. **自定义配置**  
   - `prj.conf`：设置编译选项、启用模块、驱动等。  
   - `CMakeLists.txt`：添加源文件、库依赖。  

5. **运行测试**  
   ```bash
   west test -T path/to/test
   ```

6. **文档与社区**  
   - 官方文档: https://docs.zephyrproject.org  
   - 示例代码: https://github.com/zephyrproject-rtos/zephyr/tree/main/samples  
   - 社区支持: Zephyr Slack、邮件列表、GitHub Issues

> 以上步骤仅为快速入门示例，实际项目请根据目标硬件与功能需求查阅官方文档进行详细配置。

---

> **提示**：使用 `west` 可以统一管理子模块、工具链与构建；`CMake + West` 的组合使多硬件平台的交叉编译与发布变得简洁高效。