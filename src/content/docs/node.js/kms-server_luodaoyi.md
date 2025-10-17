
---
title: kms-server
---

# KMS Server 项目

## 项目地址
[https://github.com/luodaoyi/kms-server](https://github.com/luodaoyi/kms-server)

## 主要特性
- **开源实现**：这是一个基于 Node.js 的 KMS (Key Management Service) 服务器模拟器，支持 Microsoft 产品的激活服务。
- **轻量级部署**：无需复杂环境，支持快速搭建本地 KMS 服务器，用于 Windows、Office 等软件的批量激活。
- **协议兼容**：模拟 Microsoft KMS 协议，支持 slmgr.vbs 等工具的激活请求。
- **自定义配置**：允许修改激活密钥、服务器端口和客户端限制。
- **跨平台支持**：可在 Windows、Linux 和 macOS 上运行。

## 主要功能
- **KMS 激活服务**：提供 KMS 服务器端点，允许客户端通过 TCP 端口 (默认 1688) 进行激活验证。
- **密钥管理**：内置常见 Microsoft 产品（如 Windows 10/11、Office 2016/2019）的通用激活密钥 (GVLK)。
- **日志记录**：记录激活请求、客户端 IP 和激活状态，便于调试和监控。
- **批量激活支持**：适用于企业环境或虚拟机批量激活场景。
- **安全选项**：可选添加访问控制，限制特定 IP 或子网的激活请求。

## 用法
1. **环境准备**：
   - 安装 Node.js (版本 >= 14)。
   - 克隆仓库：`git clone https://github.com/luodaoyi/kms-server.git`。
   - 进入项目目录：`cd kms-server`。

2. **安装依赖**：
   - 运行 `npm install` 以安装所需模块。

3. **配置**：
   - 编辑 `config.json` 文件，设置服务器端口 (默认 1688)、激活密钥和允许的客户端范围。
   - 示例配置：
     ```
     {
       "port": 1688,
       "keys": {
         "Windows": "W269N-WFGWX-YVC9B-4J6C9-T83GX"
       },
       "allowedClients": ["192.168.1.0/24"]
     }
     ```

4. **启动服务器**：
   - 运行 `npm start` 或 `node server.js`。
   - 服务器将在指定端口启动，输出日志显示监听状态。

5. **客户端激活**：
   - 在 Windows 客户端上，使用命令提示符 (管理员权限)：
     ```
     slmgr /skms <服务器IP>:1688
     slmgr /ato
     ```
   - 替换 `<服务器IP>` 为 KMS 服务器的 IP 地址。
   - 对于 Office：使用 `cscript ospp.vbs /sethst:<服务器IP>` 和 `cscript ospp.vbs /act`。

6. **停止服务器**：
   - 按 Ctrl+C 终止进程。

注意：此项目仅用于合法激活已购买的 Microsoft 产品。请遵守相关许可协议。