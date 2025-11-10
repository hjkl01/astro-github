---
title: mullvadvpn-app
---

# Mullvad VPN App

项目地址: https://github.com/mullvad/mullvadvpn-app

## 主要特性
- **隐私优先**：使用强加密（WireGuard / OpenVPN）确保数据安全。
- **无日志**：Mullvad 不记录用户活动、IP 地址或连接时间。
- **多平台支持**：提供 Windows、macOS、Linux、Android、iOS 与浏览器插件。
- **Kill Switch**：在 VPN 连接中断时自动断开网络，防止 IP 泄露。
- **DNS 泄露保护**：强制使用 Mullvad 或自定义安全 DNS。
- **多服务器选择**：可选择全球数百个服务器，支持按地区或最快速度排序。
- **分流（Split Tunnel）**：为部分应用或网络流量指定使用 VPN 或直连。
- **自动更新**：App 会自动检查并安装最新版本。
- **快速连接**：利用 WireGuard 的低延迟与高吞吐。
- **易用界面**：直观的图形化界面与命令行工具（CLI）可根据需求选择。

## 功能概览
| 功能 | 简述 |
|------|------|
| **连接管理** | 选择服务器、连接/断开、查看连接状态与速度。 |
| **网络安全** | Kill Switch、DNS 保护、IP 防泄露。 |
| **隐私设置** | 选择匿名身份、使用匿名账单。 |
| **分流** | 为指定应用或域名设置直连/代理。 |
| **日志查看** | 本地日志记录，帮助诊断连接问题。 |
| **配置文件** | 生成 WireGuard / OpenVPN 配置，支持第三方客户端。 |
| **自动更新** | 自动检查、下载并安装新版本。 |
| **CLI 交互** | 通过命令行快速控制 VPN，适合脚本与服务器。 |

## 用法

### 1. 安装

#### Windows / macOS / Linux
1. 访问 [release 页面](https://github.com/mullvad/mullvadvpn-app/releases) 下载对应系统的安装包。  
2. 双击安装并按提示完成安装。  
3. 启动应用后，使用 Mullvad 帐号登录（可在 Mullvad 官网生成）。

#### Android / iOS
1. 在 Google Play / App Store 搜索 “Mullvad VPN” 并安装。  
2. 打开后登录帐户，按提示完成设置。

#### CLI（Linux / macOS）
```bash
# 安装（以 Debian/Ubuntu 为例）
sudo apt install mullvad-vpn

# 登录
mullvad login

# 连接
mullvad connect

# 断开
mullvad disconnect
```

### 2. 连接服务器
1. 在主界面选择 “Servers” 或 “Locations”。  
2. 选择具体国家或城市，点击 “Connect”。  
3. 连接成功后，状态栏显示已连接。

### 3. 分流设置
1. 打开 “Settings” → “Split Tunneling”。  
2. 选择 “Apps” 或 “Domains”，添加需要直连或代理的应用/域名。  
3. 保存后重启连接。

### 4. 生成配置文件
1. 在 “Settings” → “Export Configuration”。  
2. 选择 WireGuard 或 OpenVPN，下载对应文件。  
3. 用第三方客户端导入即可。

### 5. 使用 Kill Switch
Kill Switch 默认开启，若需关闭：
1. 在 “Settings” → “Security” → “Kill Switch” 进行切换。  

### 6. 更新
- GUI 版：应用会自动提示更新。  
- CLI 版：`mullvad update` 或使用系统包管理器。

---
> **提示**：Mullvad 采用匿名支付方式（比特币或现金），无需绑定个人信息。  
> 如需进一步自定义（如使用自定义 DNS 或自定义服务器列表），请参考官方文档或 GitHub Wiki。