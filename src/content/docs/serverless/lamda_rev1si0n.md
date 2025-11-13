---
title: lamda
---

# lamda 项目描述

## 项目地址

[https://github.com/rev1si0n/lamda](https://github.com/rev1si0n/lamda)

## 主要特性

- **零依赖**：只需 root 权限即可，无需额外安装。
- **生产环境考验**：通过超 500 台设备的稳定生产环境测试。
- **中间人流量分析**：支持常规及国际 APP 流量分析，DNS 流量分析。
- **FRIDA 集成**：内置 FRIDA 15.x，支持 Java 接口暴露。
- **多架构支持**：ARM/X86 全架构，兼容安卓 6.0-13。
- **远程桌面**：内置 HTTP/SOCKS5 代理，支持 WIFI ADB。
- **自动化**：兼容 uiautomator2，支持 UI 自动化。
- **文件操作**：支持大文件上传下载，设备状态监控。
- **定时任务**：内置 crontab，支持定期执行脚本。
- **VPN 支持**：内置 OpenVPN，支持全局/非全局 VPN。
- **安全性**：支持接口及登录认证，加密连接。

## 主要功能

- **函数创建与管理**：通过 YAML 或 JSON 配置定义 Lambda 函数，包括事件源、触发器和环境变量。
- **本地测试**：提供模拟环境，支持在本地运行和调试 Lambda 函数。
- **部署自动化**：一键部署到 AWS，支持版本管理和回滚。
- **监控与日志**：集成 CloudWatch 日志输出，便于追踪函数执行状态。
- **API Gateway 集成**：简化 RESTful API 的创建和路由配置。

## 用法

1. **克隆仓库**：

   ```
   git clone https://github.com/rev1si0n/lamda.git
   cd lamda
   ```

2. **安装依赖**：
   - 对于 Python：`pip install -r requirements.txt`
   - 对于 Node.js：`npm install`

3. **配置函数**：
   - 编辑 `config.yaml` 文件，定义函数名称、代码路径和 AWS 凭证。

4. **本地测试**：

   ```
   python local_test.py --function my_lambda --event test_event.json
   ```

5. **部署**：

   ```
   python deploy.py --function my_lambda --region us-east-1
   ```

6. **查看日志**：
   - 使用 AWS CLI：`aws logs tail /aws/lambda/my_lambda`

更多细节请参考仓库的 README.md 文件。
