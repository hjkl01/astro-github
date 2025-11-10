---
title: lighter-python
---

# lighter-python

## 项目简介

lighter-python 是 Lighter 平台的官方 Python SDK，提供与 Lighter 区块链交易平台交互的完整 API 支持。Lighter 是一个基于 ZK-rollup 的去中心化交易所 (DEX)，支持高性能的加密货币交易。

## 主要功能

- **账户管理**: 查询账户信息、API 密钥、PnL（盈亏）、公共池等
- **订单操作**: 创建、取消订单，查询订单簿、活跃订单、不活跃订单
- **市场数据**: 获取 K 线图、资金费率、交易统计、最近交易
- **交易历史**: 查询账户交易、区块交易、存款/提现历史
- **区块链信息**: 获取区块信息、当前高度、交易详情
- **WebSocket 支持**: 实时同步订单簿和账户数据

## 安装

### 要求

- Python 3.8+

### 通过 pip 安装

```bash
pip install git+https://github.com/elliottech/lighter-python.git
```

## 基本用法

### 初始化客户端

```python
import lighter
import asyncio

async def main():
    client = lighter.ApiClient()
    try:
        # 使用 API
        account_api = lighter.AccountApi(client)
        account = await account_api.account(by="index", value="1")
        print(account)
    finally:
        await client.close()  # 确保连接干净关闭

if __name__ == "__main__":
    asyncio.run(main())
```

### 示例

#### 获取账户信息

```python
account_api = lighter.AccountApi(client)
account = await account_api.account(by="index", value="1")
```

#### 查询订单簿

```python
order_api = lighter.OrderApi(client)
order_books = await order_api.order_books()
```

#### WebSocket 实时数据

```python
# 参考 examples/ws.py
```

## API 端点

SDK 提供了以下主要 API 类：

- `AccountApi`: 账户相关操作
- `OrderApi`: 订单和市场数据
- `TransactionApi`: 交易操作
- `BlockApi`: 区块链信息
- `CandlestickApi`: K 线和资金数据
- `RootApi`: 基本信息和状态

详细的 API 文档请参考项目仓库中的 `docs/` 目录。

## 测试

运行测试：

```bash
pytest
```

## 许可证

Apache-2.0 License
