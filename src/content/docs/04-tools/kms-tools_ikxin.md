---
title: kms-tools
---

# KMS-Tools 项目

**GitHub 项目地址:** [https://github.com/ikxin/kms-tools](https://github.com/ikxin/kms-tools)

## 主要特性
KMS-Tools 是一个开源工具集，主要用于处理 KMS（Key Management Service）激活相关任务。它基于 Python 开发，支持 Windows、Linux 和 macOS 等平台，具有以下核心特性：
- **轻量级设计**：体积小巧，无需复杂安装，易于部署和使用。
- **多协议支持**：兼容多种 KMS 协议，包括 Microsoft 的官方 KMS 和第三方服务器。
- **自动化激活**：提供一键式激活功能，支持批量处理多个系统或应用。
- **安全性考虑**：使用加密传输，避免明文密钥暴露；支持自定义 KMS 服务器配置。
- **开源透明**：代码完全开源，允许用户审查和修改，适用于教育和测试目的。
- **跨平台兼容**：通过 Python 实现，确保在不同操作系统上的稳定性。

## 主要功能
该项目的主要功能聚焦于软件激活和密钥管理，包括：
- **KMS 激活**：为 Windows、Office 等 Microsoft 产品提供 KMS 服务器激活服务，支持在线和离线模式。
- **密钥生成与验证**：生成临时激活密钥（GVLK），并验证激活状态。
- **服务器模拟**：内置 KMS 服务器模拟器，便于本地测试激活流程。
- **日志与诊断**：记录激活过程日志，帮助用户诊断问题，如网络连接或权限错误。
- **配置管理**：支持通过配置文件自定义 KMS 服务器地址、端口和产品类型（例如 Windows 10/11、Office 365）。
- **批量操作**：处理多个设备的激活请求，适用于企业环境或虚拟机集群。

注意：该工具仅供合法授权使用，请遵守 Microsoft 的许可协议，避免用于非法激活。

## 用法
### 安装
1. 确保系统安装 Python 3.6+。
2. 克隆仓库：`git clone https://github.com/ikxin/kms-tools.git`
3. 进入目录：`cd kms-tools`
4. 安装依赖（如果有）：`pip install -r requirements.txt`（项目通常无需额外依赖）。

### 基本用法
- **激活 Windows/Office**：
  运行命令：`python kms_tools.py --server <kms_server_ip> --port 1688 --product windows`
  - `--server`：指定 KMS 服务器 IP（默认使用公共服务器）。
  - `--port`：KMS 端口（默认 1688）。
  - `--product`：产品类型，如 `windows`、`office`。

- **查看激活状态**：
  `python kms_tools.py --check`

- **模拟 KMS 服务器**：
  `python kms_server.py --host 0.0.0.0 --port 1688`

- **配置示例**（kms_config.ini 文件）：
  ```
  [KMS]
  server = kms.example.com
  port = 1688
  product = Windows10
  ```

详细用法请参考项目 README.md 文件中的示例和高级选项。运行前确保管理员权限，并测试网络连通性。