---
title: ccxt
---

# CCXT

**项目地址**: https://github.com/ccxt/ccxt

## 概述

CCXT（CryptoCurrency eXchange Trading Library）是一款多语言（JavaScript/Node.js、Python、PHP、Ruby、C#、Go、Java）支持数百个加密货币交易所的统一接口库。它提供统一的API，让开发者可以在不同交易所之间无缝切换，极大地简化了对加密货币交易所的访问与交易逻辑实现。

## 主要特性

| 特性 | 说明 |
|------|------|
| **统一接口** | 所有交易所的REST、WebSocket、私有/公有API统一成相同的方法名与参数格式。 |
| **多语言支持** | 现已支持 JavaScript/Node.js、Python、PHP、Ruby、C#、Go、Java 等多种语言。 |
| **多交易所** | 覆盖 120+ 主流加密货币交易所（Binance、Coinbase Pro、Bitfinex、Kraken 等），并持续更新。 |
| **交易所信息获取** | 提供市场行情、账户信息、订单簿、交易历史、余额、费率等统一查询。 |
| **交易功能** | 支持限价单、市价单、止损单、止盈单、撤单、批量下单等。 |
| **WebSocket支持** | 通过统一的 `watch*` 方法实时订阅行情、订单簿、交易、账户变动。 |
| **错误处理** | 一致的异常类体系，方便捕获与处理。 |
| **多线程/异步** | Node.js/JavaScript 支持 Promise/async、Python 支持 asyncio、Go 支持 goroutine。 |
| **可扩展** | 支持自定义交易所或 API 通过继承和插件方式扩展。 |

## 核心功能

1. **市场数据**  
   - `fetch_ticker(symbol)`：获取最新行情  
   - `fetch_order_book(symbol, limit)`：获取订单簿  
   - `fetch_trades(symbol, since, limit)`：获取最近成交  
   - `fetch_ohlcv(symbol, timeframe, since, limit)`：获取K线数据

2. **账户信息**  
   - `fetch_balance()`：查询余额  
   - `fetch_borrow_balance()`：查询借贷余额（如杠杆交易所）  
   - `fetch_deposit_address(currency)`：获取充值地址  

3. **交易**  
   - `create_order(symbol, type, side, amount, price, params)`：下单  
   - `cancel_order(id, symbol, params)`：撤单  
   - `fetch_order(id, symbol, params)`：查询订单  
   - `fetch_orders(symbol, since, limit, params)`：查询历史订单  
   - `fetch_my_trades(symbol, since, limit, params)`：查询账户成交  

4. **WebSocket 订阅**  
   - `watch_ticker(symbol)`  
   - `watch_order_book(symbol)`  
   - `watch_trades(symbol)`  
   - `watch_balance()`  

5. **工具与辅助**  
   - `nonce()`：生成时间戳  
   - `sign()`：请求签名  
   - `handle_errors()`：统一错误处理  

## 用法示例

### 1. Node.js 示例

```javascript
const ccxt = require('ccxt');

(async () => {
    const exchange = new ccxt.binance({
        apiKey: 'YOUR_API_KEY',
        secret: 'YOUR_SECRET',
    });

    // 获取行情
    const ticker = await exchange.fetchTicker('BTC/USDT');
    console.log('BTC/USDT ticker:', ticker);

    // 下单
    const order = await exchange.createMarketBuyOrder('BTC/USDT', 0.001);
    console.log('Order placed:', order);

    // 监听价格
    exchange.watchTicker('BTC/USDT').then(ticker => {
        console.log('Real-time ticker:', ticker);
    });
})();
```

### 2. Python 示例

```python
import ccxt

exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
})

# 获取订单簿
order_book = exchange.fetch_order_book('ETH/USDT')
print('Order book:', order_book)

# 取消订单
order_id = '123456789'
cancel = exchange.cancel_order(order_id, 'ETH/USDT')
print('Order cancelled:', cancel)

# 订阅实时成交
def on_trade(trade):
    print('New trade:', trade)

exchange.watch_trades('ETH/USDT', on_trade)
```

### 3. Go 示例

```go
package main

import (
	"fmt"
	"github.com/ccxt/ccxt-go/ccxt"
)

func main() {
	exchange := ccxt.NewBinance(ccxt.Params{
		"apiKey": "YOUR_API_KEY",
		"secret": "YOUR_SECRET",
	})

	ticker, _ := exchange.FetchTicker("BTC/USDT")
	fmt.Println("Ticker:", ticker)

	// 下单
	order, _ := exchange.CreateOrder("BTC/USDT", "market", "buy", 0.001, nil)
	fmt.Println("Order:", order)
}
```

## 如何开始

1. 安装对应语言的 CCXT 包  
   - Node.js: `npm install ccxt`  
   - Python: `pip install ccxt`  
   - PHP: `composer require ccxt/ccxt`  
   - Go: `go get github.com/ccxt/ccxt-go/ccxt`  
   - Java: `mvn install`（参见官方文档）  

2. 初始化交易所实例，填写 `apiKey` 与 `secret`（若需要私有操作）。  
3. 调用 `fetch_*` 或 `create_*` 方法，即可完成对各交易所的统一操作。  

## 参考文档

- 官方文档: https://github.com/ccxt/ccxt/wiki/Manual  
- 交易所列表: https://github.com/ccxt/ccxt/wiki/Exchange-Information  

---