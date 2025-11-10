---
title: Ic
---

# ic_dfinity

## 功能

Internet Computer Protocol (ICP) 是世界上第一个以web速度运行的区块链，可以无限扩展其容量。它由遵守ICP协议的机器组成，提供去中心化的云计算服务。

主要特点：

- 以web速度运行
- 无限扩展容量
- 去中心化
- 支持智能合约（称为canisters）
- 使用新型密码学，无需传统挖矿

## 用法

### 对于应用开发者

使用 [Canister SDK](https://sdk.dfinity.org/docs/quickstart/quickstart-intro.html) 来构建应用。它提供本地replica用于部署和测试。

### 对于节点提供者

运行replica软件，成为网络的一部分。

系统要求：

- x86-64 系统（最低16GB内存/交换空间，100GB可用磁盘空间）
- Ubuntu 22.04 或更新版本
- [Podman](https://podman.io/getting-started/installation)

构建代码：

```bash
./ci/container/build-ic.sh -i
```

构建二进制文件和canisters：

```bash
./ci/container/build-ic.sh -b -c
```

### 验证发布

使用repro-check脚本验证IC-OS更新镜像。

快速开始：

```bash
curl -fsSL https://raw.githubusercontent.com/dfinity/ic/{COMMIT_ID}/ci/scripts/repro-check | python3 - -p <proposal_number>
```

### 贡献

目前不接受pull requests，但欢迎在论坛讨论。遵循开源政策和Rust依赖政策。

更多资源：

- [ICP Dashboard](https://dashboard.internetcomputer.org)
- [开发者论坛](https://forum.dfinity.org/)
- [协议文档](https://sdk.dfinity.org/docs/interface-spec/index.html)
