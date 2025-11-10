---
title: chainlink
---


# Chainlink (smartcontractkit/chainlink)

> 项目地址: <https://github.com/smartcontractkit/chainlink>

## 主要特性  

| 特性 | 说明 |
|---|---|
| **去中心化预机网络** | 通过去中心化节点获取可信的链上外部数据。 |
| **数据馈送 (Data Feeds)** | 以低延迟、高可靠性提供加密货币价格、天气、体育赛事等实时信息。 |
| **链上随机数生成 (VRF)** | 生成可验证且不可预测的随机数，适用于NFT铸造、游戏等场景。 |
| **多链互操作 (CCIP)** | 在不同区块链之间跨链传输数据与资产。 |
| **链上升级（Chainlink 2.0）** | 支持链上合约升级、模块化适配器，降低开发门槛。 |
| **安全与审计** | 采用可证明性设计，链上内置审计日志和访问控制。 |

## 主功能  

1. **Chainlink Node**  
   - 部署自己节点，参与网络并获取 LINK 代币奖励。  
   - 支持自定义适配器，实现多种 API、IoT 设备接口，甚至高级聚合逻辑。

2. **Chainlink Clients (Smart Contracts)**  
   - 通过 `LinkTokenInterface` 与节点交互，支付请求费用。  
   - `ChainlinkRequest` 结构化请求参数，支持数据预处理与校验。

3. **Data Feeds**  
   - `AggregatorV3Interface` 返回稳定的价格、波动率等。  
   - 多种旅程（Spot、Index、Historical）可选。

4. **VRF (Verifiable Random Function)**  
   - `VRFConsumerBaseV2` 接口，支持异步随机数请求与回调。  
   - 用于公平抽奖、随机数生成、加密签名验证等。

5. **CCIP (Cross-Chain Interoperability Protocol)**  
   - `Router` 与 `ICCPEndpoint` 合约，实现跨链消息与资产转账。  
   - 专为多链环境设计，支持 EVM 与链链接。

## 用法示例  

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

// 1. 引入 Chainlink 相关接口
import "@chainlink/contracts/src/v0.8/interfaces/ChainlinkRequestInterface.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

/**
 * @title PriceConsumerV3
 * @notice 示例合约：获取 ETH/USD 价格并返回
 */
contract PriceConsumerV3 is ChainlinkClient {
    uint256 public price;
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;
    address private linkToken;

    constructor(address _oracle, address _linkToken, bytes32 _jobId, uint256 _fee) {
        setChainlinkToken(_linkToken);
        oracle = _oracle;
        jobId = _jobId;
        fee = _fee;
        linkToken = _linkToken;
    }

    // 触发链上请求
    function requestPrice() public returns (bytes32 requestId) {
        Chainlink.Request memory req = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        // 可自定义请求参数
        req.add("get", "https://api.example.com/price");
        req.add("path", "price");
        requestId = sendChainlinkRequestTo(oracle, req, fee);
    }

    // 回调函数：链上节点返回数据后执行
    function fulfill(bytes32 _requestId, uint256 _price) public recordChainlinkFulfillment(_requestId) {
        price = _price;
    }
}
```

**部署与使用步骤**

1. **部署本机或云端 Chainlink Node**  
   - 使用 Docker 或源码方式，根据官方文档启动 Node。  
   - 在链上部署 / 连接相应的 Aggregator、VRF、CCIP 合约。

2. **在合约中设置 `oracle`, `jobId`, `fee`**  
   - 通过 Chainlink 官方市场或自建节点获取 Oracle 地址和 Job ID。  
   - `fee` 为 LINK 代币数量，按网络费用计算。

3. **支付 LINK**  
   ```bash
   // 发送 LINK 代币到合约地址
   $ chainlink request 0x... 0.1 LINK
   ```

4. **执行请求并监听事件**  
   - 在前端或脚本中监听 `PriceSet` 事件，以获取数据。

---
> 以上内容为概览，完整的 API 与高级功能请参考官方仓库与文档。  
