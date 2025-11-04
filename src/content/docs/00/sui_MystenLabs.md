
---
title: sui
---


# Sui (Mysten Labs)

## 项目地址
- **GitHub**: [https://github.com/MystenLabs/sui](https://github.com/MystenLabs/sui)

## 主要特性
| 特性 | 简介 |
|------|------|
| **高性能交易** | 采用分片（sharding）和并行执行模型，单笔交易平均确认时间低于 1 秒 |
| **Move 语言生态** | 使用 Move 语言编写智能合约，支持模块化、引用计数与强类型检查 |
| **可扩展性** | Sui 通过多节点分片与共识算法实现水平扩容 |
| **安全与创新** | 引入 *object ownership*、默认免除 gas 的虚拟对象、事务组（transaction group）等创新机制 |
| **简洁的 SDK** | 提供 Go、Rust 与 JavaScript/TypeScript SDK，便于开发者快速上手 |
| **跨链兼容** | 通过 Sui Gateway 与其他区块链互通，可做资产桥接与跨链应用 |

## 核心功能
- **节点运行**  
  *运行完整节点*、*轻节点*以及 *validator*。  
- **钱包与账户**  
  新建 & 管理 Move 账户，支持多签与 ENS（可继承）.  
- **智能合约**  
  - Move 模块编译、发布、升级。  
  - Actor（合约实例）与 Object（可变状态对象）管理。  
- **RPC 与 SDK**  
  - `sui-client` 提供 RPC 及 SDK 接口。  
  - 支持查询账本状态、交易历史、对象详情等。  
- **治理与治理 Token**  
  自带治理模块，可用于投票、提案与治理 Token（SUI）锁存。  
- **CLI**  
  `sui` 命令行工具提供节点管理、交易提交与查询等功能。

## 快速开始
```bash
# 1. 克隆仓库
git clone https://github.com/MystenLabs/sui.git
cd sui

# 2. 安装依赖
make deps

# 3. 编译二进制
make build

# 4. 启动本地区块链（单节点）
./target/debug/sui --config-path sui-config/fullnode.yaml

# 5. 通过 CLI 创建钱包
./target/debug/sui client keygen

# 6. 再启动一个节点或 validator
```

## 部署 Move 合约
```bash
# 编译 Move 代码
move build

# 推送到节点
sui client publish --path ./move/target/release

# 获取对象地址并调用
# (见官方文档使用 `sui client call` 或 SDK)
```

## 开发者文档
- 详见项目 `docs/` 目录或官方文档站点:  
  * https://docs.sui.io  
  * https://docs.move.technology

## 社区与支持
- Discord 与 Telegram 社区  
- 开发者论坛：`#sui-dev`  
- Issue 与 PR 直接提交至 GitHub

> 以上信息为项目概览，更多细节请参考官方文档与源码。  

