---
title: monorepo
---

# Commonware Monorepo

Commonware是一个Rust库，提供用于构建分布式系统的核心原语和示例。旨在在对抗环境中部署，确保安全性和可靠性。

## 功能

Commonware库包含多个原语模块：

- **broadcast**: 在广域网上传播数据。
- **codec**: 序列化结构化数据。
- **coding**: 编码数据以从部分片段中恢复。
- **collector**: 收集对可提交请求的响应。
- **consensus**: 在拜占庭环境中对不透明消息进行排序。
- **cryptography**: 生成密钥、签名任意消息并确定性验证签名。
- **deployer**: 在云提供商之间部署基础设施。
- **p2p**: 通过加密连接与认证对等方通信。
- **resolver**: 解析由固定长度密钥标识的数据。
- **runtime**: 使用可配置调度程序执行异步任务。
- **storage**: 从抽象存储中持久化和检索数据。
- **stream**: 通过任意传输交换消息。

此外，还提供示例应用，如聊天、日志同步、VRF随机数生成等。

## 用法

1. 克隆仓库：

   ```bash
   git clone https://github.com/commonwarexyz/monorepo.git
   cd monorepo
   ```

2. 构建项目：

   ```bash
   cargo build
   ```

3. 运行示例：

   ```bash
   cargo run --example chat
   ```

4. 查看文档：
   访问 [https://commonware.xyz](https://commonware.xyz) 获取详细文档。

注意：示例可能包含不安全代码，仅用于演示目的，不应直接用于生产环境。
