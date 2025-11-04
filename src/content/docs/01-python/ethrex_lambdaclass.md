
---
title: ethrex
---


# ethrex - 区块链交互框架

**项目地址**: [https://github.com/lambdaclass/ethrex](https://github.com/lambdaclass/ethrex)

---

## 主要特性

- **一站式链上交互**：提供统一的 SDK，支持多种链（ETH、Polygon、BSC 等）和多层协议（ERC20、ERC721、ERC1155 等）  
- **节点与钱包支持**：内置 HTTP/WebSocket 节点，高级钱包支持（Ledger、Trezor、Web3Modal 等）  
- **易用链上事件监听**：支持实时事件监听、历史事件查询与筛选  
- **命令行工具**：提供 `ethrex-cli`，可快速部署合约、查询余额、执行交易  

---

## 主要功能

| 功能 | 说明 |
|------|------|
| **合约部署** | 自动生成 ABI，生成部署脚本，支持笔记本部署 |
| **代币交互** | ERC20/721/1155 送币、转账、查询余额、授权 |
| **质押与治理** | 与 DeFi 协议交互（Aave、Compound）、DAO 投票 |
| **高级调用** | 零知识证明、闪电贷、路由合约执行 |
| **链上数据查询** | 交易结果、区块信息、gas 费用、事件日志 |
| **钱包集成** | 插件式支持多种硬件钱包，支持多账户管理 |
| **CLI** | 直接在终端执行部署、查询、转账等操作 |

---

## 如何使用

### 安装

```bash
pip install ethrex
```

### 基本示例

```python
from ethrex import Ethrex

# 连接节点
er = Ethrex(node_url="https://mainnet.infura.io/v3/YOUR_PROJECT_ID")

# 查询 ETH 余额
balance = er.get_balance("0xYourAddress")

# 发送代币
tx_hash = er.send_token(
    token_address="0xTokenAddress",
    to="0xRecipient",
    amount=1000,  # 单位：token.smallest
    private_key="0xPrivateKey"
)
print(f"交易哈希: {tx_hash}")
```

### 使用 CLI

```bash
# 查看帮助
ethrex-cli --help

# 部署合约
ethrex-cli deploy --contract MyToken.sol --args "['My Token', 'MTK', 18]"

# 查询余额
ethrex-cli balance --address 0xYourAddress

# 发送交易
ethrex-cli send --to 0xRecipient --value 0.01
```

---

> 如需更详细的实现细节、API 文档与高级功能，请访问官方文档或查看源代码中的 README。  
> 项目地址已列出，可直接克隆、贡献或提交 Issue。  
