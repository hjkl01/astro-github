
---
title: hyperswitch
---

## hyperswitch_juspay.md

```markdown
# HyperSwitch - Juspay

**GitHub 地址**: https://github.com/juspay/hyperswitch

## 主要特性

- **多渠道支付整合**  
  通过统一接口集成多种支付方式（银行卡、电子钱包、即时支付等），简化业务开发流程。

- **微服务架构**  
  使用Spring Cloud（Java）与Kotlin实现的微服务模式，支持水平扩展、灰度发布及灰度流量控制。

- **数据一致性与事务管理**  
  统一的分布式事务设计，支持 Saga/Two‑Phase Commit、Qos 等方案，确保支付状态一致。

- **高可用与弹性**  
  K8s 原生部署，利用 Helm Chart、ConfigMap 等实现动态配置；支持熔断、限流（Resilience4J）和自愈机制。

- **安全合规**  
  PCI-DSS 兼容、端到端加密、沙箱支持，支持 PCI 1.6/2.0、PSD2 及各类监管报告。

- **可观测性**  
  Prometheus + Grafana、OpenTelemetry、zipkin 等监控链路；支持自定义指标、日志收集与异常追踪。

- **多语言 SDK**  
  提供 Node.js、Python、Go、Java 等语言 SDK，快速集成到业务代码。

- **门户与后台管理**  
  基于 React + Ant Design 的 Web 门户，支持业务配置、交易查询、风险管理与报表。

## 关键功能

| 功能 | 描述 |
|------|------|
| **支付聚合器** | 支付请求统一入口，自动路由到对应支付渠道 |
| **订单/支付状态追踪** | 订单生成、支付、退款、撤消等全流程跟踪 |
| **客服/争议处理** | 通过后台自动标记或人工介入处理支付争议 |
| **风险评估** | 集成机器学习模型（例如 K-means、决策树）对交易做风控 |
| **退款与撤销** | 提供批量退款、单笔撤回、冲正等接口 |
| **接口网关** | 支持返回码映射、签名校验、流量控制 |
| **多币种及多税费** | 统一收/付货币、费计算与税务合规 |
| **异步回调** | 支付完成后可异步推送结果，支持重试与幂等 |
| **钱包功能** | 余额实现、充值、提现、预授权等 |
| **数据分析** | 商户可通过报表查询交易分析、支付渠道占比等 |

## 快速上手

1. **克隆仓库**

   ```bash
   git clone https://github.com/juspay/hyperswitch.git
   cd hyperswitch
   ```

2. **使用 Docker Compose 启动示例环境**

   ```bash
   docker-compose up -d
   ```

   这将启动以下服务：

   - `api-gateway`
   - `order-service`
   - `payment-service`
   - `db`（PostgreSQL）
   - `redis`

3. **配置数据库**

   ```bash
   ./scripts/init-db.sh
   ```

4. **调用支付接口**

   ```bash
   curl -X POST http://localhost:8080/api/payment/initiate \
   -H 'Content-Type: application/json' \
   -d '{
         "amount": 10000,
         "currency": "USD",
         "channel": "credit_card",
         "cardNumber": "4111111111111111",
         "expMonth": "12",
         "expYear": "25",
         "cvv": "123"
       }'
   ```

   返回的响应将包含 `orderId` 和 `paymentUrl`。

5. **查询交易状态**

   ```bash
   curl http://localhost:8080/api/payment/status/{orderId}
   ```

6. **退款示例**

   ```bash
   curl -X POST http://localhost:8080/api/payment/refund \
   -H 'Content-Type: application/json' \
   -d '{
         "orderId": "abc123",
         "amount": 10000
       }'
   ```

7. **使用 SDK  (Python 示例)**

   ```bash
   pip install hyperswitch-sdk
   ```

   ```python
   from hyperswitch import Client
   
   client = Client(api_key="YOUR_API_KEY")
   
   # Initiate payment
   resp = client.payments.initiate(
       amount=10000,
       currency="USD",
       channel="credit_card",
       card_number="4111111111111111",
       exp_month="12",
       exp_year="25",
       cvv="123"
   )
   print(resp)
   ```

8. **后台管理**

   - 访问 `http://localhost:9000`（默认管理员账号: `admin`, 密码: `admin`）
   - 在“支付渠道”页面添加或修改渠道配置
   - 在“报表”页面查看每日交易量、渠道占比等

## 贡献

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 以了解如何提交代码、Issue 或 PR。

## 文档与资源

- 官方文档: [https://gusdocs.juspay.com](https://gusdocs.juspay.com)
- 代码结构: `docs/architecture.md`
- 常见问题: `docs/faq.md`

---

> 路径: `src/content/docs/00/hyperswitch_juspay.md`  

