
---
title: RD-Agent
---


# RD-Agent（Microsoft）

**项目地址**: <https://github.com/microsoft/RD-Agent>

---

## 项目概述
RD-Agent 是 Microsoft 为 .NET 应用提供的跨平台远程调试代理。它在目标机器上运行，监听调试请求，并通过网络与 Visual Studio / VS Code 等 IDE 交互，实现远程调试、堆栈跟踪、内存快照等功能。

---

## 主要特性
- **跨平台**：支持 Windows、Linux、macOS。
- **轻量级**：仅包含一个可执行文件，启动即用。
- **高性能**：使用零拷贝和异步 I/O，最低延迟。
- **安全**：支持 TLS 加密通信（可选），并提供身份验证机制。
- **可配置**：通过 CLI 参数或配置文件自定义端口、日志、身份验证等。

---

## 关键功能
| 功能 | 描述 |
|------|------|
| 远程附加 | 通过 IDE 远程附加到正在运行的 .NET 进程 |
| 堆栈跟踪 | 获取并解析 .NET 栈帧，支持跨语言（C#, F#, VB） |
| 内存快照 | 通过 `dotnet-dump` 等工具捕获进程内存 |
| 断点管理 | 设置、删除、查询断点（源代码级别） |
| 变量观察 | 读取局部变量、堆栈变量、全局变量 |
| 代码覆盖 | 收集代码执行覆盖率数据 |
| 日志与诊断 | 支持调试日志、性能指标、异常信息 |

---

## 用法

### 1. 下载与编译
```bash
git clone https://github.com/microsoft/RD-Agent.git
cd RD-Agent
dotnet build -c Release
```
编译完成后可在 `./bin/Release/netcoreapp3.1/`（或对应平台）找到 `rd-agent` 可执行文件。

### 2. 运行代理
```bash
# 默认监听本地端口 5000
./rd-agent --port 5000

# 指定 TLS 证书（可选）
./rd-agent --port 5000 --tls --cert <cert.pem> --key <key.pem>

# 开启日志
./rd-agent --port 5000 --log-level debug
```

### 3. 连接 IDE
在 VS Code / Visual Studio 中使用 **Remote Attach**，配置如下：

```json
{
  "name": ".NET Core Remote Attach",
  "type": "coreclr",
  "request": "attach",
  "processId": "1234",         // 目标进程 ID
  "pipeName": "netcoreapp1.0", // 可选
  "host": "remote-host",       // 代理所在机器 IP / 主机名
  "port": 5000,                // 代理监听端口
  "useTls": true               // 与代理 TLS 配置保持一致
}
```

### 4. 常用命令行参数
| 参数 | 作用 |
|------|------|
| `--port` | 监听端口 |
| `--tls` | 启用 TLS 加密 |
| `--cert` | TLS 证书文件 |
| `--key` | TLS 私钥文件 |
| `--log-level` | 日志级别（trace, debug, info, warn, error） |
| `--config` | 指定配置文件路径 |

---

## 配置文件示例 (`rd-agent.json`)
```json
{
  "port": 5000,
  "tls": {
    "enabled": true,
    "certPath": "cert.pem",
    "keyPath": "key.pem"
  },
  "logging": {
    "level": "debug"
  }
}
```

运行时可通过 `--config rd-agent.json` 指定。

---

## 贡献与维护
- 代码托管在 GitHub，遵循 MIT 许可证。
- 任何人都可提交 Issue 或 PR。
- 需要 .NET 6+ SDK 进行编译。

---

## 许可证
MIT © Microsoft

--- 