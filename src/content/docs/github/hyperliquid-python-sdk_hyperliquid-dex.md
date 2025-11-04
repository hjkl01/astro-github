
---
title: hyperliquid-python-sdk
---


# Hyperliquid Python SDK  
**项目地址**: <https://github.com/hyperliquid-dex/hyperliquid-python-sdk>

## 概述  
`hyperliquid-python-sdk` 是 Hyperliquid 去中心化交易所（DEX）官方推荐的 Python 客户端。它为开发者提供了以下核心功能：

- 通过 HTTP/REST 接口和 WebSocket 进行高频、低延迟的市场数据查询  
- 支持订单（限价单、限价止损单、止盈单等）的下单、撤单与查询  
- 支持账户与持仓信息的实时监控（余额、持仓、手续费等）  
- 内置签名机制，安全地使用秘钥完成身份验证  
- 完全异步（asyncio）实现，适配 `async for` 读写流  

## 安装  
```bash
pip install hyperliquid-python-sdk
```

> ⚠️ 需要 Python ≥ 3.10。若此前未授权，需在 Hyperliquid 与 `API Keys` 页面创建专属 `private_key` 与 `public_key`。

## 主要特性  

| 特性 | 说明 |
|------|------|
| **RTM 数据流** | 通过 `wss://api.hyperliquid.xyz/ws` 创建实时行情、订单簿、成交、账户事件流。 |
| **订单管理** | 支持 `market`, `limit`, `stop`, `take_profit` 等 Order Type；包括下单、撤单、查询单详情。 |
| **账户查询** | 查询余额、持仓、净资产、手续费率、限额、可用保证金等。 |
| **身份签名** | 内置 `create_signed_message`，使用 `ed25519` 对每个请求做签名，确保安全。 |
| **多币种交易** | 支持所有 Hyperliquid 上的交易对（USDC、BTC/USDC、ETH/USDC 等）。 |
| **高性能** | 异步实现 + 低 GC 需求，适合做高频量化策略。 |

## 核心模块

1. `hyperliquid.client`  
   - `HyperliquidClient`：主入口类。负责建立 HTTP + WebSocket 连接，封装所有的 RPC 与事件订阅。  
   - `order`：订单相关 API (`create_order`, `cancel_order`, `get_order` 等)。  
   - `account`：账户/余额/持仓相关 API。  

2. `hyperliquid.stream`  
   - `MarketDataStream`：行情数据订阅。  
   - `OrderbookStream`：订单簿快照与增量更新。  
   - `TradeStream`：成交数据。  

3. `hyperliquid.utils`  
   - `signature.py`：签名工具。  
   - `schema.py`：定义请求/响应的数据模型。  

## 基础使用示例

```python
import asyncio
from hyperliquid.client import HyperliquidClient

API_KEY = "YOUR_PUBLIC_KEY"
API_SECRET = "YOUR_PRIVATE_KEY"

async def main():
    client = HyperliquidClient(api_key=API_KEY, secret_key=API_SECRET)

    # 1. 获取最近 5 条行情记录
    candles = await client.get_candles(symbol="BTC/USDC", resolution="1m", limit=5)
    print("最近行情:", candles)

    # 2. 开启行情流
    async for tick in client.subscribe("BTC/USDC", channel="ticker"):
        print("实时行情:", tick)

    # 3. 下限价单
    order_id = await client.create_order(
        symbol="BTC/USDC",
        side="buy",
        order_type="limit",
        price=26000,
        quantity=0.01,
        time_in_force="GTC",
    )
    print("下单成功，订单 ID:", order_id)

    # 4. 查询订单状态
    order_info = await client.get_order(order_id)
    print("订单信息:", order_info)

    # 5. 撤销订单
    await client.cancel_order(order_id)
    print("订单已撤销")

# 运行异步入口
if __name__ == "__main__":
    asyncio.run(main())
```

> 运行示例前，请确认 `API_KEY` 与 `API_SECRET` 已正确配置，并已在 Hyperliquid 账户后台开启相应权限。

## 参考文档

- 官方 GitHub 代码仓库: <https://github.com/hyperliquid-dex/hyperliquid-python-sdk>  
- API 文档（REST & WebSocket）: <https://api.hyperliquid.xyz/docs>  
- 描述水平: `[GitHub docs]`，内含 `README.md`、`examples/` 与 `docs/`  

---

**注意**：所有示例均为演示用途，请根据实际交易策略与风险管理要求自行添加必要的容错、重试及风险检测逻辑。