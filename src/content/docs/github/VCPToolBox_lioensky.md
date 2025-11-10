---
title: VCPToolBox
---

# VCPToolBox

项目地址: <https://github.com/lioensky/VCPToolBox>

## 概述
VCPToolBox 是一个跨平台的 Python 库，专为 Virtual COM Port（VCP）通信设计。它提供了统一的 API，简化了端口扫描、连接、数据读写、日志记录和错误处理等操作。

## 主要特性
- **端口自动检测**：一次扫描即可列出所有可用的 COM 端口。  
- **多线程读写**：后台线程实时读取数据，主线程可安全发出写入请求。  
- **数据帧解析**：支持自定义帧头/帧尾、长度字段、校验和等协议。  
- **日志与调试**：可将通信日志写入文件或控制台，方便排错。  
- **跨平台**：兼容 Windows、Linux、macOS。  
- **命令行工具**：提供 `vcp_toolbox_cli`，可直接在终端中测试端口。

## 功能

| 模块/类 | 作用 |
|---|---|
| `VCPToolBox` | 主类，负责端口管理与数据处理。 |
| `PortScanner` | 扫描并返回可用端口列表。 |
| `DataParser` | 解析并构造自定义帧。 |
| `Logger` | 记录通信日志。 |
| `CLI` | 命令行交互工具。 |

## 用法

```python
# 安装
pip install vcp_toolbox

# 示例代码
import asyncio
from vcp_toolbox import VCPToolBox

async def main():
    # 端口扫描
    ports = await VCPToolBox.scan_ports()
    print("可用端口:", ports)

    # 连接到第一个可用端口
    vcp = VCPToolBox(port=ports[0], baudrate=115200)
    await vcp.connect()

    # 发送数据
    await vcp.send(b'\x01\x02\x03\x04')

    # 接收数据（异步）
    async for frame in vcp.receive():
        print("收到帧:", frame)

    await vcp.disconnect()

asyncio.run(main())
```

### 命令行工具

```bash
# 查看帮助
vcp_toolbox_cli --help

# 连接并监控 COM3
vcp_toolbox_cli -p COM3 -b 115200 -s 8 -p 0 -f 1
```

> 详细使用说明请参阅项目 README。