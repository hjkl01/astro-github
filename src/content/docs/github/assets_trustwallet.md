
---
title: assets
---


# TrustWallet 资产列表

**项目地址**: [https://github.com/trustwallet/assets](https://github.com/trustwallet/assets)

---

## 主要特性

| 特性 | 描述 |
|------|------|
| **统一资产列表** | 汇总了数千种加密资产（币种、代币、NFT 等）的信息，方便开发者快速引用。 |
| **多链支持** | 覆盖 Ethereum、Binance Smart Chain、Polygon、Solana、Avalanche、Fantom、Arbitrum、Optimism、KuCoin-Chain、OKExChain 等主流公链。 |
| **多语言标签** | 每种资产提供多语言（英文、中文、日文、韩文、俄文、阿拉伯文等）名称与符号，便于国际化。 |
| **标准化字段** | 统一定义字段如 `symbol`、`address`、`decimals`、`type`、`website`、`ico` 等，保证数据一致性。 |
| **版本管理** | 通过 Git 标签和 `README.md` 记录版本变更，保持资产信息及时更新。 |
| **易于迭代** | 采用 JSON/YAML/Markdown 结构，便于区块链项目快速拉取、同步或贡献。 |

---

## 功能亮点

1. **全链资产索引**  
   - 支持 > 10,000+ 资产。  
   - 每个链单独目录，方便按链筛选。

2. **多币种资产分类**  
   - **Token**: ERC20/Mintable Token、BEP2、TRC20 等。  
   - **Coin**: 原生链币。  
   - **NFT**: ERC721、ERC1155 等。  
   - **Stable**: USDT、USDC、DAI 等稳定币。

3. **链外相关信息**  
   - 官网、白皮书、GitHub、社区（Telegram、Discord、Twitter）。  
   - 社交 Uni 链接：`website`、`blockchain_explorer`、`official_site` 等。

4. **前端与后端双向兼容**  
   - JSON 对象可直接用于前端 React/Vue 项目。  
   - `csv`/`xlsx` 版本便于导入数据库或数据分析工具。

---

## 如何使用

1. **克隆仓库**  
   ```bash
   git clone https://github.com/trustwallet/assets.git
   cd assets
   ```

2. **获取所需链的资产**  
   - 进入对应链目录，例如 `ethereum`、`bsc`、`polygon` 等。  
   - 书包中有 `tokens`、`coins`、`nfts` 子文件夹。

3. **引入文件**  
   ```javascript
   // ES6 引入
   import tokens from './ethereum/tokens/tokens.json';
   import coins from './ethereum/coins/coins.json';
   ```

4. **查询资产（示例）**  
   ```javascript
   const getTokenInfo = (symbol) => {
     return tokens.find(token => token.symbol === symbol);
   };
   
   const daiInfo = getTokenInfo('DAI');
   console.log(daiInfo);
   ```

5. **贡献资产**  
   - 在 GitHub 上 fork 并创建 PR。  
   - 资产文件遵循 `assets.csv` 规范（字段顺序与注释保持一致）。  
   - PR 将会被审查并合并至主仓库。

---

## 常用命令

| 命令 | 说明 |
|------|------|
| `npm run lint` | 语法检查（JSON/YAML） |
| `npm run build` | 生成压缩版 JSON（可选） |
| `npm test` | 运行测试脚本（功能检查） |

---

## 发展方向

- **实时监控**：结合链上事件实时更新资产列表。  
- **支持更多链**：计划加入更侧链与 Layer2。  
- **多终端支持**：提供移动端 SDK，方便钱包直接集成。

---

*如需进一步了解或参与项目，请访问：* [https://github.com/trustwallet/assets](https://github.com/trustwallet/assets) 。

```
ptw-assets
└── src
    └── content
        └── docs
            └── 00
                └── assets_trustwallet.md
```
